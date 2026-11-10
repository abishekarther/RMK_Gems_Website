import * as THREE from 'three';
import { GLTFExporter } from 'three/examples/jsm/exporters/GLTFExporter.js';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const outDir = path.resolve(__dirname, '../public/models');

if (!fs.existsSync(outDir)) {
  fs.mkdirSync(outDir, { recursive: true });
}

function createBrilliantCutGeometry() {
  const poly = new THREE.IcosahedronGeometry(1.15, 1);
  poly.computeVertexNormals();
  return poly;
}

function createEmeraldCutGeometry() {
  const geom = new THREE.BoxGeometry(1.3, 0.9, 1.8, 2, 2, 2);
  const pos = geom.attributes.position;
  for (let i = 0; i < pos.count; i++) {
    let y = pos.getY(i);
    let x = pos.getX(i);
    let z = pos.getZ(i);
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

function createOvalCutGeometry() {
  const geom = new THREE.IcosahedronGeometry(1.2, 1);
  const pos = geom.attributes.position;
  for (let i = 0; i < pos.count; i++) {
    const z = pos.getZ(i);
    pos.setZ(i, z * 1.35);
  }
  geom.computeVertexNormals();
  return geom;
}

function createCushionCutGeometry() {
  const geom = new THREE.DodecahedronGeometry(1.18, 1);
  geom.computeVertexNormals();
  return geom;
}

function createCabochonGeometry() {
  const geom = new THREE.SphereGeometry(1.15, 32, 16, 0, Math.PI * 2, 0, Math.PI * 0.55);
  geom.scale(1.1, 0.85, 1.1);
  geom.computeVertexNormals();
  return geom;
}

function createPearlGeometry() {
  const geom = new THREE.SphereGeometry(1.1, 48, 48);
  geom.computeVertexNormals();
  return geom;
}

const cuts = [
  { name: 'brilliant', geom: createBrilliantCutGeometry(), color: 0xe0e6ed },
  { name: 'emerald', geom: createEmeraldCutGeometry(), color: 0x1b8a5a },
  { name: 'oval', geom: createOvalCutGeometry(), color: 0xb22222 },
  { name: 'cushion', geom: createCushionCutGeometry(), color: 0xe5b832 },
  { name: 'cabochon', geom: createCabochonGeometry(), color: 0x9b8b38 },
  { name: 'pearl', geom: createPearlGeometry(), color: 0xf4f1ea },
];

const exporter = new GLTFExporter();

for (const cut of cuts) {
  const material = new THREE.MeshStandardMaterial({
    color: cut.color,
    roughness: 0.1,
    metalness: 0.1,
  });
  const mesh = new THREE.Mesh(cut.geom, material);
  mesh.name = cut.name;

  exporter.parse(
    mesh,
    (gltf) => {
      const filePath = path.join(outDir, `${cut.name}.glb`);
      fs.writeFileSync(filePath, Buffer.from(gltf));
      console.log(`Generated: ${filePath} (${fs.statSync(filePath).size} bytes)`);
    },
    (err) => console.error(`Error exporting ${cut.name}:`, err),
    { binary: true }
  );
}

