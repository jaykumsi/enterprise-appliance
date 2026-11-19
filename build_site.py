"""Build the static site in the style of the SQL Assignments hub (domain_workbooks/render_hub.py).

Layout:
    index.html                             all companies (search + group filter), like the hub
    assets/site.css, assets/site.js        the hub's styles and behaviour, shared by every page
    domains/<company>/index.html           company home page
    domains/<company>/assignments.html     Assignments tab
    domains/<company>/control-tower.html   Control Tower tab (placeholder)
    domains/<company>/sql/                 the company's SQL data, questions and (private) solutions

Styles, icons, company colours/logos and the footer come straight from render_hub.py, so the site and the
online hub stay identical. Workbook URLs come from domain_workbooks/pages/links.json.

Usage: python build_site.py
"""
import html
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
DOMAINS = REPO / 'domains'
EX = DOMAINS / 'SQL' / 'Excerises'
WB = EX / 'domain_workbooks'
sys.path[:0] = [str(EX), str(WB)]

import render_hub as hub                      # noqa: E402  (CSS, SYMBOLS, SOCIAL, GROUPS, ORDER, HEALTHCARE)
from render_pages import logo                 # noqa: E402
from translate import MODELS                  # noqa: E402
from wb_domains import DOMAINS as WB_DOMAINS  # noqa: E402
from company_paths import FOLDERS             # noqa: E402

LINKS = json.loads((WB / 'pages' / 'links.json').read_text(encoding='utf-8'))
e = html.escape

GRADS = ['#8b7bff,#5b46f5', '#4fd1ff,#0891b2', '#ff6fb5,#db2777', '#a78bfa,#7c3aed', '#34d399,#059669', '#fbbf24,#f97316']

EXTRA_CSS = r'''
/* ---- site additions (company pages) ---- */
.app { --dc-use: var(--dc, var(--primary)); }
@media (prefers-color-scheme: light) { :root:not([data-theme="dark"]) .app { --dc-use: var(--dl, var(--primary)); } }
:root[data-theme="light"] .app { --dc-use: var(--dl, var(--primary)); }
.tb-btn[aria-current="page"] { background: #f1f1f3; color: #1f2023; border-color: #f1f1f3; }
.tb-btn[aria-current="page"]:hover { background: #fff; }
.sub-brand { text-decoration: none; }
.sub-brand sup { white-space: nowrap; }
.co-head { display: flex; align-items: center; gap: 18px; }
.co-head .app-icon { width: 72px; height: 72px; }
.co-head .kicker { color: var(--dc-use); }
.hero .actions { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 22px; }
.btn.outline { background: transparent; color: var(--dc-use); border: 1px solid color-mix(in srgb, var(--dc-use) 55%, transparent); box-shadow: none; }
.card-foot .links-2 { display: flex; gap: 8px; flex-wrap: wrap; justify-content: flex-end; }
.card-foot .btn { height: 38px; padding: 0 14px; }
.panel { position: relative; padding: 20px; border-radius: var(--r); background: var(--glass); border: 1px solid var(--line); box-shadow: var(--shadow);
  backdrop-filter: blur(20px) saturate(160%); -webkit-backdrop-filter: blur(20px) saturate(160%); margin-bottom: 18px; }
.panel p { margin: 0 0 14px; color: var(--muted); }
.ico.num { font: 800 .85rem var(--mono); }
.badge { font: 700 .7rem var(--mono); letter-spacing: .06em; text-transform: uppercase; padding: 4px 10px; border-radius: 99px;
  color: var(--dc-use); border: 1px dashed color-mix(in srgb, var(--dc-use) 50%, transparent); }
.soon { text-align: center; padding: 48px 20px; border-style: dashed; }
.soon .app-icon { width: 64px; height: 64px; margin: 0 auto 12px; display: block; }
.soon h2 { margin: 0 0 8px; font: 800 1.6rem var(--display); letter-spacing: -0.02em; }
.soon p { max-width: 60ch; margin: 0 auto; }
.stats.three { grid-template-columns: repeat(3, minmax(0, 1fr)); }
@media (max-width: 860px) { .stats.three { grid-template-columns: minmax(0, 1fr); } .co-head .app-icon { width: 56px; height: 56px; } }
'''

