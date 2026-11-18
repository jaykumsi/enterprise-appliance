"""Render the SQL assignments hub: an Ionic-style home page with one card per domain company.

Usage: python render_hub.py [links.json]     links.json = {"healthcare": "https://claude.ai/artifact/...", "banking": ...}
Output: pages/hub.html
"""
import html
import json
import sys
from pathlib import Path

from render_pages import logo
from translate import MODELS
from wb_domains import DOMAINS

HERE = Path(__file__).resolve().parent

HEALTHCARE = dict(company='AmeriMed Healthcare', short='AmeriMed', industry='Healthcare', color='#2dd4bf', light='#0d9488',
                  tagline='Clinic network with patients, doctors, medications, encounters and prescriptions', icon='cross')
GROUPS = {  # segment filter: key -> (label, domains)
    'finance': ('Health & Finance', ['healthcare', 'banking', 'brokerage']),
    'industry': ('Pharma, Energy & Online', ['pharma', 'oil', 'ecommerce']),
    'maple': ('Maple & Main', ['retail', 'retail_supply_chain', 'retail_logistics']),
}
ORDER = [d for _, ds in GROUPS.values() for d in ds]
CROSS = ('<rect x="1" y="1" width="46" height="46" rx="13" fill="url(#g-{s})"/><path d="M19 9h10v10h10v10H29v10H19V29H9V19h10z" fill="#ffffff"/>'
         '<path d="M11 24h7l2.5-5 4 10 2.5-5h10" fill="none" stroke="var(--dc-use)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>')


def group_of(slug):
    return next(k for k, (_, ds) in GROUPS.items() if slug in ds)


def card(slug, url):
    cfg = HEALTHCARE if slug == 'healthcare' else DOMAINS[slug]
    m = MODELS[slug]
    grad = (f'<defs><linearGradient id="g-{slug}" x1="0" y1="0" x2="1" y2="1">'
            f'<stop offset="0" stop-color="{cfg["color"]}"/><stop offset="1" stop-color="{cfg["light"]}"/></linearGradient></defs>')
    if slug == 'healthcare':
        icon = grad + CROSS.format(s=slug)
    else:
        icon = grad + logo(cfg, f'url(#g-{slug})').replace('rx="12"', 'rx="13"')
    tables = [t['name'] for t in m['tables']]
    chips = ''.join(f'<span class="chip">{t}</span>' for t in tables)
    label = 'Maple &amp; Main group' if slug.startswith('retail') else html.escape(cfg['industry'])
    search = ' '.join([cfg['company'], cfg['industry'], slug, cfg['tagline']] + tables).lower()
    action = (f'<a class="btn" href="{url}" target="_blank" rel="noopener">Open workbook'
              f'<svg class="i" aria-hidden="true"><use href="#i-arrow"/></svg></a>') if url else '<span class="btn ghost">Coming soon</span>'
    return f'''<article class="card" data-group="{group_of(slug)}" data-search="{html.escape(search)}" style="--dc:{cfg['color']};--dl:{cfg['light']}">
          <div class="card-head">
            <svg class="app-icon" viewBox="0 0 48 48" aria-hidden="true">{icon}</svg>
            <div class="card-title"><span class="kicker">{label}</span><h3>{html.escape(cfg['company'])}</h3></div>
          </div>
          <p class="tagline">{html.escape(cfg['tagline'])}.</p>
          <div class="meta"><span><svg class="i" aria-hidden="true"><use href="#i-db"/></svg><code>{slug}</code></span><span>{len(tables)} tables</span></div>
          <div class="chips" aria-label="Tables">{chips}</div>
          <div class="card-foot">
            <span class="count"><strong>490</strong> questions<br><small>16 topics + 10 interview challenges</small></span>
            {action}
          </div>
        </article>'''


