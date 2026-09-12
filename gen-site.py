#!/usr/bin/env python3
"""Generate the learn-vectordb-school docs: index, lesson-diagrams, landscape."""
GH = "https://github.com/BaluRaut/learn-vectordb-school/blob"
P1, P2 = "#2563eb", "#16a34a"

L = [
 (1,"lesson-01-why-vector-db","01-why-vector-db","🗺️ Why vector DBs","The library sorted by MEANING — keywords match strings, not ideas.",35,P1),
 (2,"lesson-02-text-to-vectors","02-text-to-vectors","🔢 Text to vectors","Giving every text a seat — our honest toy vs learned embeddings.",40,P1),
 (3,"lesson-03-similarity","03-similarity","📐 Similarity","Direction beats distance — and the normalize-then-dot trick.",35,P1),
 (4,"lesson-04-nearest-neighbors","04-nearest-neighbors","🏃 Nearest neighbors","Asking everyone vs the friendship map (HNSW) — the recall dial.",40,P1),
 (5,"lesson-05-build-a-vector-db","05-build-a-vector-db","🔬 Build a vector DB","70 honest lines: embed, cosine, store, filter, top-k.",45,P2),
 (6,"lesson-06-chunking-metadata","06-chunking-metadata","✂️ Chunking &amp; metadata","Cards and colored stickers — the quality lever bigger than any index.",40,P2),
 (7,"lesson-07-rag-wiring","07-rag-wiring","📖 RAG wiring","The open-book exam, end to end — with OUR page-finder.",45,P2),
 (8,"lesson-08-landscape","08-landscape","🏬 The landscape","pgvector, Pinecone, Chroma, FAISS — picking without a bake-off.",40,P2),
]