JS = r'''(function () {
  const $ = s => document.querySelector(s);
  const theme = $("#theme");
  if (theme) theme.addEventListener("click", () => {
    const r = document.documentElement;
    const light = r.dataset.theme ? r.dataset.theme === "light" : matchMedia("(prefers-color-scheme: light)").matches;
    r.dataset.theme = light ? "dark" : "light";
    try { localStorage.setItem("tinitiate-theme", r.dataset.theme); } catch (e) {}
  });
  const menu = $(".menu");
  if (menu) {
    document.addEventListener("click", e => { if (menu.open && !menu.contains(e.target)) menu.open = false; });
    document.addEventListener("keydown", e => { if (e.key === "Escape") menu.open = false; });
  }
  const seg = $("#seg");
  if (seg) {
    const thumb = seg.querySelector(".seg-thumb"), cards = [...document.querySelectorAll(".card")];
    let group = "all", query = "";
    const moveThumb = () => {
      const on = seg.querySelector('.seg-btn[aria-selected="true"]');
      if (!on) return;
      thumb.style.width = on.offsetWidth + "px";
      thumb.style.transform = "translateX(" + (on.offsetLeft - 4) + "px)";
    };
    const apply = () => {
      let shown = 0;
      cards.forEach(c => {
        const ok = (group === "all" || c.dataset.group === group) && (!query || c.dataset.search.includes(query));
        c.hidden = !ok; if (ok) shown++;
      });
      $("#empty").classList.toggle("show", shown === 0);
    };
    seg.querySelectorAll(".seg-btn").forEach(b => b.addEventListener("click", () => {
      seg.querySelectorAll(".seg-btn").forEach(x => x.setAttribute("aria-selected", x === b));
      group = b.dataset.group; moveThumb(); apply();
    }));
    $("#q").addEventListener("input", ev => { query = ev.target.value.trim().toLowerCase(); apply(); });
    window.addEventListener("resize", moveThumb);
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(moveThumb);
    moveThumb();
  }
  const copy = $("#copy");
  if (copy) copy.addEventListener("click", () => {
    const done = () => { copy.textContent = "Copied"; setTimeout(() => copy.textContent = "Copy", 1200); };
    const sel = () => { const r = document.createRange(); r.selectNodeContents($("#mail")); const s = getSelection(); s.removeAllRanges(); s.addRange(r); };
    try { navigator.clipboard.writeText($("#mail").textContent).then(done, sel); } catch (e) { sel(); }
  });
})();
'''


def cfg(slug):
    return hub.HEALTHCARE if slug == 'healthcare' else WB_DOMAINS[slug]


def icon_svg(slug, cls='app-icon'):
    c = cfg(slug)
    grad = (f'<defs><linearGradient id="g-{slug}" x1="0" y1="0" x2="1" y2="1">'
            f'<stop offset="0" stop-color="{c["color"]}"/><stop offset="1" stop-color="{c["light"]}"/></linearGradient></defs>')
    body = hub.CROSS.format(s=slug) if slug == 'healthcare' else logo(c, f'url(#g-{slug})').replace('rx="12"', 'rx="13"')
    return f'<svg class="{cls}" viewBox="0 0 48 48" aria-hidden="true">{grad}{body}</svg>'


def i(name):
    return f'<svg class="i" aria-hidden="true"><use href="#{name}"/></svg>'


def item(href, ico, grad, title, sub, external=False):
    tgt = ' target="_blank" rel="noopener"' if external else ''
    inner = (f'<span class="ico{" num" if not ico.startswith("i-") else ""}" style="--c:linear-gradient(135deg,{grad})">'
             f'{i(ico) if ico.startswith("i-") else e(ico)}</span>'
             f'<div class="item-body"><b>{title}</b><span>{sub}</span></div>')
    if href:
        return f'<li><a class="item" href="{href}"{tgt}>{inner}<span class="end">{i("i-chev")}</span></a></li>'
    return f'<li class="item">{inner}</li>'


