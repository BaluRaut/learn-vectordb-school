"""A REAL mini vector database in pure Python — readable in full. (Lessons 02–06)

Text → vector (hashed bag-of-words) → cosine similarity → top-k search,
with metadata filters. Zero dependencies.

HONEST LABEL: real systems use LEARNED embeddings (an AI model turns text
into meaning-coordinates — AI school, lesson 04). Our toy uses word-count
vectors, so it finds SHARED WORDS, not shared MEANING. The demo makes that
limitation visible on purpose — it's the best argument for real embeddings
you'll ever run.

    python3 vectordb/demo.py
"""
import hashlib
import math
import re

DIMS = 256   # our "meaning space" has 256 seats-directions (real ones: 768-3072)

# ───────────────── 1) TEXT → VECTOR (lesson 02) ─────────────────
def _tokens(text):
    return re.findall(r"[a-z0-9]+", text.lower())

def embed(text):
    """Hashed bag-of-words: each word bumps one of DIMS buckets.
    Real life: replace THIS function with a call to an embedding model —
    everything else in the file stays exactly the same."""
    v = [0.0] * DIMS
    for tok in _tokens(text):
        bucket = int(hashlib.md5(tok.encode()).hexdigest(), 16) % DIMS
        v[bucket] += 1.0
    return _normalize(v)

def _normalize(v):
    n = math.sqrt(sum(x * x for x in v))
    return [x / n for x in v] if n else v

# ───────────────── 2) SIMILARITY (lesson 03) ─────────────────
def cosine(a, b):
    """Both vectors are normalized → cosine = plain dot product.
    1.0 = same direction (same words) · 0.0 = nothing in common."""
    return sum(x * y for x, y in zip(a, b))

# ───────────────── 3) THE DATABASE (lessons 04–06) ─────────────────
class MiniVectorDB:
    """add() stores (id, vector, text, metadata); search() is exact
    brute-force kNN — fine for thousands. Millions need ANN indexes
    (HNSW/IVF): same answers, shortcut maps (lesson 04)."""

    def __init__(self):
        self.rows = []                      # each: (id, vector, text, meta)

    def add(self, doc_id, text, **meta):
        self.rows.append((doc_id, embed(text), text, meta))

    def search(self, query, k=3, **filters):
        qv = embed(query)
        candidates = [
            (cosine(qv, vec), doc_id, text, meta)
            for doc_id, vec, text, meta in self.rows
            if all(meta.get(key) == val for key, val in filters.items())
        ]                                    # metadata filter = colored stickers 🏷️
        candidates.sort(reverse=True)        # highest similarity first
        return candidates[:k]

    def __len__(self):
        return len(self.rows)
