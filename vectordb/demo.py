"""The mini vector DB, working — including its honest limitation. (Lessons 05–07)

    python3 vectordb/demo.py
"""
from vectordb import MiniVectorDB

db = MiniVectorDB()

# ── index the school's little library (chunk + metadata, lesson 06) ──
DOCS = [
    ("rules-1",  "Students must return library books within two weeks.",        {"kind": "rules"}),
    ("rules-2",  "The picnic requires one pizza per three students, round up.", {"kind": "rules"}),
    ("3a-1",     "Class 3A has twelve students and meets in the red building.", {"kind": "class", "room": "3A"}),
    ("3b-1",     "Class 3B has eleven students and meets in the blue building.",{"kind": "class", "room": "3B"}),
    ("robot-1",  "The school robot learns from examples, not from rulebooks.",  {"kind": "story"}),
    ("robot-2",  "The robot reads books in the library every single evening.",  {"kind": "story"}),
    ("lunch-1",  "The canteen serves dal and rice for lunch on Tuesdays.",      {"kind": "food"}),
]
for doc_id, text, meta in DOCS:
    db.add(doc_id, text, **meta)
print(f"📚 indexed {len(db)} chunks into the mini vector DB\n")

def show(title, results):
    print(title)
    for score, doc_id, text, meta in results:
        print(f"   {score:.2f}  [{doc_id}]  {text}")
    print()

# ── 1) semantic-ish search: shared words rank the right chunks up ──
show("🔎 query: 'how many pizzas for the picnic students?'",
     db.search("how many pizzas for the picnic students?", k=3))

# ── 2) metadata filters: colored stickers narrow the shelf (lesson 06) ──
show("🏷️ query: 'how many students?' — filtered to kind='class' only:",
     db.search("how many students?", k=2, kind="class"))

# ── 3) THE HONEST FAILURE — why real embeddings exist (lesson 02!) ──
show("😬 query: 'pupils' (a synonym our word-vectors can NOT see):",
     db.search("pupils", k=2))
print("💡 'pupils' shares no WORD with any chunk → useless scores above.")
print("   A LEARNED embedding model seats 'pupils' next to 'students'")
print("   (AI school L04) — swap embed() for a model call and this works.")
print("   The DATABASE part you just used stays exactly the same. 🗺️")
