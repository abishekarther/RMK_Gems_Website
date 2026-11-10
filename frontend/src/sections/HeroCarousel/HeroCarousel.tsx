import React, { useState, useEffect, useRef, useCallback } from 'react';
import { Link } from 'react-router-dom';
import { ChevronLeft, ChevronRight, Pause, Play, Sparkles } from 'lucide-react';
import type { HomepageSlide } from '../../types/gemstone';
import { fetchHomepageSlides } from '../../services/api';

export const HeroCarousel: React.FC = () => {
  const [slides, setSlides] = useState<HomepageSlide[]>([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isPaused, setIsPaused] = useState(false);
  const [userInteracted, setUserInteracted] = useState(false);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);

  // Check prefers-reduced-motion
  const prefersReducedMotion = typeof window !== 'undefined'
    ? window.matchMedia('(prefers-reduced-motion: reduce)').matches
    : false;

  useEffect(() => {
    fetchHomepageSlides().then((data) => {
      if (data && data.length > 0) {
        setSlides(data);
      }
    });
  }, []);

  const total = slides.length;

  const goToNext = useCallback(() => {
    setCurrentIndex((prev) => (total > 0 ? (prev + 1) % total : 0));
  }, [total]);

  const goToPrev = useCallback(() => {
    setCurrentIndex((prev) => (total > 0 ? (prev - 1 + total) % total : 0));
  }, [total]);

  // Autoplay management
  useEffect(() => {
    if (prefersReducedMotion || isPaused || total <= 1) {
      if (timerRef.current) clearInterval(timerRef.current);
      return;
    }

    timerRef.current = setInterval(() => {
      goToNext();
    }, 6000);

    return () => {
      if (timerRef.current) clearInterval(timerRef.current);
    };
  }, [prefersReducedMotion, isPaused, total, goToNext]);

  if (total === 0) {
    return (
      <div className="h-[520px] bg-[#F5EFEB] flex items-center justify-center animate-pulse">
        <p className="font-serif text-lg text-[#997A48]">Loading Gemstone Heritage...</p>
      </div>
    );
  }

  const currentSlide = slides[currentIndex];

  return (
    <section
      className="relative w-full h-[520px] sm:h-[600px] lg:h-[650px] overflow-hidden bg-[#1A1A1A] text-white"
      aria-roledescription="carousel"
      aria-label="Gemstone Historical Significance Showcase"
      onMouseEnter={() => setIsPaused(true)}
      onMouseLeave={() => !userInteracted && setIsPaused(false)}
      onFocus={() => setIsPaused(true)}
      onBlur={() => !userInteracted && setIsPaused(false)}
    >
      {/* Slide Images */}
      {slides.map((slide, idx) => (
        <div
          key={slide.id || idx}
          className={`absolute inset-0 transition-opacity duration-1000 ease-in-out ${
            idx === currentIndex ? 'opacity-100 z-10 pointer-events-auto' : 'opacity-0 z-0 pointer-events-none'
          }`}
          aria-hidden={idx !== currentIndex}
        >
          <img
            src={slide.image_url}
            alt={slide.image_alt_text}
            className="w-full h-full object-cover object-center filter brightness-[0.72]"
            loading={idx === 0 ? 'eager' : 'lazy'}
          />

          {/* Deep luxury radial & linear gradients for maximum legibility */}
          <div className="absolute inset-0 bg-gradient-to-r from-black/85 via-black/60 to-black/30" />
          <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-black/30" />
        </div>
      ))}

      {/* Slide Content Box */}
      <div className="relative z-20 max-w-7xl mx-auto h-full px-4 sm:px-6 lg:px-8 flex items-center">
        <div
          className="max-w-2xl bg-black/40 backdrop-blur-md p-6 sm:p-10 rounded-2xl border border-white/15 shadow-2xl"
          aria-live={isPaused ? "polite" : "off"}
        >
          {/* Historical Tagline */}
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#997A48]/30 border border-[#C5A880]/40 text-[#E5D7C2] text-xs font-medium tracking-widest uppercase mb-4">
            <Sparkles className="w-3.5 h-3.5 text-[#C5A880]" />
            <span>Gemstone History & Heritage</span>
          </div>

          <h2 className="font-serif text-3xl sm:text-4xl lg:text-5xl font-bold text-white tracking-tight leading-tight">
            {currentSlide.title}
          </h2>

          <p className="mt-4 text-sm sm:text-base text-[#D1C7BA] leading-relaxed font-sans">
            {currentSlide.subtitle}
          </p>

          {/* CTA Link */}
          <div className="mt-8 flex items-center gap-4">
            <Link
              to={currentSlide.button_link}
              className="px-6 py-3 text-xs sm:text-sm font-semibold tracking-wider text-white bg-[#997A48] hover:bg-[#806437] transition-all rounded-full shadow-lg hover:shadow-xl focus:outline-none focus-visible:ring-2 focus-visible:ring-white"
            >
              {currentSlide.button_text} &rarr;
            </Link>

            <Link
              to="/precious-gemstones"
              className="text-xs sm:text-sm font-medium text-[#E5D7C2] hover:text-white underline underline-offset-4 decoration-[#997A48] transition-colors"
            >
              View Catalogue
            </Link>
          </div>
        </div>
      </div>

      {/* Prev / Next Controls */}
      <div className="absolute z-20 bottom-8 right-4 sm:right-10 flex items-center gap-3">
        {/* Pause / Play Toggle */}
        <button
          type="button"
          onClick={() => {
            setUserInteracted(true);
            setIsPaused(!isPaused);
          }}
          className="p-2.5 rounded-full bg-black/50 hover:bg-black/75 border border-white/20 text-white transition-colors focus:outline-none focus-visible:ring-2 focus-visible:ring-[#997A48]"
          aria-label={isPaused ? "Play carousel autoplay" : "Pause carousel autoplay"}
        >
          {isPaused ? <Play className="w-4 h-4" /> : <Pause className="w-4 h-4" />}
        </button>

        {/* Prev Slide */}
        <button
          type="button"
          onClick={() => {
            setUserInteracted(true);
            goToPrev();
          }}
          className="p-2.5 rounded-full bg-black/50 hover:bg-black/75 border border-white/20 text-white transition-colors focus:outline-none focus-visible:ring-2 focus-visible:ring-[#997A48]"
          aria-label="Previous gemstone history slide"
        >
          <ChevronLeft className="w-5 h-5" />
        </button>

        {/* Next Slide */}
        <button
          type="button"
          onClick={() => {
            setUserInteracted(true);
            goToNext();
          }}
          className="p-2.5 rounded-full bg-black/50 hover:bg-black/75 border border-white/20 text-white transition-colors focus:outline-none focus-visible:ring-2 focus-visible:ring-[#997A48]"
          aria-label="Next gemstone history slide"
        >
          <ChevronRight className="w-5 h-5" />
        </button>
      </div>

      {/* Slide Indicators */}
      <div
        className="absolute z-20 bottom-8 left-4 sm:left-10 flex items-center gap-2"
        role="tablist"
        aria-label="Slides"
      >
        {slides.map((_, idx) => (
          <button
            key={idx}
            type="button"
            role="tab"
            aria-selected={idx === currentIndex}
            aria-label={`Go to slide ${idx + 1}`}
            onClick={() => {
              setUserInteracted(true);
              setCurrentIndex(idx);
            }}
            className={`h-2 rounded-full transition-all duration-300 focus:outline-none focus-visible:ring-2 focus-visible:ring-white ${
              idx === currentIndex ? 'w-8 bg-[#C5A880]' : 'w-2 bg-white/40 hover:bg-white/70'
            }`}
          />
        ))}
      </div>
    </section>
  );
};