BASE_CSS = """
  :root { --bg:#f8fafc; --card:#fff; --ink:#0f172a; --muted:#475569; --line:#e2e8f0; --accent:#2563eb; --ok:#16a34a; --blue:#2563eb; --bad:#dc2626; }
  @media (prefers-color-scheme: dark) { :root { --bg:#0b1220; --card:#131c2e; --ink:#e2e8f0; --muted:#94a3b8; --line:#253349; } }
  * { margin:0; padding:0; box-sizing:border-box; }
  body { background:var(--bg); color:var(--ink); font-family:-apple-system,"Segoe UI",Helvetica,Arial,sans-serif; line-height:1.6; }
  .wrap { max-width:1280px; margin:0 auto; padding:28px 20px 60px; }
  @media (min-width: 1660px) { .wrap { max-width: 1580px; } }
  a { color:var(--blue); } h1 { font-size:2rem; line-height:1.25; } h2 { font-size:1.4rem; margin:44px 0 6px; }
  .sub { color:var(--muted); max-width:74ch; }
  .chips { display:flex; flex-wrap:wrap; gap:8px; margin:16px 0 8px; }
  .chip { border:1px solid var(--line); background:var(--card); border-radius:999px; padding:6px 14px; font-size:.85rem; color:var(--muted); }
  .grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(240px,1fr)); gap:14px; margin-top:16px; }
  .lesson { background:var(--card); border:1px solid var(--line); border-top:5px solid var(--c,var(--accent)); border-radius:14px; padding:16px; display:flex; flex-direction:column; gap:6px; }
  .lesson .top { display:flex; align-items:center; gap:10px; }
  .lesson .num { flex:none; width:30px; height:30px; border-radius:50%; background:var(--c,var(--accent)); color:#fff; display:inline-flex; align-items:center; justify-content:center; font-weight:800; font-size:.9rem; }
  .lesson h3 { font-size:1.02rem; line-height:1.3; } .lesson .ana { color:var(--muted); font-size:.9rem; }
  .lesson code { font-size:.78rem; background:var(--bg); border:1px solid var(--line); border-radius:6px; padding:1px 6px; }
  .lesson a.go { margin-top:auto; font-weight:600; font-size:.9rem; text-decoration:none; } .lesson a.go+a.go { margin-top:0; } .lesson a.go:hover { text-decoration:underline; }
  .callout { background:var(--card); border:1px solid var(--line); border-left:6px solid var(--ok); border-radius:14px; padding:18px 20px; margin-top:16px; }
  pre { background:var(--card); border:1px solid var(--line); border-radius:12px; padding:14px 16px; overflow-x:auto; font-size:.88rem; margin-top:12px; }
  .btn { display:inline-block; background:var(--accent); color:#fff; border-radius:10px; padding:10px 18px; text-decoration:none; font-weight:700; margin:14px 10px 0 0; }
  .btn.alt { background:transparent; color:var(--ink); border:1px solid var(--line); }
  .vs { display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:14px; margin-top:16px; }
  .vcol { background:var(--card); border:1px solid var(--line); border-radius:14px; padding:18px; } .vcol h3 { margin-bottom:8px; }
  .vcol ul { margin-left:18px; color:var(--muted); font-size:.93rem; }
  .toc { display:flex; flex-wrap:wrap; gap:8px; margin:18px 0 6px; }
  .toc a { border:1px solid var(--line); background:var(--card); border-radius:999px; padding:5px 12px; font-size:.82rem; color:var(--muted); text-decoration:none; }
  .toc a:hover { color:var(--ink); border-color:var(--muted); }
  .quad { display:grid; grid-template-columns:repeat(auto-fit,minmax(230px,1fr)); gap:12px; margin-top:10px; }
  .q { border:1px solid var(--line); border-radius:12px; padding:14px; }
  .q h4 { margin-bottom:6px; font-size:.98rem; } .q ul { margin-left:18px; color:var(--muted); font-size:.92rem; }
  .q.merit { border-top:4px solid var(--ok); } .q.demerit { border-top:4px solid var(--bad); }
  .q.use { border-top:4px solid var(--blue); }
  footer { margin-top:56px; border-top:1px solid var(--line); padding-top:18px; color:var(--muted); font-size:.88rem; }
"""
DSEC_CSS = """
  .dsec { background:var(--card); border:1px solid var(--line); border-top:6px solid var(--c,var(--accent)); border-radius:16px; padding:22px 22px 16px; margin-top:26px; scroll-margin-top:16px; }
  .dsec h2 { font-size:1.25rem; display:flex; align-items:center; gap:10px; }
  .dsec h2 .ln { flex:none; width:32px; height:32px; border-radius:50%; background:var(--c,var(--accent)); color:#fff; display:inline-flex; align-items:center; justify-content:center; font-size:.95rem; font-weight:800; }
  .dsec p.d { color:var(--muted); font-size:.95rem; margin:6px 0 4px; }
  .dsec svg { width:100%; height:auto; display:block; margin-top:10px; } .dsec .foot { margin-top:8px; font-size:.92rem; }
  .box { fill:var(--card); stroke:var(--c,var(--accent)); stroke-width:2; }
  .soft { fill:var(--bg); stroke:var(--line); stroke-width:1.5; }
  .dead { fill:var(--bg); stroke:var(--muted); stroke-width:1.5; stroke-dasharray:6 5; }
  .t { font:600 14px -apple-system,"Segoe UI",sans-serif; fill:var(--ink); }
  .s { font:12px -apple-system,"Segoe UI",sans-serif; fill:var(--muted); } .m { text-anchor:middle; }
  .arr { stroke:#64748b; stroke-width:2; fill:none; marker-end:url(#arw); } .dash { stroke-dasharray:6 5; }
  .nc { fill:var(--c,var(--accent)); } .nt { font:700 12px -apple-system,sans-serif; fill:#fff; text-anchor:middle; }
"""
MARKER = '<svg width="0" height="0" style="position:absolute"><defs><marker id="arw" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="#64748b"/></marker></defs></svg>'

def head(title, desc):
    return (f'<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
      f'<meta name="viewport" content="width=device-width, initial-scale=1">\n<title>{title}</title>\n'
      f'<meta name="description" content="{desc}">\n<meta property="og:title" content="{title}">\n<meta property="og:description" content="{desc}">\n<meta property="og:image" content="https://baluraut.github.io/learn-vectordb-school/images/big-picture-4k.png">\n<meta property="og:type" content="website">\n<meta name="twitter:card" content="summary_large_image">\n<style>{BASE_CSS}{DSEC_CSS}</style>\n</head>\n<body>\n')

