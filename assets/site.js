(function () {
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