def footer():
    socials = ''.join(f'<a class="social" style="--sc:{c}" href="{u}" target="_blank" rel="noopener">{i(ic)}{lbl}</a>'
                      for lbl, ic, c, u in hub.SOCIAL)
    return f'''<footer class="site-foot gutter" id="contact">
    <div class="wrap">
      <div class="foot-grid">
        <div>
          <h2 class="foot-h">{i("i-building")}Tinitiate AI Enterprise Domains</h2>
          <p class="foot-desc">Hands-on training on realistic company data, part of Tinitiate AI Academy's industry-aligned training
            that moves software engineers, cloud architects and data professionals into high-impact AI, GenAI and Distributed Lakehouse Engineering roles.</p>
          <span class="foot-label">Company social channels</span>
          <div class="socials">{socials}</div>
        </div>
        <div>
          <h2 class="foot-h contact">{i("i-phone")}Contact &amp; Call Us</h2>
          <div class="contact-row"><span class="contact-ico">{i("i-mail")}</span>
            <div><span class="foot-label">Email support</span><a href="mailto:contact@tinitiateai.com">contact@tinitiateai.com</a></div></div>
          <div class="contact-row"><span class="contact-ico">{i("i-globe")}</span>
            <div><span class="foot-label">Official portal</span><a href="https://tinitiateai.com" target="_blank" rel="noopener">tinitiateai.com</a></div></div>
        </div>
      </div>
      <div class="foot-base"><span>&copy; 2026 Tinitiate AI Academy. All rights reserved.</span><span>Fictional companies for practice only</span></div>
    </div>
  </footer>'''


def shell(title, root, body, sub_brand, nav, style=''):
    lam = '<svg class="lam" viewBox="0 0 20 20" aria-hidden="true"><path d="M1.6 20 10 1.5 18.4 20" fill="none" stroke="currentColor" stroke-width="3.6"/></svg>'
    menu = ''.join(
        f'<a href="{root}domains/{FOLDERS[s]}/index.html" style="--dc:{cfg(s)["color"]}"><i></i>{e(cfg(s)["company"])}'
        f'<small>{e(cfg(s)["industry"])}</small></a>' for s in hub.ORDER)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@700;800&family=JetBrains+Mono:wght@500;700&family=Krona+One&display=swap">
<script>
  (function () {{
    try {{ var t = localStorage.getItem("tinitiate-theme"); if (t === "light" || t === "dark") document.documentElement.setAttribute("data-theme", t); }} catch (e) {{}}
  }})();
</script>
<link rel="stylesheet" href="{root}assets/site.css">
</head>
<body>
{hub.SYMBOLS}
<div class="aurora" aria-hidden="true"><span></span><span></span><span></span></div>

<div class="app"{style}>
  <header class="toolbar gutter">
    <div class="wrap">
      <a class="brand" href="{root}index.html" aria-label="Tinitiate AI, all companies">
        <svg class="chev" viewBox="0 0 30 24" aria-hidden="true"><path d="M0 0h13l13 12-13 12H0l13-12z" fill="#f5d90a"/></svg>
        <span class="wordmark">TINITI{lam}TE<span class="gap"></span>{lam}I</span></a>
      {sub_brand}
      <nav class="tb-actions" aria-label="Main">
        {nav}
        <details class="menu"><summary class="tb-btn">{i("i-grid")}<span class="label">Companies</span><svg class="i caret" aria-hidden="true"><use href="#i-down"/></svg></summary>
          <div class="menu-panel">{menu}</div></details>
        <button id="theme" class="tb-btn icon" type="button" aria-label="Switch between light and dark theme">{i("i-sun")}</button>
      </nav>
    </div>
  </header>

{body}

  {footer()}
