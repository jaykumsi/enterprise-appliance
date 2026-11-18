"""The hub's Tinitiate AI header and black footer, applied to the workbook pages (student and instructor).

Everything here is namespaced with "tn-" so it never collides with the workbook page's own classes, and it uses fixed
colours (charcoal header, black footer) that look the same in light and dark themes, exactly like the hub.
The page's own working controls keep their ids: #jumpSearch (search) and #theme (theme toggle).

apply(s, slug, instructor=False) replaces the page's <header class="nav ..."> and <footer class="foot ..."> (or a
header/footer added by an earlier run) and returns the new page text.
"""
import html
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
HEADER_RE = re.compile(r'<!--tn-header-->.*?<!--/tn-header-->|<header class="nav gutter">.*?</header>', re.S)
FOOTER_RE = re.compile(r'<!--tn-footer-->.*?<!--/tn-footer-->|<footer class="foot gutter">.*?</footer>', re.S)
ASSETS_RE = re.compile(r'<!--tn-assets-->.*?<!--/tn-assets-->\n?', re.S)

CSS = '''<style>
/* Tinitiate AI site header + footer (same as the assignments hub) */
.tn-bar { position: sticky; top: env(safe-area-inset-top, 0px); z-index: 50; padding-block: 10px; background: #1f2023;
  border-bottom: 1px solid #000; box-shadow: 0 6px 24px rgba(0,0,0,.35); color-scheme: dark; }
.tn-bar .tn-wrap, .tn-foot .tn-wrap { max-width: 1240px; margin: 0 auto; }
.tn-bar .tn-wrap { display: flex; align-items: center; gap: 20px; }
.tn-brand { display: flex; align-items: center; gap: 10px; text-decoration: none; color: #fff; flex: none; }
.tn-brand .tn-chev { width: 30px; height: 24px; flex: none; }
.tn-word { display: inline-flex; align-items: center; gap: .04em; font: 400 1.5rem/1 "Krona One", "Inter", sans-serif; letter-spacing: .02em; white-space: nowrap; }
.tn-word .tn-lam { width: .82em; height: .78em; margin: 0 .02em; }
.tn-word .tn-gap { width: .45em; }
.tn-sub { position: relative; display: flex; align-items: center; padding-left: 20px; border-left: 1px solid #3a3b40; flex: none;
  font: 800 1.3rem/1 "Plus Jakarta Sans", "Inter", sans-serif; color: #fff; text-decoration: none; letter-spacing: -0.01em; white-space: nowrap; }
.tn-sub sup { position: absolute; top: -10px; right: -8px; font: 500 .66rem "JetBrains Mono", monospace; color: #f5d90a; letter-spacing: 0; white-space: nowrap; }
.tn-sub.tn-key sup { color: #c4b5fd; }
.tn-acts { display: flex; align-items: center; gap: 8px; flex: 1; min-width: 0; }
.tn-btn { display: inline-flex; align-items: center; gap: 8px; height: 38px; padding: 0 13px; border-radius: 8px; cursor: pointer;
  color: #f1f1f3; background: transparent; border: 1px solid #44464c; font: 700 .86rem "Inter", sans-serif; text-decoration: none;
  white-space: nowrap; transition: background .2s ease, border-color .2s ease; list-style: none; transform: none; }
.tn-btn::-webkit-details-marker { display: none; }
.tn-btn.tn-plain { border-color: transparent; }
.tn-btn:hover { background: #2b2c31; border-color: #5a5c63; color: #fff; }
.tn-btn svg.i { width: 16px; height: 16px; }
.tn-btn .tn-caret { width: 14px; height: 14px; transition: transform .2s ease; }
.tn-btn .kbd { font: 600 .7rem "JetBrains Mono", monospace; padding: 1px 6px; border-radius: 5px; border: 1px solid #44464c; color: #b9b9c4; }
.tn-push { margin-left: auto; }
.tn-btn.tn-icon { width: 38px; padding: 0; justify-content: center; }
.tn-menu { position: relative; }
.tn-menu[open] .tn-caret { transform: rotate(180deg); }
.tn-panel { position: absolute; top: calc(100% + 8px); left: 0; z-index: 60; min-width: 300px; padding: 6px; border-radius: 12px;
  background: #1f2023; border: 1px solid #3a3b40; box-shadow: 0 18px 40px rgba(0,0,0,.5); }
.tn-panel p { margin: 4px 10px 6px; font: 700 .68rem "Inter", sans-serif; letter-spacing: .1em; text-transform: uppercase; color: #8a8a98; }
.tn-panel a { display: flex; align-items: center; gap: 10px; padding: 9px 10px; border-radius: 8px; color: #f1f1f3; text-decoration: none; font-size: .88rem; }
.tn-panel a:hover { background: #2b2c31; }
.tn-panel a[aria-current="page"] { background: #2b2c31; box-shadow: inset 3px 0 0 var(--tn-dc); }
.tn-panel a i { width: 10px; height: 10px; border-radius: 3px; background: var(--tn-dc); flex: none; }
.tn-panel a small { margin-left: auto; color: #9a9aa8; font-size: .74rem; }
.tn-panel hr { border: 0; border-top: 1px solid #3a3b40; margin: 6px 4px; }
@media (max-width: 1100px) { .tn-wide { display: none; } }
@media (max-width: 760px) { .tn-sub { display: none; } }
@media (max-width: 560px) {
  .tn-word { font-size: 1.05rem; } .tn-brand .tn-chev { width: 22px; height: 18px; }
  .tn-bar .tn-wrap { gap: 8px; } .tn-acts { gap: 4px; } .tn-btn { padding: 0 10px; } .tn-lbl, .tn-btn .kbd { display: none; }
  .tn-panel { position: fixed; left: 16px; right: 16px; top: 64px; min-width: 0; }
}

.tn-foot { margin-top: 48px; padding-block: 48px 28px; background: #000; color: #c9c9d3; color-scheme: dark; border-top: 1px solid rgba(255,255,255,.12); }
.tn-fgrid { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 300px); gap: 48px; }
.tn-fh { display: flex; align-items: center; gap: 10px; margin: 0 0 16px; padding-bottom: 16px; border-bottom: 1px solid rgba(255,255,255,.12);
  font: 800 1.2rem "Plus Jakarta Sans", "Inter", sans-serif; letter-spacing: -0.01em; color: #f4f4f7; }
.tn-fh svg.i { width: 22px; height: 22px; color: #4fd1ff; }
.tn-fh.tn-contact svg.i { color: #34d399; }
.tn-fdesc { margin: 0 0 18px; max-width: 62ch; color: #c9c9d3; line-height: 1.6; }
.tn-flabel { display: block; margin-bottom: 10px; font: 700 .72rem "Inter", sans-serif; letter-spacing: .1em; text-transform: uppercase; color: #9a9aa8; }
.tn-socials { display: flex; flex-wrap: wrap; gap: 10px; }
.tn-social { display: inline-flex; align-items: center; gap: 9px; height: 42px; padding: 0 16px; border-radius: 10px; text-decoration: none;
  font: 700 .88rem "Inter", sans-serif; color: #f4f4f7; background: #141418; border: 1px solid rgba(255,255,255,.16);
  transition: transform .2s ease, border-color .2s ease, background .2s ease; }
.tn-social:hover { transform: translateY(-2px); border-color: var(--tn-sc); background: color-mix(in srgb, var(--tn-sc) 10%, #141418); }
.tn-social svg.i { width: 17px; height: 17px; color: var(--tn-sc); }
.tn-crow { display: flex; gap: 14px; align-items: flex-start; }
.tn-crow + .tn-crow { margin-top: 18px; }
.tn-cico { display: grid; place-items: center; width: 38px; height: 38px; flex: none; border-radius: 10px;
  background: #141418; border: 1px solid rgba(255,255,255,.16); color: #4fd1ff; }
.tn-cico svg.i { width: 18px; height: 18px; }
.tn-crow a { color: #4fd1ff; font-weight: 700; text-decoration: none; overflow-wrap: anywhere; }
.tn-crow a:hover { text-decoration: underline; }
.tn-instr b { display: block; color: #f4f4f7; font-weight: 700; }
.tn-role { display: block; margin-top: 2px; font-size: .85rem; color: #9a9aa8; }
.tn-plinks { display: flex; gap: 14px; margin-top: 6px; font-size: .88rem; }
.tn-fbase { margin-top: 36px; padding-top: 18px; border-top: 1px solid rgba(255,255,255,.12); color: #9a9aa8; font-size: .82rem;
  display: flex; flex-wrap: wrap; justify-content: space-between; gap: 8px; }
@media (max-width: 860px) { .tn-fgrid { grid-template-columns: minmax(0, 1fr); gap: 32px; } }
@media (prefers-reduced-motion: reduce) { .tn-btn, .tn-social, .tn-caret { transition: none !important; } }
</style>'''

