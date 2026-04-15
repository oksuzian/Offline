# DetectorSolenoidGeom

**Role:** Describes the Detector Solenoid (DS) cryostat, coils, vacuum volumes, and internal shielding.

## Overview
The DS is the large solenoid enclosing the stopping target, tracker, and calorimeter; this package provides the C++ geometry objects used by the Geometry service and passed to the Mu2eG4 construction code. Positioning is derived from TS5, the torus radius, and DS envelope half-lengths so that upstream transport geometry and downstream detector geometry stay consistent. The package defines only geometry data; material placement and Geant4 volumes are built elsewhere.

## Key contents
- `DetectorSolenoid.hh` - cryostat radii, lengths, coils, vacuum regions
- `DetectorSolenoidShielding.hh` - downstream/internal shielding tubes
- `src/DetectorSolenoidMaker.cc` - builds instances from SimpleConfig
- Depends on [[GeomPrimitives]] (Tube, PlacedTubs) and Mu2eInterfaces::Detector

## Inputs / Outputs
- **Consumes:** `Mu2eG4/geom/*.txt` SimpleConfig parameters; TS geometry for z-alignment
- **Produces:** `DetectorSolenoid`, `DetectorSolenoidShielding` detector objects registered with [[GeometryService]]

## Related
- [[GeomPrimitives]]
- [[Mu2eHallGeom]]
- [[ExternalShieldingGeom]]
- [[MBSGeom]]
- [[StoppingTargetGeom]]
- [[MECOStyleProtonAbsorberGeom]]
- [[ServicesGeom]]