SYMBOLS = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <symbol id="i-home" viewBox="0 0 24 24"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 22V12h6v10"/></symbol>
  <symbol id="i-search" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></symbol>
  <symbol id="i-sun" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></symbol>
  <symbol id="i-db" viewBox="0 0 24 24"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5v14c0 1.7 4 3 9 3s9-1.3 9-3V5"/><path d="M3 12c0 1.7 4 3 9 3s9-1.3 9-3"/></symbol>
  <symbol id="i-grid" viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></symbol>
  <symbol id="i-arrow" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></symbol>
  <symbol id="i-layers" viewBox="0 0 24 24"><path d="m12 2 10 5-10 5L2 7z"/><path d="m2 17 10 5 10-5M2 12l10 5 10-5"/></symbol>
  <symbol id="i-bars" viewBox="0 0 24 24"><path d="M6 20V10M12 20V4M18 20v-7"/></symbol>
  <symbol id="i-check" viewBox="0 0 24 24"><path d="M20 6 9 17l-5-5"/></symbol>
  <symbol id="i-file" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M9 13h6M9 17h4"/></symbol>
  <symbol id="i-user" viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></symbol>
  <symbol id="i-mail" viewBox="0 0 24 24"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></symbol>
  <symbol id="i-globe" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/></symbol>
  <symbol id="i-in" viewBox="0 0 24 24"><rect x="2" y="2" width="20" height="20" rx="4"/><path d="M7 10v7M7 7v.01M11 17v-7M11 13a3 3 0 0 1 6 0v4"/></symbol>
  <symbol id="i-gh" viewBox="0 0 24 24"><path d="M9 19c-4.3 1.4-4.3-2.5-6-3m12 5v-3.5c0-1 .1-1.4-.5-2 2.8-.3 5.5-1.4 5.5-6a4.6 4.6 0 0 0-1.3-3.2 4.2 4.2 0 0 0-.1-3.2s-1.1-.3-3.5 1.3a12.3 12.3 0 0 0-6.2 0C6.5 2.8 5.4 3.1 5.4 3.1a4.2 4.2 0 0 0-.1 3.2A4.6 4.6 0 0 0 4 9.5c0 4.6 2.7 5.7 5.5 6-.6.6-.6 1.2-.5 2V21"/></symbol>
  <symbol id="i-chev" viewBox="0 0 24 24"><path d="m9 18 6-6-6-6"/></symbol>
  <symbol id="i-down" viewBox="0 0 24 24"><path d="m6 9 6 6 6-6"/></symbol>
  <symbol id="i-yt" viewBox="0 0 24 24"><rect x="2" y="5" width="20" height="14" rx="4"/><path d="m10 9 5 3-5 3z"/></symbol>
  <symbol id="i-fb" viewBox="0 0 24 24"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></symbol>
  <symbol id="i-ig" viewBox="0 0 24 24"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5v.01"/></symbol>
  <symbol id="i-x" viewBox="0 0 24 24"><path d="M4 4l16 16M20 4 4 20"/></symbol>
  <symbol id="i-building" viewBox="0 0 24 24"><rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-4h6v4M8 6h.01M12 6h.01M16 6h.01M8 10h.01M12 10h.01M16 10h.01M8 14h.01M12 14h.01M16 14h.01"/></symbol>
  <symbol id="i-phone" viewBox="0 0 24 24"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></symbol>
</svg>'''

SOCIAL = [  # (label, icon, brand colour, url) — company channels from tinitiateai.com; GitHub is Jay's profile
    ('LinkedIn', 'i-in', '#0a66c2', 'https://www.linkedin.com/company/tinitiate-ai/'),
    ('YouTube', 'i-yt', '#ff0033', 'https://www.youtube.com/channel/UCXVm8lbVkHOxEJ4XzggTeJw'),
    ('Facebook', 'i-fb', '#1877f2', 'https://www.facebook.com/profile.php?id=61589182754060'),
    ('Instagram', 'i-ig', '#e1306c', 'https://www.instagram.com/tinitiate.ai/'),
    ('X', 'i-x', 'var(--ink)', 'https://x.com/TinitiateAI'),
    ('GitHub', 'i-gh', 'var(--ink)', 'https://github.com/jaykumsi'),
]

CSS = r'''<style>
/* Layout: Ionic-style app shell. Translucent toolbar, iOS large title, searchbar + sliding segment,
   app-icon cards per company, inset grouped lists for "How it works" and the instructor. Dark-first. */
