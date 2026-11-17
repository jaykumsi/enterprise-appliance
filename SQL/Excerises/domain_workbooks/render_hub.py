"""Render the SQL assignments hub: one card per domain company, linking to each domain's workbook page.

Usage: python render_hub.py [links.json]     links.json = {"healthcare": "https://claude.ai/artifact/...", "banking": ...}
Output: pages/hub.html
"""
import html
import json
import re
import sys
from pathlib import Path

from render_pages import ICONS, TEMPLATE, logo, words
from translate import MODELS
from wb_domains import DOMAINS

HERE = Path(__file__).resolve().parent

HEALTHCARE = dict(company='AmeriMed Healthcare', short='AmeriMed', industry='Healthcare', color='#2dd4bf', light='#0d9488',
                  tagline='Clinic network with patients, doctors, medications, encounters and prescriptions', icon='cross')
ORDER = ['healthcare', 'banking', 'brokerage', 'pharma', 'oil', 'retail', 'retail_inventory', 'retail_logistics',
         'retail_manufacturing']
CROSS = ('<rect x="1" y="1" width="46" height="46" rx="12" fill="{c}"/><path d="M19 9h10v10h10v10H29v10H19V29H9V19h10z" fill="#ffffff"/>'
         '<path d="M11 24h7l2.5-5 4 10 2.5-5h10" fill="none" stroke="{c}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>')


def card(slug, url):
    cfg = HEALTHCARE if slug == 'healthcare' else DOMAINS[slug]
    m = MODELS[slug]
    icon = CROSS.format(c='var(--dc)') if slug == 'healthcare' else logo(cfg, 'var(--dc)')
    chips = ''.join(f'<span>{t["name"]}</span>' for t in m['tables'])
    group = 'Maple &amp; Main group' if slug.startswith('retail') else cfg['industry']
    link = (f'<a class="open" href="{url}" target="_blank" rel="noopener">Open workbook '
            f'<svg class="i"><use href="#i-arrow"/></svg></a>') if url else '<span class="open soon">Link coming next</span>'
    return f'''<article class="dcard" style="--dc:{cfg['color']};--dl:{cfg['light']}">
        <div class="dtop"><svg class="dlogo" viewBox="0 0 48 48" aria-hidden="true">{icon}</svg>
          <div class="dname"><span class="dind">{html.escape(group)}</span><h3>{html.escape(cfg['company'])}</h3></div></div>
        <p class="dtag">{html.escape(cfg['tagline'])}.</p>
        <p class="dschema">Schema <code>{slug}</code> &middot; {len(m['tables'])} tables</p>
        <div class="chips" aria-label="Tables">{chips}</div>
        <div class="dfoot"><span class="qn"><strong>480</strong> questions &middot; 16 topics</span>{link}</div>
      </article>'''


