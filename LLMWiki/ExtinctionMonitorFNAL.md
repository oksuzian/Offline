# ExtinctionMonitorFNAL

**Role:** Full subsystem package for the FNAL Extinction Monitor (ExtMonFNAL) pixel telescope: geometry, digitization, reconstruction, analyses, and truth helpers.

## Overview
ExtMonFNAL measures the proton beam extinction by tracking scattered protons downstream of the production target. Unlike the other folders in this cluster, this package is not purely a geometry description - it contains the complete offline chain for the detector: geometry classes served through [[GeometryService]], a Geant4-hit-to-pixel-digitization step, raw/reco clusterization, tracklet + track reconstruction, MC-truth algorithms, analyses, and shared utilities. FHiCL prologs wire the pieces together for standard production jobs.

## Key contents
- `Geometry/` - `ExtMonFNAL`, `ExtMonFNALBuilding`, `ExtMonFNALMagnet`, `ExtMonFNALPlane(Stack)`, `ExtMonFNALModule`, pixel chip + ID converters.
- `Digitization/` - `ExtMonFNALHitMaker` and pixel-response modules that produce pixel digis from G4 steps.
- `Reconstruction/` - raw/reco clusterization, `Tracklet`, `TrackExtrapolator`, `LinearRegression`, `PixelHitLookup`.
- `TruthAlgs/`, `Analyses/`, `ComponentTests/`, `Utilities/` - MC truth association, analysis modules, component unit tests, helpers.
- `fcl/prolog.fcl` - standard producer configurations (`pixelDigitization`, `pixelRawClusterization`, `pixelRecoClusterization`, ...).

## Inputs / Outputs
- **Consumes:** G4 step/hit collections (`g4run`), `ExtMonFNAL` geometry via [[GeometryService]], conditions, FHiCL (`prolog.fcl`).
- **Produces:** pixel digis, raw and reco pixel clusters, tracklets and extrapolated tracks, MC-truth matches, analysis ntuples.

## Example usage
```
#include "Offline/ExtinctionMonitorFNAL/fcl/prolog.fcl"
physics.producers.pixelDigitization        : @local::pixelDigitization
physics.producers.pixelRawClusterization   : @local::pixelRawClusterization
physics.producers.pixelRecoClusterization  : @local::pixelRecoClusterization
```

## Related
- [[GeometryService]]
- [[GeomPrimitives]]
- [[ProtonBeamDumpGeom]]
- [[ProductionTargetGeom]]
