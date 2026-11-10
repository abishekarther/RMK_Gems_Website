import React, { useRef, useMemo } from 'react';
import { useFrame } from '@react-three/fiber';
import * as THREE from 'three';
import { getGemstoneGeometry } from './GemstoneGeometry';
import { getGemstoneVisualConfig } from './gemstoneVisuals';

interface GemstoneMeshProps {
  slug: string;
  isHovered?: boolean;
  scale?: number;
}

export const GemstoneMesh: React.FC<GemstoneMeshProps> = ({
  slug,
  isHovered = false,
  scale = 1.0,
}) => {
  const meshRef = useRef<THREE.Mesh>(null);
  const config = useMemo(() => getGemstoneVisualConfig(slug), [slug]);
  const geometry = useMemo(() => getGemstoneGeometry(config.cut), [config.cut]);

  // Check reduced motion preference
  const prefersReducedMotion = useMemo(() => {
    return window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  }, []);

  // Frame animation: continuous slow idle rotation with slight bobbing
  useFrame((state, delta) => {
    if (!meshRef.current) return;
    if (!prefersReducedMotion) {
      // Slow elegant continuous rotation
      const speed = isHovered ? 0.9 : 0.4;
      meshRef.current.rotation.y += delta * speed;
      meshRef.current.rotation.x = Math.sin(state.clock.elapsedTime * 0.5) * 0.12;
    }
  });

  return (
    <group scale={scale}>
      <mesh
        ref={meshRef}
        geometry={geometry}
        castShadow
        receiveShadow
      >
        <meshPhysicalMaterial
          color={config.color}
          roughness={isHovered ? Math.max(0.01, config.roughness * 0.7) : config.roughness}
          metalness={config.metalness}
          transmission={config.transmission}
          ior={config.ior}
          thickness={1.6}
          transparent
          opacity={config.opacity}
          emissive={isHovered ? config.color : '#000000'}
          emissiveIntensity={isHovered ? 0.35 : 0.0}
          reflectivity={0.9}
          clearcoat={1.0}
          clearcoatRoughness={0.05}
          flatShading={config.cut !== 'cabochon' && config.cut !== 'pearl'}
        />
      </mesh>
    </group>
  );
};
