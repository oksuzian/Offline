# BeamlineGeom

**Role:** Geometry description for the Mu2e beamline, primarily the Transport Solenoid (TS) and its internal collimators, coils, and windows.

## Overview
Provides the "dumb data" classes that represent the straight, torus, and cone sections of the Transport Solenoid, the TS1/TS3/TS5 collimators, pbar windows, and the TS degrader (TSdA). These objects are populated by a corresponding Maker in [[GeometryService]] from SimpleConfig and then handed out via `GeomHandle<Beamline>` so that G4 construction, field evaluation, and analysis code all share one consistent description.

## Key contents
- `Beamline.hh` - top-level container holding a `TransportSolenoid` and the overall solenoid offset.
- `TransportSolenoid.hh`, `TSSection.hh`, `StraightSection.hh`, `TorusSection.hh`, `ConeSection.hh` - TS segment primitives.
- `Collimator.hh` and `Collimator_TS1/3/5.hh` - collimator descriptions in the TS.
- `Coil.hh`, `PbarWindow.hh`, `TSdA.hh` - superconducting coils, pbar absorber windows, TS antiproton degrader.

## Inputs / Outputs
- **Consumes:** SimpleConfig geometry parameters (read by the Maker in [[GeometryService]]); [[GeomPrimitives]] shape classes.
- **Produces:** `Beamline` Detector object served through [[GeometryService]]; used by G4 construction, [[BFieldGeom]] region placement, and downstream reco/analysis.

## Related
- [[GeometryService]]
- [[GeomPrimitives]]
- [[BFieldGeom]]
- [[ProductionSolenoidGeom]]
