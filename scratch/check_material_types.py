import sys
sys.path.insert(0, '.')
from backend.app.seed.seed_data import get_seed_data
from collections import Counter

cats, slides, shop, hours, prec, semi = get_seed_data()
counts = Counter(s.get('material_type') for s in prec + semi)
print("material_type distribution:", counts)

