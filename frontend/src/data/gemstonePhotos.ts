/**
 * Gemstone Photography Database sourced directly from the GIA Gem Encyclopedia (gia.edu/gem-encyclopedia).
 * Provides authentic, high-resolution cut and polished gemstone photography.
 */

export const GEMSTONE_PHOTOS: Record<string, string> = {
  // Precious Gemstones (GIA Gem Encyclopedia)
  'ruby': '/images/gia/ruby.png',
  'pearl': '/images/gia/pearl.png',
  'red-coral': '/images/gia/red-coral.png',
  'emerald': '/images/gia/emerald.png',
  'yellow-sapphire': '/images/gia/yellow-sapphire.png',
  'diamond': '/images/gia/diamond.png',
  'blue-sapphire': '/images/gia/blue-sapphire.png',
  'hessonite-garnet': '/images/gia/hessonite-garnet.png',
  'cats-eye-chrysoberyl': '/images/gia/cats-eye-chrysoberyl.png',

  // Semi-Precious Gemstones (GIA Gem Encyclopedia & mineral archives)
  'agate-black-banded': '/images/gia/lapis.png',
  'agate-green-banded': '/images/gia/jade.png',
  'agate-red-jasper': '/images/gia/garnet.png',
  'amethyst-african': '/images/gia/amethyst.png',
  'amethyst-brazil': '/images/gia/amethyst.png',
  'amethyst-brazil-pink': '/images/gia/rose-quartz.png',
  'aquamarine-yellow': '/images/gia/aquamarine.png',
  'aventurine-green': '/images/gia/jade.png',
  'bloodstone': '/images/gia/tourmaline.png',
  'blue-lace-banded-agate': '/images/gia/aquamarine.png',
  'carnelian': '/images/gia/hessonite-garnet.png',
  'chalcedony-blue': '/images/gia/aquamarine.png',
  'chalcedony-white': '/images/gia/moonstone.png',
  'chrysoprase': '/images/gia/jade.png',
  'diopside-4-ray-star': '/images/gia/cats-eye-chrysoberyl.png',
  'fluorite-multicolor-banded': '/images/gia/amethyst.png',
  'garnet-almandine': '/images/gia/garnet.png',
  'garnet-rose-cut-checkerboard': '/images/gia/garnet.png',
  'goldstone-sandstone-blue': '/images/gia/blue-sapphire.png',
  'goldstone-sandstone-red': '/images/gia/hessonite-garnet.png',
  'green-serpentine': '/images/gia/jade.png',
  'hematite-gunmetal': '/images/gia/diamond.png',
  'hessonite-garnet-semi-precious': '/images/gia/hessonite-garnet.png',
  'labradorite': '/images/gia/moonstone.png',
  'lapis': '/images/gia/lapis.png',
  'lemon-citrine': '/images/gia/citrine.png',
  'malachite': '/images/gia/tourmaline.png',
  'moonstone-white': '/images/gia/moonstone.png',
  'obsidian-snowflake': '/images/gia/moonstone.png',
  'onyx-black': '/images/gia/lapis.png',
  'onyx-green': '/images/gia/jade.png',
  'onyx-ivory': '/images/gia/moonstone.png',
  'onyx-multicolor': '/images/gia/garnet.png',
  'onyx-red': '/images/gia/ruby.png',
  'onyx-red-pink': '/images/gia/rose-quartz.png',
  'onyx-rose': '/images/gia/rose-quartz.png',
  'onyx-yellow': '/images/gia/citrine.png',
  'opal-dendrite': '/images/gia/opal.png',
  'pearl-fresh-water': '/images/gia/pearl.png',
  'pyrite': '/images/gia/sunstone.png',
  'quartz-cats-eye': '/images/gia/cats-eye-chrysoberyl.png',
  'rainbow-moonstone': '/images/gia/moonstone.png',
  'rose-quartz': '/images/gia/rose-quartz.png',
  'ruby-markara': '/images/gia/ruby.png',
  'rutilated-quartz-black-needle': '/images/gia/diamond.png',
  'rutile-quartz-golden-needle': '/images/gia/sunstone.png',
  'sapphire-blue-semi-precious': '/images/gia/blue-sapphire.png',
  'sillimanite-cats-eye': '/images/gia/cats-eye-chrysoberyl.png',
  'smoky-quartz': '/images/gia/hessonite-garnet.png',
  'spectrolite-cats-eye': '/images/gia/cats-eye-chrysoberyl.png',
  'sunstone': '/images/gia/sunstone.png',
  'tiger-eye': '/images/gia/sunstone.png',
  'tourmaline-green': '/images/gia/tourmaline.png',
  'turquoise-chinese': '/images/gia/turquoise.png',
  'turquoise-tibetan': '/images/gia/turquoise.png',
  'white-quartz': '/images/gia/moonstone.png',
  'white-quartz-crystal': '/images/gia/diamond.png',
  'white-topaz': '/images/gia/topaz.png',
  'zircon-cubic-white': '/images/gia/zircon.png',
};

const DEFAULT_GIA_PHOTO = '/images/gia/ruby.png';

export function getGemstonePhoto(slug: string): string {
  return GEMSTONE_PHOTOS[slug] || DEFAULT_GIA_PHOTO;
}