B='<rect class="box"'; S='<rect class="soft"'; D='<rect class="dead"'; DASH=' dash'
def t(x,y,s): return f'<text class="t m" x="{x}" y="{y}">{s}</text>'
def sm(x,y,s): return f'<text class="s m" x="{x}" y="{y}">{s}</text>'
def num(x,y,n): return f'<g transform="translate({x},{y})"><circle r="11" class="nc"/><text class="nt" dy="4">{n}</text></g>'
def arr(a,b,c,d,dash=""): return f'<line class="arr{dash}" x1="{a}" y1="{b}" x2="{c}" y2="{d}"/>'

SVG = {}
SVG[1]=(f'<svg viewBox="0 0 940 300" role="img">{D} x="40" y="60" width="340" height="180" rx="14"/>{t(210,95,"📇 keyword catalog")}{sm(210,125,"&#39;kind to animals&#39; →")}{sm(210,147,"match exact strings →")}{sm(210,169,"❌ &#39;Every Living Thing&#39; missed")}{sm(210,205,"strings, not meaning")}{num(40,60,1)}'
 f'{B} x="440" y="40" width="460" height="220" rx="14"/>{t(670,75,"🗺️ the meaning hall — a vector DB")}'
 f'{S} x="465" y="95" width="190" height="60" rx="10"/>{sm(560,120,"1 seat the question")}{sm(560,142,"(embed it)")}'
 f'{S} x="680" y="95" width="195" height="60" rx="10"/>{sm(777,120,"2 find nearest seats")}{sm(777,142,"fast, at any scale")}'
 f'{S} x="565" y="175" width="210" height="60" rx="10"/>{sm(670,200,"3 ✅ &#39;Every Living Thing&#39;")}{sm(670,222,"zero shared words!")}'
 f'{arr(655,125,676,125)}{arr(777,155,700,171)}{num(440,40,2)}'
 f'{sm(470,290,"store millions of seats · return the k nearest · with stickers 🏷️ — that&#39;s the whole product")}</svg>')
SVG[2]=(f'<svg viewBox="0 0 940 300" role="img">{S} x="40" y="40" width="270" height="200" rx="14"/>{t(175,72,"🔤 toy: count words")}{sm(175,100,"hash each word → bump 1 of")}{sm(175,122,"256 buckets → normalize")}{D} x="65" y="145" width="220" height="70" rx="10"/>{sm(175,172,"😬 nearsighted: shared WORDS")}{sm(175,194,"&#39;pupils&#39; ≠ &#39;students&#39; (0.00!)")}{num(40,40,1)}'
 f'{B} x="350" y="40" width="270" height="200" rx="14"/>{t(485,72,"🧠 real: embedding model")}{sm(485,100,"a trained network → 768-3072")}{sm(485,122,"dims where directions = MEANING")}{S} x="375" y="145" width="220" height="70" rx="10"/>{sm(485,172,"✅ &#39;pupils&#39; sits beside &#39;students&#39;")}{sm(485,194,"across phrasing &amp; languages")}{num(350,40,2)}'
 f'{B} x="680" y="75" width="230" height="130" rx="14"/>{t(795,110,"🗺️ the DB doesn&#39;t care")}{sm(795,138,"vectors in, neighbors out —")}{sm(795,160,"embed() is ONE swappable")}{sm(795,182,"function (lesson 05)")}{num(680,75,3)}'
 f'{arr(310,140,346,140)}{arr(620,140,676,140)}'
 f'{sm(470,285,"⚠️ the same-model rule: query and documents must use the SAME embedder — change it → re-embed everything")}</svg>')
SVG[3]=(f'<svg viewBox="0 0 940 300" role="img">{B} x="40" y="40" width="420" height="130" rx="14"/>{t(250,72,"🧭 cosine: compare DIRECTIONS")}{sm(250,100,"10-page robot essay &amp; 1-line robot note")}{sm(250,122,"point the SAME way → 0.95 ✅ siblings")}{sm(250,150,"meaning is a direction; length is volume 📢")}{num(40,40,1)}'
 f'{D} x="490" y="40" width="420" height="130" rx="14"/>{t(700,72,"📏 distance: compare POSITIONS")}{sm(700,100,"the essay &#39;stands far&#39; from the note →")}{sm(700,122,"fooled by length — wrong verdict for text")}{num(490,40,2)}'
 f'{B} x="190" y="200" width="560" height="70" rx="14"/>{t(470,228,"⚡ the trick: normalize at WRITE time → cosine = plain dot product at READ time")}{sm(470,252,"one line, hardware-fast — our cosine() is just sum(x·y) because _normalize already ran")}{num(190,200,3)}</svg>')
