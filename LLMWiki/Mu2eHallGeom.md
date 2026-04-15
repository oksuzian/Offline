# Mu2eHallGeom

**Role:** Geometry of the Mu2e experimental hall: concrete building volumes and surrounding dirt/berm.

## Overview
Stores the full map of building (concrete) and dirt volumes from which the G4 world is assembled. Construction is staged: building volumes are built first, their envelope is computed, then dirt volumes are generated to fill around the envelope; finally Mu2eG4 places everything via `constructHall.cc`. This package is the outermost layer of the detector-region geometry and sets the global envelope used by all downstream placements.

## Key contents
- `Mu2eHall.hh` - map of all hall and dirt solids, with staged construction docs
- `src/Mu2eHallMaker.cc` - `makeBuilding(...)` and `makeDirt(...)` stages
- Uses extruded and generic solids from [[GeomPrimitives]]

## Inputs / Outputs
- **Consumes:** `Mu2eG4/geom/hall*.txt`, `dirt*.txt` SimpleConfig files
- **Produces:** `Mu2eHall` detector object used by `Mu2eG4/src/constructHall.cc` and by `WorldG4Maker` (dirt grade level)

## Related
- [[ExternalShieldingGeom]]
- [[DetectorSolenoidGeom]]
- [[ServicesGeom]]
- [[GeomPrimitives]]
