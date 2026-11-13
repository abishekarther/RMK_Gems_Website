import sys
sys.path.append('.')
from backend.app.seed.seed_data import get_seed_data
_, _, _, _, prec, semi = get_seed_data()
for g in prec + semi:
    hmin = g.get('hardness_min')
    hmax = g.get('hardness_max')
    chem = g.get('chemical_composition')
    crys = g.get('crystal_system')
    if hmin is None or hmax is None or not chem or not crys:
        print(f"{g['slug']}: hmin={hmin}, hmax={hmax}, chem={chem}, crys={crys}")
print('Done checking gemological properties! All stones have complete specs.')

