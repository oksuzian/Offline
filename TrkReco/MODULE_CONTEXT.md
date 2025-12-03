# TrkReco Module Context

## Overview

Reconstruction algorithms and modules for Trk

## Module Type

- **Type**: library+art_module

## Art Modules

- `MergeKalSeeds`
- `MergeHelices`
- `SelectReflections`
- `TrackMatching`
- `TrackResolution`
- `SelectSameTrack`
- `MergeHelices (EDProducer)`
- `SelectSameTrack (EDFilter)`
- `TrackResolution (EDProducer)`
- `TrackMatching (EDProducer)`
- `SelectReflections (EDFilter)`
- `MergeKalSeeds (EDProducer)`

## Dependencies

- `BFieldGeom`
- `BTrkData`
- `CalorimeterGeom`
- `ConditionsService`
- `DataProducts`
- `GeneralUtilities`
- `GeometryService`
- `Mu2eBTrk`
- `Mu2eUtilities`
- `ProditionsService`
- `RecoDataProducts`
- `StoppingTargetGeom`
- `TrackerConditions`
- `TrackerGeom`
- `TrkReco`

## Source Files

Key source files:
- `AmbigResolver.cc`
- `DoubletAmbigResolver.cc`
- `FixedAmbigResolver.cc`
- `HitAmbigResolver.cc`
- `KalFit.cc`
- `KalFitData.cc`
- `MergeHelices_module.cc`
- `MergeKalSeeds_module.cc`
- `PanelAmbigResolver.cc`
- `PanelAmbigStructs.cc`
- ... and 13 more

## Header Files

Key header files:
- `AmbigResolver.hh`
- `DoubletAmbigResolver.hh`
- `FixedAmbigResolver.hh`
- `HitAmbigResolver.hh`
- `KalFit.hh`
- `KalFitData.hh`
- `KalSeedSelector.hh`
- `PanelAmbigResolver.hh`
- `PanelAmbigStructs.hh`
- `PanelStateIterator.hh`
- ... and 8 more

## Structure

- Has FCL configuration files: Yes
- Has test directory: Yes
- Number of source files: 23
- Number of header files: 18

## Notes

*This context file was auto-generated. Please update with specific details about the module's purpose and usage.*
