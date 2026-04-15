# HelloWorld

**Role:** Minimal tutorial modules demonstrating how to write the simplest possible art producer and analyzer in Mu2e Offline.

## Overview
Pedagogical package used by newcomers as their first Mu2e-on-art example. The three modules do nothing physics-relevant; they exist to show the boilerplate of an art `EDAnalyzer` / `EDProducer`, fhicl configuration tables, and how to drive a job from a tiny fcl file.

## Key contents
- `src/HelloWorld_module.cc`, `HelloWorld2_module.cc` — analyzers that print a greeting per event
- `src/HelloProducer_module.cc` — trivial producer example
- `test/hello.fcl`, `tableExample.fcl`, `prolog.fcl`, `erase.fcl` — runnable fcl demos

## Inputs / Outputs
- **Consumes:** `EmptyEvent` source (no real inputs)
- **Produces:** stdout messages; no persistent data products

## Example usage
```
mu2e -c Offline/HelloWorld/test/hello.fcl
```

## Related
- [[TestTools]]
