# CosmicReco

**Role:** Straight-line (cosmic-ray) track reconstruction in the tracker, used for alignment, calibration, and cosmic-veto studies.

## Overview
CosmicReco finds and fits near-straight tracks produced by cosmic muons traversing the tracker when there is no magnetic bending hypothesis. It clusters tracker hits in time, seeds a line fit, then refines with a drift-aware Minuit fit including a PDF likelihood. Outputs feed alignment, timing calibration, and cosmic-veto cross-checks against [[CRVReco]].

## Key contents
- `CosmicTrackFinder_module.cc`, `LineFinder_module.cc` — seed finding and straight-line pattern recognition
- `CosmicTrackFit` / `MinuitDriftFitter` / `PDFFit` — drift-time aware line fit infrastructure
- `DriftFitUtils` — geometry/drift helpers shared by the fitters
- `SimpleTimeCluster_module.cc` — simple time-based hit clustering for cosmics
- `CosmicSeedFilter_module.cc`, `CosmicShowerFilter_module.cc` — trigger/analysis filters on cosmic seeds
- `CosmicTrackDiag_module.cc`, `CosmicFitDisplay_module.cc` — diagnostics and event-display hooks

## Inputs / Outputs
- **Consumes:** `ComboHitCollection`, `StrawDigiMCCollection`, tracker geometry, `StrawResponse` conditions
- **Produces:** `CosmicTrackSeedCollection`, filter decisions, diagnostic ntuples/histograms

## Example usage
```
physics.producers.LineFinder : @local::CosmicReco.LineFinder
physics.producers.CosmicTrackFinder : @local::CosmicReco.CosmicTrackFinder
```

## Related
- [[TrkHitReco]] — upstream hit/ComboHit producer
- [[TrkReco]] — shared utilities (e.g. RobustHelixFit ecosystem)
- [[Mu2eKinKal]] — curved-track counterpart
- [[CRVReco]] — cosmic-ray-veto cross-checks
