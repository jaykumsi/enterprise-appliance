"""Translate the healthcare (AmeriMed) workbook items into another domain's tables, columns and nouns."""
import json
import re
from decimal import Decimal
from pathlib import Path

from wb_domains import DOMAINS, HC

ROOT = Path(__file__).resolve().parent.parent
MODELS = {m['slug']: m for m in json.loads((ROOT / 'domain_models.json').read_text(encoding='utf-8'))}

# Words that must not survive translation (healthcare-only vocabulary or data).
LEFTOVER = re.compile(r'Office visit|primary care|encounter|patient|doctor|medicat|prescri|\bvisit|clinic|amerimed|healthcare|HealthcareQA|\bHEA-|\bPT-|\bMED-|\bRX-|\bLIC-|'
                      r'refill|readmi|\bwards?\b|\bbeds?\b|telehealth|specialt|cardiolog|\bRx\b|\brx\b|\bDr\.', re.I)
CODE = re.compile(r'```sql\n.*?```|`[^`\n]+`', re.S)
WORD = re.compile(r'[A-Za-z_][A-Za-z0-9_]*')


NEEDS = [
    ('D', re.compile(r'Doctor|doctor')), ('M', re.compile(r'Medication|medication')),
    ('L', re.compile(r'Prescri|prescri|\brx\b|\bRx\b')), ('PARENT', re.compile(r'ParentEncounterID')),
    ('Mprice', re.compile(r'UnitCost')), ('Lref', re.compile(r'PrescriptionReference|RX-')),
    ('HC', re.compile(r'(?i:dr\.)|Specialty|Cardiology|readmi|telehealth|Telehealth|\bWards?\b|refill|LIC-')),
]


def needs(*texts):
    blob = ' '.join(t or '' for t in texts)
    return {k for k, rx in NEEDS if rx.search(blob)}


def has(cfg, need):
    if need in ('D', 'M', 'L'):
        return bool(cfg[need])
    if need == 'Mprice':
        return bool(cfg['M'] and cfg['M'][4])
    if need == 'Lref':
        return bool(cfg['L'] and cfg['L'][2])
    return False  # PARENT, HC: healthcare only


def stem(table):
    return re.sub(r'(ches|ses|xes)$', lambda m: m.group(1)[:-2], table) if re.search(r'(ches|ses|xes)$', table) else re.sub(r's$', '', table)


