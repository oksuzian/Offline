# GeomPrimitives

**Role:** Shared lightweight geometric shape classes (Tube, Cone, Box, Polycone, Torus, ...) reused across all geometry packages.

## Overview
Provides pure-data primitive classes that wrap CLHEP vectors and G4-style shape parameters without any Geant4 dependency. These primitives let higher-level detector geometry classes ([[DetectorSolenoidGeom]], [[MBSGeom]], [[Mu2eHallGeom]], etc.) describe volumes in a portable way; Mu2eG4 construction code then translates them into G4Solids at run time. This decouples geometry description from the Geant4 build.

## Key contents
- `Tube.hh`, `TubsParams.hh`, `PlacedTubs.hh` - cylindrical tubs
- `Polycone.hh`, `PolyconsParams.hh`, `Polyhedra.hh`, `PolyhedraParams.hh` - polycones/polyhedra
- `Box.hh`, `Cone.hh`, `Torus.hh`, `TorusParams.hh` - basic solids
- `ExtrudedSolid.hh`, `RotExtrudedSolid.hh`, `GenericTrap.hh` - extrusions / traps
- `Hole.hh`, `Notch.hh` - subtraction helpers
- Depends only on CLHEP, Boost, cetlib_except

## Inputs / Outputs
- **Consumes:** none (pure headers/classes)
- **Produces:** reusable shape classes linked by virtually every `*Geom` library

## Related
- [[DetectorSolenoidGeom]]
- [[ExternalShieldingGeom]]
- [[MBSGeom]]
- [[MECOStyleProtonAbsorberGeom]]
- [[Mu2eHallGeom]]
- [[ServicesGeom]]
- [[StoppingTargetGeom]]
