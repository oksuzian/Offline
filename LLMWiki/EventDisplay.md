# EventDisplay

**Role:** Interactive ROOT/TGeo-based graphical event display for Mu2e events (tracker, calorimeter, CRV, virtual detectors and MC truth).

## Overview
The EventDisplay is an art analyzer that opens a GUI window (built on ROOT's TGFrame / TEve) and draws the detector geometry together with hits, clusters, tracks, and MC trajectories for each event. It supports the standard detector configurations (MDC2020, Run1/Run1a/Run1b, Run2) plus the CRV wideband and extracted-position test-beam geometries via dedicated top-level fcl files. Content selection and a save-dialog let users filter which collections to draw and snapshot views to file.

## Key contents
- `src/EventDisplay_module.cc` — art analyzer entry point; bridges art event data to the display
- `src/EventDisplayFrame.{h,cc}` — main GUI frame (menus, view controls, navigation)
- `src/DataInterface.{h,cc}`, `ContentSelector.{h,cc}` — adapt art collections to drawable objects
- `src/Track.h`, `Straw.h`, `Cylinder.h`, `Cone.h`, `Hexagon.h`, `Sphere.h`, `Cube.h`, `VirtualShape.h` — drawable primitive wrappers
- `src/dict_classes/` — ROOT dictionary classes (component info, TGeo volumes, hist-draw helpers)
- `fcl/EventDisplay{MDC2020,Run1,Run2,Wideband...}.fcl` — per-campaign / per-configuration driver files

## Inputs / Outputs
- **Consumes:** `RootInput` art files with hits, clusters, KalSeeds, CRV coincidences, SimParticles, StepPointMCs; geometry via `GeometryService`; CRV calibration via Proditions
- **Produces:** interactive GUI display; optional ROOT snapshot files of views

## Example usage
```
mu2e -c Offline/EventDisplay/fcl/EventDisplayMDC2020.fcl -s reco.art
```

## Related
- [[GeometryService]]
- [[RecoDataProducts]]
- [[MCDataProducts]]
- [[CaloVisualizer]]
- [[Analyses]]
