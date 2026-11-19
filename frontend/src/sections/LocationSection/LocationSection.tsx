import React from 'react';
import { Link } from 'react-router-dom';
import { Truck, ArrowRight } from 'lucide-react';
import { SHOP_CONFIG } from '../../config/shop';

export const LocationSection: React.FC = () => {
  return (
    <section className="pt-12 pb-6 sm:pt-16 sm:pb-8 bg-[#FAF8F5]">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Brand Statement */}
        <div className="max-w-3xl mx-auto text-center p-6 sm:p-10 rounded-2xl bg-[#F4EFE6]/70 border border-[#E8E2D9] shadow-xs">
          <h1 className="text-xs font-semibold uppercase tracking-[0.25em] text-[#997A48] mb-2 block">
            RMK Gems &bull; Fine Natural Gemstones in Tenkasi
          </h1>
          
          <p className="font-brand-statement text-2xl sm:text-3xl text-[#1E1E1E] leading-relaxed font-medium">
            &ldquo;{SHOP_CONFIG.aboutDescription}&rdquo;
          </p>

          <div className="mt-5 inline-flex items-center gap-2 text-xs font-medium text-[#4A4A4A] bg-white px-4 py-1.5 rounded-full border border-[#E8E2D9] shadow-2xs">
            <Truck className="w-3.5 h-3.5 text-[#997A48]" />
            <span>{SHOP_CONFIG.deliveryStatement}</span>
          </div>

          <div className="mt-6 pt-5 border-t border-[#E8E2D9]/80 flex justify-center">
            <Link
              to="/contact"
              className="inline-flex items-center gap-2 text-xs font-semibold uppercase tracking-wider text-[#997A48] hover:text-[#806437] transition-colors"
            >
              <span>Visit Our Shop in Tenkasi</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </Link>
          </div>
        </div>

      </div>
    </section>
  );
};
