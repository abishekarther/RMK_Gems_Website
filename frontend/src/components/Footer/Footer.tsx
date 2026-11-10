import React from 'react';
import { Link } from 'react-router-dom';
import { Phone, MessageSquare, MapPin, Truck } from 'lucide-react';
import { SHOP_CONFIG, createGeneralWhatsAppEnquiry } from '../../config/shop';

export const Footer: React.FC = () => {
  return (
    <footer className="bg-[#1A1A1A] text-[#D1C7BA] pt-14 pb-10 border-t border-[#2D2D2D]">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Main Footer Grid: 2 Clean, Distinct Columns */}
        <div className="grid grid-cols-1 md:grid-cols-12 gap-10 pb-10 border-b border-[#2D2D2D]">
          
          {/* Col 1: Brand & Craft (7 cols) */}
          <div className="md:col-span-7 space-y-4">
            <div>
              <span className="font-serif text-2xl font-bold tracking-wider text-white">
                RMK GEMS
              </span>
              <p className="text-xs uppercase tracking-widest text-[#997A48] mt-0.5">
                Tenkasi, Tamil Nadu, India
              </p>
            </div>
            
            <p className="text-xs sm:text-sm text-[#A8A196] leading-relaxed max-w-md">
              Sourcing, crafting, and delivering authentic natural gemstones across India.
            </p>

            <div className="inline-flex items-center gap-2 text-xs text-[#E5D7C2] bg-[#242424] px-3.5 py-1.5 rounded-full border border-[#333333]">
              <Truck className="w-3.5 h-3.5 text-[#C5A880] shrink-0" />
              <span>{SHOP_CONFIG.deliveryStatement}</span>
            </div>
          </div>

          {/* Col 2: Direct Connect & Location (5 cols) */}
          <div className="md:col-span-5 space-y-3 md:pl-6">
            <h4 className="font-serif text-sm font-semibold text-white tracking-wider uppercase text-xs">
              Quick Connect
            </h4>
            <div className="space-y-2.5 text-xs sm:text-sm">
              <p className="flex items-center gap-2.5">
                <Phone className="w-4 h-4 text-[#C5A880] shrink-0" />
                <a href={`tel:${SHOP_CONFIG.phoneTel}`} className="hover:text-white transition-colors font-medium">
                  {SHOP_CONFIG.phoneDisplay}
                </a>
              </p>

              <p className="flex items-center gap-2.5">
                <MessageSquare className="w-4 h-4 text-[#C5A880] shrink-0" />
                <a
                  href={createGeneralWhatsAppEnquiry()}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-[#C5A880] hover:underline font-medium"
                >
                  Chat on WhatsApp &rarr;
                </a>
              </p>

              <p className="flex items-start gap-2.5 text-[#A8A196]">
                <MapPin className="w-4 h-4 text-[#C5A880] shrink-0 mt-0.5" />
                <span>
                  Arafath Complex, Tenkasi •{' '}
                  <Link to="/contact" className="text-[#C5A880] hover:underline">
                    View Schedule & Map &rarr;
                  </Link>
                </span>
              </p>
            </div>
          </div>

        </div>

        {/* Bottom copyright line */}
        <div className="mt-8 flex flex-col sm:flex-row items-center justify-between text-xs text-[#7A7468] gap-4">
          <p>© {new Date().getFullYear()} RMK Gems. All rights reserved.</p>
          <p>No. 12, Arafath Complex, Keela Avani Moola Veethi, Tenkasi – 627811</p>
        </div>
      </div>
    </footer>
  );
};
