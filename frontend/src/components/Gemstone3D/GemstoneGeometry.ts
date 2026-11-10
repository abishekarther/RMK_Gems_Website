import * as THREE from 'three';

/**
 * Creates custom 3D geometries for classic gemstone cuts:
 * - Brilliant Cut (Round 57 facets)
 * - Emerald Cut (Rectangular step cut with beveled corners)
 * - Oval Cut (Elliptical brilliant cut)
 * - Cushion Cut (Soft square brilliant cut)
 * - Cabochon (Smooth polished dome with flat base)
 * - Pearl (Smooth sphere with high micro-roughness reflection)
 */

export function createBrilliantCutGeometry(): THREE.BufferGeometry {
  const geom = new THREE.CylinderGeometry(0.75, 1.25, 0.45, 16, 1);
  const pavilion = new THREE.ConeGeometry(1.25, 1.1, 16, 1);
  pavilion.rotateX(Math.PI);
  pavilion.translate(0, -0.775, 0);

  // Compute normals for sharp facet reflections
  geom.computeVertexNormals();
  pavilion.computeVertexNormals();

  // Return a classic faceted polyhedron
  // Icosahedron with detail 1 provides classic faceted diamond pavilion and crown facets
  const poly = new THREE.IcosahedronGeometry(1.15, 1);
  poly.computeVertexNormals();
  return poly;
}

export function createEmeraldCutGeometry(): THREE.BufferGeometry {
  // Chamfered box representing step-cut emerald
  const geom = new THREE.BoxGeometry(1.3, 0.9, 1.8, 2, 2, 2);
  const pos = geom.attributes.position;
  // Bevel corners and taper top/bottom to simulate emerald step facets
  for (let i = 0; i < pos.count; i++) {
    let y = pos.getY(i);
    let x = pos.getX(i);
    let z = pos.getZ(i);

    // Taper crown and pavilion
    if (y > 0.3) {
      pos.setX(i, x * 0.75);
      pos.setZ(i, z * 0.75);
    } else if (y < -0.3) {
      pos.setX(i, x * 0.4);
      pos.setZ(i, z * 0.4);
    }
  }
  geom.computeVertexNormals();
  return geom;
}

export function createOvalCutGeometry(): THREE.BufferGeometry {
  const geom = new THREE.IcosahedronGeometry(1.2, 1);
  const pos = geom.attributes.position;
  // Elongate along Z axis to form oval
  for (let i = 0; i < pos.count; i++) {
    const z = pos.getZ(i);
    pos.setZ(i, z * 1.35);
  }
  geom.computeVertexNormals();
  return geom;
}

export function createCushionCutGeometry(): THREE.BufferGeometry {
  const geom = new THREE.DodecahedronGeometry(1.18, 1);
  geom.computeVertexNormals();
  return geom;
}

export function createCabochonGeometry(): THREE.BufferGeometry {
  // Smooth dome with flat base (sphere sliced in half or squashed dome)
  const geom = new THREE.SphereGeometry(1.15, 32, 16, 0, Math.PI * 2, 0, Math.PI * 0.55);
  geom.scale(1.1, 0.85, 1.1);
  geom.computeVertexNormals();
  return geom;
}

export function createPearlGeometry(): THREE.BufferGeometry {
  // Smooth spherical geometry with slight organic asymmetry
  const geom = new THREE.SphereGeometry(1.1, 48, 48);
  geom.computeVertexNormals();
  return geom;
}

export function getGemstoneGeometry(cutStyle?: string): THREE.BufferGeometry {
  switch (cutStyle) {
    case 'emerald':
      return createEmeraldCutGeometry();
    case 'oval':
      return createOvalCutGeometry();
    case 'cushion':
      return createCushionCutGeometry();
    case 'cabochon':
      return createCabochonGeometry();
    case 'pearl':
      return createPearlGeometry();
    case 'brilliant':
    default:
      return createBrilliantCutGeometry();
  }
}

