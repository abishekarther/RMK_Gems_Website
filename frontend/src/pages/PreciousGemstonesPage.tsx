import React, { useEffect, useState } from 'react';
import { Sparkles } from 'lucide-react';
import type { GemstoneItem } from '../types/gemstone';
import { fetchGemstones } from '../services/api';
import { GemstoneCard } from '../components/GemstoneCard/GemstoneCard';
import { FALLBACK_GEMSTONES } from '../data/gemstoneFallbackData';

export const PreciousGemstonesPage: React.FC = () => {
  const [gemstones, setGemstones] = useState<GemstoneItem[]>(() =>
    FALLBACK_GEMSTONES.filter((g) => g.category_slug === 'precious')
  );
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    window.scrollTo(0, 0);
    fetchGemstones({ category: 'precious', page_size: 50 })
      .then((res) => {
        setGemstones(res.items);
      })
      .finally(() => setLoading(false));
  }, []);

  return (
    <main className="py-12 sm:py-16 bg-[#FAF8F5] min-h-screen">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Page Header */}
        <div className="text-center max-w-3xl mx-auto mb-16">
          <div className="inline-flex items-center gap-1.5 text-xs font-semibold uppercase tracking-[0.2em] text-[#997A48] mb-3">
            <Sparkles className="w-4 h-4" />
            <span>Master Collection</span>
          </div>

          <h1 className="font-serif text-3xl sm:text-5xl font-bold text-[#1E1E1E] tracking-tight">
            Precious Gemstones
          </h1>

          <div className="w-20 h-0.5 bg-[#C5A880] mx-auto mt-4 mb-5" />

          <p className="text-sm sm:text-base text-[#717171] leading-relaxed">
            Revered across millennia for rarity, brilliance, and cultural significance. Select any stone to view its details.
          </p>
        </div>

        {/* Gemstone Gallery Grid */}
        {loading && gemstones.length === 0 ? (
          <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-3 gap-6 sm:gap-10 py-12 animate-pulse">
            {[...Array(6)].map((_, i) => (
              <div key={i} className="aspect-square bg-[#F4EFE6] rounded-xl flex items-center justify-center text-xs text-[#997A48]">
                Loading...
              </div>
            ))}
          </div>
        ) : (
          <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-3 gap-6 sm:gap-10">
            {gemstones.map((gemstone) => (
              <GemstoneCard key={gemstone.id} gemstone={gemstone} />
            ))}
          </div>
        )}

      </div>
    </main>
  );
};