class Translator:
    def __init__(self, slug, stats=None):
        self.slug, self.cfg, self.model = slug, DOMAINS[slug], MODELS[slug]
        cfg, mp = self.cfg, self.model['map']
        E = self.model['base'][0]
        ids = {'healthcare': slug, 'Encounters': E}
        for hc_col, generic in HC['E'].items():
            if generic:
                ids[hc_col] = mp[generic]
        for role in 'PDML':
            src, dst = HC[role], cfg[role]
            if not dst:
                continue
            if role == 'L':  # Prescriptions(PrescriptionID, PrescriptionReference, Quantity) + FKs
                pairs = zip(src, dst)
            else:
                pairs = zip(src, dst)
            for a, b in pairs:
                if b:
                    ids[a] = b
        if cfg['L'] and cfg['M']:
            ids['MedicationID'] = cfg['M'][1]
        # stems used inside CamelCase identifiers such as NorthPatients, FK_Encounters_PatientID
        self.stems = {'Encounter': stem(E), 'Patient': stem(cfg['P'][0])}
        for role, word in (('D', 'Doctor'), ('M', 'Medication'), ('L', 'Prescription')):
            if cfg[role]:
                self.stems[word] = stem(cfg[role][0])
        self.ids = dict(sorted(ids.items(), key=lambda kv: -len(kv[0])))
        n = cfg['n']
        self.nouns = {}
        for hcw, key in (('encounter', 'ev'), ('visit', 'ev'), ('patient', 'pt'), ('charge', 'amt'),
                         ('doctor', 'd'), ('medication', 'm'), ('prescription', 'l')):
            if key in n:
                self.nouns[hcw], self.nouns[hcw + 's'] = n[key]
        self.nouns['amerimed'] = cfg['short']
        self.nouns['clinic'] = cfg['short']
        self.nouns['prescribed'] = cfg.get('lverb', 'prescribed')
        self.stems = {'Visits': E, **self.stems}
        self.stems['Visit'] = self.stems['Encounter']
        self.ids['Rx'] = 'Lines'
        self.stems['clinical'] = 'ops'
        self.stems['clinic'] = 'ops'
        self.stems['Amerimed'] = cfg['db'].replace('Practice', '')
        self.ids['HealthcareQA'] = cfg['db']
        self.codes = {}  # literal code prefix -> (domain prefix, digit width) ; filled by set_samples
        self.stats = stats or {}

    # ---------- identifiers ----------
    def ident(self, tok):
        if tok in self.ids:
            return self.ids[tok]
        out = tok
        for a, b in self.ids.items():
            if len(a) > 4 and a in out and a != b:
                out = out.replace(a, b)
        for a, b in self.stems.items():
            out = out.replace(a, b)
        return out

    def set_samples(self, samples):
        """samples: {'PT': 'CUS-000001', 'MED': ..., 'HEA': 'RET-2024...', 'RX': ..., 'LIC': ...} (code of row 1)."""
        for k, v in samples.items():
            if not v:
                continue
            m = re.match(r'^(\D*)(\d+)$', v)
            if k == 'HEA':
                self.codes[k] = (v.split('-')[0] + '-', 0)
            elif m and m.group(1):
                self.codes[k] = (m.group(1), len(m.group(2)))
            elif m:  # all digits, e.g. account numbers: keep the first 4 digits as the "prefix"
                self.codes[k] = (v[:4], len(v) - 4)

    def literals(self, s):
        """Healthcare code literals (PT-0000101, MED-00001, HEA-..., RX-..., LIC-...) in the domain's code format."""
        def rep(m):
            k, rest = m.group(1), m.group(2)
            if k not in self.codes:
                return m.group(0)
            pre, width = self.codes[k]
            if rest and rest.isdigit() and width:
                return pre + rest.zfill(width)[-width:]
            return pre + rest
        return re.sub(r'\b(PT|MED|HEA|RX|LIC)-([A-Za-z0-9-]*)', rep, s)

    # ---------- required extra columns on INSERT ----------
    def extra(self):
        E = [t for t in self.model['tables'] if t['name'] == self.model['base'][0]][0]
        gen = set(self.model['map'].values())
        cols = [c for c in E['columns'] if c['name'] not in gen and c['rule'] == 'NOT NULL']
        vals = ["'IN'" if c['name'] == 'Direction' else '1' for c in cols]
        return ''.join(', ' + c['name'] for c in cols), ''.join(', ' + v for v in vals)

    def p_extra(self):
        P = [t for t in self.model['tables'] if t['name'] == self.cfg['P'][0]][0]
        return [c['name'] for c in P['columns'] if c['name'] not in self.cfg['P'] and c['rule'] == 'NOT NULL']

    @staticmethod
    def _values_end(s, i):
        """Index just after the tuples of a VALUES list that starts at s[i] (right after the VALUES keyword)."""
        depth, q = 0, False
        while i < len(s):
            ch = s[i]
            if q:
                q = ch != "'"
            elif ch == "'":
                q = True
            elif ch == '(':
                depth += 1
            elif ch == ')':
                depth -= 1
            elif depth == 0 and ch not in ' \t\r\n,':
                return i
            i += 1
        return i

    @staticmethod
    def _add_to_tuples(seg, add):
        out, depth, q = [], 0, False
        for ch in seg:
            if q:
                q = ch != "'"
            elif ch == "'":
                q = True
            elif ch == '(':
                depth += 1
            elif ch == ')':
                depth -= 1
                if depth == 0:
                    out.append(add)
            out.append(ch)
        return ''.join(out)

    def p_inserts(self, s):
        """Party tables with extra NOT NULL foreign keys (banking, brokerage): add them to every INSERT."""
        cols = self.p_extra()
        if not cols:
            return s
        P = f"{self.slug}.{self.cfg['P'][0]}"
        add_c = ''.join(', ' + c for c in cols)
        add_v = ''.join(', 1' for _ in cols)
        pat = re.compile(r'INSERT\s+INTO\s+' + re.escape(P) + r'\s*(?:\(([^)]*)\))?\s*', re.I)
        out, pos = [], 0
        while True:
            m = pat.search(s, pos)
            if not m:
                out.append(s[pos:])
                break
            out.append(s[pos:m.start()])
            colist = m.group(1)
            out.append(f'INSERT INTO {P} ' + (f'({colist}{add_c})\n' if colist is not None else ''))
            i = m.end()
            if re.match(r'VALUES\b', s[i:], re.I):
                end = self._values_end(s, i + 6)
                out.append(s[i:i + 6] + self._add_to_tuples(s[i + 6:end], add_v))
                pos = end
            elif re.match(r'SELECT\b', s[i:], re.I):
                fm = re.search(r'\s+FROM\b|;|\n\s*UNION\b', s[i:], re.I)
                end = i + (fm.start() if fm else len(s) - i)
                out.append(s[i:end] + add_v)
                pos = end
            else:
                pos = i
        s = ''.join(out)
        if re.search(r'MERGE\s+' + re.escape(P) + r'\b', s, re.I):
            s = re.sub(r'(INSERT\s*\()([^)]*)(\)\s*VALUES\s*\()([^)]*)(\))',
                       lambda m: m.group(1) + m.group(2) + add_c + m.group(3) + m.group(4) + add_v + m.group(5), s, count=1)
        return s

    # ---------- code ----------
    def literal_words(self, lit):
        """Translate healthcare words inside a SQL string literal (codes and identifiers are left alone)."""
        def w(m):
            t = m.group(0)
            if t in ('Clinic', 'clinic'):
                return self.cfg['industry'] if t == 'Clinic' else self.cfg['industry'].lower()
            if t.lower() in ('visit', 'visits', 'encounter', 'encounters', 'patient', 'patients'):
                return self.noun(t)
            return t
        return re.sub(r'\b[A-Za-z]+\b', w, lit)

    def code(self, s):
        xc, xv = self.extra()
        s = s.replace('{{XC}}', xc).replace('{{XV}}', xv)
        s = self.literals(s)
        s = re.sub(r'\brx\b', 'li', s)
        s = WORD.sub(lambda m: self.ident(m.group(0)), s)
        s = re.sub(r"N?'[^'\n]*'|--[^\n]*", lambda m: self.literal_words(m.group(0)), s)
        s = self.p_inserts(s)
        return s.replace('Amerimed', self.cfg['short'].replace(' & ', '').replace(' ', ''))

    # ---------- prose ----------
    def noun(self, w):
        lw = w.lower()
        if lw in self.nouns:
            t = self.nouns[lw]
            return t[0].upper() + t[1:] if w[0].isupper() else t
        return None

    def prose(self, s):
        def word(m):
            w = m.group(0)
            if w in ('Encounters', 'Patients', 'Doctors', 'Medications', 'Prescriptions') or w in self.ids or not w.isalpha() \
                    or re.search(r'[a-z][A-Z]', w):
                return self.ident(w)
            if w == 'Amerimed':
                return self.cfg['short']
            if w == 'healthcare':
                return self.slug
            if w == 'Healthcare':
                return self.cfg['industry']
            r = self.noun(w)
            return r if r is not None else w
        s = self.literals(s)
        ev = self.nouns['encounter']
        s = re.sub(r'\bvisited\b', 'had ' + ('an ' if ev[0] in 'aeio' else 'a ') + ev, s)
        s = WORD.sub(word, s.replace('per-patient', 'per-' + self.nouns['patient']))
        # a/an before a word that now starts with a different sound
        heads = {v.split()[0].lower() for v in self.nouns.values()}
        s = re.sub(r'\b([Aa])n? (?=([A-Za-z]+))',
                   lambda m: (m.group(1) + ('n ' if m.group(2)[0].lower() in 'aeio' else ' '))
                   if m.group(2).lower() in heads else m.group(0), s)
        return s

    def text(self, s):
        """Prose with embedded code spans/blocks."""
        if not s:
            return s
        out, pos = [], 0
        for m in CODE.finditer(s):
            out.append(self.prose(s[pos:m.start()]))
            out.append(self.code(m.group(0)))
            pos = m.end()
        out.append(self.prose(s[pos:]))
        return ''.join(out)

    # ---------- numeric thresholds ----------
    def scale_amounts(self, sql, texts):
        """Rescale charge thresholds: row-level comparisons by quantile, totals by the ratio of the averages."""
        ratio = self.stats.get('amt')
        if not ratio:
            return sql, texts
        pat = re.compile(r'((?:\bCharge|Total\w*|ClosedCharge|SUM\([\w.]*Charge\))\s*(?:[<>]=?|=|<>)\s*)(\d+(?:\.\d+)?)'
                         r'|(\bCharge\s+BETWEEN\s+)(\d+(?:\.\d+)?)(\s+AND\s+)(\d+(?:\.\d+)?)')

        def nice(x, row=False):
            if row and self.stats.get('q'):
                hc, dom = self.stats['q']
                f = sum(1 for v in hc if v <= float(x)) / len(hc)
                v = dom[min(len(dom) - 1, max(0, round(f * len(dom)) - 1))]
            else:
                v = float(x) * ratio
            if v >= 100:
                mag = 10 ** (len(str(int(v))) - 2)
                return str(int(round(v / mag) * mag))
            return str(round(v, 2))

        mapping = {}

        def rep(m):
            if m.group(2):
                row = m.group(1).lstrip().startswith('Charge')
                mapping.setdefault(m.group(2), nice(m.group(2), row))
                return m.group(1) + mapping[m.group(2)]
            for g in (4, 6):
                mapping.setdefault(m.group(g), nice(m.group(g), True))
            return m.group(3) + mapping[m.group(4)] + m.group(5) + mapping[m.group(6)]
        sql = pat.sub(rep, sql)
        for k, t in texts.items():
            for n, v in mapping.items():
                t = re.sub(r'(?<![\w.-])' + re.escape(n) + r'(?![\w.])', v, t) if t else t
            texts[k] = t
        return sql, texts
