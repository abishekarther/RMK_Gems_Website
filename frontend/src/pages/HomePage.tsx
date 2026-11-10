import React from 'react';
import { HeroCarousel } from '../sections/HeroCarousel/HeroCarousel';
import { CategorySelection } from '../sections/CategorySelection/CategorySelection';
import { LocationSection } from '../sections/LocationSection/LocationSection';

export const HomePage: React.FC = () => {
  return (
    <main>
      {/* 1. Five-Slide Gemstone History Carousel */}
      <HeroCarousel />

      {/* 2. Brand Statement & Values */}
      <LocationSection />

      {/* 3. Curated Gemstone Galleries (Precious & Semi-Precious) */}
      <CategorySelection />
    </main>
  );
};
