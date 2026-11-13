import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { Sparkles, ArrowRight } from 'lucide-react';
import type { GemstoneItem } from '../../types/gemstone';
import { fetchFeaturedGemstones } from '../../services/api';
import { GemstoneCard } from '../../components/GemstoneCard/GemstoneCard';
import { FALLBACK_GEMSTONES } from '../../data/gemstoneFallbackData';

export const FeaturedGemstones: React.FC = () => {
  const [featured, setFeatured] = useState<GemstoneItem[]>(() =>
    FALLBACK_GEMSTONES.filter((g) => g.is_featured)
  );

  useEffect(() => {
    fetchFeaturedGemstones().then((items) => {
      if (items && items.length > 0) {
        setFeatured(items);
      }
    });
  }, []);

  if (featured.length === 0) return null;

  return (
    <section className="py-20 bg-gradient-to-b from-[#FAF8F5] via-[#F6F1EA] to-[#FAF8F5] border-y border-[#E8E2D9]">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Section Header */}
        <div className="flex flex-col md:flex-row md:items-end justify-between mb-12">
          <div>
            <div className="inline-flex items-center gap-1.5 text-xs font-semibold uppercase tracking-widest text-[#997A48] mb-2">
              <Sparkles className="w-3.5 h-3.5" />
              <span>Signature Highlights</span>
            </div>
            <h2 className="font-serif text-3xl sm:text-4xl font-bold text-[#1E1E1E] tracking-tight">
              Featured Gemstones
            </h2>
          </div>

          <div className="mt-4 md:mt-0">
            <Link
              to="/precious-gemstones"
              className="inline-flex items-center gap-2 text-sm font-semibold text-[#997A48] hover:text-[#806437] transition-colors"
            >
              <span>View Full Precious Collection</span>
              <ArrowRight className="w-4 h-4" />
            </Link>
          </div>
        </div>

        {/* Featured Showcase Grid */}
        <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-6 lg:gap-8">
          {featured.slice(0, 8).map((gemstone) => (
            <GemstoneCard key={gemstone.id} gemstone={gemstone} />
          ))}
        </div>

      </div>
    </section>
  );
};
