# CaloConditions

**Role:** Proditions (run-dependent conditions) providers for calorimeter calibrations and DAQ channel mapping.

## Overview
Wraps database-backed calibration constants (gains, timing offsets, energy scale) and the offline/DAQ channel map into cached Proditions objects consumable by reco modules. Works together with the calorimeter DbTables and [[DbService]] to deliver per-run constants to [[CaloReco]] and friends.

## Key contents
- `CalCalib` / `CalCalibMaker` / `CalCalibCache` — per-channel ADC-to-MeV and timing calibration Prodition
- `CalCalibPar`, `CalCombinedEnergyCalibStatus` — underlying parameter containers
- `CaloDAQMap` / `CaloDAQMapMaker` / `CaloDAQMapCache` — online-to-offline channel mapping Prodition
- `data/nominal.txt`, `data/caloDMAP_nominal.dat` — default constants shipped with the release
- `fcl/prolog.fcl` — `calCalib` and `CaloDAQConditions` defaults (`useDb`, `ADC2MeV`, etc.)

## Inputs / Outputs
- **Consumes:** [[DbService]] / [[DbTables]] conditions payloads, fallback text files under `data/`
- **Produces:** `CalCalib`, `CaloDAQMap` Proditions handles registered via [[ProditionsService]]

## Related
- [[CaloConfig]] — matching fhicl ConfigTools structs
- [[CaloReco]] — primary consumer (digi calibration)
- [[DAQConditions]], [[DbService]], [[DbTables]]
