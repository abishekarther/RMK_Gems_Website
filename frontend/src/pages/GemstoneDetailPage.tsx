import React, { useEffect, useState } from 'react';
import { useParams, Link, useNavigate } from 'react-router-dom';
import { MessageSquare, ArrowLeft, Shield, Truck } from 'lucide-react';
import type { GemstoneDetail } from '../types/gemstone';
import { fetchGemstoneBySlug } from '../services/api';
import { getGemstonePhoto, getGemstoneAltText, isRepresentativePhoto } from '../data/gemstonePhotos';
import { createWhatsAppEnquiry, SHOP_CONFIG } from '../config/shop';
import { FALLBACK_GEMSTONES } from '../data/gemstoneFallbackData';

const formatMaterialType = (type?: string): string => {
  if (!type) return 'Gemstone';
  const t = type.toLowerCase();
  if (t === 'organic') return 'Organic gemstone';
  if (t === 'treated') return 'Treated gemstone';
  if (t === 'imitation') return 'Imitation';
  return 'Gemstone';
};

export const GemstoneDetailPage: React.FC = () => {
  const { slug } = useParams<{ slug: string }>();
  const navigate = useNavigate();
  const initialStone = slug ? (FALLBACK_GEMSTONES.find((g) => g.slug === slug) || null) : null;
  const [gemstone, setGemstone] = useState<GemstoneDetail | null>(initialStone);

  useEffect(() => {
    window.scrollTo(0, 0);
    if (!slug) return;

    fetchGemstoneBySlug(slug)
      .then((data) => {
        setGemstone(data);
      });
  }, [slug]);

  if (!gemstone) {
    return (
      <main className="py-24 bg-[#FAF8F5] min-h-screen flex items-center justify-center">
        <div className="text-center max-w-md mx-auto p-8 bg-white rounded-2xl border border-[#E8E2D9] shadow-xs">
          <h2 className="font-serif text-2xl font-bold text-[#1E1E1E] mb-3">Gemstone Not Found</h2>
          <p className="text-sm text-[#717171] mb-6">
            The requested gemstone is not available.
          </p>
          <Link
            to="/precious-gemstones"
            className="px-5 py-2.5 text-xs font-semibold tracking-wider text-white bg-[#997A48] hover:bg-[#806437] transition-colors rounded-full"
          >
            Browse Collections
          </Link>
        </div>
      </main>
    );
  }

  const categoryPath = gemstone.category_slug === 'semi-precious'
    ? '/semi-precious-gemstones'
    : '/precious-gemstones';

  const categoryLabel = gemstone.category_name || (gemstone.category_slug === 'semi-precious' ? 'Semi-Precious Gemstones' : 'Precious Gemstones');
  const photoUrl = getGemstonePhoto(gemstone.slug);

  return (
    <main className="py-10 sm:py-16 bg-[#FAF8F5] min-h-screen">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Breadcrumb Navigation */}
        <nav className="flex items-center space-x-2 text-xs text-[#717171] mb-8" aria-label="Breadcrumb">
          <Link to="/" className="hover:text-[#1E1E1E] transition-colors">Home</Link>
          <span>/</span>
          <Link to={categoryPath} className="hover:text-[#1E1E1E] transition-colors">{categoryLabel}</Link>
          <span>/</span>
          <span className="text-[#997A48] font-medium">{gemstone.name}</span>
        </nav>

        {/* Back Link */}
        <div className="mb-6">
          <button
            type="button"
            onClick={() => navigate(-1)}
            className="inline-flex items-center gap-1.5 text-xs font-medium text-[#717171] hover:text-[#1E1E1E] transition-colors focus:outline-none"
          >
            <ArrowLeft className="w-3.5 h-3.5" />
            <span>Back</span>
          </button>
        </div>

        {/* Gemstone Presentation Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">
          
          {/* Left Column (5 cols): Original Gemstone Photo (sticky only on desktop) */}
          <div className="lg:col-span-5 relative lg:sticky lg:top-28 space-y-4">
            <div className="w-full aspect-square overflow-hidden rounded-2xl bg-white border border-[#E8E2D9] shadow-sm flex items-center justify-center p-8">
              <img
                src={photoUrl}
                alt={getGemstoneAltText(gemstone.name, gemstone.colour)}
                className="w-full h-full object-contain object-center drop-shadow-xl"
              />
            </div>
            {isRepresentativePhoto(gemstone.slug) && (
              <p className="text-xs text-[#717171] italic text-center mt-2">
                Representative image. Actual stones vary in colour and cut.
              </p>
            )}

            {/* Delivery Note */}
            <div className="p-4 rounded-xl bg-white border border-[#E8E2D9] shadow-2xs space-y-2.5">
              <div className="flex items-center gap-2.5 text-xs text-[#1E1E1E] font-medium">
                <Truck className="w-4 h-4 text-[#997A48] shrink-0" />
                <span>{SHOP_CONFIG.deliveryStatement}</span>
              </div>
              <div className="flex items-center gap-2.5 text-xs text-[#717171]">
                <Shield className="w-4 h-4 text-[#997A48] shrink-0" />
                <span>Carefully curated gemstone sourcing by RMK Gems, Tenkasi.</span>
              </div>
            </div>
          </div>

          {/* Right Column (7 cols): Clean Name & Details & Single Direct WhatsApp Button */}
          <div className="lg:col-span-7 space-y-8">
            
            {/* Title Header */}
            <div>
              <span className="text-xs font-semibold uppercase tracking-widest text-[#997A48]">
                {categoryLabel}
              </span>
              <h1 className="font-serif text-3xl sm:text-4xl lg:text-5xl font-bold text-[#1E1E1E] mt-1 tracking-tight">
                {gemstone.name}
              </h1>

              {gemstone.short_description && (
                <p className="mt-3 text-base text-[#4A4A4A] leading-relaxed">
                  {gemstone.short_description}
                </p>
              )}
            </div>

            {/* Clean, Simple Single WhatsApp Enquiry Button */}
            <div>
              <a
                href={createWhatsAppEnquiry(gemstone.name)}
                target="_blank"
                rel="noopener noreferrer"
                className="w-full py-4 px-6 rounded-xl bg-[#997A48] hover:bg-[#806437] text-white font-semibold text-sm tracking-wide transition-all shadow-md hover:shadow-lg flex items-center justify-center gap-2.5 focus:outline-none focus:ring-2 focus:ring-[#997A48] focus:ring-offset-2"
              >
                <MessageSquare className="w-5 h-5" />
                <span>Enquire for {gemstone.name} on WhatsApp</span>
              </a>
            </div>

            {/* Factual Gemological Properties Grid */}
            <div className="bg-white rounded-2xl p-6 sm:p-8 border border-[#E8E2D9] shadow-2xs space-y-6">
              <h2 className="font-serif text-xl font-bold text-[#1E1E1E] border-b border-[#E8E2D9] pb-3">
                Gemological Specifications
              </h2>

              <dl className="grid grid-cols-1 sm:grid-cols-2 gap-x-6 gap-y-4 text-xs sm:text-sm">
                {/* Hardness */}
                <div className="border-b border-[#F4EFE6] pb-2">
                  <dt className="text-[#717171] uppercase tracking-wider text-[11px] font-medium">Mohs Hardness</dt>
                  <dd className="font-semibold text-[#1E1E1E] mt-0.5">
                    {gemstone.hardness_min !== undefined && gemstone.hardness_max !== undefined
                      ? gemstone.hardness_min === gemstone.hardness_max
                        ? `${gemstone.hardness_min}`
                        : `${gemstone.hardness_min} – ${gemstone.hardness_max}`
                      : 'Not specified'}
                  </dd>
                </div>

                {/* Colour */}
                {gemstone.colour && (
                  <div className="border-b border-[#F4EFE6] pb-2">
                    <dt className="text-[#717171] uppercase tracking-wider text-[11px] font-medium">Colour</dt>
                    <dd className="font-semibold text-[#1E1E1E] mt-0.5">{gemstone.colour}</dd>
                  </div>
                )}

                {/* Chemical Composition */}
                {gemstone.chemical_composition && (
                  <div className="border-b border-[#F4EFE6] pb-2">
                    <dt className="text-[#717171] uppercase tracking-wider text-[11px] font-medium">Chemical Formula</dt>
                    <dd className="font-semibold text-[#1E1E1E] mt-0.5 font-mono text-xs">{gemstone.chemical_composition}</dd>
                  </div>
                )}

                {/* Crystal System */}
                {gemstone.crystal_system && (
                  <div className="border-b border-[#F4EFE6] pb-2">
                    <dt className="text-[#717171] uppercase tracking-wider text-[11px] font-medium">Crystal System</dt>
                    <dd className="font-semibold text-[#1E1E1E] mt-0.5">{gemstone.crystal_system}</dd>
                  </div>
                )}

                {/* Material Type */}
                {gemstone.material_type && (
                  <div className="border-b border-[#F4EFE6] pb-2">
                    <dt className="text-[#717171] uppercase tracking-wider text-[11px] font-medium">Mineral Classification</dt>
                    <dd className="font-semibold text-[#1E1E1E] mt-0.5">{formatMaterialType(gemstone.material_type)}</dd>
                  </div>
                )}

                {/* Typical Treatments */}
                {gemstone.treatments && (
                  <div className="border-b border-[#F4EFE6] pb-2">
                    <dt className="text-[#717171] uppercase tracking-wider text-[11px] font-medium">Standard Treatments</dt>
                    <dd className="text-[#4A4A4A] mt-0.5">{gemstone.treatments}</dd>
                  </div>
                )}
              </dl>

              {/* Full Description / Overview */}
              {gemstone.full_description && (
                <div className="pt-2">
                  <h3 className="text-xs uppercase tracking-wider font-semibold text-[#717171] mb-2">Overview</h3>
                  <p className="text-sm text-[#4A4A4A] leading-relaxed">
                    {gemstone.full_description}
                  </p>
                </div>
              )}

              {/* Origin */}
              {gemstone.origin && (
                <div className="pt-2 border-t border-[#F4EFE6]">
                  <h3 className="text-xs uppercase tracking-wider font-semibold text-[#717171] mb-2">Primary Sources</h3>
                  <p className="text-sm text-[#4A4A4A] leading-relaxed">
                    {gemstone.origin}
                  </p>
                </div>
              )}

              {/* History */}
              {gemstone.history_notes && (
                <div className="pt-2 border-t border-[#F4EFE6]">
                  <h3 className="text-xs uppercase tracking-wider font-semibold text-[#717171] mb-2">History & Significance</h3>
                  <p className="text-sm text-[#4A4A4A] leading-relaxed">
                    {gemstone.history_notes}
                  </p>
                </div>
              )}

              {/* Care Instructions */}
              {gemstone.care_instructions && (
                <div className="pt-4 border-t border-[#E8E2D9] bg-[#FAF8F5] -mx-6 sm:-mx-8 -mb-6 sm:-mb-8 p-6 rounded-b-2xl">
                  <h3 className="text-xs uppercase tracking-wider font-semibold text-[#1E1E1E] mb-1.5 flex items-center gap-1.5">
                    <Shield className="w-3.5 h-3.5 text-[#997A48]" />
                    <span>Care & Maintenance</span>
                  </h3>
                  <p className="text-xs text-[#717171] leading-relaxed">
                    {gemstone.care_instructions}
                  </p>
                </div>
              )}
            </div>

          </div>

        </div>

      </div>
    </main>
  );
};
