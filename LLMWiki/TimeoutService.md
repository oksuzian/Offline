# TimeoutService

**Role:** art service providing cooperative per-event and per-module timeout budgets.

## Overview
`TimeoutWatchdog` tracks wall-clock deadlines for the current event and the currently executing module. Long-running algorithms poll `check()` or observe a `std::stop_token` to bail out gracefully when they exceed their budget. A `ModuleGuard` RAII helper pairs with `pre/postModule` boundaries so module authors only need to sprinkle cooperative check-points. Timeouts are disabled by default (`<= 0` budget).

## Key contents
- `TimeoutWatchdog.hh` - service, fhicl `Config`, `ModuleGuard` RAII helper
- `TimeoutWatchdog.cc`, `TimeoutWatchdog_service.cc` - implementation + art registration

## Inputs / Outputs
- **Consumes:** fcl `eventTimeoutMs`, `moduleTimeoutMs`, `registerPreEventCallback`, `debugLevel`
- **Produces:** `TimeoutWatchdog` art service exposing `check()` and a `std::stop_token` to client modules

## Example usage
```
services.TimeoutWatchdog : {
  eventTimeoutMs  : 30000
  moduleTimeoutMs : 10000
  debugLevel      : 1
}
```

## Related
- [[SeedService]]