MENU_JS = '''<script>
(function () {
  var m = document.querySelector(".tn-menu"); if (!m) return;
  document.addEventListener("click", function (e) { if (m.open && !m.contains(e.target)) m.open = false; });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") m.open = false; });
})();
</script>'''

LAM = '<svg class="tn-lam" viewBox="0 0 20 20" aria-hidden="true"><path d="M1.6 20 10 1.5 18.4 20" fill="none" stroke="currentColor" stroke-width="3.6"/></svg>'
FONTS = 'family=Krona+One&family=Plus+Jakarta+Sans:wght@700;800&'


def _links(name):
    p = HERE / 'pages' / name
    return json.loads(p.read_text()) if p.exists() else {}


def _symbols():
    from render_hub import SYMBOLS
    return re.sub(r'id="i-', 'id="tn-i-', SYMBOLS)


def _cfg(slug):
    from render_hub import HEALTHCARE
    from wb_domains import DOMAINS
    return HEALTHCARE if slug == 'healthcare' else DOMAINS[slug]


def header(slug, instructor=False):
    from render_hub import ORDER
    student, keys = _links('links.json'), _links('instructor_links.json')
    hub = student.get('hub', '#top')
    cfg = _cfg(slug)

    def entry(s, url):
        c = _cfg(s)
        cur = ' aria-current="page"' if s == slug else ''
        return (f'<a href="{url}" target="_blank" rel="noopener"{cur} style="--tn-dc:{c["color"]}"><i></i>'
                f'{html.escape(c["company"])}<small>{html.escape(c["industry"])}</small></a>')
    if instructor:
        menu = '<p>Instructor answer keys</p>' + ''.join(entry(s, keys[s]) for s in ORDER if keys.get(s))
        menu += f'<hr><p>Student pages</p><a href="{hub}" target="_blank" rel="noopener" style="--tn-dc:#f5d90a"><i></i>All workbooks (hub)</a>'
        if student.get(slug):
            menu += entry(slug, student[slug]).replace(' aria-current="page"', '').replace('<small>', '<small>student page · ')
        sub = (f'<a class="tn-sub tn-key" href="#top">{html.escape(cfg["short"])}<sup>instructor key</sup></a>')
    else:
        menu = f'<a href="{hub}" target="_blank" rel="noopener" style="--tn-dc:#f5d90a"><i></i>All workbooks<small>hub</small></a><hr>'
        menu += ''.join(entry(s, student[s]) for s in ORDER if student.get(s))
        sub = f'<a class="tn-sub" href="#top">{html.escape(cfg["short"])}<sup>workbook</sup></a>'
    return f'''<!--tn-header-->
  <header class="tn-bar gutter">
    <div class="tn-wrap">
      <a class="tn-brand" href="{hub}" target="_blank" rel="noopener" aria-label="Tinitiate AI, all SQL assignments">
        <svg class="tn-chev" viewBox="0 0 30 24" aria-hidden="true"><path d="M0 0h13l13 12-13 12H0l13-12z" fill="#f5d90a"/></svg>
        <span class="tn-word">TINITI{LAM}TE<span class="tn-gap"></span>{LAM}I</span></a>
      {sub}
      <nav class="tn-acts" aria-label="Main">
        <a class="tn-btn tn-plain tn-wide" href="https://tinitiateai.com" target="_blank" rel="noopener"><svg class="i" aria-hidden="true"><use href="#tn-i-home"/></svg>Home</a>
        <details class="tn-menu"><summary class="tn-btn"><svg class="i" aria-hidden="true"><use href="#tn-i-grid"/></svg><span class="tn-lbl">Workbooks</span><svg class="i tn-caret" aria-hidden="true"><use href="#tn-i-down"/></svg></summary>
          <div class="tn-panel">{menu}</div></details>
        <a class="tn-btn tn-wide" href="#start-here"><svg class="i" aria-hidden="true"><use href="#tn-i-file"/></svg>Start here</a>
        <a class="tn-btn tn-wide" href="#curriculum"><svg class="i" aria-hidden="true"><use href="#tn-i-layers"/></svg>Topics</a>
        <a class="tn-btn tn-wide" href="#contact"><svg class="i" aria-hidden="true"><use href="#tn-i-mail"/></svg>Contact</a>
        <button id="jumpSearch" class="tn-btn tn-push" type="button"><svg class="i" aria-hidden="true"><use href="#tn-i-search"/></svg><span class="tn-lbl">Search</span> <span class="kbd">/</span></button>
        <button id="theme" class="tn-btn tn-icon" type="button" aria-label="Switch between light and dark theme"><svg class="i" aria-hidden="true"><use href="#tn-i-sun"/></svg></button>
      </nav>
    </div>
  </header>
<!--/tn-header-->'''


