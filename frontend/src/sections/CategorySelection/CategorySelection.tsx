import React from 'react';
import { Link } from 'react-router-dom';
import { Sparkles, ArrowRight, Gem } from 'lucide-react';

export const CategorySelection: React.FC = () => {
  return (
    <section className="py-20 bg-[#FAF8F5]">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Section Heading */}
        <div className="text-center max-w-3xl mx-auto mb-16">
          <p className="text-xs uppercase tracking-[0.25em] text-[#997A48] font-semibold mb-2">
            Curated Collections
          </p>
          <h2 className="font-serif text-3xl sm:text-4xl text-[#1E1E1E] font-bold tracking-tight">
            Explore RMK Gemstone Galleries
          </h2>
          <div className="w-16 h-0.5 bg-[#C5A880] mx-auto mt-4 mb-4" />
          <p className="text-sm sm:text-base text-[#717171] leading-relaxed">
            Browse our curated categories of precious and semi-precious gemstones with direct WhatsApp assistance.
          </p>
        </div>

        {/* 2 Category Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 lg:gap-12">
          
          {/* Card 1: Precious Gemstones */}
          <div className="group relative bg-white rounded-2xl p-8 sm:p-10 border border-[#E8E2D9] shadow-xs hover:shadow-xl transition-all duration-300 flex flex-col justify-between overflow-hidden">
            <div className="absolute top-0 right-0 w-32 h-32 bg-[#997A48]/5 rounded-bl-full pointer-events-none -z-0" />
            
            <div className="relative z-10">
              <div className="w-12 h-12 rounded-xl bg-[#F4EFE6] flex items-center justify-center text-[#997A48] mb-6 group-hover:scale-110 transition-transform duration-300">
                <Sparkles className="w-6 h-6" />
              </div>

              <span className="text-xs font-semibold uppercase tracking-widest text-[#997A48]">
                Timeless Rarity & Value
              </span>
              
              <h3 className="font-serif text-2xl sm:text-3xl font-bold text-[#1E1E1E] mt-2 group-hover:text-[#997A48] transition-colors">
                Precious Gemstones
              </h3>

              <p className="text-sm sm:text-base text-[#5A5A5A] mt-4 leading-relaxed font-sans">
                Precious gemstones are rare, natural stones prized for their exceptional beauty, extraordinary hardness, and enduring value. Historically celebrated across cultures, they represent the pinnacle of fine jewelry.
              </p>
            </div>

            <div className="relative z-10 mt-10 pt-6 border-t border-[#E8E2D9]">
              <Link
                to="/precious-gemstones"
                className="inline-flex items-center gap-2 text-sm font-semibold text-[#997A48] group-hover:text-[#806437] transition-colors"
              >
                <span>Browse Precious Gallery</span>
                <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
              </Link>
            </div>
          </div>

          {/* Card 2: Semi-Precious Gemstones */}
          <div className="group relative bg-white rounded-2xl p-8 sm:p-10 border border-[#E8E2D9] shadow-xs hover:shadow-xl transition-all duration-300 flex flex-col justify-between overflow-hidden">
            <div className="absolute top-0 right-0 w-32 h-32 bg-[#997A48]/5 rounded-bl-full pointer-events-none -z-0" />
            
            <div className="relative z-10">
              <div className="w-12 h-12 rounded-xl bg-[#F4EFE6] flex items-center justify-center text-[#997A48] mb-6 group-hover:scale-110 transition-transform duration-300">
                <Gem className="w-6 h-6" />
              </div>

              <span className="text-xs font-semibold uppercase tracking-widest text-[#997A48]">
                Vibrant Variety & Color
              </span>
              
              <h3 className="font-serif text-2xl sm:text-3xl font-bold text-[#1E1E1E] mt-2 group-hover:text-[#997A48] transition-colors">
                Semi-Precious Gemstones
              </h3>

              <p className="text-sm sm:text-base text-[#5A5A5A] mt-4 leading-relaxed font-sans">
                Semi-precious gemstones encompass all other fine natural mineral gemstones. Prized for their wide spectrum of vibrant colors, distinctive patterns, and accessible charm, they are cherished for both ornamental elegance and everyday adornment.
              </p>
            </div>

            <div className="relative z-10 mt-10 pt-6 border-t border-[#E8E2D9]">
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
    </section>
  );
};
