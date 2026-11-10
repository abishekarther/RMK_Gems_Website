import React from 'react';
import { HeroCarousel } from '../sections/HeroCarousel/HeroCarousel';
import { CategorySelection } from '../sections/CategorySelection/CategorySelection';
import { LocationSection } from '../sections/LocationSection/LocationSection';

export const HomePage: React.FC = () => {
  return (
    <main>
      {/* 1. Five-Slide Gemstone History Carousel */}
      <HeroCarousel />

      {/* 2. Category Selection: Precious Gemstones & Semi-Precious Gemstones */}
      <CategorySelection />

      {/* 3. Brand Statement & Location Preview */}
      <LocationSection />
    </main>
  );
};