</div>
<script src="{root}assets/site.js"></script>
</body>
</html>
'''


def root_card(slug):
    c = cfg(slug)
    tables = [t['name'] for t in MODELS[slug]['tables']]
    chips = ''.join(f'<span class="chip">{t}</span>' for t in tables)
    label = 'Maple &amp; Main group' if slug.startswith('retail') else e(c['industry'])
    search = ' '.join([c['company'], c['industry'], slug, FOLDERS[slug], c['tagline']] + tables).lower()
    home = f'domains/{FOLDERS[slug]}/'
    return f'''<article class="card" data-group="{hub.group_of(slug)}" data-search="{e(search)}" style="--dc:{c['color']};--dl:{c['light']}">
          <div class="card-head">
            {icon_svg(slug)}
            <div class="card-title"><span class="kicker">{label}</span><h3>{e(c['company'])}</h3></div>
          </div>
          <p class="tagline">{e(c['tagline'])}.</p>
          <div class="meta"><span>{i("i-db")}<code>{FOLDERS[slug]}</code></span><span>{len(tables)} tables</span></div>
          <div class="chips" aria-label="Tables">{chips}</div>
          <div class="card-foot">
            <span class="count"><a href="{home}assignments.html">Assignments</a> &middot; <a href="{home}control-tower.html">Control Tower</a></span>
            <a class="btn" href="{home}index.html">Open{i("i-arrow")}</a>
          </div>
        </article>'''


def build_root():
    cards = '\n        '.join(root_card(s) for s in hub.ORDER)
    counts = {k: len(ds) for k, (_, ds) in hub.GROUPS.items()}
    segs = ''.join(f'<button class="seg-btn" type="button" role="tab" id="seg-{k}" data-group="{k}" aria-selected="false">'
                   f'{e(lbl)}<span class="n">{counts[k]}</span></button>' for k, (lbl, _) in hub.GROUPS.items())
    nav = (f'<a class="tb-btn plain" href="https://tinitiateai.com" target="_blank" rel="noopener">{i("i-home")}<span class="label">Academy</span></a>'
           f'<a class="tb-btn wide" href="{LINKS["hub"]}" target="_blank" rel="noopener">{i("i-file")}SQL workbooks</a>'
           f'<a class="tb-btn wide" href="#how">{i("i-layers")}How it works</a>')
    body = f'''  <section class="hero gutter" id="top">
    <div class="wrap">
      <span class="eyebrow"><span class="dot"></span>Tinitiate AI Academy &middot; Enterprise domains</span>
      <h1>Nine companies,<br><em>one business world</em></h1>
      <p>Every company has its own home page, Assignments and Control Tower, all built on the same realistic tables. Pick a company to start.</p>
      <div class="stats">
        <div class="stat"><strong>9</strong><span>companies</span></div>
        <div class="stat"><strong>{sum(len(MODELS[s]["tables"]) for s in hub.ORDER)}</strong><span>tables in total</span></div>
        <div class="stat"><strong>5,940</strong><span>levelled SQL questions per company</span></div>
        <div class="stat"><strong>490</strong><span>online workbook questions per company</span></div>
      </div>
    </div>
  </section>

  <div class="controls gutter">
    <div class="wrap">
      <label class="search" for="q">{i("i-search")}
        <input id="q" type="search" placeholder="Search companies or tables, e.g. Loans or Shipments" autocomplete="off"></label>
      <div class="seg-wrap"><div class="segment" id="seg" role="tablist" aria-label="Filter by group"><span class="seg-thumb"></span>
        <button class="seg-btn" type="button" role="tab" id="seg-all" data-group="all" aria-selected="true">All<span class="n">9</span></button>{segs}
      </div></div>
    </div>
  </div>

  <main class="section gutter" id="domains">
    <div class="wrap">
      <div class="cards" id="cards">
        {cards}
      </div>
      <p class="empty" id="empty">No company matches that search. Try a table name such as Orders, Batches or Executions.</p>
      <p class="note">The three Maple &amp; Main companies are divisions of one retailer: Stores (selling), Supply Chain (buying, making
        and stocking products) and Distribution (deliveries).</p>
    </div>
  </main>

  <section class="section gutter" id="how">
    <div class="wrap two">
      <div>
        <h2 class="h2">How it works</h2>
        <p class="sub">Every company follows the same layout, so switching industries never means relearning it.</p>
        <ul class="list">
          {item(None, "i-home", GRADS[0], "Company home", "Business focus, core tables and quick links.")}
          {item(None, "i-file", GRADS[1], "Assignments", "16 SQL topic books, interview practice and the online workbook.")}
          {item(None, "i-bars", GRADS[2], "Control Tower", "Operational overview for the company. Coming soon.")}
          {item(None, "i-db", GRADS[4], "Company data", "Each company folder has an <code>sql</code> subfolder with its setup scripts.")}
        </ul>
      </div>
      <div>
        <h2 class="h2">Shared resources</h2>
        <p class="sub">Curriculum, scripts and practice material used by every company.</p>
        <ul class="list">
          {item("docs.html?f=domains/SQL/Excerises/README.md", "i-layers", GRADS[3], "SQL curriculum", "Lessons, generators and validation scripts")}
          {item("docs.html?f=domains/SQL/Excerises/DOMAIN_ASSIGNMENTS.md", "i-file", GRADS[1], "SQL assignments by domain", "53,460 levelled questions across nine companies")}
          {item(LINKS["hub"], "i-grid", GRADS[0], "All online SQL workbooks", "Interactive workbooks with expected results", True)}
          {item("docs.html?f=interview-practice-bank/catalog.md", "i-check", GRADS[4], "Interview practice bank", "Cross-subject questions")}
        </ul>
      </div>
    </div>
  </section>'''
    (REPO / 'index.html').write_text(shell('Tinitiate Enterprise Domains', '', body, '<a class="sub-brand" href="#domains">Domains<sup>+academy</sup></a>', nav),
                                     encoding='utf-8')


def company_pages(slug):
    c = cfg(slug)
    folder = FOLDERS[slug]
    d = DOMAINS / folder
    q = d / 'sql' / 'questions'
    m = MODELS[slug]
    tables = [t['name'] for t in m['tables']]
    style = f' style="--dc:{c["color"]};--dl:{c["light"]}"'
    sub_brand = f'<a class="sub-brand" href="index.html">{e(c["short"])}<sup>{e(c["industry"].lower())}</sup></a>'

    def nav(active):
        tabs = [('index.html', 'Home', 'i-home', 'home'), ('assignments.html', 'Assignments', 'i-file', 'assignments'),
                ('control-tower.html', 'Control Tower', 'i-bars', 'tower')]
        return ''.join(f'<a class="tb-btn{" plain" if k != active else ""}" href="{h}"{" aria-current=\"page\"" if k == active else ""}>'
                       f'{i(ic)}<span class="label">{lbl}</span></a>' for h, lbl, ic, k in tabs)

    def head(eyebrow, title, text, actions=''):
        return f'''  <section class="hero gutter" id="top">
    <div class="wrap">
      <span class="eyebrow"><span class="dot"></span>{eyebrow}</span>
      <div class="co-head">{icon_svg(slug)}<h1>{title}</h1></div>
      <p>{text}</p>{actions}
    </div>
  </section>'''

    chips = ''.join(f'<span class="chip">{t}</span>' for t in tables)

    # Home
    home = head(f'{e(c["industry"])} &middot; Company home', e(c['company']), e(c['tagline']) + '.',
                f'<div class="actions"><a class="btn" href="assignments.html">Assignments{i("i-arrow")}</a>'
                f'<a class="btn outline" href="control-tower.html">Control Tower</a></div>') + f'''
  <section class="section gutter">
    <div class="wrap">
      <div class="stats" style="margin-top:0">
        <div class="stat"><strong>{len(tables)}</strong><span>tables</span></div>
        <div class="stat"><strong>16</strong><span>SQL topics</span></div>
        <div class="stat"><strong>5,940</strong><span>levelled questions</span></div>
        <div class="stat"><strong>490</strong><span>online workbook questions</span></div>
      </div>
    </div>
  </section>
  <section class="section gutter">
    <div class="wrap two">
      <div>
        <h2 class="h2">Business focus</h2>
        <p class="sub">What the data is for.</p>
        <div class="panel"><p>{e(m.get("business", ""))}</p><div class="chips" aria-label="Tables">{chips}</div></div>
      </div>
      <div>
        <h2 class="h2">Get started</h2>
        <p class="sub">Quick links for {e(c["short"])}.</p>
        <ul class="list">
          {item("assignments.html", "i-file", GRADS[0], "Assignments", "Interactive workbook: 16 topics + interview challenges")}
          {item(f"../../docs.html?f=domains/{folder}/sql/questions/README.md", "i-layers", GRADS[3], "Full question bank", "5,940 levelled questions in topic books")}
          {item("control-tower.html", "i-bars", GRADS[2], "Control Tower", "Operational overview (coming soon)")}
          {item(f"../../docs.html?f=domains/{folder}/sql/questions/DOMAIN_GUIDE.md", "i-db", GRADS[1], "Table definitions", "Columns, keys and sample rows")}
          {item(f"../../docs.html?f=domains/{folder}/sql/questions/PRACTICE_DATA.md", "i-layers", GRADS[4], "Large practice dataset", "Realistic volumes for practice")}
        </ul>
      </div>
    </div>
  </section>'''
    (d / 'index.html').write_text(shell(c['company'], '../../', home, sub_brand, nav('home'), style), encoding='utf-8')

    # Assignments: the interactive workbook, see workbook_page()
    workbook_page(slug)

    # Control Tower (placeholder)
    tower = head(f'{e(c["company"])} &middot; Control Tower', 'Control Tower',
                 f'Operational overview for {e(c["company"])}.') + f'''
  <section class="section gutter">
    <div class="wrap">
      <div class="panel soon">
        {icon_svg(slug)}
        <span class="badge">Coming soon</span>
        <h2 style="margin-top:14px">The control tower is on its way</h2>
        <p>This page is a placeholder. It will bring together key metrics, alerts and data pipeline status for {e(c["company"])}.</p>
      </div>
      <ul class="list">
        {item(None, "i-bars", GRADS[0], "Key metrics", "Daily business KPIs from the company tables")}
        {item(None, "i-check", GRADS[4], "Alerts", "Data quality and business rule checks")}
        {item(None, "i-layers", GRADS[1], "Pipeline status", "Loads, freshness and run history")}
      </ul>
    </div>
  </section>'''
    (d / 'control-tower.html').write_text(shell(f'{c["company"]} Control Tower', '../../', tower, sub_brand, nav('tower'), style),
                                          encoding='utf-8')


DOCS_CSS = r"""
.doc-crumb { display: flex; flex-wrap: wrap; align-items: center; gap: 6px; margin: 10px 0 14px; font: 600 .85rem var(--mono); color: var(--dim); }
.doc-crumb a { color: var(--primary); text-decoration: none; }
.doc-crumb a:hover { text-decoration: underline; }
.doc { padding: 28px clamp(18px, 4vw, 44px); overflow-wrap: anywhere; }
.doc h1 { font: 800 clamp(1.8rem, 4vw, 2.6rem)/1.1 var(--display); letter-spacing: -0.03em; margin: 0 0 16px; }
.doc h2 { font: 800 1.5rem var(--display); letter-spacing: -0.02em; margin: 36px 0 12px; padding-top: 12px; border-top: 1px solid var(--line); }
.doc h3 { font: 800 1.15rem var(--display); margin: 26px 0 8px; }
.doc h4 { font: 700 .82rem var(--mono); letter-spacing: .06em; color: var(--primary); margin: 26px 0 6px; }
.doc h2, .doc h3, .doc h4 { scroll-margin-top: 80px; }
.doc p, .doc li { color: var(--ink); line-height: 1.65; }
.doc a { color: var(--primary); }
.doc :target { background: color-mix(in srgb, var(--primary) 14%, transparent); border-radius: 6px; }
.doc table { display: block; max-width: 100%; overflow-x: auto; border-collapse: collapse; margin: 14px 0; font-size: .92rem; }
.doc th, .doc td { padding: 8px 12px; border: 1px solid var(--line-strong); text-align: left; }
.doc th { background: color-mix(in srgb, var(--primary) 10%, transparent); font-weight: 700; }
.doc code { padding: 1px 6px; border-radius: 6px; background: color-mix(in srgb, var(--primary) 10%, transparent); }
.doc pre { padding: 14px 16px; border-radius: 12px; overflow-x: auto; background: #0e0f1d; border: 1px solid var(--line); color: #e8e9ff; }
.doc pre code { padding: 0; background: none; font-size: .86rem; font-weight: 500; }
.doc blockquote { margin: 14px 0; padding: 4px 16px; border-left: 3px solid var(--primary); color: var(--muted); }
.doc hr { border: 0; border-top: 1px solid var(--line); margin: 28px 0; }
.doc-status { color: var(--muted); }
"""

DOCS_JS = r"""(function () {
  const params = new URLSearchParams(location.search);
  const f = (params.get("f") || "").split(String.fromCharCode(92)).join("/");
  const out = document.getElementById("doc"), crumb = document.getElementById("crumb");
  const fail = msg => { out.innerHTML = '<p class="doc-status"></p>'; out.firstChild.textContent = msg; };
  if (!/^[\w .&()+,'-]+(\/[\w .&()+,'-]+)*\.md$/.test(f) || f.split("/").includes("..")) { fail("No document selected."); return; }
  const parts = f.split("/");
  // breadcrumb: Home / domains / company (links to its home page) / ... / file
  let html = '<a href="index.html">Home</a>';
  parts.forEach((p, i) => {
    html += " / ";
    const company = i === 1 && parts[0] === "domains" && p !== "SQL";
    if (company) html += '<a href="domains/' + encodeURIComponent(p) + '/index.html"></a>';
    else html += "<span></span>";
  });
  crumb.innerHTML = html;
  [...crumb.querySelectorAll("a, span")].slice(1).forEach((el, i) => el.textContent = parts[i]);
  document.title = parts[parts.length - 1].replace(/\.md$/, "").replace(/_/g, " ") + " · Tinitiate";
  const base = new URL(f, location.href);
  fetch(f).then(r => { if (!r.ok) throw new Error(r.status); return r.text(); }).then(md => {
    out.innerHTML = marked.parse(md, { gfm: true });
    const seen = {};
    out.querySelectorAll("h1,h2,h3,h4,h5,h6").forEach(h => {
      let id = h.textContent.trim().toLowerCase().replace(/[^\w\- ]+/g, "").replace(/ /g, "-");
      if (seen[id] !== undefined) { seen[id]++; id += "-" + seen[id]; } else seen[id] = 0;
      h.id = id;
    });
    const root = new URL(".", location.href);
    out.querySelectorAll("a[href]").forEach(a => {
      const href = a.getAttribute("href");
      if (/^([a-z]+:|#)/i.test(href)) { if (/^https?:/i.test(href)) { a.target = "_blank"; a.rel = "noopener"; } return; }
      const u = new URL(href, base);
      if (!u.href.startsWith(root.href)) return;
      const rel = decodeURIComponent(u.pathname.slice(root.pathname.length));
      a.href = /\.md$/i.test(rel) ? "docs.html?f=" + encodeURIComponent(rel).replace(/%2F/g, "/") + u.hash : u.href;
    });
    out.querySelectorAll("img[src]").forEach(img => { img.src = new URL(img.getAttribute("src"), base).href; });
    if (location.hash) { const t = document.getElementById(decodeURIComponent(location.hash.slice(1))); if (t) t.scrollIntoView(); }
  }).catch(() => fail("Could not load " + f + ". Open the site through a web server (for example: python -m http.server)."));
})();
"""


def build_docs():
    """docs.html?f=<path>.md renders any Markdown file in the repository with the site's look."""
    nav = f'<a class="tb-btn plain" href="index.html">{i("i-home")}<span class="label">All companies</span></a>'
    body = f"""  <main class="section gutter">
    <div class="wrap">
      <nav class="doc-crumb" id="crumb" aria-label="Breadcrumb"></nav>
      <article class="panel doc" id="doc"><p class="doc-status">Loading…</p></article>
    </div>
  </main>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/marked/12.0.2/marked.min.js"></script>
  <script src="assets/docs.js"></script>"""
    (REPO / 'assets' / 'docs.js').write_text(DOCS_JS, encoding='utf-8')
    (REPO / 'docs.html').write_text(shell('Tinitiate Docs', '', body, '<a class="sub-brand" href="index.html">Docs<sup>+academy</sup></a>', nav),
                                    encoding='utf-8')


WB_NAV_CSS = '''<style>
.tn-btn[aria-current="page"] { background: #f1f1f3; color: #1f2023; border-color: #f1f1f3; }
.tn-btn[aria-current="page"]:hover { background: #fff; }
.tn-panel a[aria-current="page"] { background: #2b2c31; }
</style>'''


def workbook_header(slug):
    """The site's company header, built from the workbook's own tn- header classes (site_chrome.py)."""
    import site_chrome
    c = cfg(slug)
    lam = site_chrome.LAM

    def ti(name):
        return f'<svg class="i" aria-hidden="true"><use href="#tn-{name}"/></svg>'
    menu = f'<a href="../../index.html" style="--tn-dc:#f5d90a"><i></i>All companies<small>home</small></a><hr>' + ''.join(
        f'<a href="../{FOLDERS[s]}/assignments.html"{" aria-current=\"page\"" if s == slug else ""} style="--tn-dc:{cfg(s)["color"]}"><i></i>'
        f'{e(cfg(s)["company"])}<small>{e(cfg(s)["industry"])}</small></a>' for s in hub.ORDER)
    return f'''<!--tn-header-->
  <header class="tn-bar gutter">
    <div class="tn-wrap">
      <a class="tn-brand" href="../../index.html" aria-label="Tinitiate AI, all companies">
        <svg class="tn-chev" viewBox="0 0 30 24" aria-hidden="true"><path d="M0 0h13l13 12-13 12H0l13-12z" fill="#f5d90a"/></svg>
        <span class="tn-word">TINITI{lam}TE<span class="tn-gap"></span>{lam}I</span></a>
      <a class="tn-sub" href="index.html">{e(c["short"])}<sup>assignments</sup></a>
      <nav class="tn-acts" aria-label="Main">
        <a class="tn-btn tn-plain" href="index.html">{ti("i-home")}<span class="tn-lbl">Home</span></a>
        <a class="tn-btn" href="assignments.html" aria-current="page">{ti("i-file")}<span class="tn-lbl">Assignments</span></a>
        <a class="tn-btn tn-plain" href="control-tower.html">{ti("i-bars")}<span class="tn-lbl">Control Tower</span></a>
        <details class="tn-menu"><summary class="tn-btn">{ti("i-grid")}<span class="tn-lbl">Companies</span><svg class="i tn-caret" aria-hidden="true"><use href="#tn-i-down"/></svg></summary>
          <div class="tn-panel">{menu}</div></details>
        <a class="tn-btn tn-wide" href="#curriculum">{ti("i-layers")}Topics</a>
        <button id="jumpSearch" class="tn-btn tn-push" type="button">{ti("i-search")}<span class="tn-lbl">Search</span> <span class="kbd">/</span></button>
        <button id="theme" class="tn-btn tn-icon" type="button" aria-label="Switch between light and dark theme">{ti("i-sun")}</button>
      </nav>
    </div>
  </header>
<!--/tn-header-->'''


def workbook_page(slug):
    """Assignments tab = the company's interactive SQL workbook (pages/<slug>.html), with the site header."""
    import re
    src = WB / 'pages' / f'{slug}.html'
    s = src.read_text(encoding='utf-8')
    s = re.sub(r'<!--tn-header-->.*?<!--/tn-header-->', lambda _: workbook_header(slug), s, count=1, flags=re.S)
    # links to other online workbooks / the hub -> the local pages
    for other, url in LINKS.items():
        local = '../../index.html' if other == 'hub' else f'../{FOLDERS[other]}/assignments.html' if other in FOLDERS else None
        if local:
            s = s.replace(f'href="{url}" target="_blank" rel="noopener"', f'href="{local}"').replace(f'href="{url}"', f'href="{local}"')
    s = re.sub(r'<title>.*?</title>', f'<title>{e(cfg(slug)["company"])} Assignments</title>', s, count=1)
    i = s.index('</style>') + len('</style>')
    s = s[:i] + '\n' + WB_NAV_CSS + s[i:]
    head = '<!doctype html>\n<meta charset="utf-8">\n'
    if 'name="viewport"' not in s:
        head += '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    (DOMAINS / FOLDERS[slug] / 'assignments.html').write_text(head + s, encoding='utf-8')


def build():
    assets = REPO / 'assets'
    assets.mkdir(exist_ok=True)
    css = hub.CSS.strip().removeprefix('<style>').removesuffix('</style>')
    (assets / 'site.css').write_text(css.strip() + '\n' + EXTRA_CSS + DOCS_CSS, encoding='utf-8')
    (assets / 'site.js').write_text(JS, encoding='utf-8')
    build_root()
    build_docs()
    for slug in hub.ORDER:
        company_pages(slug)
    print(f'Built index.html and {len(hub.ORDER)} company sites.')


if __name__ == '__main__':
    build()
