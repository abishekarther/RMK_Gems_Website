import React, { useEffect, useState, useMemo, useCallback, useRef } from 'react';
import { Search, Sparkles, X, RotateCcw } from 'lucide-react';
import type { GemstoneItem } from '../types/gemstone';
import { fetchGemstones } from '../services/api';
import { GemstoneCard } from '../components/GemstoneCard/GemstoneCard';

export const SemiPreciousGemstonesPage: React.FC = () => {
  const [gemstones, setGemstones] = useState<GemstoneItem[]>([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [loading, setLoading] = useState(true);
  const inputRef = useRef<HTMLInputElement>(null);

  const loadData = useCallback(() => {
    setLoading(true);
    fetchGemstones({ category: 'semi-precious', page_size: 100 })
      .then((res) => {
        setGemstones(res.items);
      })
      .catch((err) => {
        console.error('Error loading semi-precious gemstones:', err);
      })
      .finally(() => setLoading(false));
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
              className="w-full pl-11 pr-12 py-3 text-sm bg-white border border-[#E8E2D9] rounded-full focus:outline-none focus:ring-2 focus:ring-[#997A48] focus:border-transparent text-[#1E1E1E] placeholder-[#A09A8F] shadow-2xs transition-all"
              autoComplete="off"
            />
            <Search className="w-4 h-4 text-[#997A48] absolute left-4 top-1/2 -translate-y-1/2 pointer-events-none" />
            
            {/* Clear Button: Immediate touch & click handling */}
            {searchQuery && (
              <button
                type="button"
                onClick={handleClear}
                onMouseDown={(e) => {
                  e.preventDefault();
                  handleClear();
                }}
                onTouchEnd={(e) => {
                  e.preventDefault();
                  handleClear();
                }}
                className="absolute right-3.5 top-1/2 -translate-y-1/2 p-1.5 text-[#717171] hover:text-[#1E1E1E] bg-[#F4EFE6] hover:bg-[#EAE2D5] rounded-full transition-colors z-10 cursor-pointer"
                aria-label="Clear search"
                title="Clear search"
              >
                <X className="w-3.5 h-3.5" />
              </button>
            )}
          </div>

          {searchQuery.trim() && (
            <div className="flex items-center justify-between text-xs text-[#717171] mt-2.5 px-3">
              <span>
                Found {filteredGemstones.length} stone{filteredGemstones.length !== 1 ? 's' : ''} matching &ldquo;{searchQuery.trim()}&rdquo;
              </span>
              <button
                type="button"
                onClick={handleClear}
                className="text-[#997A48] hover:underline font-medium cursor-pointer"
              >
                Clear
              </button>
            </div>
          )}
        </div>

        {/* Gemstone Photo Grid */}
        {loading ? (
          <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-4 gap-6 py-12 animate-pulse">
            {[...Array(8)].map((_, i) => (
              <div key={i} className="aspect-square bg-[#F4EFE6] rounded-xl flex items-center justify-center text-xs text-[#997A48]">
                Loading...
              </div>
            ))}
          </div>
        ) : gemstones.length === 0 ? (
          /* Empty / Failed to load state */
          <div className="text-center py-16 bg-white rounded-2xl border border-[#E8E2D9] p-8 max-w-lg mx-auto shadow-xs">
            <p className="text-base text-[#1E1E1E] font-medium mb-2">Unable to load gemstones</p>
            <p className="text-xs text-[#717171] mb-6">Please check your connection and try reloading the catalogue.</p>
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
  );
};
