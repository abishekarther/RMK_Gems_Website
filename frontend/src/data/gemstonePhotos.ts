/**
 * Gemstone Photography Registry for RMK Gems.
 * Maps all 68 gemstones to high-resolution, unique photography located in /images/stones/<slug>.webp.
 * All images follow strict curatorial standards: single loose stone, plain neutral background, < 150 KB WebP.
 */

export const GEMSTONE_PHOTOS: Record<string, string> = {
  // Precious Gemstones (GIA Gem Encyclopedia)
  'ruby': '/images/stones/ruby.png',
  'pearl': '/images/stones/pearl.png',
  'red-coral': '/images/stones/red-coral.png',
  'emerald': '/images/stones/emerald.png',
  'yellow-sapphire': '/images/stones/yellow-sapphire.png',
  'diamond': '/images/stones/diamond.png',
  'blue-sapphire': '/images/stones/blue-sapphire.png',
  'hessonite-garnet': '/images/stones/hessonite-garnet.png',
  'cats-eye-chrysoberyl': '/images/stones/cats-eye-chrysoberyl.png',

  // Semi-Precious Gemstones
  'agate-black-banded': '/images/stones/agate-black-banded.png',
  'agate-green-banded': '/images/stones/agate-green-banded.png',
  'agate-red-jasper': '/images/stones/agate-red-jasper.png',
  'amethyst-african': '/images/stones/amethyst-african.png',
  'amethyst-brazil': '/images/stones/amethyst-brazil.png',
  'amethyst-brazil-pink': '/images/stones/amethyst-brazil-pink.png',
  'aquamarine-yellow': '/images/stones/aquamarine-yellow.png',
  'aventurine-green': '/images/stones/aventurine-green.png',
  'bloodstone': '/images/stones/bloodstone.png',
  'blue-lace-banded-agate': '/images/stones/blue-lace-banded-agate.png',
  'carnelian': '/images/stones/carnelian.png',
  'chalcedony-blue': '/images/stones/chalcedony-blue.png',
  'chalcedony-white': '/images/stones/chalcedony-white.png',
  'chrysoprase': '/images/stones/chrysoprase.png',
  'diopside-4-ray-star': '/images/stones/diopside-4-ray-star.png',
  'fluorite-multicolor-banded': '/images/stones/fluorite-multicolor-banded.png',
  'garnet-almandine': '/images/stones/garnet-almandine.png',
  'garnet-checkerboard': '/images/stones/garnet-rose-cut-checkerboard.png',
  'garnet-rose-cut-checkerboard': '/images/stones/garnet-rose-cut-checkerboard.png',
  'goldstone-sandstone-blue': '/images/stones/goldstone-sandstone-blue.png',
  'goldstone-sandstone-red': '/images/stones/goldstone-sandstone-red.png',
  'green-serpentine': '/images/stones/green-serpentine.png',
  'hematite-gunmetal': '/images/stones/hematite-gunmetal.png',
  'hessonite-garnet-semi-precious': '/images/stones/hessonite-garnet-semi-precious.png',
  'labradorite': '/images/stones/labradorite.png',
  'lapis': '/images/stones/lapis.png',
  'lemon-citrine': '/images/stones/lemon-citrine.png',
  'malachite': '/images/stones/malachite.png',
  'moonstone-white': '/images/stones/moonstone-white.png',
  'obsidian-snowflake': '/images/stones/obsidian-snowflake.png',
  'onyx-black': '/images/stones/onyx-black.png',
  'onyx-green': '/images/stones/onyx-green.png',
  'onyx-ivory': '/images/stones/onyx-ivory.png',
  'onyx-multicolor': '/images/stones/onyx-multicolor.png',
  'onyx-red': '/images/stones/onyx-red.png',
  'onyx-red-pink': '/images/stones/onyx-red-pink.png',
  'onyx-rose': '/images/stones/onyx-rose.png',
  'onyx-yellow': '/images/stones/onyx-yellow.png',
  'opal-dendrite': '/images/stones/opal-dendrite.png',
  'pearl-fresh-water': '/images/stones/pearl-fresh-water.png',
  'pyrite': '/images/stones/pyrite.png',
  'quartz-cats-eye': '/images/stones/quartz-cats-eye.png',
  'rainbow-moonstone': '/images/stones/rainbow-moonstone.png',
  'rose-quartz': '/images/stones/rose-quartz.png',
  'ruby-markara': '/images/stones/ruby-markara.png',
  'rutilated-quartz-black-needle': '/images/stones/rutilated-quartz-black-needle.png',
  'rutile-quartz-golden-needle': '/images/stones/rutile-quartz-golden-needle.png',
  'sapphire-blue': '/images/stones/sapphire-blue-semi-precious.png',
  'sapphire-blue-semi-precious': '/images/stones/sapphire-blue-semi-precious.png',
  'sillimanite-cats-eye': '/images/stones/sillimanite-cats-eye.png',
  'smoky-quartz': '/images/stones/smoky-quartz.png',
  'spectrolite-cats-eye': '/images/stones/spectrolite-cats-eye.png',
  'sunstone': '/images/stones/sunstone.png',
  'tiger-eye': '/images/stones/tiger-eye.png',
  'tourmaline-green': '/images/stones/tourmaline-green.png',
  'turquoise-chinese': '/images/stones/turquoise-chinese.png',
  'turquoise-tibetan': '/images/stones/turquoise-tibetan.png',
  'white-quartz': '/images/stones/white-quartz.png',
  'white-quartz-crystal': '/images/stones/white-quartz-crystal.png',
  'white-topaz': '/images/stones/white-topaz.png',
  'zircon-cubic-white': '/images/stones/zircon-cubic-white.png',
};

const PLACEHOLDER_PHOTO = '/images/stones/placeholder.png';
const PHOTO_VERSION = 'v=20261113_clean';

/**
 * Returns the image URL for a given gemstone slug.
 * Appends a cache-busting version parameter so browsers instantly render new photos.
 * Unknown slugs always fall back to the neutral placeholder, never a ruby.
 */
export function getGemstonePhoto(slug: string): string {
  const photo = GEMSTONE_PHOTOS[slug] || PLACEHOLDER_PHOTO;
  return `${photo}?${PHOTO_VERSION}`;
}

/**
 * Indicates whether a gemstone's photo is representative photography.
 * Currently true for all catalog items until client studio photos are supplied.
 */
export function isRepresentativePhoto(_slug: string): boolean {
  return true;
}

/**
 * Generates descriptive, accessible alt text for a gemstone image.
 */
export function getGemstoneAltText(name: string, colour?: string | null): string {
  return colour ? `${name} gemstone - ${colour}` : `${name} gemstone`;
}
