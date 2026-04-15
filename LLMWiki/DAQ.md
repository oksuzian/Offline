# DAQ

**Role:** Unpack raw DTC/artdaq fragments into offline digi data products, and package digis back into fragments for emulation.

## Overview
DAQ sits at the boundary between online readout and offline reconstruction. Its producers translate `artdaq::Fragment`s and DTC events emitted by the Mu2e trigger DAQ into per-subdetector digi collections (tracker straws, calorimeter, CRV, STM, MSD) consumed by each subsystem's reco chain. Complementary modules convert digis back into binary fragments for DAQ emulation and testbench workflows, plus filters for lumi, occupancy, and prefetching.

## Key contents
- `StrawDigisFromArtdaqFragments_module.cc`, `StrawDigisToFragments_module.cc`, `StrawDigiFilter_module.cc`, `StrawHitFilter_module.cc`
- `CaloDigisFromDTCEvents_module.cc`, `CaloHitsFromDTCEvents_module.cc`, `CaloDigisToFragments_module.cc`, `CaloDAQUtilities`
- `CrvDigisFromArtdaqFragments_module.cc` (+ FEBII variant), `CrvGRdataFromArtdaqFragments_module.cc`
- `STMWaveformDigisFromFragments_module.cc`, `MSDHitsFromDTCEvents_module.cc`
- `ArtBinaryPacketsFromDigis_module.cc`, `EventHeaderFromCFOFragment_module.cc`, `PrefetchDAQData_module.cc`
- `LumiStreamFilter`, `LumiInfoAna`, `OccupancyFilter`, collection comparators

## Inputs / Outputs
- **Consumes:** `artdaq::Fragment` collections, DTC event blobs, `CFOFragment`, panel-map conditions
- **Produces:** `StrawDigiCollection`, `CaloDigiCollection`/`CaloHitCollection`, `CrvDigiCollection`, `STMWaveformDigiCollection`, `MSDHitCollection`, `Mu2eEventHeader`, binary fragment outputs

## Example usage
```
mu2e -c Offline/DAQ/test/generateDigiFromFragment.fcl -s raw.art
mu2e -c Offline/DAQ/test/inspectSTMFile.fcl
mu2e -c Offline/DAQ/test/digi_to_frag.fcl
```

## Related
- [[DAQConditions]], [[DAQConfig]] - event-timing proditions and schema
- [[RecoDataProducts]] - target digi/hit data products
- [[TrkHitReco]], [[TrackerMC]] - consumers of `StrawDigi`s
- [[CaloReco]], [[CaloMC]] - consumers of calo digis
- [[CRVReco]] - consumer of CRV digis
- [[STMReco]] - consumer of `STMWaveformDigi`s from fragments
