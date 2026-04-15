# ProtonBeamDumpGeom

**Role:** Geometry description of the proton beam dump sitting upstream of the Mu2e hall, including its core, shielding, and orientation.

## Overview
Defines the `ProtonBeamDump` data class: core block center and rotation in the Mu2e frame plus dimensional parameters needed to position the dump relative to the hall and the extinction monitor. Because the dump is embedded in the hall structure, this package links against `Mu2eHallGeom` (rather than `GeomPrimitives`) so the dump can be placed consistently with surrounding concrete. Populated by a Maker in [[GeometryService]].

## Key contents
- `ProtonBeamDump.hh` / `ProtonBeamDump.cc` - core center, rotation, and dimensions of the beam dump.

## Inputs / Outputs
- **Consumes:** SimpleConfig parameters (via the Maker in [[GeometryService]]); `Mu2eHall` geometry for placement context.
- **Produces:** `ProtonBeamDump` Detector served through [[GeometryService]]; consumed by G4 construction and by [[ExtinctionMonitorFNAL]] for placement.

## Related
- [[GeometryService]]
- [[GeomPrimitives]]
- [[ExtinctionMonitorFNAL]]
- [[ProductionTargetGeom]]
