# Sources

**Role:** Custom art input source modules that turn non-art external files (CORSIKA, MARS, STM test-beam, tracker-prototype, PBI text lists) into art Events.

## Overview
"Sources" here means art `_source.cc` modules, not source code generally. Each file under `src/` implements an art input source that reads an external (usually binary or text) data format, unpacks it, and produces standard Mu2e MC or raw data products event-by-event. They are the bridge between upstream simulation/DAQ tooling and the Offline art chain, and typically run as the very first job in a processing pipeline.

## Key contents
- `src/FromCorsikaBinary_source.cc` + `CosmicCORSIKA.{hh,cc}` — reads CORSIKA cosmic-ray shower binaries into `GenParticle`s
- `src/FromEMFMARSFileWeighted_source.cc`, `FromExtMonFNALMARSFile_source.cc` + `ExtMonFNALMARSUtils.{hh,cc}` — ExtMonFNAL MARS flux files
- `src/FromSTMTestBeamData_source.cc` + `STMTestBeamHeaders.{hh,cc}`, `STMTestBeamFileNameDecoder.{hh,cc}` — STM test-beam raw data
- `src/FromTrackerPrototypeData_source.cc` — tracker prototype bench data
- `src/PBISequence_source.cc` — reads a text sequence of proton-bunch-intensities and emits events with matching `ProtonBunchIntensity` products
- `test/` — runnable fcl examples for each source

## Inputs / Outputs
- **Consumes:** external files (CORSIKA `.bin`, MARS text/binary, STM test-beam, PBI sequence text)
- **Produces:** `GenParticleCollection`, `StepPointMCCollection`, `ProtonBunchIntensity` / `ProtonBunchIntensitySummary`, raw STM waveforms, tracker prototype hits

## Example usage
```
mu2e -c Offline/Sources/test/PBISequence.fcl
```

## Related
- [[EventGenerator]]
- [[ExtinctionMonitorFNAL]]
- [[STMMC]]
- [[CommonMC]]
- [[DAQ]]
