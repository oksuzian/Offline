# TrackerConditions

**Role:** Proditions entities describing time-varying tracker state: alignment, status, straw electronics, physics, drift, and response.

## Overview
TrackerConditions provides the conditions objects ("Proditions") consumed by every tracker reco and MC step: aligned geometry, dead/noisy straw status, straw electronics response, ionization/drift physics, and end-to-end `StrawResponse`. Each entity follows the Mu2e `*Cache` / `*Maker` pattern so that inputs can come from fcl, text files, or the database. These conditions are the calibration substrate under [[TrackerGeom]], [[TrkHitReco]], [[TrackerMC]], and [[Mu2eKinKal]].

## Key contents
- `AlignedTracker{Maker,Cache}` — aligned tracker geometry Prodition
- `TrackerStatus{Maker,Cache}` — per-straw dead/noisy flags
- `StrawElectronics{Maker,Cache}` — preamp/ADC/TDC response
- `StrawPhysics{Maker,Cache}` — gas physics and cluster generation parameters
- `StrawDrift{Maker,Cache}` — drift-time-to-distance tables (`data/E2v.tbl`)
- `StrawResponse{Maker,Cache}` — unified response model used by hit reco and digitization
- `FullReadoutStraw`, `TrackerPanelMap`, `StrawTension`, `DriftInfo` — auxiliary conditions
- `data/` — material lists, alignment files, drift spline, panel map

## Inputs / Outputs
- **Consumes:** `ProditionsService`, `GeometryService`, configs from [[TrackerConfig]], files under `data/`, DB tables
- **Produces:** Prodition handles: `AlignedTracker`, `TrackerStatus`, `StrawResponse`, `StrawElectronics`, `StrawPhysics`, `StrawDrift`, `TrackerPanelMap`, `FullReadoutStraw`

## Example usage
```
#include "Offline/TrackerConditions/fcl/prolog.fcl"
services.ProditionsService.strawResponse : @local::StrawResponseMaker
```

## Related
- [[TrackerConfig]] — fhicl-level configuration structs
- [[TrackerGeom]] — baseline geometry
- [[TrackerMC]], [[TrkHitReco]], [[Mu2eKinKal]] — main consumers
