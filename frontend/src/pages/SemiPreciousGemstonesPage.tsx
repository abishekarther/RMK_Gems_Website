import React, { useEffect, useState, useMemo } from 'react';
import { Search, Sparkles, X } from 'lucide-react';
import type { GemstoneItem } from '../types/gemstone';
import { fetchGemstones } from '../services/api';
import { GemstoneCard } from '../components/GemstoneCard/GemstoneCard';

export const SemiPreciousGemstonesPage: React.FC = () => {
  const [gemstones, setGemstones] = useState<GemstoneItem[]>([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    window.scrollTo(0, 0);
    fetchGemstones({ category: 'semi-precious', page_size: 100 })
      .then((res) => {
        setGemstones(res.items);
      })
      .finally(() => setLoading(false));
  }, []);

  // Filter gemstones by search query
  const filteredGemstones = useMemo(() => {
    if (!searchQuery.trim()) return gemstones;
    const q = searchQuery.toLowerCase().trim();
    return gemstones.filter((g) => g.name.toLowerCase().includes(q));
  }, [gemstones, searchQuery]);

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
        <div className="max-w-md mx-auto mb-12 relative">
          <label htmlFor="gemstone-search" className="sr-only">
            Search semi-precious gemstones by name
          </label>
          <div className="relative">
            <input
              id="gemstone-search"
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Search by gemstone name (e.g. Amethyst, Moonstone, Lapis)..."
              className="w-full pl-11 pr-10 py-3 text-sm bg-white border border-[#E8E2D9] rounded-full focus:outline-none focus:ring-2 focus:ring-[#997A48] focus:border-transparent text-[#1E1E1E] placeholder-[#A09A8F] shadow-2xs"
            />
            <Search className="w-4 h-4 text-[#997A48] absolute left-4 top-1/2 -translate-y-1/2" />
            {searchQuery && (
              <button
                type="button"
                onClick={() => setSearchQuery('')}
                className="absolute right-3.5 top-1/2 -translate-y-1/2 text-[#717171] hover:text-[#1E1E1E] p-1"
                aria-label="Clear search"
              >
                <X className="w-4 h-4" />
              </button>
            )}
          </div>
          {searchQuery && (
            <p className="text-xs text-[#717171] mt-2 text-center">
              Showing {filteredGemstones.length} result{filteredGemstones.length !== 1 ? 's' : ''} for "{searchQuery}"
            </p>
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
        ) : filteredGemstones.length === 0 ? (
          <div className="text-center py-16 bg-white rounded-2xl border border-[#E8E2D9] p-8 max-w-lg mx-auto">
            <p className="text-base text-[#1E1E1E] font-medium mb-2">No gemstones found matching "{searchQuery}"</p>
            <p className="text-xs text-[#717171] mb-4">Try searching for another stone like "Quartz", "Turquoise", or "Onyx".</p>
            <button
              type="button"
              onClick={() => setSearchQuery('')}
              className="px-4 py-2 text-xs font-semibold text-[#997A48] bg-[#F4EFE6] hover:bg-[#EAE2D5] rounded-full transition-colors"
            >
              Clear Search
            </button>
          </div>
        ) : (
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
