# Bugs and Issues Found in Codebase

## Critical Memory Leaks

### 1. Memory Leak in `CRVResponse/src/CrvWidebandTest_module.cc`

**Location:** Lines 241-246 (destructor)

**Issue:** The destructor only deletes 3 arrays, but the class allocates 17 arrays with `new[]`. This causes memory leaks for 14 arrays.

**Missing cleanup for:**
- `_recoTime` (allocated line 337)
- `_fitStatus` (allocated line 338)
- `_coincidenceTime` (allocated line 341)
- `_coincidencePosX` (allocated line 342)
- `_coincidencePosY` (allocated line 343)
- `_coincidencePosZ` (allocated line 344)
- `_trackSlope` (allocated line 346)
- `_trackIntercept` (allocated line 347)
- `_trackPoints` (allocated line 348)
- `_trackPEs` (allocated line 349)
- `_trackChi2` (allocated line 350)
- `_summaryPEs` (allocated line 254)
- `_summaryFWHMs` (allocated line 255)
- `_summarySignals` (allocated line 256)
- `_summaryChi2s` (allocated line 257)

**Current destructor:**
```cpp
CrvWidebandTest::~CrvWidebandTest()
{
  delete[] _recoPEs;
  delete[] _depositedEnergy;
  delete[] _coincidencePDGid;
}
```

**Fix:** Add `delete[]` statements for all allocated arrays, or better yet, use smart pointers or std::vector.

---

### 2. Missing Destructor in `CosmicReco/inc/PDFFit.hh` - `FullDriftFit` class

**Location:** `FullDriftFit` class

**Issue:** The `FullDriftFit` class allocates memory with `new[]` in its constructor (lines 63-66 in PDFFit.cc):
- `pdf_times = new double[N_tbins];`
- `pdf_taus = new double[N_taubins];`
- `pdf_sigmas = new double[N_sbins];`
- `pdf = new double[N_tbins * N_taubins * N_sbins];`

However, the class has no destructor. Memory cleanup relies on manually calling `DeleteArrays()` method, which is error-prone and violates RAII principles.

**Current cleanup:** Manual call to `DeleteArrays()` in `MinuitDriftFitter.cc` line 211.

**Risk:** If `DeleteArrays()` is not called, or if an exception is thrown before it's called, memory will leak.

**Fix:** Add a destructor to `FullDriftFit` that calls `DeleteArrays()`, or better yet, use `std::vector` or smart pointers.

---

## Potential Issues

### 3. Unsafe `sprintf` Usage

**Location:** Multiple files in `Validation/root/` directory

**Issue:** Uses `sprintf` without buffer size checking. While buffers appear to be sized appropriately (e.g., `char tstring[200]`), this is still unsafe and could lead to buffer overflows if format strings change.

**Files affected:**
- `TValHist2.cc`
- `TValHistH.cc`
- `TValHistP.cc`
- `TValHistE.cc`

**Recommendation:** Replace `sprintf` with `snprintf` for safer string formatting.

---

### 4. Unsafe `strcpy` Usage

**Location:** `CalPatRec/src/CalHelixFinderAlg.cc` line 2168

**Issue:** Uses `strcpy` without explicit length checking. While the destination buffer `banner[200]` is large enough for the source string "refineHelixParameters", this is still unsafe.

**Current code:**
```cpp
char banner[200];
// ...
strcpy(banner,"refineHelixParameters");
```

**Recommendation:** Use `strncpy` with explicit length or `std::string`.

---

## Summary

- **2 Critical Memory Leaks** requiring immediate attention
- **2 Potential Security/Stability Issues** with unsafe string operations

The memory leaks are the most critical issues as they will cause the application to consume increasing amounts of memory over time, potentially leading to crashes or system instability.
