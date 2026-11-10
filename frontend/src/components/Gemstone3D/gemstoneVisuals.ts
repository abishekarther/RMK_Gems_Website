export interface VisualConfig {
  cut: 'brilliant' | 'oval' | 'emerald' | 'cushion' | 'cabochon' | 'pearl';
  color: string;
  roughness: number;
  metalness: number;
  transmission: number;
  ior: number;
  opacity: number;
}

const DEFAULT_CONFIG: VisualConfig = {
  cut: 'cushion',
  color: '#C5A880',
  roughness: 0.1,
  metalness: 0.05,
  transmission: 0.85,
  ior: 1.62,
  opacity: 0.95,
};

const GEMSTONE_VISUAL_MAP: Record<string, Partial<VisualConfig>> = {
  // Precious
  'ruby': {
    cut: 'oval',
    color: '#9E1B32',
    roughness: 0.04,
    metalness: 0.02,
    transmission: 0.88,
    ior: 1.76,
  },
  'pearl': {
    cut: 'pearl',
    color: '#F4F1EA',
    roughness: 0.28,
    metalness: 0.15,
    transmission: 0.1,
    ior: 1.53,
    opacity: 1.0,
  },
  'red-coral': {
    cut: 'cabochon',
    color: '#D63426',
    roughness: 0.18,
    metalness: 0.05,
    transmission: 0.05,
    ior: 1.65,
    opacity: 1.0,
  },
  'emerald': {
    cut: 'emerald',
    color: '#137547',
    roughness: 0.06,
    metalness: 0.03,
    transmission: 0.86,
    ior: 1.57,
  },
  'yellow-sapphire': {
    cut: 'cushion',
    color: '#F0BA35',
    roughness: 0.04,
    metalness: 0.02,
    transmission: 0.9,
    ior: 1.76,
  },
  'diamond': {
    cut: 'brilliant',
    color: '#EBF4FA',
    roughness: 0.01,
    metalness: 0.05,
    transmission: 0.96,
    ior: 2.417,
  },
  'blue-sapphire': {
    cut: 'oval',
    color: '#123970',
    roughness: 0.04,
    metalness: 0.02,
    transmission: 0.86,
    ior: 1.76,
  },
  'hessonite-garnet': {
    cut: 'cushion',
    color: '#B85D19',
    roughness: 0.06,
    metalness: 0.02,
    transmission: 0.82,
    ior: 1.74,
  },
  'cats-eye-chrysoberyl': {
    cut: 'cabochon',
    color: '#9E9436',
    roughness: 0.08,
    metalness: 0.05,
    transmission: 0.45,
    ior: 1.75,
  },

  // Semi-Precious
  'agate-black-banded': { cut: 'cabochon', color: '#1A1A1A', roughness: 0.15, transmission: 0.05, opacity: 1.0 },
  'agate-green-banded': { cut: 'cabochon', color: '#275844', roughness: 0.14, transmission: 0.35 },
  'amethyst-african': { cut: 'oval', color: '#4B1A6D', roughness: 0.05, transmission: 0.88, ior: 1.54 },
  'amethyst-brazil': { cut: 'cushion', color: '#78468E', roughness: 0.05, transmission: 0.88, ior: 1.54 },
  'amethyst-brazil-pink': { cut: 'oval', color: '#BA7A93', roughness: 0.06, transmission: 0.84, ior: 1.54 },
  'aventurine-green': { cut: 'cabochon', color: '#3A7359', roughness: 0.15, transmission: 0.4 },
  'bloodstone': { cut: 'cabochon', color: '#233E30', roughness: 0.16, transmission: 0.05, opacity: 1.0 },
  'blue-lace-banded-agate': { cut: 'cabochon', color: '#8BA9C4', roughness: 0.12, transmission: 0.45 },
  'carnelian': { cut: 'cabochon', color: '#C8481A', roughness: 0.1, transmission: 0.65, ior: 1.54 },
  'chalcedony-blue': { cut: 'cabochon', color: '#6A8FA8', roughness: 0.12, transmission: 0.55 },
  'chalcedony-white': { cut: 'cabochon', color: '#E4E2DC', roughness: 0.12, transmission: 0.6 },
  'chrysoprase': { cut: 'cabochon', color: '#32A865', roughness: 0.1, transmission: 0.6 },
  'diopside-4-ray-star': { cut: 'cabochon', color: '#161616', roughness: 0.12, transmission: 0.05, opacity: 1.0 },
  'fluorite-multicolor-banded': { cut: 'cushion', color: '#55367B', roughness: 0.05, transmission: 0.9, ior: 1.43 },
  'garnet-almandine': { cut: 'oval', color: '#6D0B1C', roughness: 0.04, transmission: 0.84, ior: 1.78 },
  'green-serpentine': { cut: 'cabochon', color: '#436B44', roughness: 0.2, transmission: 0.2 },
  'hematite-gunmetal': { cut: 'cabochon', color: '#3E4146', roughness: 0.08, metalness: 0.9, transmission: 0.0, opacity: 1.0 },
  'labradorite': { cut: 'cabochon', color: '#215463', roughness: 0.12, transmission: 0.35, ior: 1.56 },
  'lapis': { cut: 'cabochon', color: '#173680', roughness: 0.18, transmission: 0.05, opacity: 1.0 },
  'lemon-citrine': { cut: 'cushion', color: '#D9D72E', roughness: 0.04, transmission: 0.9, ior: 1.54 },
  'malachite': { cut: 'cabochon', color: '#15613C', roughness: 0.15, transmission: 0.05, opacity: 1.0 },
  'moonstone-white': { cut: 'cabochon', color: '#ECE8E1', roughness: 0.14, transmission: 0.65, ior: 1.52 },
  'obsidian-snowflake': { cut: 'cabochon', color: '#1E1F21', roughness: 0.12, transmission: 0.05, opacity: 1.0 },
  'onyx-black': { cut: 'cabochon', color: '#101010', roughness: 0.08, transmission: 0.02, opacity: 1.0 },
  'onyx-green': { cut: 'cabochon', color: '#196142', roughness: 0.1, transmission: 0.5 },
  'onyx-ivory': { cut: 'cabochon', color: '#E4DDD2', roughness: 0.12, transmission: 0.5 },
  'onyx-multicolor': { cut: 'cabochon', color: '#99734A', roughness: 0.14, transmission: 0.4 },
  'onyx-red': { cut: 'cabochon', color: '#961B12', roughness: 0.1, transmission: 0.5 },
  'onyx-red-pink': { cut: 'cabochon', color: '#C65B70', roughness: 0.12, transmission: 0.5 },
  'onyx-rose': { cut: 'cabochon', color: '#B86A7B', roughness: 0.12, transmission: 0.5 },
  'onyx-yellow': { cut: 'cabochon', color: '#CE9A2B', roughness: 0.1, transmission: 0.55 },
  'opal-dendrite': { cut: 'cabochon', color: '#E2DFD7', roughness: 0.16, transmission: 0.25 },
  'pyrite': { cut: 'cushion', color: '#A88D3B', roughness: 0.1, metalness: 0.85, transmission: 0.0, opacity: 1.0 },
  'quartz-cats-eye': { cut: 'cabochon', color: '#7D876E', roughness: 0.1, transmission: 0.45, ior: 1.54 },
  'rainbow-moonstone': { cut: 'cabochon', color: '#DCE4EB', roughness: 0.12, transmission: 0.7, ior: 1.56 },
  'rose-quartz': { cut: 'cushion', color: '#DE9FAE', roughness: 0.08, transmission: 0.78, ior: 1.54 },
  'rutile-quartz-golden-needle': { cut: 'cushion', color: '#D8C384', roughness: 0.04, transmission: 0.9, ior: 1.54 },
  'sillimanite-cats-eye': { cut: 'cabochon', color: '#433D30', roughness: 0.1, transmission: 0.25 },
  'smoky-quartz': { cut: 'cushion', color: '#493C32', roughness: 0.04, transmission: 0.86, ior: 1.54 },
  'spectrolite-cats-eye': { cut: 'cabochon', color: '#1B3D54', roughness: 0.12, transmission: 0.3 },
  'sunstone': { cut: 'cushion', color: '#CB6F38', roughness: 0.1, transmission: 0.65 },
  'tiger-eye': { cut: 'cabochon', color: '#A87607', roughness: 0.14, transmission: 0.2, metalness: 0.15 },
  'tourmaline-green': { cut: 'emerald', color: '#165733', roughness: 0.04, transmission: 0.88, ior: 1.63 },
  'turquoise-chinese': { cut: 'cabochon', color: '#27A881', roughness: 0.22, transmission: 0.05, opacity: 1.0 },
  'turquoise-tibetan': { cut: 'cabochon', color: '#1F8C7D', roughness: 0.22, transmission: 0.05, opacity: 1.0 },
  'white-quartz': { cut: 'cushion', color: '#E4E4DE', roughness: 0.08, transmission: 0.7, ior: 1.54 },
  'white-quartz-crystal': { cut: 'brilliant', color: '#F0F4F7', roughness: 0.02, transmission: 0.94, ior: 1.54 },
  'white-topaz': { cut: 'brilliant', color: '#EBF1F5', roughness: 0.02, transmission: 0.95, ior: 1.61 },
};

export function getGemstoneVisualConfig(slug: string): VisualConfig {
  const custom = GEMSTONE_VISUAL_MAP[slug];
  if (!custom) return DEFAULT_CONFIG;
  return { ...DEFAULT_CONFIG, ...custom };
}

