# STMConditions

**Role:** Proditions (run-dependent conditions) for converting STM digis to calibrated energies.

## Overview
STMConditions provides the Prodition entity `STMEnergyCalib`, which carries per-channel pedestals, sampling frequencies, and energy-correction parameters for the HPGe and LaBr3 STM detectors. The maker loads values either from the conditions database or from fcl (`useDb : false`) and caches them per IOV. It is consumed by STM waveform/hit reconstruction modules to convert ADC counts to energy and ticks to time.

## Key contents
- `STMEnergyCalib.hh` - Prodition entity (pedestal, sampling freq, calibration map per `STMChannel`)
- `STMEnergyCalibMaker.hh/.cc` - builds the entity from fcl or database
- `STMEnergyCalibCache.hh` - IOV cache wrapper
- `STMEnergyCorr.hh` - per-channel energy correction struct
- `fcl/prolog.fcl` - default HPGe/LaBr pedestals and sampling rates (320 / 370.37 MHz)

## Inputs / Outputs
- **Consumes:** fcl stanza `STMEnergyCalib` (see [[STMConfig]]), or DbTables rows when `useDb : true`
- **Produces:** `STMEnergyCalib` Prodition consumed by [[STMReco]] modules

## Example usage
```
services.ProditionsService.stmEnergyCalib : @local::STMEnergyCalib
```

## Related
- [[STMConfig]] - fcl schema struct
- [[STMReco]] - main consumer
- [[ProditionsService]], [[DbService]], [[DbTables]]
