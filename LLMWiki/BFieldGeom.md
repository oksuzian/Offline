# BFieldGeom

**Role:** Data classes that hold Mu2e magnetic field maps and the manager that evaluates B at an arbitrary point.

## Overview
Defines the configuration, storage, and lookup of all Mu2e B-field maps (grid-based G4BL maps and parametric maps). `BFieldManager` aggregates an ordered list of inner and outer maps and returns the field at a position with caching and overlap resolution. These are pure data classes; a companion Maker in [[GeometryService]] reads the field configuration and populates them.

## Key contents
- `BFieldManager.hh` - central accessor, returns B at a 3D point via `getBField` / `getBFieldWithStatus`.
- `BFieldConfig.hh` - user-visible configuration of map list, map type, and interpolation style.
- `BFMap.hh`, `BFGridMap.hh`, `BFParamMap.hh` - abstract map plus grid and parametric implementations.
- `BFCacheManager.hh` - per-thread/per-query caching across overlapping maps.
- `BFMapType.hh`, `BFInterpolationStyle.hh`, `Container3D.hh` - map type enum, interpolation choices, grid storage.

## Inputs / Outputs
- **Consumes:** field map files (G4BL text / parametric); FHiCL / SimpleConfig via the Maker in [[GeometryService]].
- **Produces:** `BFieldManager` Detector served through [[GeometryService]]; used by Geant4 stepping, Kalman fits, and field-scan utilities in [[BFieldTest]].

## Related
- [[GeometryService]]
- [[BFieldTest]]
- [[BeamlineGeom]]
- [[ProductionSolenoidGeom]]
- [[DetectorSolenoidGeom]]
