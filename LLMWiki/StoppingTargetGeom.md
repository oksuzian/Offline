# StoppingTargetGeom

**Role:** Geometry of the muon stopping target: foils, support structure, and z-binning helpers.

## Overview
Represents the stack of thin aluminum target foils (perpendicular to z) where muons stop and form muonic atoms, together with their wire-support structure. The class also supplies z-binning helpers used by histogramming and analysis code to align quantities with foil positions. Coordinates are detector-system mm; the object is registered with [[GeometryService]] and placed by Mu2eG4 inside the DS vacuum.

## Key contents
- `StoppingTarget.hh` - collection of `TargetFoil`s plus envelope radius/z-length
- `TargetFoil.hh` - single disk foil (radius, position, material)
- `TargetFoilSupportStructure.hh` - wire supports
- `zBinningForFoils.hh` - z-binning helper used in analysis
- `src/StoppingTargetMaker.cc` - builder from SimpleConfig

## Inputs / Outputs
- **Consumes:** `Mu2eG4/geom/stoppingTarget*.txt` SimpleConfig parameters
- **Produces:** `StoppingTarget` detector object used by `constructStoppingTarget` and by analysis/validation code

## Related
- [[DetectorSolenoidGeom]]
- [[MECOStyleProtonAbsorberGeom]]
- [[MBSGeom]]
- [[GeomPrimitives]]