SVG[4]=(f'<svg viewBox="0 0 940 300" role="img">{D} x="40" y="40" width="270" height="110" rx="14"/>{t(175,72,"🚶 brute force - exact")}{sm(175,100,"compare with ALL N seats")}{sm(175,122,"N=7k: fine · N=7M: 💀")}{num(40,40,1)}'
 f'{B} x="350" y="40" width="270" height="110" rx="14"/>{t(485,72,"🗺️ HNSW - friendship map")}{sm(485,100,"local friends + pen-pals across")}{sm(485,122,"the hall → log-ish greedy hops")}{num(350,40,2)}'
 f'{B} x="660" y="40" width="250" height="110" rx="14"/>{t(785,72,"🏘️ IVF - neighborhoods")}{sm(785,100,"pre-cluster districts; search")}{sm(785,122,"only the nearest few")}{num(660,40,3)}'
 f'{S} x="190" y="190" width="560" height="80" rx="14"/>{t(470,220,"🎯 the recall dial: speed ↔ % of TRUE neighbors found")}{sm(470,246,"95-99% recall at 100-1000× speedup is the standard trade — benchmarks without recall numbers are marketing")}{num(190,190,4)}</svg>')
SVG[5]=(f'<svg viewBox="0 0 940 300" role="img">{B} x="40" y="50" width="270" height="200" rx="14"/>{t(175,82,"1 🔢 embed()")}{sm(175,110,"hash words → 256 dims →")}{sm(175,132,"normalize · ← swap for a")}{sm(175,154,"model call HERE")}{sm(175,190,"embedder and store are")}{sm(175,212,"separate jobs — by design")}{num(40,50,1)}'
 f'{B} x="340" y="50" width="270" height="200" rx="14"/>{t(475,82,"2 📐 cosine()")}{sm(475,110,"one line: dot product")}{sm(475,132,"(normalize made it cheap)")}{num(340,50,2)}'
 f'{B} x="640" y="50" width="270" height="200" rx="14"/>{t(775,82,"3 🗄️ MiniVectorDB")}{sm(775,110,"add: embed + store")}{sm(775,132,"(id, vector, TEXT, stickers)")}{sm(775,158,"search: filter 🏷️ FIRST →")}{sm(775,180,"score → sort → top-k")}{sm(775,212,"missing on purpose: persistence,")}{sm(775,234,"deletes, ANN — your homework")}{num(640,50,3)}'
 f'{sm(470,285,"~70 lines, zero dependencies — a database you can hold entirely in your head")}</svg>')
SVG[6]=(f'<svg viewBox="0 0 940 300" role="img">{B} x="40" y="40" width="200" height="90" rx="12"/>{t(140,72,"📚 400-page book")}{sm(140,98,"can&#39;t sit in one chair")}'
 f'{B} x="300" y="40" width="300" height="90" rx="12"/>{t(450,66,"✂️ chunking - the craft")}{sm(450,90,"natural seams · self-contained ·")}{sm(450,112,"~hundreds of tokens · 10-15% overlap 🔁")}{num(300,40,1)}'
 f'{B} x="660" y="40" width="250" height="90" rx="12"/>{t(785,66,"🗂️ cards + stickers 🏷️")}{sm(785,90,"room:3A · kind:rules ·")}{sm(785,112,"source:handbook-p12 (receipts!)")}{num(660,40,2)}'
 f'{arr(240,85,296,85)}{arr(600,85,656,85)}'
 f'{D} x="40" y="170" width="420" height="100" rx="12"/>{sm(250,198,"❌ too big: five topics, one murky seat")}{sm(250,220,"❌ too small: &#39;…it must be returned&#39; — WHAT must?")}{sm(250,248,"chunking moves quality 2-5× · indexes move it 1.1×")}{num(40,170,3)}'
 f'{B} x="500" y="170" width="410" height="100" rx="12"/>{t(705,198,"🤝 hybrid search")}{sm(705,224,"meaning-search misses &#39;E-4012&#39;; keywords miss")}{sm(705,246,"synonyms — run BOTH, merge (RRF)")}{num(500,170,4)}</svg>')
