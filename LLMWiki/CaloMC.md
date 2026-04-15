# CaloMC

**Role:** Calorimeter simulation chain — from Geant4 shower steps, through readout digitisation, to MC-truth matching of reco products.

## Overview
Converts Geant4 `StepPointMC`s inside the calorimeter into compressed `CaloShowerStep`s, then through the SiPM/readout model into `CaloDigi`s with realistic noise and pulse shapes. Also provides the truth-matching modules that link reco hits/clusters back to `SimParticle`s. Sits between [[Mu2eG4]] and [[CaloReco]] in the simulation data flow.

## Key contents
- `CaloShowerStepMaker_module` — compresses Geant4 calo steps (Z-slices, time grouping)
- `CaloShowerROMaker_module` — applies SiPM readout response (photoelectrons, timing)
- `CaloShowerUpdater_module` — propagates MC weights after event mixing
- `CaloDigiMaker_module` — builds `CaloDigiCollection` with `CaloNoiseSimGenerator` and `CaloPhotonPropagation`
- `CaloHitTruthMatch_module`, `CaloClusterTruthMatch_module` — link reco hits/clusters to truth
- `fcl/prolog.fcl` — producer definitions and the MC reco sequence

## Inputs / Outputs
- **Consumes:** `StepPointMCCollection("g4run:calorimeter")`, physical volume info, [[DAQConditions]] / [[ProditionsService]]
- **Produces:** `CaloShowerStepCollection`, `CaloShowerROCollection`, `CaloDigiCollection`, `CaloHitMCTruthAssn`, `CaloClusterMCTruthAssn`

## Example usage
```
mu2e -c Offline/CaloMC/test/RunCaloCalibGun.fcl
```

## Related
- [[Mu2eG4]] — source of step points
- [[CaloReco]], [[CaloCluster]] — downstream reco consumers
- [[CalorimeterGeom]], [[DAQConditions]]
