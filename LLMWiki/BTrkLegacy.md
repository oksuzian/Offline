# BTrkLegacy

**Role:** Minimal legacy shim preserving a handful of BaBar-track (BTrk) types still referenced by older Mu2e code.

## Overview
This folder is a deprecated compatibility layer left from the BaBar Kalman filter era. It only keeps the small header/class surface (particle id, T0, helix parameters, error codes) that legacy consumers still link against, now that tracking has migrated to [[Mu2eKinKal]]. New code should not depend on it.

## Key contents
- `inc/TrkParticle.hh`, `src/TrkParticle.cc` — particle-type enum used by old track classes
- `inc/TrkT0.hh` — track T0 (time-zero) struct
- `inc/HelixParams.hh` — legacy 5-parameter helix representation
- `inc/TrkErrCode.hh`, `src/TrkErrCode.cc` — error-code utility carried over from BTrk

## Inputs / Outputs
- **Consumes:** nothing directly; header-only types
- **Produces:** a small static library linked by legacy reconstruction/analysis code

## Related
- [[Mu2eKinKal]] — modern replacement for BaBar Kalman tracking
- [[KalmanTests]] — legacy test/plot macros tied to this era
- [[TrkReco]]
