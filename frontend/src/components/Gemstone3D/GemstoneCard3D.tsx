import React, { useState, useEffect, useRef } from 'react';
import { Link } from 'react-router-dom';
import { Canvas } from '@react-three/fiber';
import { GemstoneMesh } from './GemstoneMesh';
import { getGemstoneVisualConfig } from './gemstoneVisuals';
import type { GemstoneItem } from '../../types/gemstone';

interface GemstoneCard3DProps {
  gemstone: GemstoneItem;
  priority?: boolean;
}

export const GemstoneCard3D: React.FC<GemstoneCard3DProps> = ({ gemstone, priority = false }) => {
  const [isHovered, setIsHovered] = useState(false);
  const [isInView, setIsInView] = useState(priority);
  const containerRef = useRef<HTMLDivElement>(null);
  const config = getGemstoneVisualConfig(gemstone.slug);

  useEffect(() => {
    if (priority) return;

    const observer = new IntersectionObserver(
      ([entry]) => {
        setIsInView(entry.isIntersecting);
      },
      { rootMargin: '120px' }
    );

    if (containerRef.current) {
      observer.observe(containerRef.current);
    }

    return () => observer.disconnect();
  }, [priority]);

  return (
    <div
      ref={containerRef}
      className="group relative flex flex-col items-center justify-center p-4 transition-all duration-300 rounded-xl hover:bg-white/70"
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
      onTouchStart={() => setIsHovered(true)}
    >
      <Link
        to={`/gemstones/${gemstone.slug}`}
        className="block w-full focus:outline-none focus-visible:ring-2 focus-visible:ring-[#997A48] rounded-xl"
        aria-label={`View details of ${gemstone.name}`}
      >
        {/* 3D Model Display / Preview */}
        <div className="relative w-full aspect-square flex items-center justify-center overflow-hidden rounded-lg">
          {isInView ? (
            <Canvas
              camera={{ position: [0, 0, 3.2], fov: 45 }}
              dpr={[1, 1.5]}
              gl={{ antialias: true, alpha: true, powerPreference: 'low-power' }}
              className="w-full h-full cursor-pointer"
            >
              <ambientLight intensity={1.2} />
              <directionalLight position={[5, 8, 5]} intensity={1.8} />
              <directionalLight position={[-5, -4, -4]} intensity={0.9} color="#FFF8EE" />
              <pointLight position={[0, 4, 3]} intensity={1.5} color="#FFFFFF" />
              <GemstoneMesh slug={gemstone.slug} isHovered={isHovered} />
            </Canvas>
          ) : (
            /* Lightweight luxury preview fallback for out-of-viewport items */
            <div
              className="w-24 h-24 rounded-full opacity-80 blur-xs transition-transform duration-500 group-hover:scale-105"
              style={{
                background: `radial-gradient(circle at 35% 35%, #FFFFFF 0%, ${config.color} 50%, #1A1A1A 100%)`,
                boxShadow: `0 10px 25px -5px ${config.color}40`,
              }}
            />
          )}

          {/* Gentle ambient glow ring behind gemstone */}
          <div
            className={`absolute inset-0 pointer-events-none rounded-full transition-opacity duration-500 -z-10 ${
              isHovered ? 'opacity-40' : 'opacity-10'
            }`}
            style={{
              background: `radial-gradient(circle, ${config.color} 0%, transparent 70%)`,
            }}
          />
        </div>

        {/* Gemstone Name & Details */}
        <div className="mt-3 text-center w-full">
          <h3 className="text-base sm:text-lg font-serif font-medium text-[#1E1E1E] tracking-wide transition-colors duration-200 group-hover:text-[#997A48]">
            {gemstone.name}
          </h3>
          <p className="text-xs text-[#717171] uppercase tracking-wider mt-0.5 capitalize">
            {config.cut} Cut • {gemstone.material_type || 'Natural'}
          </p>
          
          {/* Subtle View link */}
          <div className="mt-1.5 opacity-0 group-hover:opacity-100 transition-opacity duration-200 text-xs font-medium text-[#997A48]">
            View Details &rarr;
          </div>
        </div>
      </Link>
    </div>
  );
};