def render(links):
    style = re.search(r'<style>\n/\* Layout: Tinitiate portal family.*?</style>', TEMPLATE, re.S).group(0)
    symbols = re.search(r'<svg width="0" height="0".*?</svg>\n', TEMPLATE, re.S).group(0)
    footer = re.search(r'<footer class="foot gutter">.*?</footer>', TEMPLATE, re.S).group(0)
    footer = footer.replace('This workbook covers SQL Server practice on the Amerimed healthcare dataset.',
                            'These workbooks cover SQL Server practice on nine fictional companies, one per industry.')
    footer = re.sub(r'<a class="nav-btn" href="#curriculum">.*?</a>\s*<a class="nav-btn" href="#workbench">.*?</a>',
                    '<a class="nav-btn" href="#domains"><svg class="i" style="color:var(--violet)"><use href="#i-grid"/></svg>All domains</a>',
                    footer, flags=re.S)
    footer = footer.replace('Amerimed Healthcare SQL Workbook', 'SQL Assignments by Domain')
    script_tail = re.search(r'\$\("#theme"\)\.onclick = .*?\n};\n', TEMPLATE, re.S).group(0)
    copy = re.search(r'function copyText\(.*?\n}\n', TEMPLATE, re.S).group(0)
    retail_note = ('The four Maple &amp; Main workbooks are divisions of one retailer: stores, merchandising (stock), '
                   'distribution (deliveries) and private label (manufacturing).')
    cards = '\n      '.join(card(s, links.get(s)) for s in ORDER)
    fav = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 48 48'%3E%3Crect x='1' y='1' width='46' "
           "height='46' rx='12' fill='%238b5cf6'/%3E%3Cpath d='M12 14h24M12 24h24M12 34h14' stroke='%23fff' stroke-width='4' "
           "stroke-linecap='round'/%3E%3C/svg%3E")
    hub_css = '''<style>
.domains { display: grid; grid-template-columns: repeat(auto-fill, minmax(min(100%, 330px), 1fr)); gap: 18px; }
.dcard { position: relative; overflow: hidden; display: flex; flex-direction: column; gap: 12px; padding: 22px; border-radius: var(--r-lg);
  border: 1.5px solid var(--line); background: var(--card); min-width: 0; transition: transform .25s cubic-bezier(.16, 1, .3, 1), border-color .25s ease, box-shadow .25s ease; }
.dcard { --dc-use: var(--dc); }
@media (prefers-color-scheme: light) { :root:not([data-theme="dark"]) .dcard { --dc-use: var(--dl); } }
:root[data-theme="light"] .dcard { --dc-use: var(--dl); }
.dcard::before { content: ""; position: absolute; inset: 0 0 auto; height: 3px; background: var(--dc-use); }
.dcard:hover { transform: translateY(-3px); border-color: color-mix(in srgb, var(--dc-use) 45%, transparent);
  box-shadow: var(--shadow), 0 0 24px color-mix(in srgb, var(--dc-use) 16%, transparent); }
.dtop { display: flex; align-items: center; gap: 14px; }
.dlogo { width: 46px; height: 46px; flex: none; }
.dname { min-width: 0; }
.dind { font: 700 .68rem var(--mono); letter-spacing: .07em; text-transform: uppercase; color: var(--dc-use); }
.dname h3 { margin: 2px 0 0; font-size: 1.18rem; font-weight: 800; letter-spacing: -0.01em; text-wrap: balance; }
.dtag { margin: 0; color: var(--muted); }
.dschema { margin: 0; font-size: .84rem; color: var(--dim); }
.chips { display: flex; flex-wrap: wrap; gap: 6px; }
.chips span { font: 600 .72rem var(--mono); padding: 3px 9px; border-radius: 20px; color: var(--muted); border: 1px solid var(--line);
  background: color-mix(in srgb, var(--ink) 3%, transparent); }
.dfoot { margin-top: auto; padding-top: 12px; border-top: 1px dashed var(--line); display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px; }
.qn { font-size: .84rem; color: var(--muted); font-variant-numeric: tabular-nums; }
.qn strong { font: 800 .95rem var(--mono); color: var(--ink); }
.open { display: inline-flex; align-items: center; gap: 6px; padding: 8px 14px; border-radius: var(--r-md); font-weight: 700; font-size: .86rem;
  text-decoration: none; color: var(--ink); border: 1px solid color-mix(in srgb, var(--dc-use) 50%, transparent);
  background: color-mix(in srgb, var(--dc-use) 14%, transparent); }
.open:hover { background: color-mix(in srgb, var(--dc-use) 24%, transparent); }
.open.soon { color: var(--dim); border-style: dashed; }
.note { margin: 18px 0 0; color: var(--muted); max-width: 80ch; }
.how { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 240px), 1fr)); gap: 14px; }
.how div { padding: 18px; border-radius: 16px; border: 1px solid var(--line); background: var(--card); }
.how h4 { margin: 0 0 6px; font-size: 1rem; font-weight: 800; }
.how p { margin: 0; color: var(--muted); font-size: .92rem; }
</style>'''
    return f'''<title>SQL Assignments by Domain</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="icon" href="{fav}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;700&display=swap">
<script>
  (function () {{
    try {{ var t = localStorage.getItem("tinitiate-theme"); if (t === "light" || t === "dark") document.documentElement.setAttribute("data-theme", t); }} catch (e) {{}}
  }})();
</script>
{style}
{hub_css}
{symbols}
<div class="glow a"></div>
<div class="glow b"></div>

<div class="shell">
  <header class="nav gutter">
    <div class="inner">
      <a class="brand" href="#top" aria-label="Tinitiate SQL assignments">
        <svg class="logo" viewBox="0 0 48 48" aria-hidden="true"><rect x="1" y="1" width="46" height="46" rx="12" fill="var(--violet)"/><path d="M12 14h24M12 24h24M12 34h14" stroke="#ffffff" stroke-width="4" stroke-linecap="round"/></svg>
        <span class="brand-name">Tinitiate</span>
        <span class="badge">SQL Assignments</span>
      </a>
      <nav class="nav-links" aria-label="Sections">
        <a class="nav-btn" href="https://tinitiateai.com" target="_blank" rel="noopener"><svg class="i"><use href="#i-home"/></svg>Academy Home</a>
        <a class="nav-btn" href="#domains"><svg class="i"><use href="#i-grid"/></svg>Domains</a>
        <a class="nav-btn" href="#how"><svg class="i"><use href="#i-flask"/></svg>How it works</a>
      </nav>
      <div class="nav-actions">
        <button id="theme" class="nav-btn" type="button" aria-label="Toggle light or dark theme"><svg class="i"><use href="#i-theme"/></svg></button>
        <span class="chip"><span class="dot"></span>Instructor <strong>Jayathirth Kumsiravinder</strong></span>
      </div>
    </div>
  </header>

  <section class="hero gutter" id="top">
    <div class="inner">
      <span class="eyebrow"><svg class="i"><use href="#i-db"/></svg>Tinitiate AI Academy &bull; SQL Server Track</span>
      <h1>Pick an Industry,<br><span class="grad">Practise SQL on Its Data</span></h1>
      <p class="sub">Nine fictional companies, one per industry. Each workbook has the same 16 topics and 480 questions, written for that company's own tables, with the expected result for every query so you can check your work.</p>
      <div class="stats">
        <span class="stat"><svg class="i" style="color:var(--violet)"><use href="#i-building"/></svg>Companies: <strong>9</strong></span>
        <span class="stat"><svg class="i" style="color:var(--cyan)"><use href="#i-grid"/></svg>Topics each: <strong>16</strong></span>
        <span class="stat"><svg class="i" style="color:var(--amber)"><use href="#i-db"/></svg>Questions: <strong>4,320</strong></span>
        <span class="stat"><svg class="i" style="color:var(--emerald)"><use href="#i-check"/></svg>Levels: <strong>B &middot; I &middot; A</strong></span>
      </div>
    </div>
  </section>

  <section class="sec gutter" id="domains">
    <div class="inner">
      <h2 class="sec-title"><svg class="i"><use href="#i-grid"/></svg>Choose a domain</h2>
      <p class="sec-sub">Each card opens that company's workbook in a new tab. Your Done ticks are saved per workbook, in your browser.</p>
      <div class="domains">
      {cards}
      </div>
      <p class="note">{retail_note}</p>
    </div>
  </section>

  <section class="sec gutter" id="how">
    <div class="inner">
      <h2 class="sec-title"><svg class="i"><use href="#i-flask"/></svg>How it works</h2>
      <p class="sec-sub">Every workbook follows the same path, so you can switch industries without relearning the layout.</p>
      <div class="how">
        <div><h4>Same 16 topics</h4><p>Introduction, DQL, operators, aggregates, joins, set operations, data types, DDL, constraints, DML, security, string and date functions, subqueries, CTEs and window functions.</p></div>
        <div><h4>10 / 10 / 10 per topic</h4><p>Beginner, Intermediate and Advanced questions. Advanced ones are interview patterns: top-N per group, running totals, gaps and islands, fan-out traps.</p></div>
        <div><h4>Check your own result</h4><p>Write and run your SQL first, then compare with the expected rows. A different query that returns the same rows is still correct.</p></div>
        <div><h4>One setup script</h4><p>Each domain folder has a <code>data_setup.sql</code>. Run it once in a new practice database and every question works.</p></div>
      </div>
    </div>
  </section>

  {footer}
</div>

<script>
const $ = s => document.querySelector(s);
{copy}{script_tail}document.querySelectorAll(".ccopy").forEach(b => b.onclick = () => copyText(b.dataset.copy, b, b.previousElementSibling));
</script>
'''


if __name__ == '__main__':
    links = json.loads(Path(sys.argv[1]).read_text()) if len(sys.argv) > 1 else {}
    out = HERE / 'pages' / 'hub.html'
    out.write_text(render(links), encoding='utf-8')
    print(out, out.stat().st_size // 1024, 'KB')