SVG[7]=(f'<svg viewBox="0 0 940 300" role="img">{S} x="40" y="40" width="400" height="100" rx="12"/>{t(240,66,"🗂️ index time - once, on change")}{sm(240,92,"docs → ✂️ chunk → 🔢 embed → 🗄️ store")}{sm(240,114,"(re-index tonight, &#39;knows&#39; it tomorrow)")}{num(40,40,1)}'
 f'{B} x="500" y="40" width="410" height="100" rx="12"/>{t(705,66,"❓ question time - every query")}{sm(705,92,"embed the question (SAME model) → search k=4")}{sm(705,114,"(+ stickers 🏷️) → optional rerank 🧐")}{num(500,40,2)}'
 f'{B} x="190" y="170" width="560" height="100" rx="14"/>{t(470,200,"🪑 the desk: cards + &#39;answer ONLY from these, cite ids&#39;")}{sm(470,226,"→ ✅ grounded answer with receipts 🧾 (AI school L08-L10, now with YOUR page-finder)")}{sm(470,252,"debugging drill: bad answer? print the CARDS first — retrieval bug ≠ generation bug")}{num(190,170,3)}'
 f'{arr(440,90,496,90)}{arr(705,140,560,166)}{arr(240,140,340,166)}</svg>')
SVG[8]=(f'<svg viewBox="0 0 940 300" role="img">{B} x="40" y="40" width="270" height="100" rx="12"/>{t(175,68,"🐘 pgvector")}{sm(175,92,"the library you already have —")}{sm(175,114,"SQL + vectors, one backup")}{num(40,40,1)}'
 f'{B} x="340" y="40" width="270" height="100" rx="12"/>{t(475,68,"☁️ managed - Pinecone &amp; co")}{sm(475,92,"the rented hall — scale without")}{sm(475,114,"ops (the AWS build-vs-rent call)")}{num(340,40,2)}'
 f'{B} x="640" y="40" width="270" height="100" rx="12"/>{t(775,68,"🧪 Chroma · Qdrant · LanceDB")}{sm(775,92,"the lab bench — developer-first,")}{sm(775,114,"embedded to mid-scale")}{num(640,40,3)}'
 f'{B} x="190" y="165" width="270" height="100" rx="12"/>{t(325,193,"⚙️ FAISS · hnswlib")}{sm(325,217,"engine blocks, not databases —")}{sm(325,239,"max control, zero ops help")}{num(190,165,4)}'
 f'{B} x="490" y="165" width="270" height="100" rx="12"/>{t(625,193,"🔎 your old store, new tricks")}{sm(625,217,"OpenSearch/Redis/Mongo grew")}{sm(625,239,"a vector column — one less system")}{num(490,165,5)}'
 f'{sm(470,292,"the boring pick order: pgvector → embedded lab bench → managed/self-hosted at real scale · &lt;100k vectors? a loop is fine 😄")}</svg>')

def dsec(n):
    _,slug,folder,title,ana,_,color = L[n-1]
    return (f'\n<section class="dsec" id="l{n:02d}" style="--c:{color}">\n'
      f'  <h2><span class="ln">{n}</span> {title}</h2>\n  <p class="d">{ana}</p>\n  {SVG[n]}\n'
      f'  <p class="foot"><a href="{GH}/{slug}/lessons/{folder}/README.md">Read full lesson {n:02d} →</a></p>\n</section>\n')
ALL_DSECS = "".join(dsec(n) for n in range(1,9))

def card(n):
    _,slug,folder,title,ana,_,color = L[n-1]
    return (f'    <div class="lesson" style="--c:{color}"><div class="top"><span class="num">{n}</span><h3>{title}</h3></div>'
      f'<span class="ana">{ana}</span><code>{slug}</code>'
      f'<a class="go" href="{GH}/{slug}/lessons/{folder}/README.md">Read lesson →</a>'
      f'<a class="go" href="lesson-diagrams.html#l{n:02d}">See the diagram ↗</a></div>')

