# DataProducts

**Role:** Lightweight, detector-agnostic identifier, enum, and utility classes shared by every subsystem's data products.

## Overview
DataProducts is the lowest level in the Mu2e data-product stack: the "vocabulary" used by [[MCDataProducts]], [[RecoDataProducts]], geometry, and conditions to name channels, particles, and surfaces. It has no art dependencies and only light ROOT math dependencies, so it can be reused freely by analysis and python bindings. Every reco, MC, and conditions package links against it.

## Key contents
- Tracker IDs: `StrawId`, `StrawEnd`, `PanelId`, `PlaneId`, `LayerId`, `StrawIdMask`, `StrawStatus`, `TrkTypes`
- Calorimeter IDs: `CrystalId`, `CaloSiPMId`, `CaloRawSiPMId`, `CaloConst`
- CRV / ExtMon / STM IDs: `CRVId`, `CRSScintillatorBarIndex`, `ExtMonFNAL*Id`, `STMChannel`
- Particle & physics enums: `PDGCode`, `CompressedPDGCode`, `Helicity`, `VirtualDetectorId`
- Geometry math helpers: `GenVector`, `SurfaceId`, `IndexMap`, `AHist`, `MVAMask`
- Filter bookkeeping: `FilterFraction`, `PrescaleFilterFraction`, `EventWindowMarker`

## Inputs / Outputs
- **Consumes:** GeneralUtilities only; no art/conditions dependencies
- **Produces:** Header-only/value classes with ROOT dictionaries; optional Python (SWIG) bindings

## Related
- [[MCDataProducts]]
- [[RecoDataProducts]]
- [[GeometryService]]
- [[TrackerGeom]]
- [[CalorimeterGeom]]
- [[GeneralUtilities]]
