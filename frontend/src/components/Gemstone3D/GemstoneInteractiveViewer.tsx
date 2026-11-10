import React, { useState, Suspense } from 'react';
import { Canvas } from '@react-three/fiber';
import { OrbitControls } from '@react-three/drei';
import { RotateCw, Pause, Play, Sparkles } from 'lucide-react';
import { GemstoneMesh } from './GemstoneMesh';
import { getGemstoneVisualConfig } from './gemstoneVisuals';

interface GemstoneInteractiveViewerProps {
  slug: string;
  name: string;
}

export const GemstoneInteractiveViewer: React.FC<GemstoneInteractiveViewerProps> = ({ slug, name: _name }) => {
  const [isRotating, setIsRotating] = useState(true);
  const [isHovered, setIsHovered] = useState(false);
  const config = getGemstoneVisualConfig(slug);

  return (
    <div className="relative w-full aspect-square max-w-lg mx-auto bg-gradient-to-b from-[#FAF8F5] via-[#F4EFE6]/50 to-[#FAF8F5] rounded-2xl p-4 sm:p-6 border border-[#E8E2D9] shadow-sm flex flex-col items-center justify-center">
      {/* 3D Canvas */}
      <div
        className="w-full h-full relative cursor-grab active:cursor-grabbing"
        onMouseEnter={() => setIsHovered(true)}
        onMouseLeave={() => setIsHovered(false)}
      >
        <Canvas
          camera={{ position: [0, 0, 3.4], fov: 42 }}
          dpr={[1, 2]}
          gl={{ antialias: true, alpha: true }}
          className="w-full h-full"
        >
          <ambientLight intensity={1.4} />
          <directionalLight position={[6, 9, 6]} intensity={2.2} />
          <directionalLight position={[-6, -4, -4]} intensity={1.1} color="#FFF5EB" />
          <pointLight position={[0, 4, 3]} intensity={2.0} color="#FFFFFF" />
          <pointLight position={[-3, -3, 2]} intensity={1.0} color={config.color} />

          <Suspense fallback={null}>
            <GemstoneMesh
              slug={slug}
              isHovered={isHovered}
              scale={1.15}
            />
          </Suspense>

          <OrbitControls
            enableZoom={true}
            minDistance={2.0}
            maxDistance={5.0}
            autoRotate={isRotating}
            autoRotateSpeed={1.5}
            enablePan={false}
          />
        </Canvas>

        {/* Floating background radiant light ring */}
        <div
          className="absolute inset-0 pointer-events-none rounded-full blur-2xl -z-10 transition-opacity duration-700 opacity-30"
          style={{
            background: `radial-gradient(circle at center, ${config.color} 0%, transparent 70%)`,
          }}
        />
      </div>

      {/* Floating Interactive Controls */}
      <div className="absolute top-4 right-4 flex items-center space-x-2 bg-white/90 backdrop-blur-md px-3 py-1.5 rounded-full border border-[#E8E2D9] shadow-xs text-xs text-[#4A4A4A]">
        <button
          type="button"
          onClick={() => setIsRotating(!isRotating)}
          className="p-1 hover:text-[#997A48] focus:outline-none focus:ring-1 focus:ring-[#997A48] rounded transition-colors"
          title={isRotating ? "Pause rotation" : "Resume rotation"}
          aria-label={isRotating ? "Pause 3D rotation" : "Resume 3D rotation"}
        >
          {isRotating ? <Pause className="w-4 h-4" /> : <Play className="w-4 h-4" />}
        </button>
        <span className="text-[#D1C7BA]">|</span>
        <span className="flex items-center gap-1 text-[11px] font-medium text-[#717171]">
          <RotateCw className="w-3 h-3 text-[#997A48]" /> Drag to Rotate
        </span>
      </div>

      {/* Representative Model Notice (Section 5 & Appendix A) */}
      <div className="mt-2 text-center">
        <p className="text-[11px] text-[#717171] tracking-wide flex items-center justify-center gap-1.5">
          <Sparkles className="w-3 h-3 text-[#997A48]" />
          <span>Representative 3D model; actual gemstones vary naturally in colour and cut.</span>
        </p>
      </div>
    </div>
  );
};
