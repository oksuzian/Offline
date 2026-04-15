# ConfigTools

**Role:** Lightweight configuration-file library used by Mu2e code that predates (or sits outside of) the art `fhicl` ecosystem.

## Overview
ConfigTools provides `SimpleConfig`, a key/value text-configuration parser historically used for geometry and other non-fcl configuration files, along with a `ConfigFileLookupPolicy` that finds config files via the standard Mu2e search path. It also offers utility helpers for detecting stale configuration and enforcing unique keys. Most modern code uses fhicl instead, but geometry and some legacy subsystems still rely on these utilities.

## Key contents
- `SimpleConfig` / `SimpleConfigRecord` - the core text-config parser.
- `ConfigFileLookupPolicy` - wraps the Mu2e include-path search.
- `checkForStale`, `requireUniqueKey` - sanity-check helpers.

## Inputs / Outputs
- **Consumes:** plain-text `.txt` configuration files living alongside subsystem data (notably in `*Geom` and `GlobalConstantsService`).
- **Produces:** a linkable library (`Offline::ConfigTools`) consumed by geometry and conditions code.

## Related
- [[GeneralUtilities]]
- [[GeometryService]]
- [[GlobalConstantsService]]
- [[fcl]]