def footer(slug, instructor=False):
    from render_hub import SOCIAL
    cfg = _cfg(slug)
    socials = ''.join(f'<a class="tn-social" style="--tn-sc:{c}" href="{u}" target="_blank" rel="noopener">'
                      f'<svg class="i" aria-hidden="true"><use href="#tn-{i}"/></svg>{l}</a>' for l, i, c, u in SOCIAL)
    label = f'{html.escape(cfg["company"])} {"Instructor Answer Key" if instructor else "SQL Workbook"}'
    return f'''<!--tn-footer-->
  <footer class="tn-foot gutter" id="contact">
    <div class="tn-wrap">
      <div class="tn-fgrid">
        <div>
          <h2 class="tn-fh"><svg class="i" aria-hidden="true"><use href="#tn-i-building"/></svg>Tinitiate AI Assignments</h2>
          <p class="tn-fdesc">Hands-on SQL assignments on realistic company data, part of Tinitiate AI Academy's industry-aligned training
            that moves software engineers, cloud architects and data professionals into high-impact AI, GenAI and Distributed Lakehouse Engineering roles.</p>
          <span class="tn-flabel">Company social channels</span>
          <div class="tn-socials">{socials}</div>
        </div>
        <div>
          <h2 class="tn-fh tn-contact"><svg class="i" aria-hidden="true"><use href="#tn-i-phone"/></svg>Contact &amp; Call Us</h2>
          <div class="tn-crow"><span class="tn-cico"><svg class="i" aria-hidden="true"><use href="#tn-i-mail"/></svg></span>
            <div><span class="tn-flabel">Email support</span><a href="mailto:contact@tinitiateai.com">contact@tinitiateai.com</a></div></div>
          <div class="tn-crow"><span class="tn-cico"><svg class="i" aria-hidden="true"><use href="#tn-i-globe"/></svg></span>
            <div><span class="tn-flabel">Official portal</span><a href="https://tinitiateai.com" target="_blank" rel="noopener">tinitiateai.com</a></div></div>
          <div class="tn-crow tn-instr"><span class="tn-cico"><svg class="i" aria-hidden="true"><use href="#tn-i-user"/></svg></span>
            <div><span class="tn-flabel">Your instructor</span><b>Jayathirth Kumsiravinder</b><span class="tn-role">Director and Instructor, Tinitiate AI Academy</span>
              <span class="tn-plinks"><a href="https://www.linkedin.com/in/jayathirth-kumsi" target="_blank" rel="noopener">LinkedIn</a><a href="https://github.com/jaykumsi" target="_blank" rel="noopener">GitHub</a></span></div></div>
        </div>
      </div>
      <div class="tn-fbase"><span>&copy; 2026 Tinitiate AI Academy. All rights reserved.</span><span>{label}</span></div>
    </div>
  </footer>
'''+MENU_JS+'''
<!--/tn-footer-->'''


def apply(s, slug, instructor=False):
    assert HEADER_RE.search(s) and FOOTER_RE.search(s), slug
    s = HEADER_RE.sub(lambda _: header(slug, instructor), s, count=1)
    s = FOOTER_RE.sub(lambda _: footer(slug, instructor), s, count=1)
    s = ASSETS_RE.sub('', s)
    # fonts, styles, icons and the dropdown script, added once right after the page's own <style>
    if 'Krona+One' not in s:
        s = s.replace('fonts.googleapis.com/css2?', 'fonts.googleapis.com/css2?' + FONTS, 1)
    i = s.index('</style>') + len('</style>')
    s = s[:i] + '\n<!--tn-assets-->' + CSS + _symbols() + '<!--/tn-assets-->\n' + s[i:]
    return s