INDEX = head("Learn Vector Databases the school way — with a runnable mini DB",
  "8 lessons on vector databases with a real zero-dependency mini vector DB in the repo: embeddings, cosine similarity, ANN indexes, chunking, RAG wiring, and the product landscape.") + MARKER + f'''
<div class="wrap">
  <header>
    <h1>🗺️ Learn Vector Databases the school way</h1>
    <p class="sub">The library sorted by <b>meaning</b> — the machine under semantic search, RAG and
    agent memory. Taught the school way: <b>a real mini vector DB in the repo</b> (~70 lines, pure
    Python, zero dependencies) that you read in full — including one honest, deliberate failure
    that explains why learned embeddings exist.</p>
    <div class="chips">
      <span class="chip">🔢 embeddings</span><span class="chip">📐 cosine</span>
      <span class="chip">🏃 kNN &amp; HNSW</span><span class="chip">✂️ chunking</span>
      <span class="chip">🏷️ metadata filters</span><span class="chip">📖 RAG</span><span class="chip">🏬 the landscape</span>
    </div>
  </header>

  <div class="vs">
    <div class="vcol" style="border-top:5px solid {P1}">
      <h3>💡 Part 1 — THE IDEA (1–4)</h3>
      <ul>
        <li>keywords match strings; meaning needs seats 🗺️</li>
        <li>text → coordinates: the toy way and the real way</li>
        <li>similarity = direction (normalize, then dot) 🧭</li>
        <li>millions of seats: the friendship map (HNSW) 🏃</li>
      </ul>
    </div>
    <div class="vcol" style="border-top:5px solid {P2}">
      <h3>🔧 Part 2 — FOR REAL (5–8)</h3>
      <ul>
        <li>read the database whole: 70 honest lines 🔬</li>
        <li>scissors &amp; stickers: chunking is the quality lever ✂️</li>
        <li>RAG end to end, with YOUR page-finder 📖</li>
        <li>pgvector → Pinecone: picking without a bake-off 🏬</li>
      </ul>
    </div>
  </div>

  <pre><code># the 60-second wow — search by meaning, filters, and one honest failure:
git clone https://github.com/BaluRaut/learn-vectordb-school.git &amp;&amp; cd learn-vectordb-school
python3 vectordb/demo.py</code></pre>

  <h2 id="big-picture">🗺️ The big picture — one diagram, both worlds</h2>
  <p class="sub">Click for the <a href="images/big-picture-4k.png">4K version</a>.</p>
  <figure style="background:var(--card);border:1px solid var(--line);border-radius:14px;padding:14px;margin-top:16px">
    <a href="images/big-picture-4k.png"><img src="images/big-picture.svg" alt="The big picture: the idea (seats, similarity, neighbors) and the practice (build, chunking, RAG, landscape)" loading="lazy" style="width:100%;height:auto;border-radius:8px;background:#fff"></a>
  </figure>

  <h2 id="lessons">🎓 The 8 lessons</h2>
  <p class="sub">One git branch = one idea; branch 05 contains lessons 01–05. The natural deep-dive
  after the <a href="https://baluraut.github.io/learn-ai-school/">AI course</a>'s embeddings (L04)
  and RAG (L10) lessons — and the memory layer of the
  <a href="https://baluraut.github.io/learn-agents-school/">Agents school</a>.</p>
  <div class="grid">
{chr(10).join(card(n) for n in range(1,9))}
  </div>

  <div class="callout">🏬 <b>The showcase:</b> <a href="landscape.html">the product landscape</a> —
  pgvector, Pinecone-class, Chroma/Qdrant/LanceDB, FAISS, and your-old-store-with-new-tricks —
  compared honestly, with the boring pick order.</div>

  <h2 id="diagrams">📐 The lesson diagrams — follow the numbers</h2>
  <p class="sub">Blue = the idea, green = for real. Also on a
  <a href="lesson-diagrams.html">standalone page</a>.</p>
{ALL_DSECS}
  <a class="btn" href="{GH}/lesson-01-why-vector-db/lessons/01-why-vector-db/README.md">Start Lesson 01 →</a>
  <a class="btn alt" href="landscape.html">🏬 The landscape</a>
  <a class="btn alt" href="lesson-diagrams.html">📐 All 8 lesson diagrams</a>
  <a class="btn alt" href="quiz.html">🧪 Quiz</a>
  <a class="btn alt" href="study-plan.html">🗓️ Study plan</a>
  <a class="btn alt" href="https://baluraut.github.io/learn-ai-school/">🧠 The AI course</a>

  <footer>
    Learn VectorDB School · the hall is in the repo ·
    <a href="https://github.com/BaluRaut/learn-vectordb-school">github.com/BaluRaut/learn-vectordb-school</a> ·
    siblings: <a href="https://baluraut.github.io/learn-ai-school/">AI</a> ·
    <a href="https://baluraut.github.io/learn-agents-school/">Agents</a> ·
    <a href="https://baluraut.github.io/learn-mcp-school/">MCP</a>
   ·
  <a href="https://baluraut.github.io/school/">🏫 all schools</a>
 ·
  <a href="https://github.com/BaluRaut/learn-vectordb-school/issues">🐛 found a mistake?</a>
</footer>
</div>
</body>
</html>
'''

