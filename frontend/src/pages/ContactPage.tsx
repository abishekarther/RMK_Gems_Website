import React, { useEffect } from 'react';
import { MapPin, Phone, MessageSquare, Clock, Truck, ExternalLink, Sparkles, Navigation } from 'lucide-react';
import { SHOP_CONFIG, createGeneralWhatsAppEnquiry } from '../config/shop';
import { LeafletMap } from '../components/Map/LeafletMap';

export const ContactPage: React.FC = () => {
  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  return (
    <main className="py-12 sm:py-20 bg-[#FAF8F5] min-h-screen">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Page Header */}
        <div className="text-center max-w-3xl mx-auto mb-14">
          <div className="inline-flex items-center gap-1.5 text-xs font-semibold uppercase tracking-[0.2em] text-[#997A48] mb-3">
            <Sparkles className="w-4 h-4" />
            <span>Customer Assistance</span>
          </div>

          <h1 className="font-serif text-3xl sm:text-5xl font-bold text-[#1E1E1E] tracking-tight">
            Contact & Shop Visit
          </h1>

          <div className="w-20 h-0.5 bg-[#C5A880] mx-auto mt-4 mb-5" />

          <p className="text-sm sm:text-base text-[#717171] leading-relaxed">
            Connect with RMK Gems for tailored gemstone consultations, certified availability, and nationwide delivery.
          </p>
        </div>

        {/* 3 Direct Contact Pillars */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
          
          {/* Pillar 1: WhatsApp */}
          <div className="bg-white rounded-2xl p-6 border border-[#E8E2D9] shadow-xs flex flex-col justify-between">
            <div>
              <div className="w-10 h-10 rounded-xl bg-[#F4EFE6] flex items-center justify-center text-[#997A48] mb-4">
                <MessageSquare className="w-5 h-5" />
              </div>
              <h3 className="font-serif text-lg font-bold text-[#1E1E1E]">WhatsApp Consultation</h3>
              <p className="text-xs text-[#717171] mt-1.5 leading-relaxed">
                Direct one-on-one assistance for gemstone inquiries, real photos, and custom requirements.
              </p>
            </div>
            <div className="mt-6 pt-4 border-t border-[#F4EFE6]">
              <a
                href={createGeneralWhatsAppEnquiry()}
                target="_blank"
                rel="noopener noreferrer"
                className="w-full py-2.5 px-4 text-xs font-semibold tracking-wider text-white bg-[#997A48] hover:bg-[#806437] transition-colors rounded-full flex items-center justify-center gap-2"
              >
                <span>Chat on WhatsApp</span>
              </a>
            </div>
          </div>

          {/* Pillar 2: Phone */}
          <div className="bg-white rounded-2xl p-6 border border-[#E8E2D9] shadow-xs flex flex-col justify-between">
            <div>
              <div className="w-10 h-10 rounded-xl bg-[#F4EFE6] flex items-center justify-center text-[#997A48] mb-4">
                <Phone className="w-5 h-5" />
              </div>
              <h3 className="font-serif text-lg font-bold text-[#1E1E1E]">Direct Phone Call</h3>
              <p className="text-xs text-[#717171] mt-1.5 leading-relaxed">
                Speak directly with our shop team during business hours for immediate guidance.
              </p>
            </div>
            <div className="mt-6 pt-4 border-t border-[#F4EFE6]">
              <a
                href={`tel:${SHOP_CONFIG.phoneTel}`}
                className="w-full py-2.5 px-4 text-xs font-semibold tracking-wider text-[#1E1E1E] bg-[#F4EFE6] hover:bg-[#EAE2D5] transition-colors rounded-full flex items-center justify-center gap-2"
              >
                <span>Call {SHOP_CONFIG.phoneDisplay}</span>
              </a>
            </div>
          </div>

          {/* Pillar 3: Delivery */}
          <div className="bg-white rounded-2xl p-6 border border-[#E8E2D9] shadow-xs flex flex-col justify-between">
            <div>
              <div className="w-10 h-10 rounded-xl bg-[#F4EFE6] flex items-center justify-center text-[#997A48] mb-4">
                <Truck className="w-5 h-5" />
              </div>
              <h3 className="font-serif text-lg font-bold text-[#1E1E1E]">Nationwide Delivery</h3>
              <p className="text-xs text-[#717171] mt-1.5 leading-relaxed">
                {SHOP_CONFIG.deliveryStatement} Secure, insured dispatch to your location.
              </p>
            </div>
            <div className="mt-6 pt-4 border-t border-[#F4EFE6]">
              <span className="w-full py-2.5 px-4 text-xs font-semibold text-[#997A48] bg-[#FAF8F5] rounded-full flex items-center justify-center">
                All-India Insured Transit
              </span>
            </div>
          </div>

        </div>

        {/* Shop Location & Visiting Hours Unified Card */}
        <div className="bg-white rounded-2xl p-6 sm:p-10 border border-[#E8E2D9] shadow-xs">
          
          <div className="mb-8 pb-6 border-b border-[#E8E2D9]">
            <span className="text-xs font-semibold uppercase tracking-widest text-[#997A48]">
              Shop Location
            </span>
            <h2 className="font-serif text-2xl sm:text-3xl font-bold text-[#1E1E1E] mt-1">
              RMK Gems — Tenkasi, Tamil Nadu
            </h2>
            <p className="mt-2 text-sm text-[#4A4A4A] flex items-start gap-2">
              <MapPin className="w-4 h-4 text-[#997A48] shrink-0 mt-0.5" />
              <span>{SHOP_CONFIG.address}</span>
            </p>
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
            
            {/* Left: Schedule Table (6 cols) */}
            <div className="lg:col-span-6 space-y-4">
              <h3 className="text-xs uppercase tracking-wider font-semibold text-[#1E1E1E] flex items-center gap-2">
                <Clock className="w-4 h-4 text-[#997A48]" />
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

              <div className="pt-2 flex gap-3">
                <a
                  href={SHOP_CONFIG.directionsUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="px-4 py-2 text-xs font-semibold bg-[#F4EFE6] hover:bg-[#EAE2D5] text-[#1E1E1E] rounded-full transition-colors flex items-center gap-1.5"
                >
                  <Navigation className="w-3.5 h-3.5 text-[#997A48]" />
                  <span>Get Directions</span>
                </a>

                <a
                  href={SHOP_CONFIG.mapSearchUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="px-4 py-2 text-xs font-semibold bg-[#F4EFE6] hover:bg-[#EAE2D5] text-[#1E1E1E] rounded-full transition-colors flex items-center gap-1.5"
                >
                  <span>Open in Google Maps</span>
                  <ExternalLink className="w-3.5 h-3.5 text-[#997A48]" />
                </a>
              </div>
            </div>

            {/* Right: Embedded Interactive Leaflet.js Map Card (6 cols) */}
            <div className="lg:col-span-6 rounded-2xl overflow-hidden border border-[#E8E2D9] shadow-xs bg-white flex flex-col">
              {/* Top Outer Cover Header */}
              <div className="px-4 py-3 bg-[#FAF8F5] border-b border-[#E8E2D9] flex items-center justify-between">
                <div>
                  <span className="text-xs font-semibold text-[#1E1E1E] block">Location Map</span>
                  <span className="text-[11px] text-[#717171]">Arafath Complex, Keela Avani Moola Veethi</span>
                </div>
                <a
                  href={SHOP_CONFIG.mapSearchUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-[11px] text-[#997A48] hover:underline flex items-center gap-1 font-medium"
                >
                  <span>Open in Google Maps</span>
                  <ExternalLink className="w-3 h-3" />
                </a>
              </div>

              {/* Leaflet.js Interactive Map Viewport */}
              <div className="relative w-full h-[320px] sm:h-[350px] bg-[#EDE8E0] z-0">
                <LeafletMap />
              </div>

              {/* Bottom Outer Cover Footer */}
              <div className="px-4 py-3 bg-[#FAF8F5] text-xs text-[#717171] border-t border-[#E8E2D9] flex items-center justify-between">
                <span>Near Theppakulam, Tenkasi – 627811</span>
                <a
                  href={SHOP_CONFIG.directionsUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-[#997A48] hover:underline font-medium flex items-center gap-1"
                >
                  <span>Get Directions</span>
                  <span>&rarr;</span>
                </a>
              </div>
            </div>

          </div>

        </div>

      </div>
    </main>
  );
};
