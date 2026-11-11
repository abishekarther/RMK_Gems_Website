import React, { useState, useEffect, useRef, useCallback } from 'react';
import { Link } from 'react-router-dom';
import { ChevronLeft, ChevronRight } from 'lucide-react';
import type { HomepageSlide } from '../../types/gemstone';
import { fetchHomepageSlides } from '../../services/api';

export const HeroCarousel: React.FC = () => {
  const [slides, setSlides] = useState<HomepageSlide[]>([]);
  const [currentIndex, setCurrentIndex] = useState(0);
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
      goToNext();
    } else if (distance < -minSwipeDistance) {
      goToPrev();
    }
    touchStartX.current = null;
    touchEndX.current = null;
  };

  // Continuous autoplay that runs without stopping, even when cursor is on the banner
  useEffect(() => {
    if (prefersReducedMotion || total <= 1) return;

    timerRef.current = setInterval(() => {
      goToNext();
    }, 5000);

    return () => {
      if (timerRef.current) clearInterval(timerRef.current);
    };
  }, [prefersReducedMotion, total, goToNext, currentIndex]);

  if (total === 0) {
    return (
      <section className="w-full bg-[#FAF8F5] py-0 lg:py-6">
        <div className="w-full lg:w-[80%] max-w-[1300px] mx-auto aspect-[16/9] bg-[#12100E] lg:rounded-2xl flex items-center justify-center animate-pulse">
          <p className="font-serif text-sm sm:text-base text-[#C5A880]">Loading Gemstone Heritage...</p>
        </div>
      </section>
    );
  }

  const currentSlide = slides[currentIndex];

  return (
    <section
      className="w-full bg-[#FAF8F5] py-0 lg:py-6 text-white select-none"
      aria-roledescription="carousel"
      aria-label="RMK Gems Featured Showcase"
      onTouchStart={handleTouchStart}
      onTouchMove={handleTouchMove}
      onTouchEnd={handleTouchEnd}
    >
      {/* 
        Native 16:9 Aspect Ratio on Mobile/Tablet so 100% of the image graphics & typography fit without any cropping.
        On Laptop/Desktop: 80% width centered with rounded luxury frame.
      */}
      <div className="relative w-full lg:w-[80%] max-w-[1300px] mx-auto aspect-[16/9] overflow-hidden lg:rounded-2xl lg:shadow-2xl lg:border lg:border-[#E8E2D9] bg-[#1A1A1A]">
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

            {/* Subtle bottom shadow vignette for controls readability without obscuring slide artwork */}
            <div className="absolute inset-x-0 bottom-0 h-12 sm:h-20 lg:h-28 bg-gradient-to-t from-black/75 via-black/25 to-transparent pointer-events-none" />
          </div>
        ))}

        {/* Floating CTA Pill (Bottom Left) */}
        {currentSlide && currentSlide.button_link && (
          <div className="absolute z-20 bottom-2.5 sm:bottom-4 lg:bottom-6 left-2.5 sm:left-4 lg:left-8">
            <Link
              to={currentSlide.button_link}
              className="inline-flex items-center gap-1 sm:gap-1.5 lg:gap-2 px-2.5 py-1 sm:px-3.5 sm:py-1.5 lg:px-5 lg:py-2 rounded-full bg-black/65 hover:bg-black/90 backdrop-blur-md border border-[#C5A880]/70 text-white text-[10px] sm:text-xs lg:text-sm font-medium transition-all shadow-md hover:border-[#C5A880] hover:scale-105 focus:outline-none focus-visible:ring-2 focus-visible:ring-[#C5A880]"
            >
              <span>{currentSlide.button_text}</span>
              <span className="text-[#C5A880] font-bold">&rarr;</span>
            </Link>
          </div>
        )}

        {/* Prev / Next Controls (Bottom Right - No Stop Button) */}
        <div className="absolute z-20 bottom-2.5 sm:bottom-4 lg:bottom-6 right-2.5 sm:right-4 lg:right-8 flex items-center gap-1.5 sm:gap-2">
          {/* Prev Slide */}
          <button
            type="button"
            onClick={(e) => {
              e.stopPropagation();
              goToPrev();
            }}
            className="p-1 sm:p-1.5 lg:p-2 rounded-full bg-black/55 hover:bg-black/85 backdrop-blur-sm border border-white/20 text-white transition-all hover:scale-110 hover:border-[#C5A880] focus:outline-none focus-visible:ring-2 focus-visible:ring-[#C5A880]"
            aria-label="Previous slide"
          >
            <ChevronLeft className="w-3.5 h-3.5 sm:w-4 sm:h-4 lg:w-5 lg:h-5" />
          </button>

          {/* Next Slide */}
          <button
            type="button"
            onClick={(e) => {
              e.stopPropagation();
              goToNext();
            }}
            className="p-1 sm:p-1.5 lg:p-2 rounded-full bg-black/55 hover:bg-black/85 backdrop-blur-sm border border-white/20 text-white transition-all hover:scale-110 hover:border-[#C5A880] focus:outline-none focus-visible:ring-2 focus-visible:ring-[#C5A880]"
            aria-label="Next slide"
          >
            <ChevronRight className="w-3.5 h-3.5 sm:w-4 sm:h-4 lg:w-5 lg:h-5" />
          </button>
        </div>

        {/* Slide Indicators (Bottom Center) */}
        <div
          className="absolute z-20 bottom-3 sm:bottom-5 lg:bottom-7 left-1/2 -translate-x-1/2 flex items-center gap-1 sm:gap-1.5 lg:gap-2"
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
                setCurrentIndex(idx);
              }}
              className={`h-1 sm:h-1.5 rounded-full transition-all duration-300 focus:outline-none focus-visible:ring-2 focus-visible:ring-[#C5A880] ${
                idx === currentIndex ? 'w-4 sm:w-6 lg:w-8 bg-[#C5A880]' : 'w-1 sm:w-1.5 lg:w-2 bg-white/40 hover:bg-white/70'
              }`}
            />
          ))}
        </div>
      </div>
    </section>
  );
};
