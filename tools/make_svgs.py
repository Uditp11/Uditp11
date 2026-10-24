"""Generate the profile SVGs (light and dark) from one data block.

Run: python tools/make_svgs.py
Writes into assets/. Edit CARDS below when a number changes, then rerun.
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(exist_ok=True)

SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"

THEMES = {
    "light": dict(bg="#f6f8fa", border="#d0d7de", text="#1f2328", muted="#59636e",
                  accent="#8250df", green="#1a7f37", pill_bg="#ddf4ff", pill="#0969da",
                  warn_bg="#fff8c5", warn="#9a6700", line="#d0d7de"),
    "dark": dict(bg="#151b23", border="#3d444d", text="#f0f6fc", muted="#9198a1",
                 accent="#ab7df8", green="#3fb950", pill_bg="#0d2847", pill="#4493f8",
                 warn_bg="#2e2208", warn="#d29922", line="#3d444d"),
}

LANES = ["ML and AI engineering", "Java and Python backend", "full-stack",
         "QA and test automation", "data and automation"]

# Every number here comes from the README or docs file named in its src line.
# Re-check it in that repo before changing a card.
CARDS = [
    dict(slug="cifar10", repo="cifar10-from-scratch", pill=None,
         big="96.06%", label="test top-1, evaluated once",
         body=["ResNet-18 written from scratch in PyTorch.",
               "10,000 held-out images. Every recipe choice",
               "tested in a logged ablation."],
         src="README results · docs/EXPERIMENTS.md"),
    dict(slug="applytrack", repo="applytrack", pill=None,
         big="86 tests", label="0 skipped in CI",
         body=["Java and Spring Boot API. A status state machine",
               "refuses illegal moves. Kubernetes deploy in CI,",
               "Terraform deploy to Azure."],
         src="README results table"),
    dict(slug="vectordb", repo="vectordb-from-scratch", pill=None,
         big="3", label="search algorithms, by hand",
         body=["HNSW, KD-Tree and brute force in Python and NumPy.",
               "Tests prove KD-Tree matches brute force exactly.",
               "Recall and latency benchmarked, local RAG."],
         src="docs/TESTING.md · docs/BENCHMARK.md"),
    dict(slug="solar-inspect", repo="solar-inspect", pill=("v1.0", "pill"),
         big="5 modules", label="each test split read once",
         body=["Solar panel inspection in PyTorch: U-Net from",
               "scratch, YOLOv8 detection, Kalman and SORT,",
               "defect classifier, plant analytics with SQL."],
         src="README headline results · docs/EXPERIMENTS.md"),
    dict(slug="shift-log", repo="shift-log", pill=("live", "pill"),
         big="2 browsers", label="end-to-end tested",
         body=["Offline-first phone app my friends and I use.",
               "Playwright in WebKit and Chromium, one branch",
               "per task, tests run before every deploy."],
         src="playwright.config.js · pages.yml"),
    dict(slug="shree-shyam", repo="Shree_Shyam_Constructions", pill=("live", "pill"),
         big="Live", label="site for a paying client",
         body=["Website in English and Hindi.",
               "Next.js, TypeScript, Tailwind CSS."],
         src="shree-shyam-constructions.vercel.app"),
]

REDUCED = "@media (prefers-reduced-motion: reduce) { .anim { animation: none !important; } .lane { opacity: 0 !important; } .lane-static { opacity: 1 !important; } }"


def header(t):
    c = THEMES[t]
    n, step = len(LANES), 2.6
    cycle = n * step
    lanes = "".join(
        f'<text class="lane anim" x="40" y="214" style="animation-delay:{i * step:.1f}s">{escape(l)}</text>'
        for i, l in enumerate(LANES))
    # small network: 3 input dots, 2 hidden dots
    ins = [(590, 78), (590, 108), (590, 138)]
    hid = [(640, 93), (640, 123)]
    edges = "".join(f'<line x1="{a}" y1="{b}" x2="{x}" y2="{y}"/>' for a, b in ins for x, y in hid)
    dots = "".join(f'<circle cx="{x}" cy="{y}" r="6"/>' for x, y in ins + hid)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="840" height="240" viewBox="0 0 840 240" role="img" aria-labelledby="t d">
<title id="t">Udit Parihar</title>
<desc id="d">I build machine learning models I can measure, and the APIs, web apps and tests around them. Frankfurt am Main. M.Sc. Global Software Development, Hochschule Fulda. Open to roles in {", ".join(LANES)}.</desc>
<style>
.name {{ font: 700 40px {SANS}; fill: {c["text"]}; }}
.pitch {{ font: 400 18px {SANS}; fill: {c["text"]}; }}
.meta {{ font: 400 14px {SANS}; fill: {c["muted"]}; }}
.cap {{ font: 600 11px {MONO}; fill: {c["muted"]}; letter-spacing: 1.5px; }}
.lane, .lane-static {{ font: 700 20px {SANS}; fill: {c["accent"]}; }}
.lane {{ opacity: 0; animation: show {cycle:.1f}s infinite; }}
.lane-static {{ opacity: 0; font-size: 15px; }}
@keyframes show {{ 0% {{ opacity: 0; transform: translateY(6px); }} 4% {{ opacity: 1; transform: none; }} 17% {{ opacity: 1; }} 20% {{ opacity: 0; }} 100% {{ opacity: 0; }} }}
.net line {{ stroke: {c["line"]}; stroke-width: 1.5; }}
.net circle {{ fill: {c["accent"]}; }}
.wire {{ stroke: {c["line"]}; stroke-width: 2; stroke-dasharray: 4 5; fill: none; }}
.box {{ fill: {c["bg"]}; stroke: {c["border"]}; stroke-width: 1.5; }}
.brace {{ font: 700 22px {MONO}; fill: {c["text"]}; }}
.ok {{ fill: {c["green"]}; }}
.tick {{ stroke: #ffffff; stroke-width: 3; fill: none; stroke-linecap: round; stroke-linejoin: round; }}
.lbl {{ font: 400 11px {MONO}; fill: {c["muted"]}; }}
.pulse {{ fill: {c["accent"]}; offset-path: path("M646 108 L780 108"); animation: run 3.2s ease-in-out infinite; }}
@keyframes run {{ 0% {{ offset-distance: 0%; opacity: 0; }} 10% {{ opacity: 1; }} 85% {{ opacity: 1; }} 100% {{ offset-distance: 100%; opacity: 0; }} }}
{REDUCED}
</style>
<text class="name" x="40" y="62">Udit Parihar</text>
<text class="pitch" x="40" y="98">I build machine learning models I can measure,</text>
<text class="pitch" x="40" y="124">and the APIs, web apps and tests around them.</text>
<text class="meta" x="40" y="156">Frankfurt am Main  ·  M.Sc. Global Software Development, Hochschule Fulda</text>
<text class="cap" x="40" y="188">OPEN TO ROLES IN</text>
{lanes}
<text class="lane-static" x="40" y="212">ML and AI · Java and Python backend · full-stack · QA · data and automation</text>
<g class="net">{edges}{dots}</g>
<path class="wire" d="M646 108 L690 108 M750 108 L784 108"/>
<rect class="box" x="690" y="88" width="60" height="40" rx="8"/>
<text class="brace" x="720" y="116" text-anchor="middle">{{ }}</text>
<circle class="ok" cx="798" cy="108" r="15"/>
<path class="tick" d="M791 108 l5 5 l9 -10"/>
<circle class="pulse anim" r="4"/>
<text class="lbl" x="615" y="172" text-anchor="middle">model</text>
<text class="lbl" x="720" y="172" text-anchor="middle">API</text>
<text class="lbl" x="798" y="172" text-anchor="middle">tests</text>
</svg>
'''


def card(t, d):
    c = THEMES[t]
    pill = ""
    if d["pill"]:
        txt, kind = d["pill"]
        bg, fg = (c["warn_bg"], c["warn"]) if kind == "warn" else (c["pill_bg"], c["pill"])
        w = 14 + 7.2 * len(txt)
        pill = (f'<rect x="{384 - w:.0f}" y="18" width="{w:.0f}" height="22" rx="11" fill="{bg}"/>'
                f'<text x="{384 - w / 2:.0f}" y="33" text-anchor="middle" class="pill" fill="{fg}">{escape(txt)}</text>')
    body = "".join(f'<text class="body" x="20" y="{127 + i * 19}">{escape(l)}</text>' for i, l in enumerate(d["body"]))
    alt = f'{d["repo"]}: {d["big"]}, {d["label"]}. {" ".join(d["body"])}'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="400" height="206" viewBox="0 0 400 206" role="img" aria-labelledby="t">
<title id="t">{escape(alt)}</title>
<style>
.repo {{ font: 600 14px {MONO}; fill: {c["muted"]}; }}
.big {{ font: 700 30px {SANS}; fill: {c["accent"]}; }}
.label {{ font: 400 15px {SANS}; fill: {c["text"]}; }}
.body {{ font: 400 13px {SANS}; fill: {c["text"]}; }}
.src {{ font: 400 10.5px {MONO}; fill: {c["muted"]}; }}
.pill {{ font: 600 11px {SANS}; }}
</style>
<rect x="0.75" y="0.75" width="398.5" height="204.5" rx="12" fill="{c["bg"]}" stroke="{c["border"]}" stroke-width="1.5"/>
<text class="repo" x="20" y="34">{escape(d["repo"])}</text>{pill}
<text class="big" x="20" y="76">{escape(d["big"])}</text>
<text class="label" x="20" y="100">{escape(d["label"])}</text>
{body}
<text class="src" x="20" y="192">{escape(d["src"])}</text>
</svg>
''', alt


def divider(t):
    c = THEMES[t]
    stars = "".join(f'<circle cx="{x}" cy="12" r="{r}" fill="{c["accent"]}"/>' for x, r in [(408, 2), (420, 3), (432, 2)])
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="840" height="24" viewBox="0 0 840 24" role="img" aria-label="divider">
<defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="{c["line"]}" stop-opacity="0"/><stop offset="0.5" stop-color="{c["line"]}"/><stop offset="1" stop-color="{c["line"]}" stop-opacity="0"/></linearGradient></defs>
<rect x="40" y="11.5" width="350" height="1" fill="url(#g)"/><rect x="450" y="11.5" width="350" height="1" fill="url(#g)"/>
{stars}
</svg>
'''


def footer(t):
    c = THEMES[t]
    stars = "".join(f'<circle class="star anim" cx="{x}" cy="{y}" r="1.4" style="animation-delay:{d}s"/>'
                    for x, y, d in [(120, 30, 0), (170, 78, 1.1), (250, 22, 2.3), (560, 26, .6), (640, 70, 1.8), (720, 34, 2.9), (330, 86, 1.4), (500, 88, .3)])
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="840" height="110" viewBox="0 0 840 110" role="img" aria-label="A small planet with a football orbiting it">
<style>
.planet {{ fill: {c["accent"]}; }}
.ring {{ fill: none; stroke: {c["muted"]}; stroke-width: 1.5; }}
.ball {{ fill: {c["bg"]}; stroke: {c["text"]}; stroke-width: 1.2; offset-path: path("M360 55 A60 18 -12 1 0 480 55 A60 18 -12 1 0 360 55"); animation: orbit 9s linear infinite; }}
.patch {{ fill: {c["text"]}; }}
.star {{ fill: {c["muted"]}; animation: tw 4s ease-in-out infinite; }}
@keyframes orbit {{ to {{ offset-distance: 100%; }} }}
@keyframes tw {{ 0%,100% {{ opacity: .25; }} 50% {{ opacity: 1; }} }}
{REDUCED}
</style>
{stars}
<ellipse class="ring" cx="420" cy="55" rx="60" ry="18" transform="rotate(-12 420 55)"/>
<circle class="planet" cx="420" cy="55" r="20"/>
<g class="ball anim"><circle r="7"/><path class="patch" d="M0 -3 L2.9 -0.9 L1.8 2.4 L-1.8 2.4 L-2.9 -0.9 Z"/></g>
</svg>
'''


if __name__ == "__main__":
    alts = {}
    for t in THEMES:
        (OUT / f"header-{t}.svg").write_text(header(t), encoding="utf-8")
        (OUT / f"divider-{t}.svg").write_text(divider(t), encoding="utf-8")
        (OUT / f"footer-{t}.svg").write_text(footer(t), encoding="utf-8")
        for d in CARDS:
            svg, alt = card(t, d)
            (OUT / f"card-{d['slug']}-{t}.svg").write_text(svg, encoding="utf-8")
            alts[d["slug"]] = alt
    for k, v in alts.items():
        print(k, "|", v)
