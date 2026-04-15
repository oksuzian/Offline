# Mu2eInterfaces

**Role:** Abstract base classes and marker interfaces shared across Offline - detectors, conditions, and proditions entities.

## Overview
This header-only package defines the minimal interfaces that many other packages inherit from without pulling in heavy dependencies. It underpins the conditions/proditions framework (`ProditionsEntity`, `ProditionsCache`, `ConditionsEntity`) and the `Detector` base used by subsystem geometry classes. Cross-referenced widely; essentially every conditions and geometry package in Offline depends on these headers.

## Key contents
- `inc/Detector.hh` - base for all Detector geometry objects
- `inc/ProditionsEntity.hh` - base for cached proditions payloads (tracks contributing CIDs)
- `inc/ProditionsCache.hh` - base for proditions caches keyed by IOV
- `inc/ConditionsEntity.hh` - legacy conditions-entity base

## Inputs / Outputs
- **Consumes:** nothing at runtime; compile-time dependency only
- **Produces:** abstract interfaces consumed by [[GeometryService]], [[ProditionsService]], [[DbService]], and subsystem conditions/geom packages

## Related
- [[ProditionsService]]
- [[GeometryService]]
- [[DbService]]
- [[Mu2eG4]]
