# 🏬 Lesson 08 — The landscape: picking a vector database for real

**📍 You are here:** Lesson **08** of 8 — the final lesson!

---

## 📦 What's in this branch

The complete course, **plus** the map of actual products and an honest
picking guide — expanded with comparison cards on
**🌐 [the landscape page](https://baluraut.github.io/learn-vectordb-school/landscape.html)**.

## 🧒 The families, in school words

- **🐘 "The library you already have" — pgvector** (an extension inside
  PostgreSQL): your data, your vectors, one database, one backup, SQL
  JOINs next to similarity search. The boring, excellent default for
  teams already on Postgres — up to millions of vectors.
- **☁️ "The rented hall" — Pinecone & managed friends**: fully hosted,
  scales past what you want to operate, filtered-ANN done for you —
  the AWS-course build-vs-rent question (EC2 L08!), answered "rent",
  with the same trade-offs (cost per query, data leaves home, less
  control).
- **🧪 "The lab bench" — Chroma, LanceDB, Qdrant, Weaviate**:
  developer-first stores; embedded-or-server modes; great DX for
  prototypes through mid-scale, each with its specialty (Qdrant:
  filters/perf; Weaviate: batteries; LanceDB: columnar/local).
- **⚙️ "The engine block" — FAISS, hnswlib**: not databases —
  *libraries* implementing lesson 04's indexes. Maximum control and
  speed, zero ops help (no persistence/filters/replication — you build
  those). For infra teams and researchers.
- **🔎 "The old library learned new tricks" — OpenSearch/Elastic,
  Redis, Mongo, SQLite-vec…**: your existing store grew a vector
  column. If it's already deployed and fits, one less system to run.

## 🧭 The picking flowchart (spoiler: it's usually pgvector)

1. Corpus fits in one Postgres and you HAVE Postgres → **pgvector**.
2. Prototype/notebook, want zero setup → **Chroma/LanceDB** embedded.
3. Serious scale (tens of millions+, strict latency, filtered ANN)
   and no ops appetite → **managed (Pinecone-class)**.
4. Same scale WITH ops appetite (and the k8s school under your belt ☸️)
   → **Qdrant/Weaviate self-hosted**.
5. Building your own engine / research → **FAISS/hnswlib**.
6. Under ~100k vectors total? A brute-force loop (our toy + a real
   embedder) is genuinely fine — don't buy a hall for a classroom. 😄

## ❓ The questions that actually differentiate (ask these, not "is it fast")

- **Filtered search at scale** — pre-filter vs post-filter (L06's
  trap): the #1 real-world differentiator.
- **Hybrid search built in?** (keyword + vector + fusion) — or do you
  bolt it on?
- **Ops story**: persistence, backups, updates/deletes (ANN indexes
  hate deletes!), multi-tenancy (namespaces! — hello k8s L05).
- **The re-embedding day** ⚠️ (L02's rule): when you change embedding
  models, EVERYTHING re-embeds. How painful is a full rebuild? This is
  the migration nobody plans for and everyone eventually does.
- **Recall benchmarks with numbers attached** (L04): "fast at what
  recall, on whose dataset?"

## 🤔 Why

Vector DB choice is a two-way door for small teams (swapping stores is
easy — the embedder boundary you learned in L05 makes vectors
portable) and a one-way-ish door at scale (data gravity). Start boring,
measure retrieval quality (L06's golden questions), and let real
bottlenecks — not benchmarks — trigger upgrades.

## 🧪 Try it — graduate by swapping the engine

Take lesson 07's RAG script and re-point it at a real store:

```bash
# pgvector (if you have Postgres):   CREATE EXTENSION vector;
#   store: INSERT ... embedding vector(256);  search: ORDER BY embedding <=> $1 LIMIT 3
# or Chroma (pip install chromadb):  3 lines: client, collection.add, collection.query
# keep OUR embed() first — then swap embed() for a real model and
# watch 'pupils' finally find 'students'. Both swaps, independently. 🎓
```

## 🎓 The hall is yours

Meaning as seats → seats as numbers → similarity as direction →
neighbors at scale → a database you READ → scissors and stickers →
the open-book pipeline → the product map. **You can now build a small
one, buy a big one, debug either — and explain to anyone exactly what
they bought.** 🗺️🎓

```bash
git checkout main
python3 vectordb/demo.py     # one last search, for fun
```