:root {
  --bg: #0a0b1a;
  --bg-2: #11132b;
  --glass: rgba(24, 27, 56, 0.62);
  --glass-strong: rgba(30, 33, 68, 0.82);
  --line: rgba(160, 170, 255, 0.14);
  --line-strong: rgba(160, 170, 255, 0.28);
  --ink: #f3f4ff;
  --muted: #a5abd0;
  --dim: #7a80a8;
  --primary: #8b7bff;
  --primary-2: #4fd1ff;
  --pink: #ff6fb5;
  --on-primary: #ffffff;
  --aurora-1: rgba(124, 92, 255, 0.42);
  --aurora-2: rgba(34, 211, 238, 0.28);
  --aurora-3: rgba(255, 111, 181, 0.24);
  --shadow: 0 18px 40px rgba(3, 4, 20, 0.55);
  --font: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  --display: "Plus Jakarta Sans", "Inter", -apple-system, "Segoe UI", sans-serif;
  --mono: "JetBrains Mono", Consolas, monospace;
  --r: 22px;
  color-scheme: dark;
}
@media (prefers-color-scheme: light) {
  :root:not([data-theme="dark"]) {
    --bg: #f3f2fb; --bg-2: #e9e7fb; --glass: rgba(255, 255, 255, 0.72); --glass-strong: rgba(255, 255, 255, 0.9);
    --line: rgba(70, 60, 160, 0.12); --line-strong: rgba(70, 60, 160, 0.26); --ink: #16152e; --muted: #555878; --dim: #7c7f9e;
    --primary: #5b46f5; --primary-2: #0891b2; --pink: #db2777;
    --aurora-1: rgba(124, 92, 255, 0.22); --aurora-2: rgba(34, 211, 238, 0.18); --aurora-3: rgba(255, 111, 181, 0.16);
    --shadow: 0 16px 36px rgba(40, 30, 120, 0.12); color-scheme: light;
  }
}
:root[data-theme="light"] {
  --bg: #f3f2fb; --bg-2: #e9e7fb; --glass: rgba(255, 255, 255, 0.72); --glass-strong: rgba(255, 255, 255, 0.9);
  --line: rgba(70, 60, 160, 0.12); --line-strong: rgba(70, 60, 160, 0.26); --ink: #16152e; --muted: #555878; --dim: #7c7f9e;
  --primary: #5b46f5; --primary-2: #0891b2; --pink: #db2777;
  --aurora-1: rgba(124, 92, 255, 0.22); --aurora-2: rgba(34, 211, 238, 0.18); --aurora-3: rgba(255, 111, 181, 0.16);
  --shadow: 0 16px 36px rgba(40, 30, 120, 0.12); color-scheme: light;
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; scroll-padding-top: 80px; }
body { margin: 0; min-height: 100vh; background: var(--bg); color: var(--ink); font: 15px/1.6 var(--font); -webkit-font-smoothing: antialiased; }
body::before { content: ""; position: fixed; inset: 0 0 auto; height: env(safe-area-inset-top, 0px); z-index: 60; background: var(--bg); }
a { color: var(--primary); }
:focus-visible { outline: 2.5px solid var(--primary); outline-offset: 3px; border-radius: 8px; }
svg.i { width: 18px; height: 18px; flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
code { font: 600 .82em var(--mono); }

.aurora { position: fixed; inset: 0; z-index: 0; pointer-events: none; overflow: hidden; }
.aurora span { position: absolute; border-radius: 50%; filter: blur(80px); animation: drift 22s ease-in-out infinite alternate; }
.aurora span:nth-child(1) { width: 560px; height: 560px; top: -180px; left: -140px; background: var(--aurora-1); }
.aurora span:nth-child(2) { width: 480px; height: 480px; top: 18%; right: -160px; background: var(--aurora-2); animation-delay: -7s; }
.aurora span:nth-child(3) { width: 420px; height: 420px; bottom: -160px; left: 30%; background: var(--aurora-3); animation-delay: -14s; }
@keyframes drift { to { transform: translate(40px, 30px) scale(1.08); } }

.app { position: relative; z-index: 1; }
.gutter { padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }
.wrap { max-width: 1180px; margin: 0 auto; }

/* ion-toolbar */
/* Site header: always dark charcoal, like tinitiateai.com */
.toolbar { position: sticky; top: env(safe-area-inset-top, 0px); z-index: 50; padding-block: 12px; background: #1f2023;
  border-bottom: 1px solid #000; box-shadow: 0 6px 24px rgba(0,0,0,.35); color-scheme: dark; }
.toolbar .wrap { display: flex; align-items: center; gap: 22px; }
.brand { display: flex; align-items: center; gap: 10px; text-decoration: none; color: #fff; min-width: 0; flex: none; }
.brand .chev { width: 30px; height: 24px; flex: none; }
.wordmark { display: inline-flex; align-items: center; gap: .04em; font: 400 1.55rem/1 "Krona One", var(--display); letter-spacing: .02em; white-space: nowrap; }
.wordmark .lam { width: .82em; height: .78em; margin: 0 .02em; }
.wordmark .gap { width: .45em; }
.sub-brand { position: relative; display: flex; align-items: center; padding-left: 22px; border-left: 1px solid #3a3b40; flex: none;
  font: 800 1.45rem/1 var(--display); color: #fff; text-decoration: none; letter-spacing: -0.01em; }
.sub-brand sup { position: absolute; top: -9px; right: -6px; font: 500 .7rem var(--mono); color: #f5d90a; letter-spacing: 0; }
.tb-actions { display: flex; align-items: center; gap: 10px; flex: 1; min-width: 0; }
.tb-btn { display: inline-flex; align-items: center; gap: 8px; height: 38px; padding: 0 14px; border-radius: 8px; cursor: pointer;
  color: #f1f1f3; background: transparent; border: 1px solid #44464c; font: 700 .9rem var(--font); text-decoration: none; white-space: nowrap;
  transition: background .2s ease, border-color .2s ease; list-style: none; }
.tb-btn::-webkit-details-marker { display: none; }
.tb-btn.plain { border-color: transparent; }
.tb-btn:hover { background: #2b2c31; border-color: #5a5c63; }
.tb-btn svg.i { width: 16px; height: 16px; }
.tb-btn .caret { width: 14px; height: 14px; transition: transform .2s ease; }
.tb-btn.icon { width: 38px; padding: 0; justify-content: center; margin-left: auto; }
.menu { position: relative; }
.menu[open] .caret { transform: rotate(180deg); }
.menu-panel { position: absolute; top: calc(100% + 8px); left: 0; min-width: 290px; padding: 6px; border-radius: 12px;
  background: #1f2023; border: 1px solid #3a3b40; box-shadow: 0 18px 40px rgba(0,0,0,.5); }
.menu-panel a { display: flex; align-items: center; gap: 10px; padding: 9px 10px; border-radius: 8px; color: #f1f1f3; text-decoration: none; font-size: .9rem; }
.menu-panel a:hover { background: #2b2c31; }
.menu-panel a i { width: 10px; height: 10px; border-radius: 3px; background: var(--dc); flex: none; }
.menu-panel a small { margin-left: auto; color: #9a9aa8; font-size: .76rem; }
@media (max-width: 1020px) { .sub-brand, .tb-btn.wide { display: none; } }
@media (max-width: 560px) {
  .wordmark { font-size: 1.1rem; } .brand .chev { width: 22px; height: 18px; }
  .toolbar .wrap { gap: 10px; } .tb-btn.plain .label, .menu .label { display: none; }
  .menu-panel { position: fixed; left: 16px; right: 16px; top: 64px; min-width: 0; }
}

/* large title */
.hero { padding-block: 44px 18px; }
.eyebrow { display: inline-flex; align-items: center; gap: 8px; font: 700 .74rem var(--font); letter-spacing: .08em; text-transform: uppercase;
  color: var(--muted); }
.eyebrow .dot { width: 8px; height: 8px; border-radius: 50%; background: linear-gradient(135deg, var(--primary), var(--primary-2));
  box-shadow: 0 0 12px var(--primary); }
.hero h1 { margin: 10px 0 10px; font: 800 clamp(2.3rem, 5.6vw, 4rem)/1.04 var(--display); letter-spacing: -0.035em; text-wrap: balance; }
.hero h1 em { font-style: normal; background: linear-gradient(100deg, var(--primary) 0%, var(--pink) 50%, var(--primary-2) 100%);
  -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; }
.hero p { margin: 0; max-width: 62ch; color: var(--muted); font-size: 1.05rem; }

.stats { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 1px; margin-top: 26px; border-radius: var(--r); overflow: hidden;
  background: var(--line); border: 1px solid var(--line); box-shadow: var(--shadow); }
.stat { padding: 16px 18px; background: var(--glass-strong); backdrop-filter: blur(18px); -webkit-backdrop-filter: blur(18px); min-width: 0; }
.stat strong { display: block; font: 800 1.6rem/1.1 var(--display); letter-spacing: -0.02em; font-variant-numeric: tabular-nums; }
.stat span { font-size: .82rem; color: var(--muted); }

/* searchbar + segment */
.controls { position: sticky; top: calc(env(safe-area-inset-top, 0px) + 57px); z-index: 40; padding-block: 12px; }
.controls .wrap { display: flex; flex-wrap: wrap; gap: 12px; align-items: center; }
.search { flex: 1 1 260px; display: flex; align-items: center; gap: 8px; height: 44px; padding: 0 14px; border-radius: 14px;
  background: var(--glass-strong); border: 1px solid var(--line); color: var(--dim);
  backdrop-filter: blur(18px); -webkit-backdrop-filter: blur(18px); }
.search input { flex: 1; min-width: 0; height: 100%; border: 0; outline: 0; background: transparent; color: var(--ink); font: 500 .95rem var(--font); }
.search input::placeholder { color: var(--dim); }
.seg-wrap { max-width: 100%; overflow-x: auto; scrollbar-width: none; }
.seg-wrap::-webkit-scrollbar { display: none; }
.segment { position: relative; display: inline-flex; padding: 4px; gap: 2px; border-radius: 14px; background: var(--glass-strong);
  border: 1px solid var(--line); backdrop-filter: blur(18px); -webkit-backdrop-filter: blur(18px); }
.seg-thumb { position: absolute; top: 4px; bottom: 4px; left: 0; width: 0; border-radius: 10px; z-index: 0;
  background: linear-gradient(135deg, var(--primary), color-mix(in srgb, var(--primary) 55%, var(--pink)));
  box-shadow: 0 6px 18px color-mix(in srgb, var(--primary) 40%, transparent);
  transition: transform .42s cubic-bezier(.32, .72, 0, 1), width .42s cubic-bezier(.32, .72, 0, 1); }
.seg-btn { position: relative; z-index: 1; height: 36px; padding: 0 14px; border: 0; border-radius: 10px; background: transparent; cursor: pointer;
  color: var(--muted); font: 600 .86rem var(--font); white-space: nowrap; transition: color .25s ease; }
.seg-btn[aria-selected="true"] { color: var(--on-primary); }
.seg-btn .n { margin-left: 6px; font: 700 .72rem var(--mono); opacity: .75; }

/* ion-card grid */
.section { padding-block: 12px 28px; }
.cards { display: grid; grid-template-columns: repeat(auto-fill, minmax(min(100%, 330px), 1fr)); gap: 18px; }
.card { --dc-use: var(--dc); position: relative; display: flex; flex-direction: column; gap: 14px; padding: 20px; border-radius: var(--r);
  background: var(--glass); border: 1px solid var(--line); box-shadow: var(--shadow); min-width: 0; overflow: hidden;
  backdrop-filter: blur(20px) saturate(160%); -webkit-backdrop-filter: blur(20px) saturate(160%);
  transition: transform .35s cubic-bezier(.32, .72, 0, 1), border-color .25s ease, box-shadow .35s ease; }
@media (prefers-color-scheme: light) { :root:not([data-theme="dark"]) .card { --dc-use: var(--dl); } }
:root[data-theme="light"] .card { --dc-use: var(--dl); }
.card::before { content: ""; position: absolute; inset: 0 0 auto; height: 120px; pointer-events: none;
  background: radial-gradient(120% 100% at 0% 0%, color-mix(in srgb, var(--dc-use) 26%, transparent), transparent 70%); }
.card:hover { transform: translateY(-4px); border-color: color-mix(in srgb, var(--dc-use) 45%, transparent);
  box-shadow: var(--shadow), 0 0 0 1px color-mix(in srgb, var(--dc-use) 20%, transparent), 0 20px 50px color-mix(in srgb, var(--dc-use) 18%, transparent); }
.card[hidden] { display: none; }
.card-head { position: relative; display: flex; align-items: center; gap: 14px; }
.app-icon { width: 54px; height: 54px; flex: none; filter: drop-shadow(0 8px 16px color-mix(in srgb, var(--dc-use) 40%, transparent)); }
.card-title { min-width: 0; }
.kicker { font: 700 .68rem var(--mono); letter-spacing: .08em; text-transform: uppercase; color: var(--dc-use); }
.card h3 { margin: 2px 0 0; font: 800 1.22rem/1.2 var(--display); letter-spacing: -0.015em; text-wrap: balance; }
.tagline { position: relative; margin: 0; color: var(--muted); }
.meta { display: flex; flex-wrap: wrap; gap: 6px 14px; font-size: .82rem; color: var(--dim); }
.meta span { display: inline-flex; align-items: center; gap: 6px; }
.meta svg.i { width: 15px; height: 15px; color: var(--dc-use); }
.chips { display: flex; flex-wrap: wrap; gap: 6px; }
.chip { font: 600 .74rem var(--font); padding: 4px 10px; border-radius: 99px; color: var(--ink);
  background: color-mix(in srgb, var(--dc-use) 12%, transparent); border: 1px solid color-mix(in srgb, var(--dc-use) 24%, transparent); }
.card-foot { margin-top: auto; padding-top: 14px; border-top: 1px solid var(--line); display: flex; align-items: center; justify-content: space-between; gap: 12px; }
.count { font-size: .84rem; color: var(--muted); line-height: 1.3; }
.count strong { font: 800 1.15rem var(--display); color: var(--ink); font-variant-numeric: tabular-nums; }
.count small { color: var(--dim); }
.btn { display: inline-flex; align-items: center; gap: 8px; height: 42px; padding: 0 18px; border-radius: 99px; text-decoration: none;
  font: 700 .88rem var(--font); color: #fff; white-space: nowrap;
  background: linear-gradient(135deg, var(--dc), var(--dl)); box-shadow: 0 8px 20px color-mix(in srgb, var(--dc-use) 35%, transparent);
  transition: transform .2s ease, box-shadow .2s ease; }
.btn:hover { transform: translateY(-1px) scale(1.02); }
.btn:active { transform: scale(.97); }
.btn svg.i { width: 16px; height: 16px; }
.btn.ghost { background: transparent; color: var(--dim); border: 1px dashed var(--line-strong); box-shadow: none; }
.empty { display: none; padding: 40px 20px; text-align: center; color: var(--muted); border-radius: var(--r); border: 1px dashed var(--line-strong); }
.empty.show { display: block; }
.note { margin: 18px 4px 0; color: var(--muted); font-size: .92rem; max-width: 80ch; }

/* ion-list inset grouped */
.h2 { margin: 0 4px 4px; font: 800 1.5rem var(--display); letter-spacing: -0.02em; }
.sub { margin: 0 4px 14px; color: var(--muted); }
.list { margin: 0; padding: 0; list-style: none; border-radius: var(--r); overflow: hidden; background: var(--glass); border: 1px solid var(--line);
  backdrop-filter: blur(20px) saturate(160%); -webkit-backdrop-filter: blur(20px) saturate(160%); box-shadow: var(--shadow); }
.item { display: flex; align-items: center; gap: 14px; padding: 14px 18px; min-width: 0; color: inherit; text-decoration: none; }
.item + .item { border-top: 1px solid var(--line); }
a.item:hover { background: color-mix(in srgb, var(--primary) 7%, transparent); }
.ico { display: grid; place-items: center; width: 34px; height: 34px; flex: none; border-radius: 10px; color: #fff; background: var(--c); }
.ico svg.i { width: 18px; height: 18px; }
.item-body { min-width: 0; flex: 1; }
.item-body b { display: block; font-weight: 700; }
.item-body span { color: var(--muted); font-size: .9rem; }
.item .end { margin-left: auto; color: var(--dim); display: inline-flex; align-items: center; gap: 6px; font-size: .86rem; }
.copy { height: 30px; padding: 0 12px; border-radius: 99px; border: 1px solid var(--line-strong); background: transparent; color: var(--primary);
  font: 600 .78rem var(--font); cursor: pointer; }
.two { display: grid; grid-template-columns: minmax(0, 1.2fr) minmax(0, 1fr); gap: 22px; align-items: start; }
/* site footer */
.site-foot { margin-top: 24px; padding-block: 48px 28px; border-top: 1px solid var(--line);
  background: #000; color-scheme: dark;
  --ink: #f4f4f7; --muted: #c9c9d3; --dim: #9a9aa8; --line: rgba(255,255,255,.12); --line-strong: rgba(255,255,255,.16); --glass: #141418; }
:root[data-theme="light"] .site-foot .contact-row a, :root[data-theme="light"] .site-foot .contact-ico { color: #4fd1ff; }
.foot-grid { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 300px); gap: 48px; }
.foot-h { display: flex; align-items: center; gap: 10px; margin: 0 0 16px; padding-bottom: 16px; border-bottom: 1px solid var(--line);
  font: 800 1.2rem var(--display); letter-spacing: -0.01em; color: var(--ink); }
.foot-h svg.i { width: 22px; height: 22px; color: var(--accent, #4fd1ff); }
.foot-h.contact svg.i { color: #34d399; }
.foot-desc { margin: 0 0 18px; max-width: 62ch; color: var(--muted); line-height: 1.6; }
.foot-label { display: block; margin-bottom: 10px; font: 700 .74rem var(--font); letter-spacing: .1em; text-transform: uppercase; color: var(--dim); }
.socials { display: flex; flex-wrap: wrap; gap: 10px; }
.social { display: inline-flex; align-items: center; gap: 9px; height: 42px; padding: 0 16px; border-radius: 10px; text-decoration: none;
  font: 700 .88rem var(--font); color: var(--ink); background: var(--glass); border: 1px solid var(--line-strong);
  transition: transform .2s ease, border-color .2s ease, background .2s ease; }
.social:hover { transform: translateY(-2px); border-color: var(--sc); background: color-mix(in srgb, var(--sc) 10%, var(--glass)); }
.social svg.i { width: 17px; height: 17px; color: var(--sc); }
.contact-row { display: flex; gap: 14px; align-items: flex-start; }
.contact-row + .contact-row { margin-top: 18px; }
.contact-ico { display: grid; place-items: center; width: 38px; height: 38px; flex: none; border-radius: 10px;
  background: var(--glass); border: 1px solid var(--line-strong); color: #4fd1ff; }
.contact-ico svg.i { width: 18px; height: 18px; }
.contact-row a { color: #4fd1ff; font-weight: 700; text-decoration: none; overflow-wrap: anywhere; }
.contact-row a:hover { text-decoration: underline; }
:root[data-theme="light"] .contact-row a, :root[data-theme="light"] .contact-ico { color: #0369a1; }
.foot-base { margin-top: 36px; padding-top: 18px; border-top: 1px solid var(--line); color: var(--dim); font-size: .82rem;
  display: flex; flex-wrap: wrap; justify-content: space-between; gap: 8px; }

@media (max-width: 860px) {
  .two, .foot-grid { grid-template-columns: minmax(0, 1fr); }
  .foot-grid { gap: 32px; }
  .stats { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .tb-btn.label { display: none; }
}
@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  .aurora span { animation: none; }
  *, *::before { transition: none !important; }
}
</style>'''


def render(links):
    cards = '\n        '.join(card(s, links.get(s)) for s in ORDER)
    lam = '<svg class="lam" viewBox="0 0 20 20" aria-hidden="true"><path d="M1.6 20 10 1.5 18.4 20" fill="none" stroke="currentColor" stroke-width="3.6"/></svg>'
    menu = ''.join(
        f'<a href="{links[s]}" target="_blank" rel="noopener" style="--dc:{c["color"]}"><i></i>{html.escape(c["company"])}<small>{html.escape(c["industry"])}</small></a>'
        for s in ORDER if links.get(s) for c in [HEALTHCARE if s == 'healthcare' else DOMAINS[s]])
    socials = ''.join(f'<a class="social" style="--sc:{c}" href="{u}" target="_blank" rel="noopener">'
                      f'<svg class="i" aria-hidden="true"><use href="#{i}"/></svg>{l}</a>' for l, i, c, u in SOCIAL)
    counts = {k: len(ds) for k, (_, ds) in GROUPS.items()}
    segs = ''.join(f'<button class="seg-btn" type="button" role="tab" id="seg-{k}" data-group="{k}" aria-selected="false">'
                   f'{html.escape(lbl)}<span class="n">{counts[k]}</span></button>' for k, (lbl, _) in GROUPS.items())
    fav = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 48 48'%3E%3Cdefs%3E%3ClinearGradient id='g' x1='0' y1='0' x2='1' y2='1'%3E"
           "%3Cstop offset='0' stop-color='%238b7bff'/%3E%3Cstop offset='1' stop-color='%23ff6fb5'/%3E%3C/linearGradient%3E%3C/defs%3E"
           "%3Crect x='1' y='1' width='46' height='46' rx='13' fill='url(%23g)'/%3E%3Cpath d='M13 15h22M13 24h22M13 33h13' stroke='%23fff' "
           "stroke-width='4' stroke-linecap='round'/%3E%3C/svg%3E")
    brand_logo = ('<svg viewBox="0 0 48 48" aria-hidden="true"><defs><linearGradient id="gb" x1="0" y1="0" x2="1" y2="1">'
                  '<stop offset="0" stop-color="#8b7bff"/><stop offset="1" stop-color="#ff6fb5"/></linearGradient></defs>'
                  '<rect x="1" y="1" width="46" height="46" rx="13" fill="url(#gb)"/>'
                  '<path d="M13 15h22M13 24h22M13 33h13" stroke="#fff" stroke-width="4" stroke-linecap="round"/></svg>')
    return f'''<title>SQL Assignments by Domain</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="icon" href="{fav}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@700;800&family=JetBrains+Mono:wght@500;700&family=Krona+One&display=swap">
<script>
  (function () {{
    try {{ var t = localStorage.getItem("tinitiate-theme"); if (t === "light" || t === "dark") document.documentElement.setAttribute("data-theme", t); }} catch (e) {{}}
  }})();
</script>
{CSS}
{SYMBOLS}
<div class="aurora" aria-hidden="true"><span></span><span></span><span></span></div>

<div class="app">
  <header class="toolbar gutter">
    <div class="wrap">
      <a class="brand" href="#top" aria-label="Tinitiate AI, SQL assignments home">
        <svg class="chev" viewBox="0 0 30 24" aria-hidden="true"><path d="M0 0h13l13 12-13 12H0l13-12z" fill="#f5d90a"/></svg>
        <span class="wordmark">TINITI{lam}TE<span class="gap"></span>{lam}I</span></a>
      <a class="sub-brand" href="#domains">Assignments<sup>+academy</sup></a>
      <nav class="tb-actions" aria-label="Main">
        <a class="tb-btn plain" href="https://tinitiateai.com" target="_blank" rel="noopener"><svg class="i" aria-hidden="true"><use href="#i-home"/></svg><span class="label">Home</span></a>
        <details class="menu"><summary class="tb-btn"><svg class="i" aria-hidden="true"><use href="#i-grid"/></svg><span class="label">Workbooks</span><svg class="i caret" aria-hidden="true"><use href="#i-down"/></svg></summary>
          <div class="menu-panel">{menu}</div></details>
        <a class="tb-btn wide" href="#how"><svg class="i" aria-hidden="true"><use href="#i-layers"/></svg>How it works</a>
        <a class="tb-btn wide" href="#contact"><svg class="i" aria-hidden="true"><use href="#i-mail"/></svg>Contact</a>
        <button id="theme" class="tb-btn icon" type="button" aria-label="Switch between light and dark theme"><svg class="i" aria-hidden="true"><use href="#i-sun"/></svg></button>
      </nav>
    </div>
  </header>

  <section class="hero gutter" id="top">
    <div class="wrap">
      <span class="eyebrow"><span class="dot"></span>Tinitiate AI Academy &middot; SQL Server track</span>
      <h1>Assignments,<br><em>one company per industry</em></h1>
      <p>Pick a company and practise on its own tables. Every workbook has the same 16 topics and 480 questions, from your first SELECT to the window-function patterns interviewers ask, plus 10 multi-step Interview Challenges written for that company. Every query has its expected result.</p>
      <div class="stats">
        <div class="stat"><strong>9</strong><span>companies</span></div>
        <div class="stat"><strong>16 + 10</strong><span>topics, plus interview challenges</span></div>
        <div class="stat"><strong>4,410</strong><span>questions in total</span></div>
        <div class="stat"><strong>10&middot;10&middot;10</strong><span>Beginner, Intermediate, Advanced per topic</span></div>
      </div>
    </div>
  </section>

  <div class="controls gutter">
    <div class="wrap">
      <label class="search" for="q"><svg class="i" aria-hidden="true"><use href="#i-search"/></svg>
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
      <p class="note">The three Maple &amp; Main workbooks are divisions of one retailer: Stores (selling), Supply Chain (buying, making
        and stocking products) and Distribution (deliveries). Everyday Bazaar is the high-volume one: about 32,000 online orders in a year. Each opens in a new tab, and your Done ticks are kept per workbook in this browser.</p>
    </div>
  </main>

  <section class="section gutter" id="how">
    <div class="wrap two">
      <div>
        <h2 class="h2">How it works</h2>
        <p class="sub">Every workbook follows the same path, so switching industries never means relearning the layout.</p>
        <ul class="list">
          <li class="item"><span class="ico" style="--c:linear-gradient(135deg,#8b7bff,#5b46f5)"><svg class="i"><use href="#i-file"/></svg></span>
            <div class="item-body"><b>Run one setup script</b><span>Each domain folder has a <code>data_setup.sql</code>. Run it once in a new practice database.</span></div></li>
          <li class="item"><span class="ico" style="--c:linear-gradient(135deg,#4fd1ff,#0891b2)"><svg class="i"><use href="#i-layers"/></svg></span>
            <div class="item-body"><b>Same 16 topics</b><span>From DQL, joins and aggregates to DDL, constraints, CTEs and window functions.</span></div></li>
          <li class="item"><span class="ico" style="--c:linear-gradient(135deg,#ff6fb5,#db2777)"><svg class="i"><use href="#i-bars"/></svg></span>
            <div class="item-body"><b>Three levels per topic</b><span>Advanced questions are interview patterns: top-N per group, running totals, gaps and islands, fan-out traps.</span></div></li>
          <li class="item"><span class="ico" style="--c:linear-gradient(135deg,#a78bfa,#7c3aed)"><svg class="i"><use href="#i-layers"/></svg></span>
            <div class="item-body"><b>Then the Interview Challenges</b><span>10 multi-step problems per company, like real interview rounds. The approach hint opens with the expected result, so try first.</span></div></li>
          <li class="item"><span class="ico" style="--c:linear-gradient(135deg,#34d399,#059669)"><svg class="i"><use href="#i-check"/></svg></span>
            <div class="item-body"><b>Check your own result</b><span>Run your SQL first, then compare rows. A different query that returns the same rows is still correct.</span></div></li>
        </ul>
      </div>
      <div>
        <h2 class="h2">Your instructor</h2>
        <p class="sub">Training, course advice, interview preparation and resume help.</p>
        <ul class="list">
          <li class="item"><span class="ico" style="--c:linear-gradient(135deg,#8b7bff,#ff6fb5)"><svg class="i"><use href="#i-user"/></svg></span>
            <div class="item-body"><b>Jayathirth Kumsiravinder</b><span>Director and Instructor, Tinitiate AI Academy</span></div></li>
          <li><a class="item" href="https://www.linkedin.com/in/jayathirth-kumsi" target="_blank" rel="noopener"><span class="ico" style="--c:#0a66c2"><svg class="i"><use href="#i-in"/></svg></span>
            <div class="item-body"><b>LinkedIn</b><span>jayathirth-kumsi</span></div><span class="end"><svg class="i"><use href="#i-chev"/></svg></span></a></li>
          <li><a class="item" href="https://github.com/jaykumsi" target="_blank" rel="noopener"><span class="ico" style="--c:#24292f"><svg class="i"><use href="#i-gh"/></svg></span>
            <div class="item-body"><b>GitHub</b><span>jaykumsi</span></div><span class="end"><svg class="i"><use href="#i-chev"/></svg></span></a></li>
          <li class="item"><span class="ico" style="--c:linear-gradient(135deg,#4fd1ff,#0891b2)"><svg class="i"><use href="#i-mail"/></svg></span>
            <div class="item-body"><b>Email</b><span id="mail">contact@tinitiateai.com</span></div><button class="copy" id="copy" type="button">Copy</button></li>
          <li><a class="item" href="https://tinitiateai.com" target="_blank" rel="noopener"><span class="ico" style="--c:linear-gradient(135deg,#fbbf24,#f97316)"><svg class="i"><use href="#i-globe"/></svg></span>
            <div class="item-body"><b>Academy website</b><span>tinitiateai.com</span></div><span class="end"><svg class="i"><use href="#i-chev"/></svg></span></a></li>
        </ul>
      </div>
    </div>
  </section>

  <footer class="site-foot gutter" id="contact">
    <div class="wrap">
      <div class="foot-grid">
        <div>
          <h2 class="foot-h"><svg class="i" aria-hidden="true"><use href="#i-building"/></svg>Tinitiate AI Assignments</h2>
          <p class="foot-desc">Hands-on SQL assignments on realistic company data, part of Tinitiate AI Academy's industry-aligned training
            that moves software engineers, cloud architects and data professionals into high-impact AI, GenAI and Distributed Lakehouse Engineering roles.</p>
          <span class="foot-label">Company social channels</span>
          <div class="socials">{socials}</div>
        </div>
        <div>
          <h2 class="foot-h contact"><svg class="i" aria-hidden="true"><use href="#i-phone"/></svg>Contact &amp; Call Us</h2>
          <div class="contact-row"><span class="contact-ico"><svg class="i" aria-hidden="true"><use href="#i-mail"/></svg></span>
            <div><span class="foot-label">Email support</span><a href="mailto:contact@tinitiateai.com">contact@tinitiateai.com</a></div></div>
          <div class="contact-row"><span class="contact-ico"><svg class="i" aria-hidden="true"><use href="#i-globe"/></svg></span>
            <div><span class="foot-label">Official portal</span><a href="https://tinitiateai.com" target="_blank" rel="noopener">tinitiateai.com</a></div></div>
        </div>
      </div>
      <div class="foot-base"><span>&copy; 2026 Tinitiate AI Academy. All rights reserved.</span><span>SQL Assignments by Domain</span></div>
    </div>
  </footer>
</div>

<script>
const $ = s => document.querySelector(s);
const seg = $("#seg"), thumb = seg.querySelector(".seg-thumb"), cards = [...document.querySelectorAll(".card")];
let group = "all", query = "";
function moveThumb() {{
  const on = seg.querySelector('.seg-btn[aria-selected="true"]');
  if (!on) return;
  thumb.style.width = on.offsetWidth + "px";
  thumb.style.transform = "translateX(" + (on.offsetLeft - 4) + "px)";
}}
function apply() {{
  let shown = 0;
  cards.forEach(c => {{
    const ok = (group === "all" || c.dataset.group === group) && (!query || c.dataset.search.includes(query));
    c.hidden = !ok; if (ok) shown++;
  }});
  $("#empty").classList.toggle("show", shown === 0);
}}
seg.querySelectorAll(".seg-btn").forEach(b => b.addEventListener("click", () => {{
  seg.querySelectorAll(".seg-btn").forEach(x => x.setAttribute("aria-selected", x === b));
  group = b.dataset.group; moveThumb(); apply();
}}));
$("#q").addEventListener("input", e => {{ query = e.target.value.trim().toLowerCase(); apply(); }});
window.addEventListener("resize", moveThumb);
const menu = $(".menu");
document.addEventListener("click", e => {{ if (menu.open && !menu.contains(e.target)) menu.open = false; }});
document.addEventListener("keydown", e => {{ if (e.key === "Escape") menu.open = false; }});
if (document.fonts && document.fonts.ready) document.fonts.ready.then(moveThumb);
moveThumb();
$("#theme").addEventListener("click", () => {{
  const r = document.documentElement;
  const light = r.dataset.theme ? r.dataset.theme === "light" : matchMedia("(prefers-color-scheme: light)").matches;
  r.dataset.theme = light ? "dark" : "light";
  try {{ localStorage.setItem("tinitiate-theme", r.dataset.theme); }} catch (e) {{}}
}});
$("#copy").addEventListener("click", () => {{
  const b = $("#copy"), done = () => {{ b.textContent = "Copied"; setTimeout(() => b.textContent = "Copy", 1200); }};
  const sel = () => {{ const r = document.createRange(); r.selectNodeContents($("#mail")); const s = getSelection(); s.removeAllRanges(); s.addRange(r); }};
  try {{ navigator.clipboard.writeText($("#mail").textContent).then(done, sel); }} catch (e) {{ sel(); }}
}});
</script>
'''


if __name__ == '__main__':
    links = json.loads(Path(sys.argv[1]).read_text()) if len(sys.argv) > 1 else {}
    out = HERE / 'pages' / 'hub.html'
    out.write_text(render(links), encoding='utf-8')
    print(out, out.stat().st_size // 1024, 'KB')
