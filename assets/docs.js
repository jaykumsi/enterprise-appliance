(function () {
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
