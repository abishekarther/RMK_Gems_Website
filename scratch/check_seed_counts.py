import sys, os
sys.path.insert(0, os.path.abspath('.'))
from backend.app.seed.seed_data import get_seed_data

cats, slides, shop, hours, prec, semi = get_seed_data()
all_stones = prec + semi
pub_prec = [s for s in prec if s['is_published']]
pub_semi = [s for s in semi if s['is_published']]

print(f"Total precious: {len(prec)}, published: {len(pub_prec)}")
print(f"Total semi-precious: {len(semi)}, published: {len(pub_semi)}")
print(f"Total published: {len(pub_prec) + len(pub_semi)}")

if len(pub_prec) != 9 or len(pub_semi) != 59:
    print("FAILED: Expected exactly 9 precious and 59 semi-precious published stones!")
    sys.exit(1)
else:
    print("SUCCESS: Exactly 9 precious and 59 semi-precious stones are published!")