DIAGRAMS = head("Lesson diagrams — Learn VectorDB School",
  "All 8 vector database lessons as numbered diagrams — embeddings, similarity, ANN, chunking, RAG, landscape.") + MARKER + f'''
<div class="wrap">
<header>
  <p><a href="index.html">← Back to the course home</a></p>
  <h1>📐 The 8 lessons as diagrams</h1>
  <p class="sub">Blue = the idea (1–4) · green = for real (5–8). Follow the circled numbers.</p>
  <nav class="toc">
    <a href="#l01">1 Why vector DBs</a><a href="#l02">2 Text→vectors</a><a href="#l03">3 Similarity</a>
    <a href="#l04">4 Neighbors</a><a href="#l05">5 Build</a><a href="#l06">6 Chunking</a>
    <a href="#l07">7 RAG</a><a href="#l08">8 Landscape</a>
  </nav>
</header>
{ALL_DSECS}
<footer>
  Learn VectorDB School · <a href="index.html">Course home</a> · <a href="landscape.html">Landscape</a> ·
  <a href="https://github.com/BaluRaut/learn-vectordb-school">GitHub</a>
 ·
  <a href="https://baluraut.github.io/school/">🏫 all schools</a>
 ·
  <a href="https://github.com/BaluRaut/learn-vectordb-school/issues">🐛 found a mistake?</a>
</footer>
</div>
</body>
</html>
'''

def fam(id_, color, title, what, shines, limits, pick):
    li = lambda xs: "".join(f"<li>{x}</li>" for x in xs)
    return f'''
<section class="dsec" id="{id_}" style="--c:{color}">
  <h2>{title}</h2>
  <p class="d">{what}</p>
  <div class="quad">
    <div class="q merit"><h4>✨ Where it shines</h4><ul>{li(shines)}</ul></div>
    <div class="q demerit"><h4>⚠️ Limits</h4><ul>{li(limits)}</ul></div>
    <div class="q use"><h4>🧭 Pick it when</h4><ul>{li(pick)}</ul></div>
  </div>
</section>'''

