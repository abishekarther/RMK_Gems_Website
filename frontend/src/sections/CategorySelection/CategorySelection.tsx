import React from 'react';
import { Link } from 'react-router-dom';
import { Sparkles, ArrowRight, Gem } from 'lucide-react';

export const CategorySelection: React.FC = () => {
  return (
    <section className="pt-4 pb-16 sm:pb-20 bg-[#FAF8F5]">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Section Heading - Compact, balanced spacing */}
        <div className="text-center max-w-3xl mx-auto mb-8 sm:mb-10">
          <p className="text-xs uppercase tracking-[0.25em] text-[#997A48] font-semibold mb-2">
            Curated Collections
          </p>
          <h2 className="font-serif text-3xl sm:text-4xl text-[#1E1E1E] font-bold tracking-tight">
            Explore RMK Gemstone Galleries
          </h2>
          <div className="w-16 h-0.5 bg-[#C5A880] mx-auto mt-3 mb-3" />
          <p className="text-sm sm:text-base text-[#717171] leading-relaxed max-w-2xl mx-auto">
            Browse our curated categories of precious and semi-precious gemstones with direct WhatsApp assistance.
          </p>
        </div>

        {/* 2 Category Cards - Tightly proportioned, no awkward gaps */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 lg:gap-8 max-w-5xl mx-auto">
          
          {/* Card 1: Precious Gemstones */}
          <div className="group relative bg-white rounded-2xl p-6 sm:p-8 border border-[#E8E2D9] shadow-xs hover:shadow-lg transition-all duration-300 flex flex-col overflow-hidden">
            <div className="absolute top-0 right-0 w-28 h-28 bg-[#997A48]/5 rounded-bl-full pointer-events-none" />
            
            <div className="relative z-10 flex-1 flex flex-col">
              <div className="flex items-center justify-between mb-4">
                <div className="w-11 h-11 rounded-xl bg-[#F4EFE6] flex items-center justify-center text-[#997A48] group-hover:scale-110 transition-transform duration-300">
                  <Sparkles className="w-5 h-5" />
                </div>
                <span className="text-[11px] font-semibold uppercase tracking-wider text-[#997A48] bg-[#F4EFE6] px-3 py-1 rounded-full">
                  9 Iconic Varieties
                </span>
              </div>

              <span className="text-xs font-semibold uppercase tracking-widest text-[#997A48] block">
                Timeless Rarity & Value
              </span>
              
              <h3 className="font-serif text-2xl sm:text-3xl font-bold text-[#1E1E1E] mt-1.5 group-hover:text-[#997A48] transition-colors">
                Precious Gemstones
              </h3>

              <p className="text-sm text-[#5A5A5A] mt-3 leading-relaxed font-sans flex-1">
                Precious gemstones are rare, natural stones prized for their exceptional beauty, extraordinary hardness, and enduring value. Historically celebrated across cultures, they represent the pinnacle of fine jewelry.
              </p>

              <div className="mt-6 pt-4 border-t border-[#E8E2D9]">
                <Link
                  to="/precious-gemstones"
                  className="inline-flex items-center gap-2 text-sm font-semibold text-[#997A48] group-hover:text-[#806437] transition-colors"
                >
                  <span>Browse Precious Gallery</span>
                  <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
                </Link>
              </div>
            </div>
          </div>

          {/* Card 2: Semi-Precious Gemstones */}
          <div className="group relative bg-white rounded-2xl p-6 sm:p-8 border border-[#E8E2D9] shadow-xs hover:shadow-lg transition-all duration-300 flex flex-col overflow-hidden">
            <div className="absolute top-0 right-0 w-28 h-28 bg-[#997A48]/5 rounded-bl-full pointer-events-none" />
            
            <div className="relative z-10 flex-1 flex flex-col">
              <div className="flex items-center justify-between mb-4">
                <div className="w-11 h-11 rounded-xl bg-[#F4EFE6] flex items-center justify-center text-[#997A48] group-hover:scale-110 transition-transform duration-300">
                  <Gem className="w-5 h-5" />
                </div>
                <span className="text-[11px] font-semibold uppercase tracking-wider text-[#997A48] bg-[#F4EFE6] px-3 py-1 rounded-full">
                  59 Mineral Varieties
                </span>
              </div>

              <span className="text-xs font-semibold uppercase tracking-widest text-[#997A48] block">
                Vibrant Variety & Color
              </span>
              
              <h3 className="font-serif text-2xl sm:text-3xl font-bold text-[#1E1E1E] mt-1.5 group-hover:text-[#997A48] transition-colors">
                Semi-Precious Gemstones
              </h3>

              <p className="text-sm text-[#5A5A5A] mt-3 leading-relaxed font-sans flex-1">
                Semi-precious gemstones encompass all other fine natural mineral gemstones. Prized for their wide spectrum of vibrant colors, distinctive patterns, and accessible charm, they are cherished for both ornamental elegance and everyday adornment.
              </p>

              <div className="mt-6 pt-4 border-t border-[#E8E2D9]">
                <Link
                  to="/semi-precious-gemstones"
                  className="inline-flex items-center gap-2 text-sm font-semibold text-[#997A48] group-hover:text-[#806437] transition-colors"
                >
                  <span>Browse Semi-Precious Gallery</span>
                  <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
                </Link>
              </div>
            </div>
          </div>

        </div>

      </div>
    </section>
  );
};
