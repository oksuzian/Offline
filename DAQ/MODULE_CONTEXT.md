# DAQ Module Context

## Overview

Module for DAQ functionality

## Module Type

- **Type**: library+art_module

## Art Modules

- `ArtBinaryPacketsFromDigis`
- `EventHeaderFromCFOFragment`
- `CaloHitsFromDTCEvents`
- `CaloDigisFromDTCEvents`
- `DummyLumiInfoProducer`
- `LumiInfoAna`
- `LumiStreamFilter`
- `PrefetchDAQData`
- `STMWaveformDigisFromFragments`
- `StrawDigisFromArtdaqFragments`
- `StrawHitFilter`
- `StrawDigiFilter`
- `CrvDigisFromArtdaqFragments`
- `CrvDigisFromArtdaqFragmentsFEBII`
- `CrvGRdataFromArtdaqFragments`
- `MTPHitsFromDTCEvents`
- `CrvDigisFromArtdaqFragments (EDProducer)`
- `ArtBinaryPacketsFromDigis (EDProducer)`
- `CrvDigisFromArtdaqFragmentsFEBII (EDProducer)`
- `CrvGRdataFromArtdaqFragments (EDProducer)`
- `LumiInfoAna (EDAnalyzer)`
- `StrawHitFilter (EDFilter)`
- `PrefetchDAQData (EDProducer)`
- `LumiStreamFilter (EDFilter)`
- `DummyLumiInfoProducer (EDProducer)`
- `StrawDigiFilter (EDFilter)`

## Dependencies

- `CRVConditions`
- `CaloConditions`
- `CalorimeterGeom`
- `CosmicRayShieldGeom`
- `DAQ`
- `DataProducts`
- `GeometryService`
- `ProditionsService`
- `RecoDataProducts`
- `SeedService`

## Source Files

Key source files:
- `ArtBinaryPacketsFromDigis_module.cc`
- `CaloDAQUtilities.cc`
- `CaloDigisFromDTCEvents_module.cc`
- `CaloHitsFromDTCEvents_module.cc`
- `CrvDigisFromArtdaqFragmentsFEBII_module.cc`
- `CrvDigisFromArtdaqFragments_module.cc`
- `CrvGRdataFromArtdaqFragments_module.cc`
- `DummyLumiInfoProducer_module.cc`
- `EventHeaderFromCFOFragment_module.cc`
- `LumiInfoAna_module.cc`
- ... and 7 more

## Header Files

Key header files:
- `CaloDAQUtilities.hh`

## Structure

- Has FCL configuration files: Yes
- Has test directory: Yes
- Number of source files: 17
- Number of header files: 1

## Notes

*This context file was auto-generated. Please update with specific details about the module's purpose and usage.*
