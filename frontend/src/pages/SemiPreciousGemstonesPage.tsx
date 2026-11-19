import React, { useEffect, useState, useMemo, useCallback, useRef } from 'react';
import { Search, Sparkles, X, RotateCcw } from 'lucide-react';
import type { GemstoneItem } from '../types/gemstone';
import { fetchGemstones } from '../services/api';
import { GemstoneCard } from '../components/GemstoneCard/GemstoneCard';
import { FALLBACK_GEMSTONES } from '../data/gemstoneFallbackData';
import { SEO } from '../components/SEO';

const semiPreciousSchema = {
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "Semi-Precious Gemstones Mineral Panorama | RMK Gems",
  "url": "https://rmkgems.com/semi-precious-gemstones",
  "description": "Discover authentic semi-precious gemstones at RMK Gems Tenkasi. Over 50+ mineral varieties including Amethyst, Citrine, Aquamarine, Garnet, Peridot, Tourmaline, Moonstone, and more.",
  "provider": {
    "@type": "JewelryStore",
    "name": "RMK Gems",
    "telephone": "+919385706450"
  }
};

export const SemiPreciousGemstonesPage: React.FC = () => {
  const [gemstones, setGemstones] = useState<GemstoneItem[]>(() =>
    FALLBACK_GEMSTONES.filter((g) => g.category_slug === 'semi-precious')
  );
  const [searchQuery, setSearchQuery] = useState('');
  const inputRef = useRef<HTMLInputElement>(null);

  const loadData = useCallback(() => {
    fetchGemstones({ category: 'semi-precious', page_size: 100 })
      .then((res) => {
        setGemstones(res.items);
      })
      .catch((err) => {
        console.error('Error loading semi-precious gemstones:', err);
      });
  }, []);

  useEffect(() => {
    window.scrollTo(0, 0);
    loadData();
  }, [loadData]);

  // Robust multi-word search matching across name, colour, and description
  const filteredGemstones = useMemo(() => {
    const trimmed = searchQuery.trim().toLowerCase();
    if (!trimmed) return gemstones;

    const terms = trimmed.split(/\s+/).filter(Boolean);

    return gemstones.filter((gem) => {
      const name = (gem.name || '').toLowerCase();
      const desc = (gem.short_description || '').toLowerCase();
      const colour = (gem.colour || '').toLowerCase();
      const searchableText = `${name} ${colour} ${desc}`;

      // Every word term must match somewhere in the gemstone data
      return terms.every((term) => searchableText.includes(term));
    });
  }, [gemstones, searchQuery]);

  // Clear search and restore focus to input
  const handleClear = useCallback(() => {
    setSearchQuery('');
    if (inputRef.current) {
      inputRef.current.focus();
    }
  }, []);

  return (
    <>
      <SEO
        title="Semi-Precious Gemstones Collection"
        description="Browse 50+ varieties of authentic semi-precious gemstones at RMK Gems Tenkasi: Amethyst, Aquamarine, Moonstone, Opal, Topaz, Garnet & more with direct WhatsApp enquiry."
        canonical="/semi-precious-gemstones"
        ogImage="/images/stones/amethyst.png"
        schema={semiPreciousSchema}
      />
      <main className="py-12 sm:py-16 bg-[#FAF8F5] min-h-screen">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          
          {/* Page Header */}
          <div className="text-center max-w-3xl mx-auto mb-12">
            <div className="inline-flex items-center gap-1.5 text-xs font-semibold uppercase tracking-[0.2em] text-[#997A48] mb-3">
              <Sparkles className="w-4 h-4" />
              <span>Mineral Panorama</span>
            </div>

            <h1 className="font-serif text-3xl sm:text-5xl font-bold text-[#1E1E1E] tracking-tight">
              Semi-Precious Gemstones
            </h1>

            <div className="w-20 h-0.5 bg-[#C5A880] mx-auto mt-4 mb-5" />

            <p className="text-sm sm:text-base text-[#717171] leading-relaxed">
              Discover our extensive collection of fine natural minerals and gemstones. Click any stone to view its details.
            </p>
          </div>

          {/* Search Bar */}
          <div className="max-w-md mx-auto mb-10 relative">
            <label htmlFor="gemstone-search" className="sr-only">
              Search semi-precious gemstones by name
            </label>
            <div className="relative flex items-center">
              <input
                ref={inputRef}
                id="gemstone-search"
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                placeholder="Search gemstones (e.g. Amethyst, Moonstone, Quartz)..."
                className="w-full pl-11 pr-10 py-3 text-sm bg-white border border-[#E8E2D9] rounded-full shadow-2xs focus:outline-none focus:border-[#997A48] focus:ring-1 focus:ring-[#997A48] transition-all placeholder:text-[#9A9A9A] text-[#1E1E1E]"
                aria-label="Search semi-precious gemstones"
              />
              <Search className="w-4 h-4 text-[#997A48] absolute left-4 pointer-events-none" />
              {searchQuery && (
                <button
                  type="button"
                  onClick={handleClear}
                  className="absolute right-3.5 p-1 rounded-full text-[#717171] hover:text-[#1E1E1E] hover:bg-[#F4EFE6] transition-colors focus:outline-none"
                  aria-label="Clear search input"
                >
                  <X className="w-3.5 h-3.5" />
                </button>
              )}
            </div>
          </div>

          {/* Fallback Warning if backend unreachable and we loaded 0 stones */}
          {gemstones.length === 0 ? (
            <div className="text-center py-16 bg-white rounded-2xl border border-[#E8E2D9] p-8 max-w-lg mx-auto shadow-xs">
              <p className="text-base text-[#1E1E1E] font-medium mb-2">
                Unable to load gemstone catalogue
              </p>
              <p className="text-xs text-[#717171] mb-6">
                Please check your network connection or try refreshing the page.
              </p>
              <button
                type="button"
                onClick={loadData}
                className="inline-flex items-center gap-2 px-5 py-2.5 text-xs font-semibold text-white bg-[#997A48] hover:bg-[#806437] rounded-full transition-colors cursor-pointer"
              >
                <RotateCcw className="w-3.5 h-3.5" />
                <span>Retry Catalogue</span>
              </button>
            </div>
          ) : filteredGemstones.length === 0 ? (
            /* Search yielded no results */
            <div className="text-center py-16 bg-white rounded-2xl border border-[#E8E2D9] p-8 max-w-lg mx-auto shadow-xs">
              <p className="text-base text-[#1E1E1E] font-medium mb-2">
                No gemstones found matching &ldquo;{searchQuery}&rdquo;
              </p>
              <p className="text-xs text-[#717171] mb-6">
                Try searching by mineral name like &ldquo;Quartz&rdquo;, &ldquo;Turquoise&rdquo;, &ldquo;Amethyst&rdquo;, or &ldquo;Onyx&rdquo;.
              </p>
              <button
                type="button"
                onClick={handleClear}
                className="px-5 py-2.5 text-xs font-semibold text-[#997A48] bg-[#F4EFE6] hover:bg-[#EAE2D5] rounded-full transition-colors cursor-pointer"
              >
                Clear Search & Show All ({gemstones.length})
              </button>
            </div>
          ) : (
            /* Grid of gemstones */
            <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-4 gap-6 sm:gap-8">
              {filteredGemstones.map((gemstone) => (
                <GemstoneCard key={gemstone.id} gemstone={gemstone} />
              ))}
            </div>
          )}

        </div>
      </main>
    </>
  );
};
