# Mu2eKinKal

**Role:** Mu2e adapter and modules for the external KinKal Kalman-fit library — the production track fitter.

## Overview
Mu2eKinKal wraps KinKal's templated trajectory fitter with Mu2e-specific hits, materials, B-field, and calorimeter association, then drives it from art modules (`LoopHelixFit`, `KinematicLineFit`, `CentralHelixFit`). It consumes helix/line seeds from [[TrkPatRec]]/[[CalPatRec]] and [[TrkReco]], performs iterative straw-hit ambiguity resolution, material correction, and extrapolation to surfaces from [[KinKalGeom]], producing the final `KalSeedCollection` used downstream.

## Key contents
- `LoopHelixFit_module.cc`, `KinematicLineFit_module.cc`, `CentralHelixFit_module.cc` — fitter driver modules
- `RegrowLoopHelix_module.cc`, `RegrowKinematicLine_module.cc` — refit/regrow modules
- `KKTrack`, `KKFit`, `KKStrawHit`, `KKStrawXing`, `KKCaloHit` — Mu2e-KinKal hit/material/track adapters
- `KKBField`, `KKMaterial`, `KKStrawMaterial` — magnetic-field and material services
- `ExtrapolateToZ/IPA/ST/TCRV` — target-surface extrapolation policies
- `CADSHU`, `Chi2SHU`, `DriftANNSHU`, `BkgANNSHU` — straw-hit state updaters (ambiguity/drift/background ANN)

## Inputs / Outputs
- **Consumes:** `HelixSeedCollection`, `CosmicTrackSeedCollection`, `ComboHitCollection`, `CaloClusterCollection`, `StrawResponse`, `TrackerStatus`, `AlignedTracker`, B-field, MC weight files under `data/`
- **Produces:** `KalSeedCollection` (KinKal fits), `KalIntersectionCollection`, diagnostic trees

## Example usage
```
#include "Offline/Mu2eKinKal/fcl/prolog.fcl"
physics.producers.KKLoopHelix : @local::Mu2eKinKal.LoopHelixFit
```

## Related
- [[TrkHitReco]] → [[TrkPatRec]] / [[CalPatRec]] → [[TrkReco]] → [[Mu2eKinKal]]
- [[KinKalGeom]] — extrapolation surfaces
- [[TrackerConditions]], [[TrackerGeom]], [[TrackerConfig]]
- [[CaloCluster]] — calorimeter-cluster association for timing/anchoring
