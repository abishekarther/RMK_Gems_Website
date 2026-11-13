import sys, re, json
sys.path.append('.')
from backend.app.seed.seed_data import get_seed_data

_, _, _, _, prec, semi = get_seed_data()
all_backend_gems = prec + semi

# Also load frontend fallback gemstones
with open('frontend/src/data/gemstoneFallbackData.ts', 'r', encoding='utf-8') as f:
    text = f.read()
json_part = text.split("export const FALLBACK_GEMSTONES: GemstoneDetail[] = ")[1].rstrip(";\n")
all_frontend_gems = json.loads(json_part)

forbidden = [
    'untreated', 'unheated', 'natural color', 'natural colour',
    'certif', 'premium', 'valuation', 'talisman', 'fortune',
    'luck', 'rare', 'flawless', 'finest', 'tamil'
]

print("=== RUNNING CONTENT CHECK 1: FORBIDDEN WORDS AUDIT ===")

backend_violations = []
for g in all_backend_gems:
    for k, v in g.items():
        if isinstance(v, str):
            for word in forbidden:
                if re.search(r'\b' + word, v, re.I):
                    backend_violations.append((g['slug'], k, word, v))

frontend_violations = []
for g in all_frontend_gems:
    for k, v in g.items():
        if isinstance(v, str):
            for word in forbidden:
                if re.search(r'\b' + word, v, re.I):
                    frontend_violations.append((g['slug'], k, word, v))

print(f"Backend seed data forbidden violations: {len(backend_violations)}")
for b in backend_violations:
    print(f"  [BACKEND ERROR] {b}")

print(f"Frontend fallback data forbidden violations: {len(frontend_violations)}")
for fe in frontend_violations:
    print(f"  [FRONTEND ERROR] {fe}")

if backend_violations or frontend_violations:
    print("\nFAIL: Forbidden words found!")
    sys.exit(1)
else:
    print("\nPASS: ZERO forbidden words in backend seed data AND frontend fallback data!")

