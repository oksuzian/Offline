# Mu2eReco

**Role:** Collection point for the current Mu2e-wide reconstruction geometry include file.

## Overview
A near-empty staging folder: it contains only a geometry-text pointer (`recoGeom_common_current.txt`) that fcl jobs include to pick up the canonical reconstruction geometry snapshot. The CMakeLists simply copies the geom file into the build tree. Subsystem reconstruction code itself lives in the dedicated packages (TrkReco, CaloReco, CRVReco, CosmicReco, ...).

## Key contents
- `geom/recoGeom_common_current.txt` - include file pinning the current reco geometry
- `CMakeLists.txt` - copies the geom file into the build output

## Inputs / Outputs
- **Consumes:** nothing at runtime
- **Produces:** an installed geometry include used by reconstruction fcl

## Related
- [[GeometryService]]
- [[TrkReco]]
- [[CaloReco]]
- [[CRVReco]]
- [[CommonReco]]