LANDSCAPE = head("The vector DB landscape — Learn VectorDB School",
  "pgvector, managed services, developer-first stores, FAISS-class libraries, and legacy stores with vector columns — compared honestly, with a picking guide.") + MARKER + f'''
<div class="wrap">
<header>
  <p><a href="index.html">← Back to the course home</a></p>
  <h1>🏬 The landscape — picking without a bake-off</h1>
  <p class="sub">Five families, honest verdicts, and the boring pick order. The questions that
  actually differentiate: <b>filtered search at scale · hybrid built-in · ops story (deletes!
  backups! multi-tenancy!) · the re-embedding day ⚠️ · recall numbers attached to speed claims</b>.
  Companion to <a href="{GH}/lesson-08-landscape/lessons/08-landscape/README.md">lesson 08</a>.</p>
  <nav class="toc">
    <a href="#pgvector">🐘 pgvector</a><a href="#managed">☁️ Managed</a>
    <a href="#devfirst">🧪 Developer-first</a><a href="#engines">⚙️ Engines</a><a href="#legacy">🔎 Old store, new tricks</a>
  </nav>
</header>
{fam("pgvector", P1, "🐘 pgvector — the library you already have",
  "A Postgres extension: vectors as a column type, similarity as an operator, HNSW index included. Your data and your seats in ONE database, one backup, one access model — with SQL JOINs right next to semantic search.",
  ["one system: transactions, JOINs, backups you already run","filters are just WHERE clauses — the L06 problem, solved by SQL","fine to millions of vectors with HNSW"],
  ["you operate Postgres (or pay RDS — AWS school!)","extreme scale/latency needs eventually outgrow it","vector features trail the specialists by months"],
  ["you HAVE Postgres and the corpus fits — the default answer","compliance wants data in one audited place"])}
{fam("managed", P1, "☁️ Managed — Pinecone &amp; friends (the rented hall)",
  "Fully hosted vector search: you POST vectors, they handle indexes, scaling, filtered ANN, replication. The AWS build-vs-rent question (EC2 L08), answered 'rent'.",
  ["zero ops; scales past what you'd want to operate","filtered ANN + hybrid done properly, by specialists","predictable latency SLAs at big N"],
  ["per-query/per-pod pricing adds up at volume","your data leaves home (agreements matter)","vendor coupling; migration = re-upload everything"],
  ["tens of millions of vectors + strict latency + no ops appetite","the team is product-only and speed-to-market rules"])}
{fam("devfirst", P2, "🧪 Developer-first — Chroma · Qdrant · Weaviate · LanceDB",
  "The lab benches: pip-install or one container, embedded or server mode, APIs built for AI apps. Each has a specialty — Qdrant (filters/perf, Rust), Weaviate (batteries included), Chroma (prototyping DX), LanceDB (columnar, local-first).",
  ["fastest start: notebook → prototype in minutes","embedded mode = no server at all (SQLite energy)","self-hostable at real scale (k8s school skills apply ☸️)"],
  ["another system to run once past embedded mode","maturity varies by feature — test YOUR filters + deletes","easy start can hide the ops cliff at scale"],
  ["prototypes and mid-scale products","self-hosting by choice, with the ops skills to back it"])}
{fam("engines", P2, "⚙️ Engines — FAISS · hnswlib · ScaNN",
  "Not databases: LIBRARIES implementing lesson 04's indexes at maximum speed. No persistence, no filters, no replication — you build the database around the engine.",
  ["fastest raw ANN available; total control of index params","research-grade: every algorithm, every knob","embed inside your own service — no extra hop"],
  ["everything else is DIY: storage, deletes, filters, HA","GPU/memory tuning is on you","easy to build a worse database than the ones for sale 😄"],
  ["you're building infrastructure or doing research","extreme perf needs where a stock DB measured short"])}
{fam("legacy", P2, "🔎 The old store learned new tricks — OpenSearch · Redis · Mongo · SQLite-vec",
  "Your existing search/cache/document store grew a vector column. Often the pragmatic winner: one less system, hybrid search where the keywords already live.",
  ["reuse deployed infra, auth, backups, dashboards","OpenSearch/Elastic: keyword+vector hybrid in one engine","team already knows how to operate it"],
  ["vector features are add-ons — depth varies a lot","perf ceilings below the specialists","two workloads now share one cluster's fate (noisy neighbors)"],
  ["it's already running and benchmarks say it fits","hybrid search matters and your keywords live there"])}
<section class="dsec" style="--c:{P2}">
  <h2>🧭 The boring pick order (from lesson 08)</h2>
  <p class="d">1 have Postgres + corpus fits → <b>pgvector</b> · 2 prototype → <b>embedded lab bench</b> ·
  3 big scale, no ops → <b>managed</b> · 4 big scale, ops appetite → <b>Qdrant/Weaviate self-hosted</b> ·
  5 building an engine → <b>FAISS</b> · 6 under ~100k vectors → <b>a loop is fine</b> 😄 —
  and whatever you pick, the embedder boundary (L05) keeps your vectors portable.</p>
</section>
<footer>
  Learn VectorDB School · <a href="index.html">Course home</a> ·
  <a href="lesson-diagrams.html">Lesson diagrams</a> ·
  <a href="https://github.com/BaluRaut/learn-vectordb-school">GitHub</a>
 ·
  <a href="https://baluraut.github.io/school/">🏫 all schools</a>
 ·
  <a href="https://github.com/BaluRaut/learn-vectordb-school/issues">🐛 found a mistake?</a>
</footer>
</div>
</body>
</html>
'''

import os
os.makedirs('docs', exist_ok=True)
open('docs/index.html','w').write(INDEX)
open('docs/lesson-diagrams.html','w').write(DIAGRAMS)
open('docs/landscape.html','w').write(LANDSCAPE)
print("generated: index dsec =", INDEX.count('class="dsec"'),
      "| diagrams =", DIAGRAMS.count('class="dsec"'),
      "| landscape sections =", LANDSCAPE.count('class="dsec"'))
