// Display an der Box: zeigt den Zustand vom Pi und schickt Aktionen zurück.
// Kein eigener Zustand – die Wahrheit liegt im Modell auf dem Pi (MVC, Folie 99).

const $ = (id) => document.getElementById(id);
const body = document.body;
const SLEEP_AFTER_MS = 45000; // danach Ruhezustand (Skizze 13)
const SYMBOL = { ok: "#sym-ok", soon: "#sym-soon", now: "#sym-now" };

let snapshot = null;
let sleepTimer = null;
let audio = null;

// ---------- Verbindung ----------
function connect() {
  const proto = location.protocol === "https:" ? "wss" : "ws";
  const ws = new WebSocket(`${proto}://${location.host}/ws`);
  ws.onopen = () => { $("offline").hidden = true; };
  ws.onmessage = (event) => render(JSON.parse(event.data));
  ws.onclose = () => { $("offline").hidden = false; setTimeout(connect, 1500); };
}

async function post(path, payload) {
  const res = await fetch(path, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: payload ? JSON.stringify(payload) : undefined,
  });
  if (res.ok) render(await res.json());
}

// ---------- Anzeige ----------
function symbolFor(s) {
  return s.status.level === "ok" && s.growth.harvest_ready ? "#sym-harvest" : SYMBOL[s.status.level];
}

function render(s) {
  snapshot = s;
  body.dataset.level = s.status.level;
  $("status-use").setAttribute("href", symbolFor(s));
  $("sleep-use").setAttribute("href", symbolFor(s));
  $("status-title").textContent = s.status.title;
  $("status-message").textContent = s.status.message;

  // Licht
  $("tile-light").setAttribute("aria-pressed", String(s.light.on));
  $("light-sub").textContent = s.light.on ? "an" : "aus";

  // Klima
  const c = s.climate;
  $("tile-climate").dataset.level = c.level;
  $("climate-sub").textContent = `${c.humidity_label} · ${c.temperature_label}`;
  const fillHum = clamp((c.humidity - 60) / 40);   // 60–100 % -> leer bis voll
  $("water").setAttribute("y", 150 - fillHum * 140);
  $("water").setAttribute("height", fillHum * 140);
  $("hum-label").textContent = c.humidity_label;
  $("hum-value").textContent = `Luftfeuchte ${c.humidity} %`;
  const fillTemp = clamp((c.temperature - 10) / 20); // 10–30 °C
  $("mercury").setAttribute("y", 115 - fillTemp * 100);
  $("mercury").setAttribute("height", fillTemp * 100 + 10);
  $("temp-label").textContent = c.temperature_label;
  $("temp-value").textContent = `${String(c.temperature).replace(".", ",")} °C`;
  $("climate-trend").textContent = trendText(c);

  // Hinweise
  const n = s.hints.length;
  $("tile-hints").dataset.level = n ? s.hints[0].level : "ok";
  $("hints-sub").textContent = n === 0 ? "keine" : n === 1 ? "1 Hinweis" : `${n} Hinweise`;
  $("hints-badge").hidden = n === 0;
  $("hints-badge").textContent = n;
  renderHints(s.hints);

  // Wachstum
  const g = s.growth;
  $("growth-fill").style.width = `${g.progress * 100}%`;
  $("growth-bar").setAttribute("aria-valuenow", Math.round(g.progress * 100));
  $("growth-text").textContent = g.harvest_ready ? "Erntezeit!" : `Tag ${g.day} von ~${g.harvest_day}`;
}

function trendText(c) {
  if (c.humidity_trend === "rising") return "Feuchte steigt …";
  if (c.humidity_trend === "falling") return "Feuchte sinkt …";
  if (c.temperature_trend === "falling") return "Wird kühler …";
  if (c.temperature_trend === "rising") return "Wird wärmer …";
  return "";
}

function renderHints(hints) {
  const list = $("hint-list");
  list.replaceChildren();
  if (hints.length === 0) {
    const empty = el("div", "empty");
    empty.append(svgUse("#icon-check"), text("p", "Keine Hinweise – alles in Ordnung."));
    list.append(empty);
    return;
  }
  for (const h of hints) {
    const card = el("article", "hint");
    card.dataset.level = h.level;
    const sym = svgUse(SYMBOL[h.level], "hint-symbol");
    sym.style.setProperty("--state", `var(--${h.level})`);
    sym.style.setProperty("--state-soft", `var(--${h.level}-soft)`);
    const txt = el("div", "hint-text");
    txt.append(text("h2", h.title), text("p", h.action));
    const btn = el("button", "done");
    btn.type = "button";
    if (h.resolving) {
      btn.disabled = true;
      btn.textContent = "wird besser …";
    } else {
      btn.append(svgUse("#icon-check"), document.createTextNode("Erledigt"));
      btn.addEventListener("click", () => post(`/api/hints/${h.id}/done`));
    }
    card.append(sym, txt, btn);
    list.append(card);
  }
}

// ---------- Bedienung ----------
function showView(name) {
  body.dataset.view = name;
}

$("tile-light").addEventListener("click", () => {
  if (snapshot) post("/api/light", { on: !snapshot.light.on, source: "display" });
});
$("tile-climate").addEventListener("click", () => showView("climate"));
$("tile-hints").addEventListener("click", () => showView("hints"));
for (const back of document.querySelectorAll("[data-goto]")) {
  back.addEventListener("click", () => showView(back.dataset.goto));
}

// Sofortige Rückmeldung < 100 ms: Kachel drückt sich ein + kurzer Klick (Folien 64–65, 82)
document.addEventListener("pointerdown", (event) => {
  const target = event.target.closest("button");
  if (!target || target.disabled || target.id === "sleep") return;
  target.classList.add("pressed");
  tick();
});
for (const type of ["pointerup", "pointercancel", "pointerleave"]) {
  document.addEventListener(type, () => {
    for (const b of document.querySelectorAll(".pressed")) b.classList.remove("pressed");
  }, true);
}

// Ruhezustand
function resetSleep() {
  clearTimeout(sleepTimer);
  sleepTimer = setTimeout(() => {
    body.classList.add("asleep");
    showView("home");
  }, SLEEP_AFTER_MS);
}
$("sleep").addEventListener("click", () => {
  body.classList.remove("asleep");
  resetSleep();
});
document.addEventListener("pointerdown", resetSleep);
document.addEventListener("keydown", resetSleep);

// ---------- Hilfsfunktionen ----------
function tick() {
  try {
    audio ??= new AudioContext();
    const osc = audio.createOscillator();
    const gain = audio.createGain();
    osc.frequency.value = 880;
    gain.gain.setValueAtTime(0.06, audio.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.0001, audio.currentTime + 0.06);
    osc.connect(gain).connect(audio.destination);
    osc.start();
    osc.stop(audio.currentTime + 0.07);
  } catch {
    /* ohne Ton weiter */
  }
}
function clamp(v) { return Math.max(0, Math.min(1, v)); }
function el(tag, cls) { const e = document.createElement(tag); if (cls) e.className = cls; return e; }
function text(tag, value) { const e = document.createElement(tag); e.textContent = value; return e; }
function svgUse(href, cls) {
  const ns = "http://www.w3.org/2000/svg";
  const svg = document.createElementNS(ns, "svg");
  svg.setAttribute("aria-hidden", "true");
  if (cls) svg.setAttribute("class", cls);
  const use = document.createElementNS(ns, "use");
  use.setAttribute("href", href);
  svg.append(use);
  return svg;
}

connect();
resetSleep();
