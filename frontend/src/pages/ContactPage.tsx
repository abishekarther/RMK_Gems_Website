import React, { useEffect } from 'react';
import { MapPin, Phone, MessageSquare, Clock, Truck, ExternalLink, Sparkles, Navigation } from 'lucide-react';
import { SHOP_CONFIG, createGeneralWhatsAppEnquiry } from '../config/shop';

export const ContactPage: React.FC = () => {
  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  return (
    <main className="py-12 sm:py-20 bg-[#FAF8F5] min-h-screen">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Header */}
        <div className="text-center max-w-3xl mx-auto mb-16">
          <div className="inline-flex items-center gap-1.5 text-xs font-semibold uppercase tracking-[0.2em] text-[#997A48] mb-3">
            <Sparkles className="w-4 h-4" />
            <span>Connect With Us</span>
          </div>

          <h1 className="font-serif text-3xl sm:text-5xl font-bold text-[#1E1E1E] tracking-tight">
            Contact & Location
          </h1>

          <div className="w-20 h-0.5 bg-[#C5A880] mx-auto mt-4 mb-5" />

          <p className="text-sm sm:text-base text-[#717171] leading-relaxed">
            Visit our shop in Tenkasi or get in touch directly via WhatsApp for tailored consultations, certified gemstone inquiries, and nationwide delivery.
          </p>
        </div>

        {/* Content Layout */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-10">
          
          {/* Left Column (5 cols): Business Details, Hours & Enquiry */}
          <div className="lg:col-span-5 space-y-8">
            
            {/* Address & Direct Phone Card */}
            <div className="bg-white rounded-2xl p-6 sm:p-8 border border-[#E8E2D9] shadow-xs space-y-6">
              <h2 className="font-serif text-xl sm:text-2xl font-bold text-[#1E1E1E]">
                RMK Gems
              </h2>

              <div className="space-y-4 text-sm text-[#4A4A4A]">
                <div className="flex items-start gap-3">
                  <MapPin className="w-5 h-5 text-[#997A48] shrink-0 mt-0.5" />
                  <div>
                    <span className="font-semibold text-[#1E1E1E] block">Shop Address</span>
                    <p className="mt-0.5 leading-relaxed">{SHOP_CONFIG.address}</p>
                  </div>
                </div>

                <div className="flex items-start gap-3">
                  <Phone className="w-5 h-5 text-[#997A48] shrink-0 mt-0.5" />
                  <div>
                    <span className="font-semibold text-[#1E1E1E] block">Phone Number</span>
                    <a
                      href={`tel:${SHOP_CONFIG.phoneTel}`}
                      className="mt-0.5 inline-block text-[#997A48] hover:underline font-semibold"
                    >
                      {SHOP_CONFIG.phoneDisplay}
                    </a>
                  </div>
                </div>
              </div>

              {/* Action Buttons */}
              <div className="pt-4 border-t border-[#E8E2D9] flex flex-col gap-3">
                <a
                  href={createGeneralWhatsAppEnquiry()}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="w-full py-3 px-5 text-xs font-semibold tracking-wider text-white bg-[#997A48] hover:bg-[#806437] transition-colors rounded-full flex items-center justify-center gap-2 shadow-xs"
                >
                  <MessageSquare className="w-4 h-4" />
                  <span>Enquire on WhatsApp</span>
                </a>

                <div className="flex gap-3">
                  <a
                    href={SHOP_CONFIG.directionsUrl}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="flex-1 text-center py-2.5 px-4 text-xs font-semibold bg-[#F4EFE6] hover:bg-[#EAE2D5] text-[#1E1E1E] rounded-full transition-colors flex items-center justify-center gap-1.5"
                  >
                    <Navigation className="w-3.5 h-3.5 text-[#997A48]" />
                    <span>Get Directions</span>
                  </a>

                  <a
                    href={SHOP_CONFIG.mapSearchUrl}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="flex-1 text-center py-2.5 px-4 text-xs font-semibold bg-[#F4EFE6] hover:bg-[#EAE2D5] text-[#1E1E1E] rounded-full transition-colors flex items-center justify-center gap-1.5"
                  >
                    <span>View Map</span>
                    <ExternalLink className="w-3.5 h-3.5 text-[#997A48]" />
                  </a>
                </div>
              </div>

              {/* All-India Delivery Statement */}
              <div className="p-4 rounded-xl bg-[#FAF8F5] border border-[#E8E2D9] flex items-center gap-3">
                <Truck className="w-5 h-5 text-[#997A48] shrink-0" />
                <span className="text-xs text-[#4A4A4A] font-medium leading-relaxed">
                  {SHOP_CONFIG.deliveryStatement}
                </span>
              </div>
            </div>

            {/* Opening Hours Table Card */}
            <div className="bg-white rounded-2xl p-6 sm:p-8 border border-[#E8E2D9] shadow-xs">
              <h3 className="font-serif text-lg font-bold text-[#1E1E1E] flex items-center gap-2 mb-4 border-b border-[#E8E2D9] pb-3">
                <Clock className="w-5 h-5 text-[#997A48]" />
                <span>Visiting Hours</span>
              </h3>

              <div className="overflow-hidden rounded-xl border border-[#E8E2D9] text-xs">
                <div className="grid grid-cols-2 bg-[#F4EFE6] px-4 py-2.5 font-semibold text-[#1E1E1E] border-b border-[#E8E2D9]">
                  <span>Day</span>
                  <span className="text-right">Timings</span>
                </div>
                <div className="divide-y divide-[#F4EFE6] bg-white">
                  <div className="grid grid-cols-2 px-4 py-2.5 text-[#4A4A4A]">
                    <span className="font-medium text-[#1E1E1E]">Monday</span>
                    <span className="text-right">10:30 AM – 9:00 PM</span>
                  </div>
                  <div className="grid grid-cols-2 px-4 py-2.5 text-[#4A4A4A]">
                    <span className="font-medium text-[#1E1E1E]">Tuesday</span>
                    <span className="text-right">10:30 AM – 9:00 PM</span>
                  </div>
                  <div className="grid grid-cols-2 px-4 py-2.5 text-[#4A4A4A]">
                    <span className="font-medium text-[#1E1E1E]">Wednesday</span>
                    <span className="text-right">10:30 AM – 9:00 PM</span>
                  </div>
                  <div className="grid grid-cols-2 px-4 py-2.5 text-[#4A4A4A]">
                    <span className="font-medium text-[#1E1E1E]">Thursday</span>
                    <span className="text-right">10:30 AM – 9:00 PM</span>
                  </div>
                  <div className="grid grid-cols-2 px-4 py-2.5 text-[#4A4A4A]">
                    <span className="font-medium text-[#1E1E1E]">Friday</span>
                    <span className="text-right">10:30 AM – 12:30 PM, 4:00 PM – 9:00 PM</span>
                  </div>
                  <div className="grid grid-cols-2 px-4 py-2.5 text-[#4A4A4A]">
                    <span className="font-medium text-[#1E1E1E]">Saturday</span>
                    <span className="text-right">10:30 AM – 9:00 PM</span>
                  </div>
                  <div className="grid grid-cols-2 px-4 py-2.5 text-[#4A4A4A] bg-[#FAF8F5]">
                    <span className="font-medium text-[#1E1E1E]">Sunday</span>
                    <span className="text-right font-semibold text-[#9E1B32]">Closed</span>
                  </div>
                </div>
              </div>
            </div>

          </div>

          {/* Right Column (7 cols): Interactive Embedded Map */}
          <div className="lg:col-span-7 flex flex-col">
            <div className="bg-white rounded-2xl overflow-hidden border border-[#E8E2D9] shadow-sm flex flex-col">
              
              <div className="p-4 bg-[#FAF8F5] border-b border-[#E8E2D9] flex items-center justify-between">
                <div>
                  <h3 className="font-serif text-base font-semibold text-[#1E1E1E]">
                    Location Map
                  </h3>
                  <p className="text-xs text-[#717171]">
                    No. 12, Arafath Complex, Keela Avani Moola Veethi, Tenkasi
                  </p>
                </div>

                <a
                  href={SHOP_CONFIG.mapSearchUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="px-3 py-1.5 text-xs font-medium text-[#997A48] bg-white rounded-lg border border-[#E8E2D9] hover:bg-[#F4EFE6] transition-colors flex items-center gap-1"
                >
                  <span>Open in Google Maps</span>
                  <ExternalLink className="w-3.5 h-3.5" />
                </a>
              </div>

              {/* Embedded Google Map iframe with street-level zoom */}
              <div className="w-full h-[320px] bg-[#EDE8E0]">
                <iframe
                  title="RMK Gems Shop Location Map"
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
            </div>
          </div>

        </div>

      </div>
    </main>
  );
};
