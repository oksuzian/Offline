# CalorimeterGeom

**Role:** Geometry description and navigation for the Mu2e disk CsI calorimeter.

## Overview
Provides the C++ geometry objects for the two-disk crystal calorimeter: crystal-index mappings, per-disk coordinate systems, and global disk placement. Loaded by [[GeometryService]] and used everywhere calorimeter hits, clusters, or showers need geometric context (positions, neighbours, local/global transforms).

## Key contents
- `Calorimeter` (abstract) — top-level interface returned by the geometry service
- `DiskCalorimeter` / `Disk` — concrete disk-based implementation
- `Crystal` — per-crystal position/size record
- `SquareMapper`, `SquareShiftMapper`, `CrystalMapper` — 2D index <-> coordinate mappings used by the clustering flood-fill
- `CaloGeomUtil` — helper transforms (crystal <-> disk <-> Mu2e frame)
- `CaloInfo`, `DiskGeomInfo` — lightweight descriptors

## Inputs / Outputs
- **Consumes:** `SimpleConfig` geometry parameters via [[GeometryService]]
- **Produces:** `Calorimeter` geometry handle used by all Calo* subsystems and [[Mu2eG4]]

## Related
- [[GeometryService]], [[GeomPrimitives]]
- [[CaloReco]], [[CaloCluster]], [[CaloMC]] — all depend on this library
- [[Mu2eG4]] — builds the Geant4 geometry from these objects
