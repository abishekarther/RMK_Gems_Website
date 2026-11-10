import React from 'react';
import { Link } from 'react-router-dom';
import type { GemstoneItem } from '../../types/gemstone';
import { getGemstonePhoto } from '../../data/gemstonePhotos';

interface GemstoneCardProps {
  gemstone: GemstoneItem;
}

export const GemstoneCard: React.FC<GemstoneCardProps> = ({ gemstone }) => {
  const photoUrl = getGemstonePhoto(gemstone.slug);

  return (
    <Link
      to={`/gemstones/${gemstone.slug}`}
      className="group block text-center focus:outline-none focus-visible:ring-2 focus-visible:ring-[#997A48] rounded-2xl p-3 transition-all duration-300 hover:-translate-y-1"
      aria-label={`View ${gemstone.name}`}
    >
      {/* Gemstone Original GIA Photo */}
      <div className="relative w-full aspect-square overflow-hidden rounded-2xl bg-white border border-[#EBE5DA] shadow-xs group-hover:shadow-md transition-all duration-300 flex items-center justify-center p-4">
        <img
          src={photoUrl}
          alt={gemstone.name}
          className="w-full h-full object-contain object-center group-hover:scale-108 transition-transform duration-500 drop-shadow-md"
          loading="lazy"
        />
        <div className="absolute inset-0 bg-black/0 group-hover:bg-black/2 transition-colors duration-300 pointer-events-none" />
      </div>

      {/* ONLY Gemstone Name */}
      <div className="mt-3">
        <h3 className="font-serif text-base sm:text-lg font-medium text-[#1E1E1E] tracking-wide group-hover:text-[#997A48] transition-colors">
          {gemstone.name}
        </h3>
      </div>
    </Link>
  );
};
