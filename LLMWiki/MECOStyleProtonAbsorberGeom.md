# MECOStyleProtonAbsorberGeom

**Role:** Geometry of the MECO-style (conical, multi-part) proton absorber inside the Detector Solenoid.

## Overview
Describes the inner and outer proton absorber parts (`pabs1/2`, `opabs1/2`) positioned around the stopping target region to slow/absorb recoil protons before they reach the tracker. Named for the MECO predecessor experiment whose conical absorber design was inherited. Coordinates are expressed in the detector coordinate system (mm) and the objects are registered with [[GeometryService]].

## Key contents
- `MECOStyleProtonAbsorber.hh` - top-level object with `ProtonAbsorberId` enum
- `MECOStyleProtonAbsorberPart.hh` - one conical/tubular section
- `src/MECOStyleProtonAbsorberMaker.cc` - builds from SimpleConfig
- Uses `Tube` primitive from [[GeomPrimitives]]

## Inputs / Outputs
- **Consumes:** SimpleConfig parameters from `Mu2eG4/geom/protonabsorber*.txt`
- **Produces:** `MECOStyleProtonAbsorber` detector object for [[GeometryService]]

## Related
- [[StoppingTargetGeom]]
- [[DetectorSolenoidGeom]]
- [[MBSGeom]]
- [[GeomPrimitives]]
