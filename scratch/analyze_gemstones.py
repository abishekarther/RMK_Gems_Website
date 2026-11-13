import sys, re
sys.path.append('.')
from backend.app.seed.seed_data import get_seed_data

_, _, _, _, prec, semi = get_seed_data()
all_gems = prec + semi

forbidden_patterns = [
    r'\buntreated\b',
    r'\bunheated\b',
    r'natural colo[u]?r',
    r'\bcertif\w*',
    r'\bpremium\b',
    r'\bvaluation\b',
    r'\btalisman\w*',
    r'\bfortune\b',
    r'\bluck\w*',
    r'\brare\b',
    r'\bflawless\b',
    r'\bfinest\b',
    r'tamil',
]

print("=== GEMSTONES AUDIT ===")
issues = []
for g in all_gems:
    slug = g['slug']
    name = g['name']
    gem_issues = []
    
    # Check forbidden words
    for field, val in g.items():
        if isinstance(val, str):
            for pat in forbidden_patterns:
                m = re.findall(pat, val, re.IGNORECASE)
                if m:
                    gem_issues.append(f"Field '{field}' matches forbidden '{m}'")
                    
    # Check material_type
    mt = g.get('material_type')
    expected_mt = 'unconfirmed'
    if slug in ['pearl', 'pearl-fresh-water', 'red-coral']:
        expected_mt = 'organic'
    elif slug in ['goldstone-sandstone-blue', 'goldstone-sandstone-red']:
        expected_mt = 'imitation'
    elif slug.startswith('onyx-') and slug not in ['onyx-ivory', 'onyx-multicolor']:
        expected_mt = 'treated'
    elif slug in ['agate-black-banded', 'agate-green-banded']:
        expected_mt = 'treated'
        
    if mt != expected_mt:
        gem_issues.append(f"material_type is '{mt}', should be '{expected_mt}'")
        
    if gem_issues:
        issues.append((slug, name, gem_issues))

print(f"Total stones with issues: {len(issues)} / {len(all_gems)}")
for slug, name, g_issues in issues:
    print(f"\n[{slug}] {name}:")
    for iss in g_issues:
        print(f"  - {iss}")

