import React from 'react';
import { MapPin, Phone, MessageSquare, Clock, Truck, ExternalLink } from 'lucide-react';
import { SHOP_CONFIG, createGeneralWhatsAppEnquiry } from '../../config/shop';

export const LocationSection: React.FC = () => {
  return (
    <section className="py-20 bg-[#FAF8F5]">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Confirmed Brand Statement (Section 1 & 3) */}
        <div className="max-w-3xl mx-auto text-center mb-16 p-8 sm:p-12 rounded-2xl bg-[#F4EFE6]/70 border border-[#E8E2D9]">
          <span className="text-xs font-semibold uppercase tracking-[0.25em] text-[#997A48] mb-3 block">
            About RMK Gems
          </span>
          <p className="font-serif text-xl sm:text-2xl text-[#1E1E1E] leading-relaxed italic">
            "{SHOP_CONFIG.aboutDescription}"
          </p>

          <div className="mt-6 inline-flex items-center gap-2 text-xs font-medium text-[#4A4A4A] bg-white px-4 py-2 rounded-full border border-[#E8E2D9] shadow-2xs">
            <Truck className="w-4 h-4 text-[#997A48]" />
            <span>{SHOP_CONFIG.deliveryStatement}</span>
          </div>
        </div>

        {/* Location & Map Preview Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-10 items-stretch">
          
          {/* Left: Contact Info & Opening Hours Card */}
          <div className="bg-white rounded-2xl p-8 sm:p-10 border border-[#E8E2D9] shadow-xs flex flex-col justify-between">
            <div>
              <span className="text-xs font-semibold uppercase tracking-widest text-[#997A48]">
                Visit Our Shop
              </span>
              <h3 className="font-serif text-2xl sm:text-3xl font-bold text-[#1E1E1E] mt-1 mb-6">
                Tenkasi, Tamil Nadu
              </h3>

              <div className="space-y-4 text-sm text-[#4A4A4A]">
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

              {/* Hours snippet */}
              <div className="mt-8 pt-6 border-t border-[#E8E2D9]">
                <h4 className="text-xs uppercase tracking-wider font-semibold text-[#1E1E1E] mb-3 flex items-center gap-2">
                  <Clock className="w-4 h-4 text-[#997A48]" />
                  <span>Visiting Hours</span>
                </h4>
                <div className="text-xs space-y-2 text-[#717171]">
                  <p className="flex justify-between">
                    <span>Monday, Wednesday – Saturday:</span>
                    <span className="font-medium text-[#1E1E1E]">10:30 AM – 9:00 PM</span>
                  </p>
                  <p className="flex justify-between">
                    <span>Friday:</span>
                    <span className="font-medium text-[#1E1E1E]">10:30 AM – 12:30 PM & 4:00 PM – 9:00 PM</span>
                  </p>
                  <p className="flex justify-between">
                    <span>Tuesday:</span>
                    <span className="text-[#997A48] italic">Contact shop to confirm</span>
                  </p>
                  <p className="flex justify-between">
                    <span>Sunday:</span>
                    <span className="font-medium text-[#1E1E1E]">Closed</span>
                  </p>
                </div>
              </div>
            </div>

            <div className="mt-8 pt-6 border-t border-[#E8E2D9] flex flex-wrap gap-4">
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
                <span>Get Directions</span>
                <ExternalLink className="w-3.5 h-3.5 text-[#997A48]" />
              </a>
            </div>
          </div>

          {/* Right: Interactive Embedded Map with Lazy Loading */}
          <div className="bg-white rounded-2xl overflow-hidden border border-[#E8E2D9] shadow-xs flex flex-col min-h-[350px]">
            <iframe
              title="RMK Gems Shop Location in Tenkasi"
              src={SHOP_CONFIG.embeddedMapUrl}
              width="100%"
              height="100%"
              style={{ border: 0, minHeight: '380px' }}
              allowFullScreen={false}
              loading="lazy"
              referrerPolicy="no-referrer-when-downgrade"
              className="flex-1 w-full h-full"
            />
            <div className="p-3 bg-[#FAF8F5] border-t border-[#E8E2D9] flex items-center justify-between text-xs text-[#717171]">
              <span>Near Theppakulam, Tenkasi</span>
              <a
                href={SHOP_CONFIG.mapSearchUrl}
                target="_blank"
                rel="noopener noreferrer"
                className="text-[#997A48] hover:underline flex items-center gap-1"
              >
                <span>Open in Google Maps</span>
                <ExternalLink className="w-3 h-3" />
              </a>
            </div>
          </div>

        </div>

      </div>
    </section>
  );
};
