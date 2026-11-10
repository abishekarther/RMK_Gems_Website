import React from 'react';
import { Link } from 'react-router-dom';
import { Gem, ArrowLeft } from 'lucide-react';

export const NotFoundPage: React.FC = () => {
  return (
    <main className="py-24 sm:py-32 bg-[#FAF8F5] min-h-[70vh] flex items-center justify-center">
      <div className="max-w-md mx-auto text-center px-4">
        <div className="w-16 h-16 rounded-2xl bg-[#F4EFE6] border border-[#E8E2D9] flex items-center justify-center text-[#997A48] mx-auto mb-6">
          <Gem className="w-8 h-8" />
        </div>

        <span className="text-xs font-semibold uppercase tracking-widest text-[#997A48]">
          Error 404
        </span>

        <h1 className="font-serif text-3xl sm:text-4xl font-bold text-[#1E1E1E] mt-2 mb-3">
          Page Not Found
        </h1>

        <p className="text-sm text-[#717171] leading-relaxed mb-8">
          The gemstone or page you are seeking does not exist or may have been relocated.
        </p>

        <Link
          to="/"
          className="inline-flex items-center gap-2 px-6 py-3 text-xs sm:text-sm font-semibold tracking-wider text-white bg-[#997A48] hover:bg-[#806437] transition-colors rounded-full shadow-md"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>Return to RMK Gems Home</span>
        </Link>
      </div>
    </main>
  );
};

