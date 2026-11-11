import React, { useState, useEffect, useRef, useCallback } from 'react';
import { Link } from 'react-router-dom';
import { ChevronLeft, ChevronRight, Pause, Play } from 'lucide-react';
import type { HomepageSlide } from '../../types/gemstone';
import { fetchHomepageSlides } from '../../services/api';

export const HeroCarousel: React.FC = () => {
  const [slides, setSlides] = useState<HomepageSlide[]>([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isPaused, setIsPaused] = useState(false);
  const [userInteracted, setUserInteracted] = useState(false);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);

  // Touch swipe support for mobile
  const touchStartX = useRef<number | null>(null);
  const touchEndX = useRef<number | null>(null);

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

  // Touch handlers for mobile swipe
  const handleTouchStart = (e: React.TouchEvent) => {
    touchStartX.current = e.targetTouches[0].clientX;
  };

  const handleTouchMove = (e: React.TouchEvent) => {
    touchEndX.current = e.targetTouches[0].clientX;
  };

  const handleTouchEnd = () => {
    if (!touchStartX.current || !touchEndX.current) return;
    const distance = touchStartX.current - touchEndX.current;
    const minSwipeDistance = 45;
    if (distance > minSwipeDistance) {
      setUserInteracted(true);
      goToNext();
    } else if (distance < -minSwipeDistance) {
      setUserInteracted(true);
      goToPrev();
    }
    touchStartX.current = null;
    touchEndX.current = null;
  };

  // Autoplay management
  useEffect(() => {
    if (prefersReducedMotion || isPaused || total <= 1) {
      if (timerRef.current) clearInterval(timerRef.current);
      return;
    }

    timerRef.current = setInterval(() => {
      goToNext();
    }, 5500);

    return () => {
      if (timerRef.current) clearInterval(timerRef.current);
    };
  }, [prefersReducedMotion, isPaused, total, goToNext]);

  if (total === 0) {
    return (
      <section className="pt-3 pb-2 sm:pt-6 sm:pb-3 bg-[#FAF8F5]">
        <div className="max-w-4xl mx-auto px-4 sm:px-6">
          <div className="w-full aspect-[16/9] rounded-2xl bg-[#12100E] flex items-center justify-center animate-pulse border border-[#E8E2D9]">
            <p className="font-serif text-sm sm:text-base text-[#C5A880]">Loading Gemstone Heritage...</p>
          </div>
        </div>
      </section>
    );
  }

  const currentSlide = slides[currentIndex];

  return (
    <section
      className="pt-3 pb-2 sm:pt-6 sm:pb-3 bg-[#FAF8F5] text-white select-none"
      aria-roledescription="carousel"
      aria-label="RMK Gems Featured Showcase"
      onMouseEnter={() => setIsPaused(true)}
      onMouseLeave={() => !userInteracted && setIsPaused(false)}
      onFocus={() => setIsPaused(true)}
      onBlur={() => !userInteracted && setIsPaused(false)}
      onTouchStart={handleTouchStart}
      onTouchMove={handleTouchMove}
      onTouchEnd={handleTouchEnd}
    >
      <div className="max-w-4xl mx-auto px-4 sm:px-6">
        <div className="relative w-full aspect-[16/9] rounded-2xl overflow-hidden shadow-xl border border-[#E8E2D9] bg-[#0E0C0A]">
          {/* Slide Images */}
          {slides.map((slide, idx) => (
            <div
              key={slide.id || idx}
              className={`absolute inset-0 transition-opacity duration-700 ease-in-out ${
                idx === currentIndex
                  ? 'opacity-100 z-10 pointer-events-auto'
                  : 'opacity-0 z-0 pointer-events-none'
              }`}
              aria-hidden={idx !== currentIndex}
            >
              <Link
                to={slide.button_link || '/precious-gemstones'}
                className="block w-full h-full cursor-pointer focus:outline-none focus-visible:ring-2 focus-visible:ring-[#C5A880]"
                aria-label={slide.title || `Slide ${idx + 1}`}
              >
                <img
                  src={slide.image_url}
                  alt={slide.image_alt_text || slide.title}
                  className="w-full h-full object-cover object-center"
                  loading={idx === 0 ? 'eager' : 'lazy'}
                />
              </Link>

              {/* Subtle bottom shadow vignette for controls readability without hiding slide art */}
              <div className="absolute inset-x-0 bottom-0 h-14 sm:h-20 bg-gradient-to-t from-black/70 via-black/25 to-transparent pointer-events-none" />
            </div>
          ))}

          {/* Floating CTA Pill (Bottom Left) */}
          {currentSlide && currentSlide.button_link && (
            <div className="absolute z-20 bottom-3 sm:bottom-4 left-3 sm:left-5">
              <Link
                to={currentSlide.button_link}
                className="inline-flex items-center gap-1.5 px-3 py-1 sm:px-3.5 sm:py-1.5 rounded-full bg-black/65 hover:bg-black/85 backdrop-blur-md border border-[#C5A880]/60 text-white text-[11px] sm:text-xs font-medium transition-all shadow-md hover:border-[#C5A880] hover:scale-105 focus:outline-none focus-visible:ring-2 focus-visible:ring-[#C5A880]"
              >
                <span>{currentSlide.button_text}</span>
                <span className="text-[#C5A880] font-bold">&rarr;</span>
              </Link>
            </div>
          )}

          {/* Prev / Next & Pause Controls (Bottom Right) */}
          <div className="absolute z-20 bottom-3 sm:bottom-4 right-3 sm:right-5 flex items-center gap-1.5 sm:gap-2">
            {/* Pause / Play Toggle */}
            <button
              type="button"
              onClick={(e) => {
                e.stopPropagation();
                setUserInteracted(true);
                setIsPaused(!isPaused);
              }}
              className="p-1 sm:p-1.5 rounded-full bg-black/55 hover:bg-black/80 backdrop-blur-sm border border-white/20 text-white transition-all hover:scale-105 focus:outline-none focus-visible:ring-2 focus-visible:ring-[#C5A880]"
              aria-label={isPaused ? "Play carousel autoplay" : "Pause carousel autoplay"}
            >
              {isPaused ? <Play className="w-3 h-3 sm:w-3.5 sm:h-3.5" /> : <Pause className="w-3 h-3 sm:w-3.5 sm:h-3.5" />}
            </button>

            {/* Prev Slide */}
            <button
              type="button"
              onClick={(e) => {
                e.stopPropagation();
                setUserInteracted(true);
                goToPrev();
              }}
              className="p-1 sm:p-1.5 rounded-full bg-black/55 hover:bg-black/80 backdrop-blur-sm border border-white/20 text-white transition-all hover:scale-105 focus:outline-none focus-visible:ring-2 focus-visible:ring-[#C5A880]"
              aria-label="Previous slide"
            >
              <ChevronLeft className="w-3.5 h-3.5 sm:w-4 sm:h-4" />
            </button>

            {/* Next Slide */}
            <button
              type="button"
              onClick={(e) => {
                e.stopPropagation();
                setUserInteracted(true);
                goToNext();
              }}
              className="p-1 sm:p-1.5 rounded-full bg-black/55 hover:bg-black/80 backdrop-blur-sm border border-white/20 text-white transition-all hover:scale-105 focus:outline-none focus-visible:ring-2 focus-visible:ring-[#C5A880]"
              aria-label="Next slide"
            >
              <ChevronRight className="w-3.5 h-3.5 sm:w-4 sm:h-4" />
            </button>
          </div>

          {/* Slide Indicators (Bottom Center) */}
          <div
            className="absolute z-20 bottom-3.5 sm:bottom-4.5 left-1/2 -translate-x-1/2 flex items-center gap-1.5"
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
                onClick={(e) => {
                  e.stopPropagation();
                  setUserInteracted(true);
                  setCurrentIndex(idx);
                }}
                className={`h-1.5 rounded-full transition-all duration-300 focus:outline-none focus-visible:ring-2 focus-visible:ring-[#C5A880] ${
                  idx === currentIndex ? 'w-5 sm:w-7 bg-[#C5A880]' : 'w-1.5 bg-white/40 hover:bg-white/70'
                }`}
              />
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};
