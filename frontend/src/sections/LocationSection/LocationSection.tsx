import React from 'react';
import { MapPin, Phone, MessageSquare, Clock, Truck, ExternalLink, Navigation } from 'lucide-react';
import { SHOP_CONFIG, createGeneralWhatsAppEnquiry } from '../../config/shop';

export const LocationSection: React.FC = () => {
  return (
    <section className="py-20 bg-[#FAF8F5]">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Brand Statement */}
        <div className="max-w-3xl mx-auto text-center mb-16 p-8 sm:p-12 rounded-2xl bg-[#F4EFE6]/70 border border-[#E8E2D9]">
          <span className="text-xs font-semibold uppercase tracking-[0.25em] text-[#997A48] mb-3 block">
            About RMK Gems
          </span>
          <p className="font-brand-statement text-2xl sm:text-3xl text-[#1E1E1E] leading-relaxed font-medium">
            &ldquo;{SHOP_CONFIG.aboutDescription}&rdquo;
          </p>

          <div className="mt-6 inline-flex items-center gap-2 text-xs font-medium text-[#4A4A4A] bg-white px-4 py-2 rounded-full border border-[#E8E2D9] shadow-2xs">
            <Truck className="w-4 h-4 text-[#997A48]" />
            <span>{SHOP_CONFIG.deliveryStatement}</span>
          </div>
        </div>

        {/* Location & Map Preview Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          
          {/* Left: Contact Info & Opening Hours Table (7 cols) */}
          <div className="lg:col-span-7 bg-white rounded-2xl p-6 sm:p-8 border border-[#E8E2D9] shadow-xs">
            <span className="text-xs font-semibold uppercase tracking-widest text-[#997A48]">
              Visit Our Shop
            </span>
            <h3 className="font-serif text-2xl sm:text-3xl font-bold text-[#1E1E1E] mt-1 mb-5">
              Tenkasi, Tamil Nadu
            </h3>

            <div className="space-y-3 text-sm text-[#4A4A4A]">
              <div className="flex items-start gap-3">
                <MapPin className="w-5 h-5 text-[#997A48] shrink-0 mt-0.5" />
                <span>{SHOP_CONFIG.address}</span>
              </div>

              <div className="flex items-center gap-3">
                <Phone className="w-5 h-5 text-[#997A48] shrink-0" />
                <a href={`tel:${SHOP_CONFIG.phoneTel}`} className="hover:text-[#997A48] transition-colors font-medium">
                  {SHOP_CONFIG.phoneDisplay}
                </a>
              </div>
            </div>

            {/* Visiting Hours Table */}
            <div className="mt-6 pt-6 border-t border-[#E8E2D9]">
              <h4 className="text-xs uppercase tracking-wider font-semibold text-[#1E1E1E] mb-3 flex items-center gap-2">
                <Clock className="w-4 h-4 text-[#997A48]" />
                <span>Visiting Hours</span>
              </h4>

              <div className="overflow-hidden rounded-xl border border-[#E8E2D9] text-xs">
                <div className="grid grid-cols-2 bg-[#F4EFE6] px-4 py-2 font-semibold text-[#1E1E1E] border-b border-[#E8E2D9]">
                  <span>Day</span>
                  <span className="text-right">Timings</span>
                </div>
                <div className="divide-y divide-[#F4EFE6] bg-white">
                  <div className="grid grid-cols-2 px-4 py-2 text-[#4A4A4A]">
                    <span className="font-medium text-[#1E1E1E]">Monday</span>
                    <span className="text-right">10:30 AM – 9:00 PM</span>
                  </div>
                  <div className="grid grid-cols-2 px-4 py-2 text-[#4A4A4A]">
                    <span className="font-medium text-[#1E1E1E]">Tuesday</span>
                    <span className="text-right">10:30 AM – 9:00 PM</span>
                  </div>
                  <div className="grid grid-cols-2 px-4 py-2 text-[#4A4A4A]">
                    <span className="font-medium text-[#1E1E1E]">Wednesday</span>
                    <span className="text-right">10:30 AM – 9:00 PM</span>
                  </div>
                  <div className="grid grid-cols-2 px-4 py-2 text-[#4A4A4A]">
                    <span className="font-medium text-[#1E1E1E]">Thursday</span>
                    <span className="text-right">10:30 AM – 9:00 PM</span>
                  </div>
                  <div className="grid grid-cols-2 px-4 py-2 text-[#4A4A4A]">
                    <span className="font-medium text-[#1E1E1E]">Friday</span>
                    <span className="text-right">10:30 AM – 12:30 PM, 4:00 PM – 9:00 PM</span>
                  </div>
                  <div className="grid grid-cols-2 px-4 py-2 text-[#4A4A4A]">
                    <span className="font-medium text-[#1E1E1E]">Saturday</span>
                    <span className="text-right">10:30 AM – 9:00 PM</span>
                  </div>
                  <div className="grid grid-cols-2 px-4 py-2 text-[#4A4A4A] bg-[#FAF8F5]">
                    <span className="font-medium text-[#1E1E1E]">Sunday</span>
                    <span className="text-right font-semibold text-[#9E1B32]">Closed</span>
                  </div>
                </div>
              </div>
            </div>

            {/* Action Buttons */}
            <div className="mt-6 pt-5 border-t border-[#E8E2D9] flex flex-wrap gap-3">
              <a
                href={createGeneralWhatsAppEnquiry()}
                target="_blank"
                rel="noopener noreferrer"
                className="px-5 py-2.5 text-xs font-semibold tracking-wider text-white bg-[#997A48] hover:bg-[#806437] transition-colors rounded-full flex items-center gap-2"
              >
                <MessageSquare className="w-4 h-4" />
                <span>Enquire on WhatsApp</span>
              </a>

              <a
                href={SHOP_CONFIG.directionsUrl}
                target="_blank"
                rel="noopener noreferrer"
                className="px-5 py-2.5 text-xs font-semibold tracking-wider text-[#1E1E1E] bg-[#F4EFE6] hover:bg-[#EAE2D5] transition-colors rounded-full flex items-center gap-1.5"
              >
                <Navigation className="w-3.5 h-3.5 text-[#997A48]" />
                <span>Get Directions</span>
              </a>
            </div>
          </div>

          {/* Right: Small, Compact Exact-Area Street Map (5 cols) */}
          <div className="lg:col-span-5 bg-white rounded-2xl overflow-hidden border border-[#E8E2D9] shadow-xs flex flex-col">
            <div className="px-4 py-3 bg-[#FAF8F5] border-b border-[#E8E2D9] flex items-center justify-between">
              <div>
                <span className="text-xs font-semibold text-[#1E1E1E] block">Location Map</span>
                <span className="text-[11px] text-[#717171]">Arafath Complex, Tenkasi</span>
              </div>
              <a
                href={SHOP_CONFIG.mapSearchUrl}
                target="_blank"
                rel="noopener noreferrer"
                className="text-[11px] text-[#997A48] hover:underline flex items-center gap-1 font-medium"
              >
                <span>Open in Maps</span>
                <ExternalLink className="w-3 h-3" />
              </a>
            </div>

            {/* Small Compact Map (Exact Street Level) */}
            <div className="relative w-full h-[250px] bg-[#EDE8E0]">
              <iframe
                title="RMK Gems Exact Area Map in Tenkasi"
                src={SHOP_CONFIG.embeddedMapUrl}
                width="100%"
                height="100%"
                style={{ border: 0 }}
                allowFullScreen={false}
                loading="lazy"
                referrerPolicy="no-referrer-when-downgrade"
                className="w-full h-full"
              />
            </div>

            <div className="p-3 bg-white text-[11px] text-[#717171] border-t border-[#E8E2D9] flex items-center justify-between">
              <span>Keela Avani Moola Veethi, Tenkasi</span>
              <a
                href={SHOP_CONFIG.directionsUrl}
                target="_blank"
                rel="noopener noreferrer"
                className="text-[#997A48] hover:underline font-medium"
              >
                Get Directions &rarr;
              </a>
            </div>
          </div>

        </div>

      </div>
    </section>
  );
};
