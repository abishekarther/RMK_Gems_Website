import React from 'react';
import { Link } from 'react-router-dom';
import { MapPin, Phone, MessageSquare, Clock, Truck, ExternalLink } from 'lucide-react';
import { SHOP_CONFIG, createGeneralWhatsAppEnquiry } from '../../config/shop';

export const Footer: React.FC = () => {
  return (
    <footer className="bg-[#1E1E1E] text-[#D1C7BA] pt-16 pb-12 border-t border-[#333333]">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10">
          
          {/* Col 1: Brand & Business Statement */}
          <div className="space-y-4">
            <div>
              <span className="font-serif text-2xl font-bold tracking-wider text-white">
                RMK GEMS
              </span>
              <p className="text-xs uppercase tracking-widest text-[#997A48] mt-0.5">
                Tenkasi, Tamil Nadu
              </p>
            </div>
            
            <p className="text-sm text-[#A89F91] leading-relaxed">
              {SHOP_CONFIG.aboutDescription}
            </p>

            {/* Delivery badge */}
            <div className="flex items-center gap-2 text-xs text-[#E5D7C2] bg-[#2A2A2A] px-3 py-2 rounded-lg border border-[#3A3A3A]">
              <Truck className="w-4 h-4 text-[#C5A880] shrink-0" />
              <span>{SHOP_CONFIG.deliveryStatement}</span>
            </div>
          </div>

          {/* Col 2: Navigation Links */}
          <div className="space-y-3">
            <h4 className="font-serif text-base font-semibold text-white tracking-wide">
              Gemstone Collections
            </h4>
            <ul className="space-y-2 text-sm">
              <li>
                <Link to="/" className="hover:text-white transition-colors">
                  Home
                </Link>
              </li>
              <li>
                <Link to="/precious-gemstones" className="hover:text-white transition-colors">
                  Precious Gemstones
                </Link>
              </li>
              <li>
                <Link to="/semi-precious-gemstones" className="hover:text-white transition-colors">
                  Semi-Precious Gemstones
                </Link>
              </li>
              <li>
                <Link to="/contact" className="hover:text-white transition-colors">
                  Contact & Visiting Hours
                </Link>
              </li>
            </ul>
          </div>

          {/* Col 3: Opening Hours Summary */}
          <div className="space-y-3">
            <h4 className="font-serif text-base font-semibold text-white tracking-wide flex items-center gap-1.5">
              <Clock className="w-4 h-4 text-[#C5A880]" /> Visiting Hours
            </h4>
            <div className="text-xs space-y-1.5 text-[#B8AF9F]">
              <div className="flex justify-between py-0.5 border-b border-[#2D2D2D]">
                <span>Mon, Wed, Thu, Sat:</span>
                <span className="text-white">10:30 AM – 9:00 PM</span>
              </div>
              <div className="flex justify-between py-0.5 border-b border-[#2D2D2D]">
                <span>Friday:</span>
                <span className="text-white">10:30 AM – 12:30 PM<br/>4:00 PM – 9:00 PM</span>
              </div>
              <div className="flex justify-between py-0.5 border-b border-[#2D2D2D]">
                <span>Tuesday:</span>
                <span className="text-[#C5A880] italic">Contact shop to confirm</span>
              </div>
              <div className="flex justify-between py-0.5">
                <span>Sunday:</span>
                <span className="text-white">Closed</span>
              </div>
            </div>
          </div>

          {/* Col 4: Contact & Directions */}
          <div className="space-y-3">
            <h4 className="font-serif text-base font-semibold text-white tracking-wide">
              Shop Location
            </h4>
            <div className="text-xs text-[#B8AF9F] space-y-2">
              <p className="flex items-start gap-2">
                <MapPin className="w-4 h-4 text-[#C5A880] shrink-0 mt-0.5" />
                <span>{SHOP_CONFIG.address}</span>
              </p>

              <p className="flex items-center gap-2">
                <Phone className="w-4 h-4 text-[#C5A880] shrink-0" />
                <a href={`tel:${SHOP_CONFIG.phoneTel}`} className="hover:text-white transition-colors">
                  {SHOP_CONFIG.phoneDisplay}
                </a>
              </p>

              <div className="pt-2 flex flex-col gap-2">
                <a
                  href={createGeneralWhatsAppEnquiry()}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center justify-center gap-2 px-4 py-2 text-xs font-semibold text-white bg-[#997A48] hover:bg-[#806437] transition-colors rounded-lg"
                >
                  <MessageSquare className="w-3.5 h-3.5" />
                  WhatsApp Enquiry
                </a>

                <div className="flex gap-2">
                  <a
                    href={SHOP_CONFIG.directionsUrl}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="flex-1 text-center py-1.5 px-2 text-[11px] bg-[#2A2A2A] hover:bg-[#333333] text-[#D1C7BA] rounded border border-[#3A3A3A] transition-colors flex items-center justify-center gap-1"
                  >
                    <span>Directions</span>
                    <ExternalLink className="w-3 h-3 text-[#C5A880]" />
                  </a>

                  <a
                    href={SHOP_CONFIG.mapSearchUrl}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="flex-1 text-center py-1.5 px-2 text-[11px] bg-[#2A2A2A] hover:bg-[#333333] text-[#D1C7BA] rounded border border-[#3A3A3A] transition-colors flex items-center justify-center gap-1"
                  >
                    <span>View Map</span>
                    <ExternalLink className="w-3 h-3 text-[#C5A880]" />
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Bottom copyright line */}
        <div className="mt-12 pt-6 border-t border-[#2D2D2D] text-center text-xs text-[#7A7468]">
          <p>© {new Date().getFullYear()} RMK Gems, Tenkasi. All rights reserved. Fine gemstone discovery & WhatsApp catalogue.</p>
        </div>
      </div>
    </footer>
  );
};

