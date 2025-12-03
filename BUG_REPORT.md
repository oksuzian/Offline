# Bug Analysis Report

Total bugs found: 34179

## Summary by Severity

- **HIGH**: 22408 bugs
- **MEDIUM**: 11605 bugs
- **LOW**: 166 bugs

## Summary by Bug Type

- **array_bounds**: 10884 occurrences
- **assignment_in_condition**: 1265 occurrences
- **division_by_zero**: 17776 occurrences
- **memory_leak**: 2636 occurrences
- **missing_error_handling**: 360 occurrences
- **missing_return**: 333 occurrences
- **resource_leak**: 28 occurrences
- **uninitialized_variable**: 693 occurrences
- **unused_variable**: 166 occurrences
- **use_after_free**: 38 occurrences

## Detailed Report by Module

### Analyses

Found 4272 potential bugs:

#### array_bounds (1766 occurrences)

- **/workspace/Analyses/src/TSTrackAna_module.cc:251** - Array access _mapTrkDelta[id] without bounds check
- **/workspace/Analyses/src/TSTrackAna_module.cc:252** - Array access _mapTrkIntersection[id] without bounds check
- **/workspace/Analyses/src/TSTrackAna_module.cc:253** - Array access _mapTrkDelta[id] without bounds check
- **/workspace/Analyses/src/TSTrackAna_module.cc:266** - Array access _maph2YvsR[h2Id] without bounds check
- **/workspace/Analyses/src/CountVirtualDetectorHits_module.cc:78** - Array access counter[index] without bounds check
- **/workspace/Analyses/src/CountVirtualDetectorHits_module.cc:88** - Array access enabledVDs[i] without bounds check
- **/workspace/Analyses/src/ReadTrackerSteps_module.cc:206** - Array access nt[0] without bounds check
- **/workspace/Analyses/src/ReadTrackerSteps_module.cc:207** - Array access nt[1] without bounds check
- **/workspace/Analyses/src/ReadTrackerSteps_module.cc:208** - Array access nt[2] without bounds check
- **/workspace/Analyses/src/ReadTrackerSteps_module.cc:209** - Array access nt[3] without bounds check
- ... and 1756 more

#### assignment_in_condition (30 occurrences)

- **/workspace/Analyses/src/TSTrackAna_module.cc:206** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Analyses/src/TSTrackAna_module.cc:236** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Analyses/src/TSTrackAna_module.cc:248** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Analyses/src/TSTrackAna_module.cc:254** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Analyses/src/TSTrackAna_module.cc:277** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Analyses/src/TSTrackAna_module.cc:301** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Analyses/src/TSTrackAna_module.cc:321** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Analyses/src/TSTrackAna_module.cc:341** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Analyses/src/KineticFracAnalysis_module.cc:789** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Analyses/src/CaloHitFinderInspect_module.cc:217** - Possible assignment (=) instead of comparison (==) in condition
- ... and 20 more

#### division_by_zero (2230 occurrences)

- **/workspace/Analyses/src/TSTrackAna_module.cc:4** - Potential division by zero: 27 not checked
- **/workspace/Analyses/src/TSTrackAna_module.cc:12** - Potential division by zero: MCDataProducts not checked
- **/workspace/Analyses/src/TSTrackAna_module.cc:13** - Potential division by zero: MCDataProducts not checked
- **/workspace/Analyses/src/TSTrackAna_module.cc:14** - Potential division by zero: Framework not checked
- **/workspace/Analyses/src/TSTrackAna_module.cc:15** - Potential division by zero: Framework not checked
- **/workspace/Analyses/src/TSTrackAna_module.cc:16** - Potential division by zero: TFileService not checked
- **/workspace/Analyses/src/TSTrackAna_module.cc:17** - Potential division by zero: Framework not checked
- **/workspace/Analyses/src/TSTrackAna_module.cc:18** - Potential division by zero: ParameterSet not checked
- **/workspace/Analyses/src/TSTrackAna_module.cc:126** - Potential division by zero: _cutZStep not checked
- **/workspace/Analyses/src/TSTrackAna_module.cc:138** - Potential division by zero: _cutThetaStep not checked
- ... and 2220 more

#### memory_leak (52 occurrences)

- **/workspace/Analyses/src/TSTrackAna_module.cc:170** - Potential memory leak: new TGeoMaterial without corresponding delete
- **/workspace/Analyses/src/TSTrackAna_module.cc:171** - Potential memory leak: new TGeoMedium without corresponding delete
- **/workspace/Analyses/src/TSTrackAna_module.cc:190** - Potential memory leak: new TApplication without corresponding delete
- **/workspace/Analyses/src/TSTrackAna_module.cc:248** - Potential memory leak: new for without corresponding delete
- **/workspace/Analyses/src/KineticFracAnalysis_module.cc:616** - Potential memory leak: new TF1 without corresponding delete
- **/workspace/Analyses/src/KineticFracAnalysis_module.cc:628** - Potential memory leak: new TH2F without corresponding delete
- **/workspace/Analyses/src/KineticFracAnalysis_module.cc:634** - Potential memory leak: new TH2F without corresponding delete
- **/workspace/Analyses/src/KineticFracAnalysis_module.cc:655** - Potential memory leak: new event without corresponding delete
- **/workspace/Analyses/src/ReadPSVacuum_module.cc:63** - Potential memory leak: new float[1000] without corresponding delete
- **/workspace/Analyses/src/TrackSummaryTruthMaker_module.cc:53** - Potential memory leak: new SimParticlePtrCollection without corresponding delete
- ... and 42 more

#### missing_error_handling (33 occurrences)

- **/workspace/Analyses/src/StepPointsPrinter_module.cc:34** - getHandle/getValidHandle result not checked for validity
- **/workspace/Analyses/src/TrackSummaryMCAnalyzer_module.cc:72** - getHandle/getValidHandle result not checked for validity
- **/workspace/Analyses/src/TrackSummaryTruthMaker_module.cc:55** - getHandle/getValidHandle result not checked for validity
- **/workspace/Analyses/src/TrackSummaryTruthMaker_module.cc:56** - getHandle/getValidHandle result not checked for validity
- **/workspace/Analyses/src/TrackSummaryTruthRFSelector_module.cc:84** - getHandle/getValidHandle result not checked for validity
- **/workspace/Analyses/src/TrackSummaryDataAnalyzer_module.cc:52** - getHandle/getValidHandle result not checked for validity
- **/workspace/Analyses/src/StoppedParticlesDumper_module.cc:186** - getHandle/getValidHandle result not checked for validity
- **/workspace/Analyses/src/StoppedParticlesDumper_module.cc:200** - getHandle/getValidHandle result not checked for validity
- **/workspace/Analyses/src/PtrTest_module.cc:72** - getHandle/getValidHandle result not checked for validity
- **/workspace/Analyses/src/GeomVis_module.cc:232** - getHandle/getValidHandle result not checked for validity
- ... and 23 more

#### missing_return (17 occurrences)

- **/workspace/Analyses/src/SelectPiMinusAtTS5_module.cc:73** - Function may be missing return statement
- **/workspace/Analyses/src/ReadCaloDigi_module.cc:685** - Function may be missing return statement
- **/workspace/Analyses/src/VMMonitor_module.cc:59** - Function may be missing return statement
- **/workspace/Analyses/src/SensitiveTargetEnergyDumper_module.cc:340** - Function may be missing return statement
- **/workspace/Analyses/src/SensitiveTargetEnergyDumper_module.cc:347** - Function may be missing return statement
- **/workspace/Analyses/src/SensitiveTargetEnergyDumper_module.cc:354** - Function may be missing return statement
- **/workspace/Analyses/src/SensitiveTargetEnergyDumper_module.cc:361** - Function may be missing return statement
- **/workspace/Analyses/src/SensitiveTargetEnergyDumper_module.cc:368** - Function may be missing return statement
- **/workspace/Analyses/src/SensitiveTargetEnergyDumper_module.cc:375** - Function may be missing return statement
- **/workspace/Analyses/src/PrimaryProtonEnergyDumper_module.cc:300** - Function may be missing return statement
- ... and 7 more

#### resource_leak (4 occurrences)

- **/workspace/Analyses/src/PbarAnalysis2_module.cc:273** - File handle opened but may not be closed
- **/workspace/Analyses/src/BFieldPlotter_module.cc:212** - File handle opened but may not be closed
- **/workspace/Analyses/src/StoppedParticlesPrinter_module.cc:35** - File handle opened but may not be closed
- **/workspace/Analyses/src/MTVerification_module.cc:79** - File handle opened but may not be closed

#### uninitialized_variable (127 occurrences)

- **/workspace/Analyses/src/ReadTrackerSteps_module.cc:65** - Variable _nAnalyzed may be used uninitialized
- **/workspace/Analyses/src/ReadTrackerSteps_module.cc:66** - Variable _maxFullPrint may be used uninitialized
- **/workspace/Analyses/src/G4ReactionAnalyzer_module.cc:28** - Variable pdgId_ may be used uninitialized
- **/workspace/Analyses/src/CRYGenPlots_module.cc:129** - Variable success may be used uninitialized
- **/workspace/Analyses/src/TrackSummaryTruthMaker_module.cc:35** - Variable minPrincipalHits_ may be used uninitialized
- **/workspace/Analyses/src/TrackSummaryTruthMaker_module.cc:36** - Variable minAllHits_ may be used uninitialized
- **/workspace/Analyses/src/TrackSummaryTruthRFSelector_module.cc:45** - Variable cutMinCommonFraction_ may be used uninitialized
- **/workspace/Analyses/src/FilterEmptyEvents_module.cc:54** - Variable _diagLevel may be used uninitialized
- **/workspace/Analyses/src/FilterEmptyEvents_module.cc:55** - Variable _keepTrackOrCalo may be used uninitialized
- **/workspace/Analyses/src/SelectPiMinusAtTS5_module.cc:65** - Variable _storeParents may be used uninitialized
- ... and 117 more

#### unused_variable (11 occurrences)

- **/workspace/Analyses/src/DiskCal00_module.cc:249** - Variable dt declared but possibly unused
- **/workspace/Analyses/src/KineticFracAnalysis_module.cc:333** - Variable _tol declared but possibly unused
- **/workspace/Analyses/src/KineticFracAnalysis_module.cc:719** - Variable CrMass declared but possibly unused
- **/workspace/Analyses/src/KineticFracAnalysis_module.cc:985** - Variable rad2 declared but possibly unused
- **/workspace/Analyses/src/KineticFracAnalysis_module.cc:1062** - Variable timeDiff declared but possibly unused
- **/workspace/Analyses/src/KineticFracAnalysis_module.cc:1237** - Variable ithtrk declared but possibly unused
- **/workspace/Analyses/src/CaloHitFinderInspect_module.cc:279** - Variable i declared but possibly unused
- **/workspace/Analyses/src/CosmicAnalysis_module.cc:526** - Variable k declared but possibly unused
- **/workspace/Analyses/src/CaloCalibAna_module.cc:412** - Variable cog declared but possibly unused
- **/workspace/Analyses/src/MTVerification_module.cc:103** - Variable gens declared but possibly unused
- ... and 1 more

#### use_after_free (2 occurrences)

- **/workspace/Analyses/src/InteractiveRoot_module.cc:13** - Potential use after free: the deleted but may be used later
- **/workspace/Analyses/src/InteractiveRoot_module.cc:39** - Potential use after free: of deleted but may be used later


### BFieldGeom

Found 110 potential bugs:

#### array_bounds (69 occurrences)

- **/workspace/BFieldGeom/src/BFMapType.cc:42** - Array access _xname[i] without bounds check
- **/workspace/BFieldGeom/src/BFInterpolationStyle.cc:23** - Array access nam[unknown] without bounds check
- **/workspace/BFieldGeom/src/BFInterpolationStyle.cc:24** - Array access nam[unused] without bounds check
- **/workspace/BFieldGeom/src/BFInterpolationStyle.cc:25** - Array access nam[trilinear] without bounds check
- **/workspace/BFieldGeom/src/BFInterpolationStyle.cc:26** - Array access nam[fit] without bounds check
- **/workspace/BFieldGeom/src/BFParamMap.cc:74** - Array access bessels[2] without bounds check
- **/workspace/BFieldGeom/src/BFParamMap.cc:86** - Array access _kms[n] without bounds check
- **/workspace/BFieldGeom/src/BFParamMap.cc:87** - Array access bessels[0] without bounds check
- **/workspace/BFieldGeom/src/BFParamMap.cc:88** - Array access bessels[1] without bounds check
- **/workspace/BFieldGeom/src/BFParamMap.cc:89** - Array access _iv[n] without bounds check
- ... and 59 more

#### assignment_in_condition (1 occurrences)

- **/workspace/BFieldGeom/src/BFGridMap.cc:184** - Possible assignment (=) instead of comparison (==) in condition

#### division_by_zero (38 occurrences)

- **/workspace/BFieldGeom/src/BFMapType.cc:14** - Potential division by zero: BFieldGeom not checked
- **/workspace/BFieldGeom/src/BFMapType.cc:16** - Potential division by zero: static_assert not checked
- **/workspace/BFieldGeom/src/BFMapType.cc:39** - Potential division by zero: sizeof not checked
- **/workspace/BFieldGeom/src/BFInterpolationStyle.cc:9** - Potential division by zero: BFieldGeom not checked
- **/workspace/BFieldGeom/src/BFParamMap.cc:14** - Potential division by zero: MessageLogger not checked
- **/workspace/BFieldGeom/src/BFParamMap.cc:17** - Potential division by zero: BFieldGeom not checked
- **/workspace/BFieldGeom/src/BFParamMap.cc:20** - Potential division by zero: gsl_sf_bessel not checked
- **/workspace/BFieldGeom/src/BFParamMap.cc:21** - Potential division by zero: Vector not checked
- **/workspace/BFieldGeom/src/BFParamMap.cc:22** - Potential division by zero: exception not checked
- **/workspace/BFieldGeom/src/BFParamMap.cc:93** - Potential division by zero: tmp_rho not checked
- ... and 28 more

#### uninitialized_variable (1 occurrences)

- **/workspace/BFieldGeom/src/BFParamMap.cc:75** - Variable tmp_rho may be used uninitialized

#### unused_variable (1 occurrences)

- **/workspace/BFieldGeom/src/BFParamMap.cc:150** - Variable n declared but possibly unused


### BFieldTest

Found 45 potential bugs:

#### array_bounds (5 occurrences)

- **/workspace/BFieldTest/src/BFieldTest_module.cc:109** - Array access field[0] without bounds check
- **/workspace/BFieldTest/src/BFieldTest_module.cc:125** - Array access row[0] without bounds check
- **/workspace/BFieldTest/src/BFieldTest_module.cc:126** - Array access row[1] without bounds check
- **/workspace/BFieldTest/src/BFieldTest_module.cc:127** - Array access row[2] without bounds check
- **/workspace/BFieldTest/src/BFieldTest_module.cc:131** - Array access field[0] without bounds check

#### division_by_zero (21 occurrences)

- **/workspace/BFieldTest/src/BFieldSymmetry_module.cc:19** - Potential division by zero: BFieldGeom not checked
- **/workspace/BFieldTest/src/BFieldSymmetry_module.cc:20** - Potential division by zero: GeometryService not checked
- **/workspace/BFieldTest/src/BFieldSymmetry_module.cc:21** - Potential division by zero: SeedService not checked
- **/workspace/BFieldTest/src/BFieldSymmetry_module.cc:23** - Potential division by zero: Framework not checked
- **/workspace/BFieldTest/src/BFieldSymmetry_module.cc:24** - Potential division by zero: Framework not checked
- **/workspace/BFieldTest/src/BFieldSymmetry_module.cc:25** - Potential division by zero: Framework not checked
- **/workspace/BFieldTest/src/BFieldSymmetry_module.cc:26** - Potential division by zero: TFileDirectory not checked
- **/workspace/BFieldTest/src/BFieldSymmetry_module.cc:27** - Potential division by zero: TFileService not checked
- **/workspace/BFieldTest/src/BFieldSymmetry_module.cc:29** - Potential division by zero: Random not checked
- **/workspace/BFieldTest/src/BFieldSymmetry_module.cc:30** - Potential division by zero: Units not checked
- ... and 11 more

#### resource_leak (2 occurrences)

- **/workspace/BFieldTest/src/BFieldTest_module.cc:99** - File handle opened but may not be closed
- **/workspace/BFieldTest/src/BFieldTest_module.cc:119** - File handle opened but may not be closed

#### uninitialized_variable (16 occurrences)

- **/workspace/BFieldTest/src/BFieldSymmetry_module.cc:73** - Variable x may be used uninitialized
- **/workspace/BFieldTest/src/BFieldSymmetry_module.cc:74** - Variable y may be used uninitialized
- **/workspace/BFieldTest/src/BFieldSymmetry_module.cc:75** - Variable z may be used uninitialized
- **/workspace/BFieldTest/src/BFieldSymmetry_module.cc:76** - Variable bx1 may be used uninitialized
- **/workspace/BFieldTest/src/BFieldSymmetry_module.cc:77** - Variable by1 may be used uninitialized
- **/workspace/BFieldTest/src/BFieldSymmetry_module.cc:78** - Variable bz1 may be used uninitialized
- **/workspace/BFieldTest/src/BFieldSymmetry_module.cc:79** - Variable bx2 may be used uninitialized
- **/workspace/BFieldTest/src/BFieldSymmetry_module.cc:80** - Variable by2 may be used uninitialized
- **/workspace/BFieldTest/src/BFieldSymmetry_module.cc:81** - Variable bz2 may be used uninitialized
- **/workspace/BFieldTest/src/BFieldSymmetry_module.cc:185** - Variable nPoints_ may be used uninitialized
- ... and 6 more

#### unused_variable (1 occurrences)

- **/workspace/BFieldTest/src/BFieldSymmetry_module.cc:216** - Variable i declared but possibly unused


### BTrkData

Found 53 potential bugs:

#### array_bounds (12 occurrences)

- **/workspace/BTrkData/src/Doublet.cc:17** - Array access fStrawAmbig[i] without bounds check
- **/workspace/BTrkData/src/Doublet.cc:24** - Array access fHitIndex[0] without bounds check
- **/workspace/BTrkData/src/Doublet.cc:25** - Array access fHitIndex[1] without bounds check
- **/workspace/BTrkData/src/Doublet.cc:29** - Array access fDxDz[i] without bounds check
- **/workspace/BTrkData/src/Doublet.cc:30** - Array access fChi2[i] without bounds check
- **/workspace/BTrkData/src/Doublet.cc:55** - Array access fStrawAmbig[i] without bounds check
- **/workspace/BTrkData/src/Doublet.cc:62** - Array access fTrkDir[0] without bounds check
- **/workspace/BTrkData/src/Doublet.cc:63** - Array access fTrkPos[0] without bounds check
- **/workspace/BTrkData/src/Doublet.cc:66** - Array access fHitIndex[0] without bounds check
- **/workspace/BTrkData/src/Doublet.cc:67** - Array access fHitIndex[1] without bounds check
- ... and 2 more

#### assignment_in_condition (2 occurrences)

- **/workspace/BTrkData/src/TrkCaloHit.cc:151** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/BTrkData/src/TrkStrawHit.cc:268** - Possible assignment (=) instead of comparison (==) in condition

#### division_by_zero (30 occurrences)

- **/workspace/BTrkData/src/Doublet.cc:2** - Potential division by zero: BTrkData not checked
- **/workspace/BTrkData/src/Doublet.cc:79** - Potential division by zero: i not checked
- **/workspace/BTrkData/src/Doublet.cc:90** - Potential division by zero: i not checked
- **/workspace/BTrkData/src/TrkCaloHit.cc:1** - Potential division by zero: BTrkData not checked
- **/workspace/BTrkData/src/TrkCaloHit.cc:3** - Potential division by zero: BaBar not checked
- **/workspace/BTrkData/src/TrkCaloHit.cc:4** - Potential division by zero: TrkBase not checked
- **/workspace/BTrkData/src/TrkCaloHit.cc:5** - Potential division by zero: TrkBase not checked
- **/workspace/BTrkData/src/TrkCaloHit.cc:6** - Potential division by zero: TrkBase not checked
- **/workspace/BTrkData/src/TrkCaloHit.cc:7** - Potential division by zero: TrkBase not checked
- **/workspace/BTrkData/src/TrkCaloHit.cc:8** - Potential division by zero: TrkBase not checked
- ... and 20 more

#### memory_leak (3 occurrences)

- **/workspace/BTrkData/src/Doublet.cc:82** - Potential memory leak: new staw without corresponding delete
- **/workspace/BTrkData/src/TrkCaloHit.cc:28** - Potential memory leak: new TrkLineTraj without corresponding delete
- **/workspace/BTrkData/src/TrkStrawHit.cc:52** - Potential memory leak: new TrkLineTraj without corresponding delete

#### missing_return (2 occurrences)

- **/workspace/BTrkData/src/Doublet.cc:81** - Function may be missing return statement
- **/workspace/BTrkData/src/TrkStrawHit.cc:159** - Function may be missing return statement

#### uninitialized_variable (1 occurrences)

- **/workspace/BTrkData/src/TrkStrawHit.cc:100** - Variable doca may be used uninitialized

#### use_after_free (3 occurrences)

- **/workspace/BTrkData/src/TrkCaloHit.cc:42** - Potential use after free: the deleted but may be used later
- **/workspace/BTrkData/src/TrkCaloHit.cc:43** - Potential use after free: _hittraj deleted but may be used later
- **/workspace/BTrkData/src/TrkStrawHit.cc:70** - Potential use after free: the deleted but may be used later


### BeamlineGeom

Found 1 potential bugs:

#### division_by_zero (1 occurrences)

- **/workspace/BeamlineGeom/src/TSdA.cc:1** - Potential division by zero: BeamlineGeom not checked


### Blinding

Found 120 potential bugs:

#### array_bounds (2 occurrences)

- **/workspace/Blinding/src/DisplaceDigiTimes_module.cc:172** - Array access tdc[i] without bounds check
- **/workspace/Blinding/src/DisplaceDigiTimes_module.cc:174** - Array access tdc[i] without bounds check

#### assignment_in_condition (2 occurrences)

- **/workspace/Blinding/src/BigNumberChecker_module.cc:61** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Blinding/src/UnivariateLookupKalSeedPrescaleTool.cc:22** - Possible assignment (=) instead of comparison (==) in condition

#### division_by_zero (105 occurrences)

- **/workspace/Blinding/src/KalSeedPrescaleTool.cc:5** - Potential division by zero: Blinding not checked
- **/workspace/Blinding/src/TrackDigiExtractor_module.cc:9** - Potential division by zero: Framework not checked
- **/workspace/Blinding/src/TrackDigiExtractor_module.cc:10** - Potential division by zero: Framework not checked
- **/workspace/Blinding/src/TrackDigiExtractor_module.cc:13** - Potential division by zero: exception not checked
- **/workspace/Blinding/src/TrackDigiExtractor_module.cc:16** - Potential division by zero: types not checked
- **/workspace/Blinding/src/TrackDigiExtractor_module.cc:17** - Potential division by zero: types not checked
- **/workspace/Blinding/src/TrackDigiExtractor_module.cc:18** - Potential division by zero: types not checked
- **/workspace/Blinding/src/TrackDigiExtractor_module.cc:21** - Potential division by zero: RecoDataProducts not checked
- **/workspace/Blinding/src/TrackDigiExtractor_module.cc:22** - Potential division by zero: RecoDataProducts not checked
- **/workspace/Blinding/src/TrackDigiExtractor_module.cc:23** - Potential division by zero: RecoDataProducts not checked
- ... and 95 more

#### memory_leak (1 occurrences)

- **/workspace/Blinding/src/DisplaceDigiTimes_module.cc:177** - Potential memory leak: new digi without corresponding delete

#### missing_error_handling (9 occurrences)

- **/workspace/Blinding/src/TrackDigiExtractor_module.cc:76** - getHandle/getValidHandle result not checked for validity
- **/workspace/Blinding/src/TrackDigiExtractor_module.cc:77** - getHandle/getValidHandle result not checked for validity
- **/workspace/Blinding/src/TrackDigiExtractor_module.cc:78** - getHandle/getValidHandle result not checked for validity
- **/workspace/Blinding/src/MergeDigis_module.cc:88** - getHandle/getValidHandle result not checked for validity
- **/workspace/Blinding/src/BigNumberChecker_module.cc:56** - getHandle/getValidHandle result not checked for validity
- **/workspace/Blinding/src/BigNumberChecker_module.cc:57** - getHandle/getValidHandle result not checked for validity
- **/workspace/Blinding/src/GoldwasserMicaliEncrypter_module.cc:90** - getHandle/getValidHandle result not checked for validity
- **/workspace/Blinding/src/KalSeedFunctionalPrescale_module.cc:91** - getHandle/getValidHandle result not checked for validity
- **/workspace/Blinding/src/GoldwasserMicaliDecrypter_module.cc:83** - getHandle/getValidHandle result not checked for validity

#### uninitialized_variable (1 occurrences)

- **/workspace/Blinding/src/MergeDigis_module.cc:46** - Variable _tracker_mc may be used uninitialized


### CRVConditions

Found 32 potential bugs:

#### array_bounds (9 occurrences)

- **/workspace/CRVConditions/src/CRVOrdinalMaker.cc:36** - Array access offMap[i] without bounds check
- **/workspace/CRVConditions/src/CRVOrdinalMaker.cc:74** - Array access words[0] without bounds check
- **/workspace/CRVConditions/src/CRVOrdinalMaker.cc:75** - Array access words[1] without bounds check
- **/workspace/CRVConditions/src/CRVOrdinalMaker.cc:76** - Array access words[2] without bounds check
- **/workspace/CRVConditions/src/CRVOrdinalMaker.cc:77** - Array access words[3] without bounds check
- **/workspace/CRVConditions/src/CRVCalibMaker.cc:71** - Array access cvec[row.channel()] without bounds check
- **/workspace/CRVConditions/src/CRVStatusMaker.cc:25** - Array access smap[channel] without bounds check
- **/workspace/CRVConditions/src/CRVStatusMaker.cc:47** - Array access smap[row.channel()] without bounds check
- **/workspace/CRVConditions/src/CRVPhotonYieldMaker.cc:56** - Array access svec[row.channel()] without bounds check

#### division_by_zero (21 occurrences)

- **/workspace/CRVConditions/src/CRVOrdinalMaker.cc:1** - Potential division by zero: CRVConditions not checked
- **/workspace/CRVConditions/src/CRVOrdinalMaker.cc:2** - Potential division by zero: ConfigTools not checked
- **/workspace/CRVConditions/src/CRVOrdinalMaker.cc:3** - Potential division by zero: CosmicRayShieldGeom not checked
- **/workspace/CRVConditions/src/CRVOrdinalMaker.cc:4** - Potential division by zero: GeometryService not checked
- **/workspace/CRVConditions/src/CRVOrdinalMaker.cc:5** - Potential division by zero: GeometryService not checked
- **/workspace/CRVConditions/src/CRVOrdinalMaker.cc:6** - Potential division by zero: exception not checked
- **/workspace/CRVConditions/src/CRVOrdinalMaker.cc:7** - Potential division by zero: algorithm not checked
- **/workspace/CRVConditions/src/CRVOrdinalMaker.cc:8** - Potential division by zero: algorithm not checked
- **/workspace/CRVConditions/src/CRVOrdinalMaker.cc:9** - Potential division by zero: algorithm not checked
- **/workspace/CRVConditions/src/CRVCalibMaker.cc:1** - Potential division by zero: CRVConditions not checked
- ... and 11 more

#### resource_leak (2 occurrences)

- **/workspace/CRVConditions/src/CRVOrdinalMaker.cc:54** - File handle opened but may not be closed
- **/workspace/CRVConditions/src/CRVOrdinalMaker.cc:55** - File handle opened but may not be closed


### CRVFilters

Found 27 potential bugs:

#### division_by_zero (23 occurrences)

- **/workspace/CRVFilters/src/CrvCoincidenceClusterFilter_module.cc:8** - Potential division by zero: Units not checked
- **/workspace/CRVFilters/src/CrvCoincidenceClusterFilter_module.cc:9** - Potential division by zero: GlobalConstantsService not checked
- **/workspace/CRVFilters/src/CrvCoincidenceClusterFilter_module.cc:11** - Potential division by zero: ConfigTools not checked
- **/workspace/CRVFilters/src/CrvCoincidenceClusterFilter_module.cc:13** - Potential division by zero: CalorimeterGeom not checked
- **/workspace/CRVFilters/src/CrvCoincidenceClusterFilter_module.cc:14** - Potential division by zero: CalorimeterGeom not checked
- **/workspace/CRVFilters/src/CrvCoincidenceClusterFilter_module.cc:16** - Potential division by zero: GeometryService not checked
- **/workspace/CRVFilters/src/CrvCoincidenceClusterFilter_module.cc:17** - Potential division by zero: GeometryService not checked
- **/workspace/CRVFilters/src/CrvCoincidenceClusterFilter_module.cc:19** - Potential division by zero: RecoDataProducts not checked
- **/workspace/CRVFilters/src/CrvCoincidenceClusterFilter_module.cc:20** - Potential division by zero: RecoDataProducts not checked
- **/workspace/CRVFilters/src/CrvCoincidenceClusterFilter_module.cc:21** - Potential division by zero: RecoDataProducts not checked
- ... and 13 more

#### memory_leak (1 occurrences)

- **/workspace/CRVFilters/src/CrvCoincidenceClusterFilter_module.cc:115** - Potential memory leak: new TriggerInfo without corresponding delete

#### uninitialized_variable (3 occurrences)

- **/workspace/CRVFilters/src/CrvCoincidenceClusterFilter_module.cc:78** - Variable _diagLevel may be used uninitialized
- **/workspace/CRVFilters/src/CrvCoincidenceClusterFilter_module.cc:79** - Variable _nProcess may be used uninitialized
- **/workspace/CRVFilters/src/CrvCoincidenceClusterFilter_module.cc:80** - Variable _nPass may be used uninitialized


### CRVReco

Found 392 potential bugs:

#### array_bounds (125 occurrences)

- **/workspace/CRVReco/src/CrvFPGArate_module.cc:106** - Array access eventFPGAmap[FPGAIndex] without bounds check
- **/workspace/CRVReco/src/CrvFPGArate_module.cc:107** - Array access eventHitMultiplicityMap[FPGAIndex] without bounds check
- **/workspace/CRVReco/src/CrvFPGArate_module.cc:132** - Array access eventFPGAmap[FPGAIndex] without bounds check
- **/workspace/CRVReco/src/CrvFPGArate_module.cc:136** - Array access eventHitMultiplicityMap[FPGAIndex] without bounds check
- **/workspace/CRVReco/src/CrvFPGArate_module.cc:138** - Array access eventHitMultiplicityMap[FPGAIndex] without bounds check
- **/workspace/CRVReco/src/CrvTimingStudies_module.cc:120** - Array access fpgaTimes[fpgaIndex] without bounds check
- **/workspace/CRVReco/src/CrvTimingStudies_module.cc:130** - Array access fpgaAverageTimes[fpga->first] without bounds check
- **/workspace/CRVReco/src/CrvTimingStudies_module.cc:143** - Array access _histTimeDiffs[histIndex] without bounds check
- **/workspace/CRVReco/src/CrvTimingStudies_module.cc:146** - Array access _histTimeDiffs[histIndex] without bounds check
- **/workspace/CRVReco/src/CrvTimingStudies_module.cc:152** - Array access _histTimeDiffs[histIndex] without bounds check
- ... and 115 more

#### assignment_in_condition (18 occurrences)

- **/workspace/CRVReco/src/CrvTimingStudies_module.cc:137** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CRVReco/src/CrvRecoPulsesFinder_module.cc:191** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CRVReco/src/CrvRecoPulsesFinder_module.cc:192** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CRVReco/src/CrvRecoPulsesFinder_module.cc:254** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CRVReco/src/CrvRecoPulsesFinder_module.cc:255** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CRVReco/src/CrvWidebandTriggerFilter_module.cc:91** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CRVReco/src/CrvWidebandTriggerFilter_module.cc:95** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CRVReco/src/CrvCoincidenceFinder_module.cc:616** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CRVReco/src/CrvCoincidenceFinder_module.cc:642** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CRVReco/src/CrvCoincidenceFinder_module.cc:750** - Possible assignment (=) instead of comparison (==) in condition
- ... and 8 more

#### division_by_zero (217 occurrences)

- **/workspace/CRVReco/src/CrvFPGArate_module.cc:7** - Potential division by zero: CosmicRayShieldGeom not checked
- **/workspace/CRVReco/src/CrvFPGArate_module.cc:8** - Potential division by zero: GeometryService not checked
- **/workspace/CRVReco/src/CrvFPGArate_module.cc:9** - Potential division by zero: RecoDataProducts not checked
- **/workspace/CRVReco/src/CrvFPGArate_module.cc:10** - Potential division by zero: CRVConditions not checked
- **/workspace/CRVReco/src/CrvFPGArate_module.cc:11** - Potential division by zero: ProditionsService not checked
- **/workspace/CRVReco/src/CrvFPGArate_module.cc:13** - Potential division by zero: TFileDirectory not checked
- **/workspace/CRVReco/src/CrvFPGArate_module.cc:14** - Potential division by zero: TFileService not checked
- **/workspace/CRVReco/src/CrvFPGArate_module.cc:15** - Potential division by zero: Framework not checked
- **/workspace/CRVReco/src/CrvFPGArate_module.cc:17** - Potential division by zero: Framework not checked
- **/workspace/CRVReco/src/CrvFPGArate_module.cc:18** - Potential division by zero: Framework not checked
- ... and 207 more

#### memory_leak (12 occurrences)

- **/workspace/CRVReco/src/CrvFPGArate_module.cc:68** - Potential memory leak: new art without corresponding delete
- **/workspace/CRVReco/src/CrvFPGArate_module.cc:69** - Potential memory leak: new art without corresponding delete
- **/workspace/CRVReco/src/CrvFPGArate_module.cc:167** - Potential memory leak: new element without corresponding delete
- **/workspace/CRVReco/src/CrvFPGArate_module.cc:195** - Potential memory leak: new element without corresponding delete
- **/workspace/CRVReco/src/CrvRecoPulsesFinder_module.cc:119** - Potential memory leak: new mu2eCrv without corresponding delete
- **/workspace/CRVReco/src/CrvRecoPulsesFinder_module.cc:146** - Potential memory leak: new CrvRecoPulseCollection without corresponding delete
- **/workspace/CRVReco/src/CrvCoincidenceFinder_module.cc:273** - Potential memory leak: new CrvCoincidenceClusterCollection without corresponding delete
- **/workspace/CRVReco/src/CrvCoincidenceFinder_module.cc:362** - Potential memory leak: new list without corresponding delete
- **/workspace/CRVReco/src/CrvCoincidenceFinder_module.cc:382** - Potential memory leak: new clusters without corresponding delete
- **/workspace/CRVReco/src/CrvCoincidenceFinder_module.cc:653** - Potential memory leak: new cluster without corresponding delete
- ... and 2 more

#### uninitialized_variable (19 occurrences)

- **/workspace/CRVReco/src/CrvFPGArate_module.cc:51** - Variable _minTDC may be used uninitialized
- **/workspace/CRVReco/src/CrvFPGArate_module.cc:52** - Variable _maxTDC may be used uninitialized
- **/workspace/CRVReco/src/CrvTimingStudies_module.cc:63** - Variable _PEthreshold may be used uninitialized
- **/workspace/CRVReco/src/CrvPedestalFinder_module.cc:58** - Variable _firstSampleOnly may be used uninitialized
- **/workspace/CRVReco/src/CrvPedestalFinder_module.cc:59** - Variable _histBins may be used uninitialized
- **/workspace/CRVReco/src/CrvPedestalFinder_module.cc:61** - Variable _maxADCspread may be used uninitialized
- **/workspace/CRVReco/src/CrvRecoPulsesFinder_module.cc:88** - Variable _NZSdata may be used uninitialized
- **/workspace/CRVReco/src/CrvRecoPulsesFinder_module.cc:89** - Variable _pedestalUndershootThreshold may be used uninitialized
- **/workspace/CRVReco/src/CrvRecoPulsesFinder_module.cc:93** - Variable _timeOffsetScale may be used uninitialized
- **/workspace/CRVReco/src/CrvRecoPulsesFinder_module.cc:94** - Variable _timeOffsetCutoffLow may be used uninitialized
- ... and 9 more

#### unused_variable (1 occurrences)

- **/workspace/CRVReco/src/CrvCoincidenceFinder_module.cc:866** - Variable iterHit declared but possibly unused


### CRVResponse

Found 712 potential bugs:

#### array_bounds (264 occurrences)

- **/workspace/CRVResponse/src/CRVTest_module.cc:142** - Array access ct[4] without bounds check
- **/workspace/CRVResponse/src/CRVTest_module.cc:143** - Array access cPEs[4] without bounds check
- **/workspace/CRVResponse/src/CRVTest_module.cc:174** - Array access ct[SiPM] without bounds check
- **/workspace/CRVResponse/src/CRVTest_module.cc:175** - Array access cPEs[SiPM] without bounds check
- **/workspace/CRVResponse/src/CRVTest_module.cc:185** - Array access singlePhotons[i] without bounds check
- **/workspace/CRVResponse/src/CRVTest_module.cc:200** - Array access singleCharges[i] without bounds check
- **/workspace/CRVResponse/src/CRVTest_module.cc:201** - Array access singleCharges[i] without bounds check
- **/workspace/CRVResponse/src/CRVTest_module.cc:238** - Array access ct[0] without bounds check
- **/workspace/CRVResponse/src/CrvMCHelper.cc:14** - Array access waveformIndices[i] without bounds check
- **/workspace/CRVResponse/src/CrvMCHelper.cc:19** - Array access stepPoints[j] without bounds check
- ... and 254 more

#### assignment_in_condition (33 occurrences)

- **/workspace/CRVResponse/src/CrvPlot_module.cc:263** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CRVResponse/src/MakeCrvWaveforms.cc:28** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CRVResponse/src/MakeCrvWaveforms.cc:39** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CRVResponse/src/MakeCrvWaveforms.cc:79** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CRVResponse/src/CrvPhotonGenerator_module.cc:185** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CRVResponse/src/CrvWidebandTest_module.cc:324** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CRVResponse/src/CrvWidebandTest_module.cc:332** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CRVResponse/src/CrvWidebandTest_module.cc:425** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CRVResponse/src/CrvWidebandTest_module.cc:429** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CRVResponse/src/CrvWidebandTest_module.cc:503** - Possible assignment (=) instead of comparison (==) in condition
- ... and 23 more

#### division_by_zero (354 occurrences)

- **/workspace/CRVResponse/src/CRVTest_module.cc:7** - Potential division by zero: CosmicRayShieldGeom not checked
- **/workspace/CRVResponse/src/CRVTest_module.cc:8** - Potential division by zero: DataProducts not checked
- **/workspace/CRVResponse/src/CRVTest_module.cc:10** - Potential division by zero: CRVConditions not checked
- **/workspace/CRVResponse/src/CRVTest_module.cc:11** - Potential division by zero: GeometryService not checked
- **/workspace/CRVResponse/src/CRVTest_module.cc:12** - Potential division by zero: GeometryService not checked
- **/workspace/CRVResponse/src/CRVTest_module.cc:13** - Potential division by zero: GeometryService not checked
- **/workspace/CRVResponse/src/CRVTest_module.cc:14** - Potential division by zero: MCDataProducts not checked
- **/workspace/CRVResponse/src/CRVTest_module.cc:15** - Potential division by zero: MCDataProducts not checked
- **/workspace/CRVResponse/src/CRVTest_module.cc:16** - Potential division by zero: RecoDataProducts not checked
- **/workspace/CRVResponse/src/CRVTest_module.cc:17** - Potential division by zero: RecoDataProducts not checked
- ... and 344 more

#### memory_leak (52 occurrences)

- **/workspace/CRVResponse/src/CrvDigitizer_module.cc:75** - Potential memory leak: new mu2eCrv without corresponding delete
- **/workspace/CRVResponse/src/CrvDigitizer_module.cc:80** - Potential memory leak: new CrvDigiCollection without corresponding delete
- **/workspace/CRVResponse/src/CrvDigitizer_module.cc:81** - Potential memory leak: new CrvDigiCollection without corresponding delete
- **/workspace/CRVResponse/src/MakeCrvSiPMCharges.cc:73** - Potential memory leak: new Type0 without corresponding delete
- **/workspace/CRVResponse/src/MakeCrvSiPMCharges.cc:80** - Potential memory leak: new Type1 without corresponding delete
- **/workspace/CRVResponse/src/MakeCrvSiPMCharges.cc:196** - Potential memory leak: new pixel without corresponding delete
- **/workspace/CRVResponse/src/MakeCrvSiPMCharges.cc:209** - Potential memory leak: new TFile without corresponding delete
- **/workspace/CRVResponse/src/CrvPlot_module.cc:166** - Potential memory leak: new TH1D without corresponding delete
- **/workspace/CRVResponse/src/CrvPlot_module.cc:212** - Potential memory leak: new TH1D without corresponding delete
- **/workspace/CRVResponse/src/CrvPlot_module.cc:223** - Potential memory leak: new TGaxis without corresponding delete
- ... and 42 more

#### missing_return (1 occurrences)

- **/workspace/CRVResponse/src/CrvStepsFromStepPointMCs_module.cc:83** - Function may be missing return statement

#### uninitialized_variable (6 occurrences)

- **/workspace/CRVResponse/src/CrvDigitizer_module.cc:59** - Variable _ADCconversionFactor may be used uninitialized
- **/workspace/CRVResponse/src/CrvDigitizer_module.cc:60** - Variable _pedestal may be used uninitialized
- **/workspace/CRVResponse/src/CrvDigitizer_module.cc:61** - Variable _simulateNZS may be used uninitialized
- **/workspace/CRVResponse/src/CrvStepsFromStepPointMCs_module.cc:94** - Variable _firstEvent may be used uninitialized
- **/workspace/CRVResponse/src/MakeCrvPhotons.cc:521** - Variable nPhotons may be used uninitialized
- **/workspace/CRVResponse/src/CrvCoincidenceClusterMatchMC_module.cc:63** - Variable _doNtuples may be used uninitialized

#### unused_variable (2 occurrences)

- **/workspace/CRVResponse/src/CrvWidebandTest_module.cc:297** - Variable TDC0time declared but possibly unused
- **/workspace/CRVResponse/src/MakeCrvPhotons.cc:412** - Variable iEmission declared but possibly unused


### CRVTools

Found 92 potential bugs:

#### array_bounds (52 occurrences)

- **/workspace/CRVTools/src/CrvDigiDump_module.cc:55** - Array access ADC_[nADC_] without bounds check
- **/workspace/CRVTools/src/CrvDigiDump_module.cc:71** - Array access status_eventWindowTag_[maxROCs_] without bounds check
- **/workspace/CRVTools/src/CrvDigiDump_module.cc:72** - Array access status_subeventEWT_[maxROCs_] without bounds check
- **/workspace/CRVTools/src/CrvDigiDump_module.cc:73** - Array access status_roc_eventWindowTag_[maxROCs_] without bounds check
- **/workspace/CRVTools/src/CrvDigiDump_module.cc:74** - Array access status_roc_microBunchStatus_[maxROCs_] without bounds check
- **/workspace/CRVTools/src/CrvDigiDump_module.cc:75** - Array access status_roc_activeFEBFlags_[maxROCs_] without bounds check
- **/workspace/CRVTools/src/CrvDigiDump_module.cc:77** - Array access status_roc_controllerEventWordCount_[maxROCs_] without bounds check
- **/workspace/CRVTools/src/CrvDigiDump_module.cc:78** - Array access status_roc_triggerCount_[maxROCs_] without bounds check
- **/workspace/CRVTools/src/CrvDigiDump_module.cc:80** - Array access status_linkID_[maxROCs_] without bounds check
- **/workspace/CRVTools/src/CrvDigiDump_module.cc:81** - Array access status_dtcID_[maxROCs_] without bounds check
- ... and 42 more

#### division_by_zero (40 occurrences)

- **/workspace/CRVTools/src/CrvDigiDump_module.cc:9** - Potential division by zero: Framework not checked
- **/workspace/CRVTools/src/CrvDigiDump_module.cc:10** - Potential division by zero: Framework not checked
- **/workspace/CRVTools/src/CrvDigiDump_module.cc:11** - Potential division by zero: Framework not checked
- **/workspace/CRVTools/src/CrvDigiDump_module.cc:12** - Potential division by zero: TFileService not checked
- **/workspace/CRVTools/src/CrvDigiDump_module.cc:13** - Potential division by zero: types not checked
- **/workspace/CRVTools/src/CrvDigiDump_module.cc:14** - Potential division by zero: types not checked
- **/workspace/CRVTools/src/CrvDigiDump_module.cc:15** - Potential division by zero: Utilities not checked
- **/workspace/CRVTools/src/CrvDigiDump_module.cc:17** - Potential division by zero: RecoDataProducts not checked
- **/workspace/CRVTools/src/CrvDigiDump_module.cc:18** - Potential division by zero: RecoDataProducts not checked
- **/workspace/CRVTools/src/CrvDigiDump_module.cc:70** - Potential division by zero: ROC not checked
- ... and 30 more


### CalPatRec

Found 2804 potential bugs:

#### array_bounds (1419 occurrences)

- **/workspace/CalPatRec/src/CalTimePeakFinder_module.cc:272** - Array access dtvec[i] without bounds check
- **/workspace/CalPatRec/src/DeltaFinder_types.cc:22** - Array access fPFirst[i] without bounds check
- **/workspace/CalPatRec/src/DeltaFinder_types.cc:34** - Array access panelOverlap[i] without bounds check
- **/workspace/CalPatRec/src/DeltaFinder_types.cc:55** - Array access fListOfComptonSeeds[is] without bounds check
- **/workspace/CalPatRec/src/DeltaFinder_types.cc:60** - Array access fFaceData[is] without bounds check
- **/workspace/CalPatRec/src/DeltaFinder_types.cc:98** - Array access stationZ[ist] without bounds check
- **/workspace/CalPatRec/src/DeltaFinder_types.cc:124** - Array access fFaceData[co.Station] without bounds check
- **/workspace/CalPatRec/src/DeltaFinder_types.cc:142** - Array access stationUsed[ist] without bounds check
- **/workspace/CalPatRec/src/DeltaFinder_types.cc:151** - Array access fFaceData[ich] without bounds check
- **/workspace/CalPatRec/src/DeltaFinder_types.cc:155** - Array access fFaceData[ich] without bounds check
- ... and 1409 more

#### assignment_in_condition (185 occurrences)

- **/workspace/CalPatRec/src/CalTimePeakFinder_module.cc:64** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CalPatRec/src/CalTimePeakFinder_module.cc:66** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CalPatRec/src/CalTimePeakFinder_module.cc:261** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CalPatRec/src/DeltaFinder_types.cc:159** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CalPatRec/src/DeltaFinder_types.cc:252** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CalPatRec/src/DeltaFinder_types.cc:275** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CalPatRec/src/TZClusterFilter_module.cc:449** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CalPatRec/src/TZClusterFilter_module.cc:456** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CalPatRec/src/TZClusterFilter_module.cc:487** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CalPatRec/src/TZClusterFilter_module.cc:524** - Possible assignment (=) instead of comparison (==) in condition
- ... and 175 more

#### division_by_zero (1030 occurrences)

- **/workspace/CalPatRec/src/CalTimePeakFinder_module.cc:9** - Potential division by zero: types not checked
- **/workspace/CalPatRec/src/CalTimePeakFinder_module.cc:10** - Potential division by zero: types not checked
- **/workspace/CalPatRec/src/CalTimePeakFinder_module.cc:11** - Potential division by zero: ParameterSet not checked
- **/workspace/CalPatRec/src/CalTimePeakFinder_module.cc:13** - Potential division by zero: Mu2eUtilities not checked
- **/workspace/CalPatRec/src/CalTimePeakFinder_module.cc:14** - Potential division by zero: CalPatRec not checked
- **/workspace/CalPatRec/src/CalTimePeakFinder_module.cc:17** - Potential division by zero: Framework not checked
- **/workspace/CalPatRec/src/CalTimePeakFinder_module.cc:18** - Potential division by zero: TFileService not checked
- **/workspace/CalPatRec/src/CalTimePeakFinder_module.cc:19** - Potential division by zero: Utilities not checked
- **/workspace/CalPatRec/src/CalTimePeakFinder_module.cc:21** - Potential division by zero: GeometryService not checked
- **/workspace/CalPatRec/src/CalTimePeakFinder_module.cc:22** - Potential division by zero: GeometryService not checked
- ... and 1020 more

#### memory_leak (99 occurrences)

- **/workspace/CalPatRec/src/CalTimePeakFinder_module.cc:137** - Potential memory leak: new TimeClusterCollection without corresponding delete
- **/workspace/CalPatRec/src/ComboHitFilter_module.cc:2** - Potential memory leak: new collection without corresponding delete
- **/workspace/CalPatRec/src/ComboHitFilter_module.cc:153** - Potential memory leak: new ComboHitCollection without corresponding delete
- **/workspace/CalPatRec/src/ComboHitFilter_module.cc:154** - Potential memory leak: new StrawHitFlagCollection without corresponding delete
- **/workspace/CalPatRec/src/TZClusterFilter_module.cc:286** - Potential memory leak: new TimeClusterCollection without corresponding delete
- **/workspace/CalPatRec/src/CalHelixFinder_module.cc:226** - Potential memory leak: new HelixSeedCollection without corresponding delete
- **/workspace/CalPatRec/src/CalHelixFinder_module.cc:231** - Potential memory leak: new HelixSeedCollection without corresponding delete
- **/workspace/CalPatRec/src/CalHelixFinder_module.cc:234** - Potential memory leak: new HelixSeedCollection without corresponding delete
- **/workspace/CalPatRec/src/AgnosticHelixFinderDiag_tool.cc:127** - Potential memory leak: new EventHists without corresponding delete
- **/workspace/CalPatRec/src/AgnosticHelixFinderDiag_tool.cc:140** - Potential memory leak: new TimeClusterHists without corresponding delete
- ... and 89 more

#### missing_error_handling (21 occurrences)

- **/workspace/CalPatRec/src/ComboHitFilter_module.cc:127** - getHandle/getValidHandle result not checked for validity
- **/workspace/CalPatRec/src/ComboHitFilter_module.cc:130** - getHandle/getValidHandle result not checked for validity
- **/workspace/CalPatRec/src/ComboHitFilter_module.cc:133** - getHandle/getValidHandle result not checked for validity
- **/workspace/CalPatRec/src/PhiClusterFinder_module.cc:149** - getHandle/getValidHandle result not checked for validity
- **/workspace/CalPatRec/src/AgnosticHelixFinder_module.cc:400** - getHandle/getValidHandle result not checked for validity
- **/workspace/CalPatRec/src/AgnosticHelixFinder_module.cc:403** - getHandle/getValidHandle result not checked for validity
- **/workspace/CalPatRec/src/PrefetchData_module.cc:169** - getHandle/getValidHandle result not checked for validity
- **/workspace/CalPatRec/src/PrefetchData_module.cc:174** - getHandle/getValidHandle result not checked for validity
- **/workspace/CalPatRec/src/PrefetchData_module.cc:179** - getHandle/getValidHandle result not checked for validity
- **/workspace/CalPatRec/src/PrefetchData_module.cc:184** - getHandle/getValidHandle result not checked for validity
- ... and 11 more

#### missing_return (22 occurrences)

- **/workspace/CalPatRec/src/CalHelixFinder_module.cc:319** - Function may be missing return statement
- **/workspace/CalPatRec/src/PhiClusterFinder_module.cc:289** - Function may be missing return statement
- **/workspace/CalPatRec/src/ProtonCandidate.cc:214** - Function may be missing return statement
- **/workspace/CalPatRec/src/AgnosticHelixFinder_module.cc:481** - Function may be missing return statement
- **/workspace/CalPatRec/src/AgnosticHelixFinder_module.cc:534** - Function may be missing return statement
- **/workspace/CalPatRec/src/AgnosticHelixFinder_module.cc:842** - Function may be missing return statement
- **/workspace/CalPatRec/src/CalHelixFinderAlg.cc:898** - Function may be missing return statement
- **/workspace/CalPatRec/src/CalHelixFinderAlg.cc:1482** - Function may be missing return statement
- **/workspace/CalPatRec/src/CalHelixFinderAlg.cc:2684** - Function may be missing return statement
- **/workspace/CalPatRec/src/CalHelixFinderAlg.cc:3300** - Function may be missing return statement
- ... and 12 more

#### uninitialized_variable (15 occurrences)

- **/workspace/CalPatRec/src/DeltaFinder_types.cc:113** - Variable face may be used uninitialized
- **/workspace/CalPatRec/src/CalHelixFinder_module.cc:130** - Variable face may be used uninitialized
- **/workspace/CalPatRec/src/AgnosticHelixFinderDiag_tool.cc:259** - Variable pmc may be used uninitialized
- **/workspace/CalPatRec/src/AgnosticHelixFinderDiag_tool.cc:701** - Variable mc_hits may be used uninitialized
- **/workspace/CalPatRec/src/AgnosticHelixFinderDiag_tool.cc:712** - Variable mc_hits_hlx may be used uninitialized
- **/workspace/CalPatRec/src/MergeHelixFinder_module.cc:82** - Variable _diag may be used uninitialized
- **/workspace/CalPatRec/src/MergeHelixFinder_module.cc:83** - Variable _debugLevel may be used uninitialized
- **/workspace/CalPatRec/src/CalHelixFinderAlg.cc:1604** - Variable loc may be used uninitialized
- **/workspace/CalPatRec/src/CalHelixFinderAlg.cc:2129** - Variable rc may be used uninitialized
- **/workspace/CalPatRec/src/CalHelixFinderAlg.cc:2328** - Variable wt may be used uninitialized
- ... and 5 more

#### unused_variable (11 occurrences)

- **/workspace/CalPatRec/src/DeltaFinder_types.cc:34** - Variable k declared but possibly unused
- **/workspace/CalPatRec/src/ObjectDumpUtils.cc:403** - Variable banner_printed declared but possibly unused
- **/workspace/CalPatRec/src/MergePatRecDiag_tool.cc:204** - Variable nhits declared but possibly unused
- **/workspace/CalPatRec/src/AgnosticHelixFinder_module.cc:506** - Variable itest declared but possibly unused
- **/workspace/CalPatRec/src/CalHelixFinderAlg.cc:3628** - Variable exp_dphi declared but possibly unused
- **/workspace/CalPatRec/src/DeltaFinderDiag_tool.cc:2001** - Variable radselOK declared but possibly unused
- **/workspace/CalPatRec/src/DeltaFinderDiag_tool.cc:2002** - Variable edepOK declared but possibly unused
- **/workspace/CalPatRec/src/DeltaFinderAlg.cc:941** - Variable xdelta declared but possibly unused
- **/workspace/CalPatRec/src/DeltaFinderAlg.cc:942** - Variable ydelta declared but possibly unused
- **/workspace/CalPatRec/src/DeltaFinderAna_module.cc:1047** - Variable loc declared but possibly unused
- ... and 1 more

#### use_after_free (2 occurrences)

- **/workspace/CalPatRec/src/HlPrint_ComboHit.cc:52** - Potential use after free: HlPrint deleted but may be used later
- **/workspace/CalPatRec/src/DeltaFinderAlg_findProtons.cc:173** - Potential use after free: them deleted but may be used later


### CaloCluster

Found 141 potential bugs:

#### array_bounds (59 occurrences)

- **/workspace/CaloCluster/src/CaloTrigger_module.cc:168** - Array access hitList_[index] without bounds check
- **/workspace/CaloCluster/src/CaloTrigger_module.cc:169** - Array access hitList_[index] without bounds check
- **/workspace/CaloCluster/src/CaloTrigger_module.cc:199** - Array access hitList_[itimebin] without bounds check
- **/workspace/CaloCluster/src/CaloTrigger_module.cc:221** - Array access hitList_[itimebin] without bounds check
- **/workspace/CaloCluster/src/CaloTrigger_module.cc:244** - Array access hitList_[itimebin] without bounds check
- **/workspace/CaloCluster/src/CaloTrigger_module.cc:259** - Array access hitList_[itimebin] without bounds check
- **/workspace/CaloCluster/src/ClusterUtils.cc:13** - Array access hits_[0] without bounds check
- **/workspace/CaloCluster/src/ClusterUtils.cc:23** - Array access hits_[0] without bounds check
- **/workspace/CaloCluster/src/ClusterUtils.cc:35** - Array access hits_[0] without bounds check
- **/workspace/CaloCluster/src/ClusterUtils.cc:53** - Array access hits_[0] without bounds check
- ... and 49 more

#### assignment_in_condition (3 occurrences)

- **/workspace/CaloCluster/src/CaloTrigger_module.cc:200** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CaloCluster/src/CaloTrigger_module.cc:222** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CaloCluster/src/CaloTrigger_module.cc:245** - Possible assignment (=) instead of comparison (==) in condition

#### division_by_zero (66 occurrences)

- **/workspace/CaloCluster/src/CaloTrigger_module.cc:1** - Potential division by zero: Framework not checked
- **/workspace/CaloCluster/src/CaloTrigger_module.cc:2** - Potential division by zero: Framework not checked
- **/workspace/CaloCluster/src/CaloTrigger_module.cc:3** - Potential division by zero: TFileService not checked
- **/workspace/CaloCluster/src/CaloTrigger_module.cc:4** - Potential division by zero: TFileDirectory not checked
- **/workspace/CaloCluster/src/CaloTrigger_module.cc:6** - Potential division by zero: GeometryService not checked
- **/workspace/CaloCluster/src/CaloTrigger_module.cc:7** - Potential division by zero: CalorimeterGeom not checked
- **/workspace/CaloCluster/src/CaloTrigger_module.cc:8** - Potential division by zero: GlobalConstantsService not checked
- **/workspace/CaloCluster/src/CaloTrigger_module.cc:9** - Potential division by zero: GlobalConstantsService not checked
- **/workspace/CaloCluster/src/CaloTrigger_module.cc:10** - Potential division by zero: RecoDataProducts not checked
- **/workspace/CaloCluster/src/CaloTrigger_module.cc:11** - Potential division by zero: RecoDataProducts not checked
- ... and 56 more

#### memory_leak (2 occurrences)

- **/workspace/CaloCluster/src/CaloProtoClusterMaker_module.cc:144** - Potential memory leak: new seeds without corresponding delete
- **/workspace/CaloCluster/src/CaloClusterMaker_module.cc:172** - Potential memory leak: new cluster without corresponding delete

#### missing_error_handling (4 occurrences)

- **/workspace/CaloCluster/src/CaloProtoClusterMaker_module.cc:92** - getHandle/getValidHandle result not checked for validity
- **/workspace/CaloCluster/src/CaloClusterFast_module.cc:78** - getHandle/getValidHandle result not checked for validity
- **/workspace/CaloCluster/src/CaloClusterMaker_module.cc:83** - getHandle/getValidHandle result not checked for validity
- **/workspace/CaloCluster/src/CaloClusterMaker_module.cc:84** - getHandle/getValidHandle result not checked for validity

#### uninitialized_variable (2 occurrences)

- **/workspace/CaloCluster/src/CaloTrigger_module.cc:86** - Variable mbtime_ may be used uninitialized
- **/workspace/CaloCluster/src/CaloTrigger_module.cc:188** - Variable rpeak may be used uninitialized

#### unused_variable (5 occurrences)

- **/workspace/CaloCluster/src/CaloTrigger_module.cc:153** - Variable adc2MeV declared but possibly unused
- **/workspace/CaloCluster/src/CaloTrigger_module.cc:269** - Variable iSection declared but possibly unused
- **/workspace/CaloCluster/src/CaloClusterMaker_module.cc:173** - Variable il declared but possibly unused
- **/workspace/CaloCluster/src/CaloClusterMaker_module.cc:222** - Variable time declared but possibly unused
- **/workspace/CaloCluster/src/CaloClusterMaker_module.cc:223** - Variable timeErr declared but possibly unused


### CaloConditions

Found 18 potential bugs:

#### array_bounds (5 occurrences)

- **/workspace/CaloConditions/src/CaloDAQMapMaker.cc:49** - Array access raw2Offline[rid] without bounds check
- **/workspace/CaloConditions/src/CaloDAQMapMaker.cc:52** - Array access offline2Raw[oid] without bounds check
- **/workspace/CaloConditions/src/CaloDAQMap.cc:13** - Array access _raw2Offline[rawId.id()] without bounds check
- **/workspace/CaloConditions/src/CaloDAQMap.cc:25** - Array access _offline2Raw[offId.id()] without bounds check
- **/workspace/CaloConditions/src/CaloDAQMap.cc:33** - Array access _raw2Offline[i] without bounds check

#### assignment_in_condition (3 occurrences)

- **/workspace/CaloConditions/src/CaloDAQMapMaker.cc:40** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CaloConditions/src/CaloDAQMapMaker.cc:43** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CaloConditions/src/CaloDAQMapMaker.cc:59** - Possible assignment (=) instead of comparison (==) in condition

#### division_by_zero (8 occurrences)

- **/workspace/CaloConditions/src/CaloDAQMapMaker.cc:1** - Potential division by zero: CaloConditions not checked
- **/workspace/CaloConditions/src/CaloDAQMapMaker.cc:2** - Potential division by zero: ConfigTools not checked
- **/workspace/CaloConditions/src/CaloDAQMapMaker.cc:3** - Potential division by zero: DataProducts not checked
- **/workspace/CaloConditions/src/CaloDAQMapMaker.cc:4** - Potential division by zero: exception not checked
- **/workspace/CaloConditions/src/CaloDAQMap.cc:1** - Potential division by zero: CaloConditions not checked
- **/workspace/CaloConditions/src/CaloDAQMap.cc:2** - Potential division by zero: exception not checked
- **/workspace/CaloConditions/src/CalCalibMaker.cc:1** - Potential division by zero: CaloConditions not checked
- **/workspace/CaloConditions/src/CalCalib.cc:1** - Potential division by zero: CaloConditions not checked

#### resource_leak (2 occurrences)

- **/workspace/CaloConditions/src/CaloDAQMapMaker.cc:25** - File handle opened but may not be closed
- **/workspace/CaloConditions/src/CaloDAQMapMaker.cc:26** - File handle opened but may not be closed


### CaloDiag

Found 766 potential bugs:

#### array_bounds (405 occurrences)

- **/workspace/CaloDiag/src/CaloExample_module.cc:91** - Array access cryId_[ntupLen] without bounds check
- **/workspace/CaloDiag/src/CaloExample_module.cc:92** - Array access cryTime_[ntupLen] without bounds check
- **/workspace/CaloDiag/src/CaloExample_module.cc:94** - Array access crySimId_[ntupLen] without bounds check
- **/workspace/CaloDiag/src/CaloExample_module.cc:95** - Array access crySimMom_[ntupLen] without bounds check
- **/workspace/CaloDiag/src/CaloExample_module.cc:96** - Array access crySimTime_[ntupLen] without bounds check
- **/workspace/CaloDiag/src/CaloExample_module.cc:98** - Array access cluNcrys_[ntupLen] without bounds check
- **/workspace/CaloDiag/src/CaloExample_module.cc:99** - Array access cluEnergy_[ntupLen] without bounds check
- **/workspace/CaloDiag/src/CaloExample_module.cc:100** - Array access cluCogZ_[ntupLen] without bounds check
- **/workspace/CaloDiag/src/CaloExample_module.cc:101** - Array access cluSplit_[ntupLen] without bounds check
- **/workspace/CaloDiag/src/CaloExample_module.cc:104** - Array access cluSimId_[ntupLen] without bounds check
- ... and 395 more

#### assignment_in_condition (3 occurrences)

- **/workspace/CaloDiag/src/CaloClusterCheck_module.cc:149** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CaloDiag/src/CaloNNDiag_module.cc:366** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CaloDiag/src/CaloNNDiag_module.cc:449** - Possible assignment (=) instead of comparison (==) in condition

#### division_by_zero (353 occurrences)

- **/workspace/CaloDiag/src/CaloExample_module.cc:4** - Potential division by zero: Framework not checked
- **/workspace/CaloDiag/src/CaloExample_module.cc:5** - Potential division by zero: Framework not checked
- **/workspace/CaloDiag/src/CaloExample_module.cc:6** - Potential division by zero: Framework not checked
- **/workspace/CaloDiag/src/CaloExample_module.cc:7** - Potential division by zero: TFileService not checked
- **/workspace/CaloDiag/src/CaloExample_module.cc:8** - Potential division by zero: Framework not checked
- **/workspace/CaloDiag/src/CaloExample_module.cc:9** - Potential division by zero: Framework not checked
- **/workspace/CaloDiag/src/CaloExample_module.cc:10** - Potential division by zero: Framework not checked
- **/workspace/CaloDiag/src/CaloExample_module.cc:11** - Potential division by zero: exception not checked
- **/workspace/CaloDiag/src/CaloExample_module.cc:12** - Potential division by zero: types not checked
- **/workspace/CaloDiag/src/CaloExample_module.cc:13** - Potential division by zero: types not checked
- ... and 343 more

#### uninitialized_variable (3 occurrences)

- **/workspace/CaloDiag/src/CaloClusterCheck_module.cc:72** - Variable diagLevel_ may be used uninitialized
- **/workspace/CaloDiag/src/CaloClusterCheck_module.cc:73** - Variable nProcess_ may be used uninitialized
- **/workspace/CaloDiag/src/CaloMCInspector_module.cc:51** - Variable diagLevel_ may be used uninitialized

#### unused_variable (2 occurrences)

- **/workspace/CaloDiag/src/CaloExample_module.cc:377** - Variable cog declared but possibly unused
- **/workspace/CaloDiag/src/CaloNNDiag_module.cc:390** - Variable cog declared but possibly unused


### CaloFilters

Found 453 potential bugs:

#### array_bounds (124 occurrences)

- **/workspace/CaloFilters/src/CaloLikelihood_module.cc:91** - Array access _signalHist1D[2] without bounds check
- **/workspace/CaloFilters/src/CaloLikelihood_module.cc:92** - Array access _signalHist2D[2] without bounds check
- **/workspace/CaloFilters/src/CaloLikelihood_module.cc:97** - Array access _signalCorrHist1D[2] without bounds check
- **/workspace/CaloFilters/src/CaloLikelihood_module.cc:135** - Array access _signalHist1D[0] without bounds check
- **/workspace/CaloFilters/src/CaloLikelihood_module.cc:136** - Array access _signalHist1D[0] without bounds check
- **/workspace/CaloFilters/src/CaloLikelihood_module.cc:137** - Array access _signalHist1D[0] without bounds check
- **/workspace/CaloFilters/src/CaloLikelihood_module.cc:138** - Array access _signalHist1D[0] without bounds check
- **/workspace/CaloFilters/src/CaloLikelihood_module.cc:139** - Array access _signalHist1D[0] without bounds check
- **/workspace/CaloFilters/src/CaloLikelihood_module.cc:140** - Array access _signalHist1D[0] without bounds check
- **/workspace/CaloFilters/src/CaloLikelihood_module.cc:142** - Array access _signalHist1D[1] without bounds check
- ... and 114 more

#### assignment_in_condition (9 occurrences)

- **/workspace/CaloFilters/src/CaloLikelihood_module.cc:405** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CaloFilters/src/CaloLikelihood_module.cc:406** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CaloFilters/src/CaloLikelihood_module.cc:407** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CaloFilters/src/CaloLikelihood_module.cc:438** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CaloFilters/src/CaloCosmicCalib_module.cc:134** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CaloFilters/src/FilterEcalMixedTrigger_module.cc:496** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CaloFilters/src/FilterEcalMixedTrigger_module.cc:554** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CaloFilters/src/FilterEcalMixedTrigger_module.cc:556** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CaloFilters/src/FilterEcalMixedTrigger_module.cc:609** - Possible assignment (=) instead of comparison (==) in condition

#### division_by_zero (289 occurrences)

- **/workspace/CaloFilters/src/CaloLikelihood_module.cc:8** - Potential division by zero: Units not checked
- **/workspace/CaloFilters/src/CaloLikelihood_module.cc:9** - Potential division by zero: GlobalConstantsService not checked
- **/workspace/CaloFilters/src/CaloLikelihood_module.cc:11** - Potential division by zero: ConfigTools not checked
- **/workspace/CaloFilters/src/CaloLikelihood_module.cc:13** - Potential division by zero: CalorimeterGeom not checked
- **/workspace/CaloFilters/src/CaloLikelihood_module.cc:14** - Potential division by zero: CalorimeterGeom not checked
- **/workspace/CaloFilters/src/CaloLikelihood_module.cc:15** - Potential division by zero: CaloCluster not checked
- **/workspace/CaloFilters/src/CaloLikelihood_module.cc:17** - Potential division by zero: GeometryService not checked
- **/workspace/CaloFilters/src/CaloLikelihood_module.cc:18** - Potential division by zero: GeometryService not checked
- **/workspace/CaloFilters/src/CaloLikelihood_module.cc:20** - Potential division by zero: RecoDataProducts not checked
- **/workspace/CaloFilters/src/CaloLikelihood_module.cc:21** - Potential division by zero: RecoDataProducts not checked
- ... and 279 more

#### memory_leak (8 occurrences)

- **/workspace/CaloFilters/src/CaloLikelihood_module.cc:275** - Potential memory leak: new TriggerInfo without corresponding delete
- **/workspace/CaloFilters/src/CaloClusterCounterFilter_module.cc:134** - Potential memory leak: new TriggerInfo without corresponding delete
- **/workspace/CaloFilters/src/FilterEcalMVATrigger_module.cc:138** - Potential memory leak: new TMVA without corresponding delete
- **/workspace/CaloFilters/src/FilterEcalMVATrigger_module.cc:151** - Potential memory leak: new TriggerInfo without corresponding delete
- **/workspace/CaloFilters/src/CaloCosmicCalib_module.cc:110** - Potential memory leak: new TriggerInfo without corresponding delete
- **/workspace/CaloFilters/src/FilterEcalMixedTrigger_module.cc:289** - Potential memory leak: new TMVA without corresponding delete
- **/workspace/CaloFilters/src/FilterEcalMixedTrigger_module.cc:300** - Potential memory leak: new TMVA without corresponding delete
- **/workspace/CaloFilters/src/FilterEcalMixedTrigger_module.cc:320** - Potential memory leak: new TriggerInfo without corresponding delete

#### missing_error_handling (5 occurrences)

- **/workspace/CaloFilters/src/CaloLikelihood_module.cc:284** - getHandle/getValidHandle result not checked for validity
- **/workspace/CaloFilters/src/FilterEcalNNTrigger_module.cc:70** - getHandle/getValidHandle result not checked for validity
- **/workspace/CaloFilters/src/CaloClusterCounterFilter_module.cc:138** - getHandle/getValidHandle result not checked for validity
- **/workspace/CaloFilters/src/EcalTriggerPreselect_module.cc:222** - getHandle/getValidHandle result not checked for validity
- **/workspace/CaloFilters/src/CaloCosmicCalib_module.cc:114** - getHandle/getValidHandle result not checked for validity

#### uninitialized_variable (18 occurrences)

- **/workspace/CaloFilters/src/CaloClusterCounterFilter_module.cc:80** - Variable _diagLevel may be used uninitialized
- **/workspace/CaloFilters/src/CaloClusterCounterFilter_module.cc:81** - Variable _nProcess may be used uninitialized
- **/workspace/CaloFilters/src/CaloClusterCounterFilter_module.cc:82** - Variable _nPass may be used uninitialized
- **/workspace/CaloFilters/src/CaloClusterCounterFilter_module.cc:84** - Variable _minClEnergy may be used uninitialized
- **/workspace/CaloFilters/src/CaloClusterCounterFilter_module.cc:85** - Variable _maxClEnergy may be used uninitialized
- **/workspace/CaloFilters/src/CaloClusterCounterFilter_module.cc:86** - Variable _minClRadius may be used uninitialized
- **/workspace/CaloFilters/src/CaloClusterCounterFilter_module.cc:87** - Variable _minNCl may be used uninitialized
- **/workspace/CaloFilters/src/CaloClusterCounterFilter_module.cc:89** - Variable _minNCel may be used uninitialized
- **/workspace/CaloFilters/src/CaloClusterCounterFilter_module.cc:90** - Variable _maxNCel may be used uninitialized
- **/workspace/CaloFilters/src/EcalTriggerPreselect_module.cc:189** - Variable roId may be used uninitialized
- ... and 8 more


### CaloMC

Found 242 potential bugs:

#### array_bounds (51 occurrences)

- **/workspace/CaloMC/src/ShowerStepUtil.cc:19** - Array access n_[i] without bounds check
- **/workspace/CaloMC/src/ShowerStepUtil.cc:23** - Array access n_[i] without bounds check
- **/workspace/CaloMC/src/ShowerStepUtil.cc:24** - Array access eDepG4_[i] without bounds check
- **/workspace/CaloMC/src/ShowerStepUtil.cc:25** - Array access eDepVis_[i] without bounds check
- **/workspace/CaloMC/src/ShowerStepUtil.cc:26** - Array access pIn_[i] without bounds check
- **/workspace/CaloMC/src/ShowerStepUtil.cc:27** - Array access time_[i] without bounds check
- **/workspace/CaloMC/src/ShowerStepUtil.cc:28** - Array access x_[i] without bounds check
- **/workspace/CaloMC/src/ShowerStepUtil.cc:29** - Array access y_[i] without bounds check
- **/workspace/CaloMC/src/ShowerStepUtil.cc:30** - Array access z_[i] without bounds check
- **/workspace/CaloMC/src/ShowerStepUtil.cc:31** - Array access w_[i] without bounds check
- ... and 41 more

#### assignment_in_condition (10 occurrences)

- **/workspace/CaloMC/src/CaloPhotonPropagation.cc:70** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CaloMC/src/CaloNoiseSimGenerator.cc:126** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CaloMC/src/CaloWFExtractor.cc:17** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CaloMC/src/CaloWFExtractor.cc:37** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CaloMC/src/CaloShowerStepMaker_module.cc:361** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CaloMC/src/CaloDigiMaker_module.cc:233** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CaloMC/src/CaloDigiMaker_module.cc:280** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CaloMC/src/CaloDigiMaker_module.cc:324** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CaloMC/src/CaloHitTruthMatch_module.cc:207** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CaloMC/src/CaloHitTruthMatch_module.cc:265** - Possible assignment (=) instead of comparison (==) in condition

#### division_by_zero (159 occurrences)

- **/workspace/CaloMC/src/ShowerStepUtil.cc:1** - Potential division by zero: CaloMC not checked
- **/workspace/CaloMC/src/ShowerStepUtil.cc:2** - Potential division by zero: exception not checked
- **/workspace/CaloMC/src/ShowerStepUtil.cc:4** - Potential division by zero: Vector not checked
- **/workspace/CaloMC/src/ShowerStepUtil.cc:5** - Potential division by zero: Matrix not checked
- **/workspace/CaloMC/src/ShowerStepUtil.cc:16** - Potential division by zero: ShowerStepUtil not checked
- **/workspace/CaloMC/src/ShowerStepUtil.cc:37** - Potential division by zero: ShowerStepUtil not checked
- **/workspace/CaloMC/src/ShowerStepUtil.cc:48** - Potential division by zero: ShowerStepUtil not checked
- **/workspace/CaloMC/src/ShowerStepUtil.cc:50** - Potential division by zero: w_ not checked
- **/workspace/CaloMC/src/ShowerStepUtil.cc:51** - Potential division by zero: w_ not checked
- **/workspace/CaloMC/src/ShowerStepUtil.cc:52** - Potential division by zero: w_ not checked
- ... and 149 more

#### memory_leak (7 occurrences)

- **/workspace/CaloMC/src/CaloClusterTruthMatch_module.cc:64** - Potential memory leak: new CaloClusterMCCollection without corresponding delete
- **/workspace/CaloMC/src/CaloClusterTruthMatch_module.cc:65** - Potential memory leak: new CaloClusterMCTruthAssn without corresponding delete
- **/workspace/CaloMC/src/CaloShowerUpdater_module.cc:45** - Potential memory leak: new CaloShowerStepCollection without corresponding delete
- **/workspace/CaloMC/src/CaloHitTruthMatch_module.cc:143** - Potential memory leak: new CaloHitMCCollection without corresponding delete
- **/workspace/CaloMC/src/CaloHitTruthMatch_module.cc:144** - Potential memory leak: new CaloHitMCTruthAssn without corresponding delete
- **/workspace/CaloMC/src/CaloHitTruthMatch_module.cc:145** - Potential memory leak: new CaloShowerMCTruthAssn without corresponding delete
- **/workspace/CaloMC/src/CaloHitTruthMatch_module.cc:264** - Potential memory leak: new caloEdep without corresponding delete

#### missing_error_handling (9 occurrences)

- **/workspace/CaloMC/src/CaloClusterTruthMatch_module.cc:82** - getHandle/getValidHandle result not checked for validity
- **/workspace/CaloMC/src/CaloClusterTruthMatch_module.cc:86** - getHandle/getValidHandle result not checked for validity
- **/workspace/CaloMC/src/CaloShowerUpdater_module.cc:47** - getHandle/getValidHandle result not checked for validity
- **/workspace/CaloMC/src/CaloShowerUpdater_module.cc:51** - getHandle/getValidHandle result not checked for validity
- **/workspace/CaloMC/src/CaloShowerROMaker_module.cc:207** - getHandle/getValidHandle result not checked for validity
- **/workspace/CaloMC/src/CaloDigiMaker_module.cc:168** - getHandle/getValidHandle result not checked for validity
- **/workspace/CaloMC/src/CaloHitTruthMatch_module.cc:140** - getHandle/getValidHandle result not checked for validity
- **/workspace/CaloMC/src/CaloHitTruthMatch_module.cc:171** - getHandle/getValidHandle result not checked for validity
- **/workspace/CaloMC/src/CaloHitTruthMatch_module.cc:172** - getHandle/getValidHandle result not checked for validity

#### uninitialized_variable (3 occurrences)

- **/workspace/CaloMC/src/CaloShowerROMaker_module.cc:153** - Variable diagLevel_ may be used uninitialized
- **/workspace/CaloMC/src/CaloDigiMaker_module.cc:132** - Variable addNoise_ may be used uninitialized
- **/workspace/CaloMC/src/CaloDigiMaker_module.cc:136** - Variable diagLevel_ may be used uninitialized

#### unused_variable (3 occurrences)

- **/workspace/CaloMC/src/CaloNoiseSimGenerator.cc:77** - Variable l declared but possibly unused
- **/workspace/CaloMC/src/CaloNoiseSimGenerator.cc:140** - Variable in declared but possibly unused
- **/workspace/CaloMC/src/CaloWFExtractor.cc:16** - Variable i declared but possibly unused


### CaloReco

Found 208 potential bugs:

#### array_bounds (103 occurrences)

- **/workspace/CaloReco/src/CaloTemplateWFProcessor.cc:136** - Array access ywork[i-1] without bounds check
- **/workspace/CaloReco/src/CaloTemplateWFProcessor.cc:154** - Array access ywork[ipeak] without bounds check
- **/workspace/CaloReco/src/CaloTemplateWFProcessor.cc:155** - Array access xvec[ipeak] without bounds check
- **/workspace/CaloReco/src/CaloTemplateWFProcessor.cc:157** - Array access xvec[ipeak] without bounds check
- **/workspace/CaloReco/src/CaloTemplateWFProcessor.cc:179** - Array access ywork[i-1] without bounds check
- **/workspace/CaloReco/src/CaloTemplateWFProcessor.cc:190** - Array access ywork[j] without bounds check
- **/workspace/CaloReco/src/CaloTemplateWFProcessor.cc:201** - Array access ywork[ipeak] without bounds check
- **/workspace/CaloReco/src/CaloTemplateWFProcessor.cc:202** - Array access xvec[ipeak] without bounds check
- **/workspace/CaloReco/src/CaloTemplateWFProcessor.cc:214** - Array access yvec[istartPeak] without bounds check
- **/workspace/CaloReco/src/CaloTemplateWFProcessor.cc:215** - Array access yvec[istartPeak] without bounds check
- ... and 93 more

#### assignment_in_condition (4 occurrences)

- **/workspace/CaloReco/src/CaloTemplateWFProcessor.cc:151** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CaloReco/src/CaloTemplateWFProcessor.cc:198** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CaloReco/src/CaloTemplateWFProcessor.cc:342** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CaloReco/src/CaloTemplateWFProcessor.cc:403** - Possible assignment (=) instead of comparison (==) in condition

#### division_by_zero (86 occurrences)

- **/workspace/CaloReco/src/CaloTemplateWFProcessor.cc:1** - Potential division by zero: CaloReco not checked
- **/workspace/CaloReco/src/CaloTemplateWFProcessor.cc:2** - Potential division by zero: CaloReco not checked
- **/workspace/CaloReco/src/CaloTemplateWFProcessor.cc:3** - Potential division by zero: ConditionsService not checked
- **/workspace/CaloReco/src/CaloTemplateWFProcessor.cc:4** - Potential division by zero: TFileService not checked
- **/workspace/CaloReco/src/CaloTemplateWFProcessor.cc:5** - Potential division by zero: TFileDirectory not checked
- **/workspace/CaloReco/src/CaloTemplateWFProcessor.cc:67** - Potential division by zero: float not checked
- **/workspace/CaloReco/src/CaloTemplateWFProcessor.cc:99** - Potential division by zero: float not checked
- **/workspace/CaloReco/src/CaloTemplateWFProcessor.cc:126** - Potential division by zero: float not checked
- **/workspace/CaloReco/src/CaloTemplateWFProcessor.cc:171** - Potential division by zero: float not checked
- **/workspace/CaloReco/src/CaloTemplateWFProcessor.cc:220** - Potential division by zero: 3 not checked
- ... and 76 more

#### memory_leak (2 occurrences)

- **/workspace/CaloReco/src/CaloTemplateWFProcessor.cc:239** - Potential memory leak: new rising without corresponding delete
- **/workspace/CaloReco/src/CaloTemplateWFUtil.cc:322** - Potential memory leak: new TF1 without corresponding delete

#### missing_error_handling (5 occurrences)

- **/workspace/CaloReco/src/CaloHitMakerFast_module.cc:102** - getHandle/getValidHandle result not checked for validity
- **/workspace/CaloReco/src/CaloHitMakerFast_module.cc:106** - getHandle/getValidHandle result not checked for validity
- **/workspace/CaloReco/src/CaloRecoDigiMaker_module.cc:106** - getHandle/getValidHandle result not checked for validity
- **/workspace/CaloReco/src/CaloRecoDigiMaker_module.cc:109** - getHandle/getValidHandle result not checked for validity
- **/workspace/CaloReco/src/CaloHitMaker_module.cc:95** - getHandle/getValidHandle result not checked for validity

#### missing_return (1 occurrences)

- **/workspace/CaloReco/src/CaloTemplateWFUtil.cc:35** - Function may be missing return statement

#### uninitialized_variable (3 occurrences)

- **/workspace/CaloReco/src/CaloHitMakerFast_module.cc:92** - Variable diagLevel_ may be used uninitialized
- **/workspace/CaloReco/src/CaloRecoDigiMaker_module.cc:94** - Variable diagLevel_ may be used uninitialized
- **/workspace/CaloReco/src/CaloHitMaker_module.cc:59** - Variable diagLevel_ may be used uninitialized

#### unused_variable (4 occurrences)

- **/workspace/CaloReco/src/CaloTemplateWFProcessor.cc:393** - Variable j declared but possibly unused
- **/workspace/CaloReco/src/CaloTemplateWFUtil.cc:323** - Variable j declared but possibly unused
- **/workspace/CaloReco/src/CaloTemplateWFUtil.cc:338** - Variable i declared but possibly unused
- **/workspace/CaloReco/src/CaloRawWFProcessor.cc:102** - Variable i declared but possibly unused


### CaloVisualizer

Found 24 potential bugs:

#### array_bounds (15 occurrences)

- **/workspace/CaloVisualizer/src/THMu2eCaloDisk.cc:123** - Array access tformula[i] without bounds check
- **/workspace/CaloVisualizer/src/THMu2eCaloDisk.cc:125** - Array access tformula[i-1] without bounds check
- **/workspace/CaloVisualizer/src/THMu2eCaloDisk.cc:128** - Array access tformula[i] without bounds check
- **/workspace/CaloVisualizer/src/THMu2eCaloDisk.cc:129** - Array access tformula[i] without bounds check
- **/workspace/CaloVisualizer/src/THMu2eCaloDisk.cc:130** - Array access tformula[i] without bounds check
- **/workspace/CaloVisualizer/src/THMu2eCaloDisk.cc:131** - Array access tformula[i] without bounds check
- **/workspace/CaloVisualizer/src/THMu2eCaloDisk.cc:209** - Array access cryId_map[thisChannel.cryId] without bounds check
- **/workspace/CaloVisualizer/src/THMu2eCaloDisk.cc:226** - Array access x[5] without bounds check
- **/workspace/CaloVisualizer/src/THMu2eCaloDisk.cc:227** - Array access y[5] without bounds check
- **/workspace/CaloVisualizer/src/THMu2eCaloDisk.cc:233** - Array access cryId_map[thisChannel.cryId] without bounds check
- ... and 5 more

#### division_by_zero (5 occurrences)

- **/workspace/CaloVisualizer/src/THMu2eCaloDisk.cc:17** - Potential division by zero: ConfigTools not checked
- **/workspace/CaloVisualizer/src/THMu2eCaloDisk.cc:18** - Potential division by zero: DataProducts not checked
- **/workspace/CaloVisualizer/src/THMu2eCaloDisk.cc:20** - Potential division by zero: CaloVisualizer not checked
- **/workspace/CaloVisualizer/src/THMu2eCaloDisk.cc:231** - Potential division by zero: 03d not checked
- **/workspace/CaloVisualizer/src/THMu2eCaloDisk.cc:253** - Potential division by zero: 2 not checked

#### memory_leak (3 occurrences)

- **/workspace/CaloVisualizer/src/THMu2eCaloDisk.cc:160** - Potential memory leak: new TList without corresponding delete
- **/workspace/CaloVisualizer/src/THMu2eCaloDisk.cc:166** - Potential memory leak: new THMu2eCaloDiskBin without corresponding delete
- **/workspace/CaloVisualizer/src/THMu2eCaloDisk.cc:229** - Potential memory leak: new TGraph without corresponding delete

#### missing_return (1 occurrences)

- **/workspace/CaloVisualizer/src/THMu2eCaloDisk.cc:130** - Function may be missing return statement


### CalorimeterGeom

Found 107 potential bugs:

#### array_bounds (49 occurrences)

- **/workspace/CalorimeterGeom/src/Disk.cc:71** - Array access mapToCrystal_[mapIdx] without bounds check
- **/workspace/CalorimeterGeom/src/Disk.cc:101** - Array access mapToCrystal_[mapIdx] without bounds check
- **/workspace/CalorimeterGeom/src/Disk.cc:119** - Array access apexX[i-1] without bounds check
- **/workspace/CalorimeterGeom/src/Disk.cc:120** - Array access apexX[i] without bounds check
- **/workspace/CalorimeterGeom/src/Disk.cc:144** - Array access crystalToMap_[cryId] without bounds check
- **/workspace/CalorimeterGeom/src/Disk.cc:145** - Array access rowToCrystalId[irow] without bounds check
- **/workspace/CalorimeterGeom/src/Disk.cc:154** - Array access crystalList_[i] without bounds check
- **/workspace/CalorimeterGeom/src/Disk.cc:155** - Array access crystalList_[j] without bounds check
- **/workspace/CalorimeterGeom/src/Disk.cc:161** - Array access crystalList_[cryIdx] without bounds check
- **/workspace/CalorimeterGeom/src/Disk.cc:164** - Array access crystalList_[cryIdx] without bounds check
- ... and 39 more

#### assignment_in_condition (2 occurrences)

- **/workspace/CalorimeterGeom/src/Disk.cc:297** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CalorimeterGeom/src/SquareShiftMapper.cc:115** - Possible assignment (=) instead of comparison (==) in condition

#### division_by_zero (53 occurrences)

- **/workspace/CalorimeterGeom/src/Disk.cc:9** - Potential division by zero: CalorimeterGeom not checked
- **/workspace/CalorimeterGeom/src/Disk.cc:10** - Potential division by zero: CalorimeterGeom not checked
- **/workspace/CalorimeterGeom/src/Disk.cc:11** - Potential division by zero: CalorimeterGeom not checked
- **/workspace/CalorimeterGeom/src/Disk.cc:12** - Potential division by zero: exception not checked
- **/workspace/CalorimeterGeom/src/Disk.cc:14** - Potential division by zero: Vector not checked
- **/workspace/CalorimeterGeom/src/Disk.cc:15** - Potential division by zero: Vector not checked
- **/workspace/CalorimeterGeom/src/Disk.cc:49** - Potential division by zero: nominalCellSize_ not checked
- **/workspace/CalorimeterGeom/src/Disk.cc:84** - Potential division by zero: nominalCellSize_ not checked
- **/workspace/CalorimeterGeom/src/Disk.cc:98** - Potential division by zero: nominalCellSize_ not checked
- **/workspace/CalorimeterGeom/src/Disk.cc:161** - Potential division by zero: 2 not checked
- ... and 43 more

#### memory_leak (1 occurrences)

- **/workspace/CalorimeterGeom/src/Disk.cc:36** - Potential memory leak: new SquareShiftMapper without corresponding delete

#### unused_variable (2 occurrences)

- **/workspace/CalorimeterGeom/src/SquareMapper.cc:120** - Variable iseg declared but possibly unused
- **/workspace/CalorimeterGeom/src/SquareShiftMapper.cc:140** - Variable iseg declared but possibly unused


### CommonMC

Found 308 potential bugs:

#### array_bounds (15 occurrences)

- **/workspace/CommonMC/src/MakeSurfaceSteps_module.cc:57** - Array access vdmap_[VirtualDetectorId(VirtualDetectorId::TT_FrontHollow)] without bounds check
- **/workspace/CommonMC/src/MakeSurfaceSteps_module.cc:58** - Array access vdmap_[VirtualDetectorId(VirtualDetectorId::TT_Mid)] without bounds check
- **/workspace/CommonMC/src/MakeSurfaceSteps_module.cc:59** - Array access vdmap_[VirtualDetectorId(VirtualDetectorId::TT_MidInner)] without bounds check
- **/workspace/CommonMC/src/MakeSurfaceSteps_module.cc:60** - Array access vdmap_[VirtualDetectorId(VirtualDetectorId::TT_Back)] without bounds check
- **/workspace/CommonMC/src/MakeSurfaceSteps_module.cc:61** - Array access vdmap_[VirtualDetectorId(VirtualDetectorId::TT_OutSurf)] without bounds check
- **/workspace/CommonMC/src/MakeSurfaceSteps_module.cc:62** - Array access vdmap_[VirtualDetectorId(VirtualDetectorId::TT_InSurf)] without bounds check
- **/workspace/CommonMC/src/GammaConversionPoints_module.cc:190** - Array access daughters[i] without bounds check
- **/workspace/CommonMC/src/SelectRecoMC_module.cc:214** - Array access spcc[isp] without bounds check
- **/workspace/CommonMC/src/SelectRecoMC_module.cc:234** - Array access spcc[isp] without bounds check
- **/workspace/CommonMC/src/SelectRecoMC_module.cc:255** - Array access spcc[isp] without bounds check
- ... and 5 more

#### assignment_in_condition (3 occurrences)

- **/workspace/CommonMC/src/MakeSurfaceSteps_module.cc:75** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CommonMC/src/FindMCPrimary_module.cc:58** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CommonMC/src/FindMCPrimary_module.cc:65** - Possible assignment (=) instead of comparison (==) in condition

#### division_by_zero (218 occurrences)

- **/workspace/CommonMC/src/MakeSurfaceSteps_module.cc:4** - Potential division by zero: 2024 not checked
- **/workspace/CommonMC/src/MakeSurfaceSteps_module.cc:6** - Potential division by zero: Framework not checked
- **/workspace/CommonMC/src/MakeSurfaceSteps_module.cc:7** - Potential division by zero: Framework not checked
- **/workspace/CommonMC/src/MakeSurfaceSteps_module.cc:8** - Potential division by zero: Framework not checked
- **/workspace/CommonMC/src/MakeSurfaceSteps_module.cc:9** - Potential division by zero: exception not checked
- **/workspace/CommonMC/src/MakeSurfaceSteps_module.cc:10** - Potential division by zero: types not checked
- **/workspace/CommonMC/src/MakeSurfaceSteps_module.cc:11** - Potential division by zero: Utilities not checked
- **/workspace/CommonMC/src/MakeSurfaceSteps_module.cc:12** - Potential division by zero: MessageLogger not checked
- **/workspace/CommonMC/src/MakeSurfaceSteps_module.cc:13** - Potential division by zero: GlobalConstantsService not checked
- **/workspace/CommonMC/src/MakeSurfaceSteps_module.cc:14** - Potential division by zero: DataProducts not checked
- ... and 208 more

#### memory_leak (29 occurrences)

- **/workspace/CommonMC/src/MakeSurfaceSteps_module.cc:68** - Potential memory leak: new SurfaceStepCollection without corresponding delete
- **/workspace/CommonMC/src/MakeSurfaceSteps_module.cc:109** - Potential memory leak: new SurfaceStep without corresponding delete
- **/workspace/CommonMC/src/MakeSurfaceSteps_module.cc:155** - Potential memory leak: new SurfaceStep without corresponding delete
- **/workspace/CommonMC/src/CosmicTimeOffset_module.cc:95** - Potential memory leak: new SimTimeOffset without corresponding delete
- **/workspace/CommonMC/src/CosmicTimeOffset_module.cc:104** - Potential memory leak: new GenParticleCollection without corresponding delete
- **/workspace/CommonMC/src/StoppedParticlesFinder_module.cc:2** - Potential memory leak: new SimParticlePtrCollection without corresponding delete
- **/workspace/CommonMC/src/StoppedParticlesFinder_module.cc:208** - Potential memory leak: new SimParticlePtrCollection without corresponding delete
- **/workspace/CommonMC/src/EventWindowMarkerProducer_module.cc:101** - Potential memory leak: new EventWindowMarker without corresponding delete
- **/workspace/CommonMC/src/EventWindowMarkerProducer_module.cc:102** - Potential memory leak: new ProtonBunchTimeMC without corresponding delete
- **/workspace/CommonMC/src/EventWindowMarkerProducer_module.cc:103** - Potential memory leak: new ProtonBunchTime without corresponding delete
- ... and 19 more

#### missing_error_handling (19 occurrences)

- **/workspace/CommonMC/src/MakeSurfaceSteps_module.cc:70** - getHandle/getValidHandle result not checked for validity
- **/workspace/CommonMC/src/StoppedParticlesFinder_module.cc:211** - getHandle/getValidHandle result not checked for validity
- **/workspace/CommonMC/src/SurfaceStepDiag_module.cc:110** - getHandle/getValidHandle result not checked for validity
- **/workspace/CommonMC/src/FindMCPrimary_module.cc:80** - getHandle/getValidHandle result not checked for validity
- **/workspace/CommonMC/src/ProtonBunchTimeMCFromProtonBunchTime_module.cc:45** - getHandle/getValidHandle result not checked for validity
- **/workspace/CommonMC/src/InFlightStepDumper_module.cc:59** - getHandle/getValidHandle result not checked for validity
- **/workspace/CommonMC/src/SimParticleDaughterSelector_module.cc:93** - getHandle/getValidHandle result not checked for validity
- **/workspace/CommonMC/src/SelectRecoMC_module.cc:178** - getHandle/getValidHandle result not checked for validity
- **/workspace/CommonMC/src/SelectRecoMC_module.cc:180** - getHandle/getValidHandle result not checked for validity
- **/workspace/CommonMC/src/SelectRecoMC_module.cc:182** - getHandle/getValidHandle result not checked for validity
- ... and 9 more

#### uninitialized_variable (24 occurrences)

- **/workspace/CommonMC/src/MakeSurfaceSteps_module.cc:39** - Variable debug_ may be used uninitialized
- **/workspace/CommonMC/src/MakeSurfaceSteps_module.cc:40** - Variable maxdgap_ may be used uninitialized
- **/workspace/CommonMC/src/MakeSurfaceSteps_module.cc:41** - Variable maxtgap_ may be used uninitialized
- **/workspace/CommonMC/src/CosmicTimeOffset_module.cc:51** - Variable addTimeOffset_ may be used uninitialized
- **/workspace/CommonMC/src/CosmicTimeOffset_module.cc:52** - Variable verbosityLevel_ may be used uninitialized
- **/workspace/CommonMC/src/CosmicTimeOffset_module.cc:53** - Variable intervalStart_ may be used uninitialized
- **/workspace/CommonMC/src/CosmicTimeOffset_module.cc:54** - Variable intervalEnd_ may be used uninitialized
- **/workspace/CommonMC/src/StoppedParticlesFinder_module.cc:109** - Variable numTotalParticles_ may be used uninitialized
- **/workspace/CommonMC/src/StoppedParticlesFinder_module.cc:110** - Variable numStageParticles_ may be used uninitialized
- **/workspace/CommonMC/src/StoppedParticlesFinder_module.cc:111** - Variable numRequestedTypeStops_ may be used uninitialized
- ... and 14 more


### CommonReco

Found 54 potential bugs:

#### array_bounds (4 occurrences)

- **/workspace/CommonReco/src/SelectReco_module.cc:172** - Array access sdc[sdindex] without bounds check
- **/workspace/CommonReco/src/SelectReco_module.cc:173** - Array access sdadcc[sdindex] without bounds check
- **/workspace/CommonReco/src/SelectReco_module.cc:244** - Array access indices[iindex] without bounds check
- **/workspace/CommonReco/src/SelectReco_module.cc:271** - Array access ccc[icc] without bounds check

#### division_by_zero (32 occurrences)

- **/workspace/CommonReco/src/SelectReco_module.cc:8** - Potential division by zero: types not checked
- **/workspace/CommonReco/src/SelectReco_module.cc:9** - Potential division by zero: types not checked
- **/workspace/CommonReco/src/SelectReco_module.cc:10** - Potential division by zero: Utilities not checked
- **/workspace/CommonReco/src/SelectReco_module.cc:11** - Potential division by zero: Persistency not checked
- **/workspace/CommonReco/src/SelectReco_module.cc:12** - Potential division by zero: Framework not checked
- **/workspace/CommonReco/src/SelectReco_module.cc:13** - Potential division by zero: Framework not checked
- **/workspace/CommonReco/src/SelectReco_module.cc:14** - Potential division by zero: Framework not checked
- **/workspace/CommonReco/src/SelectReco_module.cc:15** - Potential division by zero: Framework not checked
- **/workspace/CommonReco/src/SelectReco_module.cc:17** - Potential division by zero: DataProducts not checked
- **/workspace/CommonReco/src/SelectReco_module.cc:18** - Potential division by zero: DataProducts not checked
- ... and 22 more

#### memory_leak (12 occurrences)

- **/workspace/CommonReco/src/SelectReco_module.cc:128** - Potential memory leak: new RecoCount without corresponding delete
- **/workspace/CommonReco/src/SelectReco_module.cc:145** - Potential memory leak: new StrawDigiCollection without corresponding delete
- **/workspace/CommonReco/src/SelectReco_module.cc:146** - Potential memory leak: new StrawDigiADCWaveformCollection without corresponding delete
- **/workspace/CommonReco/src/SelectReco_module.cc:148** - Potential memory leak: new IndexMap without corresponding delete
- **/workspace/CommonReco/src/SelectReco_module.cc:199** - Potential memory leak: new Crv without corresponding delete
- **/workspace/CommonReco/src/SelectReco_module.cc:200** - Potential memory leak: new CrvDigiCollection without corresponding delete
- **/workspace/CommonReco/src/SelectReco_module.cc:201** - Potential memory leak: new CrvRecoPulseCollection without corresponding delete
- **/workspace/CommonReco/src/SelectReco_module.cc:202** - Potential memory leak: new CrvCoincidenceClusterCollection without corresponding delete
- **/workspace/CommonReco/src/SelectReco_module.cc:203** - Potential memory leak: new IndexMap without corresponding delete
- **/workspace/CommonReco/src/SelectReco_module.cc:250** - Potential memory leak: new data without corresponding delete
- ... and 2 more

#### missing_error_handling (3 occurrences)

- **/workspace/CommonReco/src/SelectReco_module.cc:138** - getHandle/getValidHandle result not checked for validity
- **/workspace/CommonReco/src/SelectReco_module.cc:140** - getHandle/getValidHandle result not checked for validity
- **/workspace/CommonReco/src/SelectReco_module.cc:142** - getHandle/getValidHandle result not checked for validity

#### uninitialized_variable (3 occurrences)

- **/workspace/CommonReco/src/SelectReco_module.cc:81** - Variable debug_ may be used uninitialized
- **/workspace/CommonReco/src/SelectReco_module.cc:84** - Variable ccme_ may be used uninitialized
- **/workspace/CommonReco/src/SelectReco_module.cc:85** - Variable saveunused_ may be used uninitialized


### Compression

Found 212 potential bugs:

#### array_bounds (31 occurrences)

- **/workspace/Compression/src/CompressDigiMCs_module.cc:317** - Array access _newStepPointMCs[i_instance] without bounds check
- **/workspace/Compression/src/CompressDigiMCs_module.cc:318** - Array access _newStepPointMCsPID[i_instance] without bounds check
- **/workspace/Compression/src/CompressDigiMCs_module.cc:319** - Array access _newStepPointMCGetter[i_instance] without bounds check
- **/workspace/Compression/src/CompressDigiMCs_module.cc:349** - Array access _simParticlesToKeep[i_product_id] without bounds check
- **/workspace/Compression/src/CompressDigiMCs_module.cc:472** - Array access _crvStepsMap[fake_old_ptr] without bounds check
- **/workspace/Compression/src/CompressDigiMCs_module.cc:488** - Array access _oldCaloShowerStepGetter[i_product_id] without bounds check
- **/workspace/Compression/src/CompressDigiMCs_module.cc:491** - Array access _oldCaloShowerStepGetter[i_product_id] without bounds check
- **/workspace/Compression/src/CompressDigiMCs_module.cc:493** - Array access caloShowerStepRemap[oldShowerStepPtr] without bounds check
- **/workspace/Compression/src/CompressDigiMCs_module.cc:590** - Array access _simParticlesToKeep[i_product_id] without bounds check
- **/workspace/Compression/src/CompressDigiMCs_module.cc:591** - Array access _simParticlesToKeep[i_product_id] without bounds check
- ... and 21 more

#### assignment_in_condition (53 occurrences)

- **/workspace/Compression/src/CompressDigiMCs_module.cc:294** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Compression/src/CompressDigiMCs_module.cc:302** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Compression/src/CompressDigiMCs_module.cc:305** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Compression/src/CompressDigiMCs_module.cc:368** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Compression/src/CompressDigiMCs_module.cc:373** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Compression/src/CompressDigiMCs_module.cc:379** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Compression/src/CompressDigiMCs_module.cc:396** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Compression/src/CompressDigiMCs_module.cc:401** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Compression/src/CompressDigiMCs_module.cc:414** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Compression/src/CompressDigiMCs_module.cc:429** - Possible assignment (=) instead of comparison (==) in condition
- ... and 43 more

#### division_by_zero (64 occurrences)

- **/workspace/Compression/src/CompressDigiMCs_module.cc:17** - Potential division by zero: Framework not checked
- **/workspace/Compression/src/CompressDigiMCs_module.cc:18** - Potential division by zero: Framework not checked
- **/workspace/Compression/src/CompressDigiMCs_module.cc:19** - Potential division by zero: Framework not checked
- **/workspace/Compression/src/CompressDigiMCs_module.cc:20** - Potential division by zero: Framework not checked
- **/workspace/Compression/src/CompressDigiMCs_module.cc:21** - Potential division by zero: Framework not checked
- **/workspace/Compression/src/CompressDigiMCs_module.cc:22** - Potential division by zero: Utilities not checked
- **/workspace/Compression/src/CompressDigiMCs_module.cc:23** - Potential division by zero: ParameterSet not checked
- **/workspace/Compression/src/CompressDigiMCs_module.cc:24** - Potential division by zero: types not checked
- **/workspace/Compression/src/CompressDigiMCs_module.cc:25** - Potential division by zero: MessageLogger not checked
- **/workspace/Compression/src/CompressDigiMCs_module.cc:26** - Potential division by zero: TFileService not checked
- ... and 54 more

#### memory_leak (55 occurrences)

- **/workspace/Compression/src/CompressDigiMCs_module.cc:6** - Potential memory leak: new StrawDigiMC without corresponding delete
- **/workspace/Compression/src/CompressDigiMCs_module.cc:10** - Potential memory leak: new CaloShowerStep without corresponding delete
- **/workspace/Compression/src/CompressDigiMCs_module.cc:177** - Potential memory leak: new output without corresponding delete
- **/workspace/Compression/src/CompressDigiMCs_module.cc:190** - Potential memory leak: new locations without corresponding delete
- **/workspace/Compression/src/CompressDigiMCs_module.cc:313** - Potential memory leak: new StrawDigiMCCollection without corresponding delete
- **/workspace/Compression/src/CompressDigiMCs_module.cc:314** - Potential memory leak: new CrvDigiMCCollection without corresponding delete
- **/workspace/Compression/src/CompressDigiMCs_module.cc:317** - Potential memory leak: new StepPointMCCollection without corresponding delete
- **/workspace/Compression/src/CompressDigiMCs_module.cc:321** - Potential memory leak: new StrawGasStepCollection without corresponding delete
- **/workspace/Compression/src/CompressDigiMCs_module.cc:325** - Potential memory leak: new CrvStepCollection without corresponding delete
- **/workspace/Compression/src/CompressDigiMCs_module.cc:329** - Potential memory leak: new SurfaceStepCollection without corresponding delete
- ... and 45 more

#### missing_error_handling (6 occurrences)

- **/workspace/Compression/src/CompressDigiMCs_module.cc:345** - getHandle/getValidHandle result not checked for validity
- **/workspace/Compression/src/CompressDigiMCs_module.cc:455** - getHandle/getValidHandle result not checked for validity
- **/workspace/Compression/src/CompressDigiMCs_module.cc:486** - getHandle/getValidHandle result not checked for validity
- **/workspace/Compression/src/CompressDigiMCs_module.cc:536** - getHandle/getValidHandle result not checked for validity
- **/workspace/Compression/src/CompressDigiMCs_module.cc:561** - getHandle/getValidHandle result not checked for validity
- **/workspace/Compression/src/CompressDigiMCs_module.cc:588** - getHandle/getValidHandle result not checked for validity

#### missing_return (2 occurrences)

- **/workspace/Compression/src/CompressDetStepMCs_module.cc:638** - Function may be missing return statement
- **/workspace/Compression/src/CompressDetStepMCs_module.cc:671** - Function may be missing return statement

#### uninitialized_variable (1 occurrences)

- **/workspace/Compression/src/CompressDigiMCsCheck_module.cc:59** - Variable _checkTrackerDuplicateSteps may be used uninitialized


### ConditionsService

Found 13 potential bugs:

#### array_bounds (1 occurrences)

- **/workspace/ConditionsService/src/ConditionsService.cc:66** - Array access _entities[typeid(ENTITY).name()] without bounds check

#### division_by_zero (11 occurrences)

- **/workspace/ConditionsService/src/CalorimeterCalibrations.cc:7** - Potential division by zero: ConditionsService not checked
- **/workspace/ConditionsService/src/CalorimeterCalibrations.cc:8** - Potential division by zero: ConfigTools not checked
- **/workspace/ConditionsService/src/CalorimeterCalibrations.cc:9** - Potential division by zero: ConfigTools not checked
- **/workspace/ConditionsService/src/CalorimeterCalibrations.cc:33** - Potential division by zero: MeV not checked
- **/workspace/ConditionsService/src/ConditionsService_service.cc:5** - Potential division by zero: Framework not checked
- **/workspace/ConditionsService/src/ConditionsService_service.cc:6** - Potential division by zero: ConditionsService not checked
- **/workspace/ConditionsService/src/ConditionsService.cc:13** - Potential division by zero: MessageLogger not checked
- **/workspace/ConditionsService/src/ConditionsService.cc:14** - Potential division by zero: Framework not checked
- **/workspace/ConditionsService/src/ConditionsService.cc:17** - Potential division by zero: ConditionsService not checked
- **/workspace/ConditionsService/src/ConditionsService.cc:18** - Potential division by zero: GeometryService not checked
- ... and 1 more

#### memory_leak (1 occurrences)

- **/workspace/ConditionsService/src/ConditionsService.cc:82** - Potential memory leak: new CalorimeterCalibrations without corresponding delete


### ConfigTools

Found 85 potential bugs:

#### array_bounds (25 occurrences)

- **/workspace/ConfigTools/src/SimpleConfig.cc:128** - Array access counter[name] without bounds check
- **/workspace/ConfigTools/src/SimpleConfig.cc:420** - Array access tmp[0] without bounds check
- **/workspace/ConfigTools/src/SimpleConfig.cc:429** - Array access tmp[0] without bounds check
- **/workspace/ConfigTools/src/SimpleConfig.cc:438** - Array access tmp[0] without bounds check
- **/workspace/ConfigTools/src/SimpleConfig.cc:447** - Array access tmp[0] without bounds check
- **/workspace/ConfigTools/src/SimpleConfig.cc:475** - Array access _image[i] without bounds check
- **/workspace/ConfigTools/src/SimpleConfig.cc:477** - Array access _image[i] without bounds check
- **/workspace/ConfigTools/src/SimpleConfig.cc:494** - Array access _image[i] without bounds check
- **/workspace/ConfigTools/src/SimpleConfig.cc:495** - Array access _image[i] without bounds check
- **/workspace/ConfigTools/src/SimpleConfig.cc:645** - Array access _rmap[key] without bounds check
- ... and 15 more

#### assignment_in_condition (13 occurrences)

- **/workspace/ConfigTools/src/SimpleConfig.cc:641** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/ConfigTools/src/SimpleConfig.cc:764** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/ConfigTools/src/SimpleConfig.cc:1086** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/ConfigTools/src/SimpleConfig.cc:1090** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/ConfigTools/src/SimpleConfig.cc:1094** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/ConfigTools/src/requireUniqueKey.cc:44** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/ConfigTools/src/SimpleConfigRecord.cc:233** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/ConfigTools/src/SimpleConfigRecord.cc:293** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/ConfigTools/src/SimpleConfigRecord.cc:328** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/ConfigTools/src/SimpleConfigRecord.cc:337** - Possible assignment (=) instead of comparison (==) in condition
- ... and 3 more

#### division_by_zero (18 occurrences)

- **/workspace/ConfigTools/src/SimpleConfig.cc:21** - Potential division by zero: functional not checked
- **/workspace/ConfigTools/src/SimpleConfig.cc:24** - Potential division by zero: exception not checked
- **/workspace/ConfigTools/src/SimpleConfig.cc:25** - Potential division by zero: MessageLogger not checked
- **/workspace/ConfigTools/src/SimpleConfig.cc:28** - Potential division by zero: ConfigTools not checked
- **/workspace/ConfigTools/src/SimpleConfig.cc:29** - Potential division by zero: ConfigTools not checked
- **/workspace/ConfigTools/src/SimpleConfig.cc:30** - Potential division by zero: ConfigTools not checked
- **/workspace/ConfigTools/src/SimpleConfig.cc:31** - Potential division by zero: GeneralUtilities not checked
- **/workspace/ConfigTools/src/requireUniqueKey.cc:11** - Potential division by zero: MessageLogger not checked
- **/workspace/ConfigTools/src/requireUniqueKey.cc:12** - Potential division by zero: Utilities not checked
- **/workspace/ConfigTools/src/requireUniqueKey.cc:15** - Potential division by zero: ConfigTools not checked
- ... and 8 more

#### memory_leak (6 occurrences)

- **/workspace/ConfigTools/src/SimpleConfig.cc:619** - Potential memory leak: new SimpleConfigRecord without corresponding delete
- **/workspace/ConfigTools/src/SimpleConfig.cc:656** - Potential memory leak: new record without corresponding delete
- **/workspace/ConfigTools/src/SimpleConfigRecord.cc:385** - Potential memory leak: new stringBuffer without corresponding delete
- **/workspace/ConfigTools/src/SimpleConfigRecord.cc:427** - Potential memory leak: new item without corresponding delete
- **/workspace/ConfigTools/src/SimpleConfigRecord.cc:434** - Potential memory leak: new item without corresponding delete
- **/workspace/ConfigTools/src/SimpleConfigRecord.cc:449** - Potential memory leak: new item without corresponding delete

#### missing_return (17 occurrences)

- **/workspace/ConfigTools/src/requireUniqueKey.cc:51** - Function may be missing return statement
- **/workspace/ConfigTools/src/SimpleConfigRecord.cc:156** - Function may be missing return statement
- **/workspace/ConfigTools/src/SimpleConfigRecord.cc:196** - Function may be missing return statement
- **/workspace/ConfigTools/src/SimpleConfigRecord.cc:198** - Function may be missing return statement
- **/workspace/ConfigTools/src/SimpleConfigRecord.cc:419** - Function may be missing return statement
- **/workspace/ConfigTools/src/SimpleConfigRecord.cc:428** - Function may be missing return statement
- **/workspace/ConfigTools/src/SimpleConfigRecord.cc:435** - Function may be missing return statement
- **/workspace/ConfigTools/src/SimpleConfigRecord.cc:459** - Function may be missing return statement
- **/workspace/ConfigTools/src/SimpleConfigRecord.cc:468** - Function may be missing return statement
- **/workspace/ConfigTools/src/SimpleConfigRecord.cc:476** - Function may be missing return statement
- ... and 7 more

#### uninitialized_variable (6 occurrences)

- **/workspace/ConfigTools/src/SimpleConfig.cc:812** - Variable count may be used uninitialized
- **/workspace/ConfigTools/src/SimpleConfig.cc:813** - Variable nValues may be used uninitialized
- **/workspace/ConfigTools/src/SimpleConfig.cc:815** - Variable accessedCount may be used uninitialized
- **/workspace/ConfigTools/src/SimpleConfig.cc:816** - Variable accessednValues may be used uninitialized
- **/workspace/ConfigTools/src/SimpleConfigRecord.cc:664** - Variable i may be used uninitialized
- **/workspace/ConfigTools/src/SimpleConfigRecord.cc:681** - Variable d may be used uninitialized


### CosmicRayShieldGeom

Found 39 potential bugs:

#### array_bounds (21 occurrences)

- **/workspace/CosmicRayShieldGeom/src/CosmicRayShield.cc:20** - Array access _scintillatorShields[s] without bounds check
- **/workspace/CosmicRayShieldGeom/src/CosmicRayShield.cc:36** - Array access minPoint[i] without bounds check
- **/workspace/CosmicRayShieldGeom/src/CosmicRayShield.cc:37** - Array access maxPoint[i] without bounds check
- **/workspace/CosmicRayShieldGeom/src/CosmicRayShield.cc:45** - Array access position[i] without bounds check
- **/workspace/CosmicRayShieldGeom/src/CosmicRayShield.cc:46** - Array access position[i] without bounds check
- **/workspace/CosmicRayShieldGeom/src/CosmicRayShield.cc:47** - Array access minPoint[i] without bounds check
- **/workspace/CosmicRayShieldGeom/src/CosmicRayShield.cc:48** - Array access maxPoint[i] without bounds check
- **/workspace/CosmicRayShieldGeom/src/CosmicRayShield.cc:66** - Array access halfLengths[i] without bounds check
- **/workspace/CosmicRayShieldGeom/src/CosmicRayShield.cc:79** - Array access position[i] without bounds check
- **/workspace/CosmicRayShieldGeom/src/CRSScintillatorBarDetail.cc:40** - Array access worldPosition[_localToWorld[i] without bounds check
- ... and 11 more

#### division_by_zero (18 occurrences)

- **/workspace/CosmicRayShieldGeom/src/CRSScintillatorModule.cc:11** - Potential division by zero: CosmicRayShieldGeom not checked
- **/workspace/CosmicRayShieldGeom/src/CRSAluminumSheet.cc:7** - Potential division by zero: CosmicRayShieldGeom not checked
- **/workspace/CosmicRayShieldGeom/src/CRSFEB.cc:7** - Potential division by zero: CosmicRayShieldGeom not checked
- **/workspace/CosmicRayShieldGeom/src/CosmicRayShield.cc:8** - Potential division by zero: CosmicRayShieldGeom not checked
- **/workspace/CosmicRayShieldGeom/src/CosmicRayShield.cc:66** - Potential division by zero: 2 not checked
- **/workspace/CosmicRayShieldGeom/src/CosmicRayShield.cc:79** - Potential division by zero: 2 not checked
- **/workspace/CosmicRayShieldGeom/src/CRSScintillatorLayer.cc:11** - Potential division by zero: CosmicRayShieldGeom not checked
- **/workspace/CosmicRayShieldGeom/src/CRSScintillatorLayer.cc:12** - Potential division by zero: CosmicRayShieldGeom not checked
- **/workspace/CosmicRayShieldGeom/src/CRSScintillatorBar.cc:9** - Potential division by zero: CosmicRayShieldGeom not checked
- **/workspace/CosmicRayShieldGeom/src/CRSScintillatorBar.cc:10** - Potential division by zero: CosmicRayShieldGeom not checked
- ... and 8 more


### CosmicReco

Found 1311 potential bugs:

#### array_bounds (488 occurrences)

- **/workspace/CosmicReco/src/CosmicShowerFilter_module.cc:96** - Array access tccol[index] without bounds check
- **/workspace/CosmicReco/src/CosmicShowerFilter_module.cc:103** - Array access it[0] without bounds check
- **/workspace/CosmicReco/src/CosmicShowerFilter_module.cc:110** - Array access shcol[0] without bounds check
- **/workspace/CosmicReco/src/CosmicShowerFilter_module.cc:111** - Array access shcol[0] without bounds check
- **/workspace/CosmicReco/src/CosmicShowerFilter_module.cc:114** - Array access shcol[ich] without bounds check
- **/workspace/CosmicReco/src/CosmicShowerFilter_module.cc:121** - Array access straws[panelid] without bounds check
- **/workspace/CosmicReco/src/CosmicShowerFilter_module.cc:135** - Array access straws[i] without bounds check
- **/workspace/CosmicReco/src/CosmicShowerFilter_module.cc:136** - Array access straws[i] without bounds check
- **/workspace/CosmicReco/src/CosmicShowerFilter_module.cc:139** - Array access straws[i] without bounds check
- **/workspace/CosmicReco/src/CosmicShowerFilter_module.cc:141** - Array access straws[i] without bounds check
- ... and 478 more

#### assignment_in_condition (21 occurrences)

- **/workspace/CosmicReco/src/CosmicTrackFinder_module.cc:178** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CosmicReco/src/CosmicTrackFinder_module.cc:216** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CosmicReco/src/CosmicTrackFinder_module.cc:308** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CosmicReco/src/CosmicSeedFilter_module.cc:99** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CosmicReco/src/CosmicTrackFit.cc:500** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CosmicReco/src/CosmicMuonInfo_module.cc:379** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CosmicReco/src/SimpleTimeCluster_module.cc:160** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CosmicReco/src/SimpleTimeCluster_module.cc:172** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CosmicReco/src/SimpleTimeCluster_module.cc:193** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/CosmicReco/src/CosmicFitDisplay_module.cc:651** - Possible assignment (=) instead of comparison (==) in condition
- ... and 11 more

#### division_by_zero (684 occurrences)

- **/workspace/CosmicReco/src/CosmicShowerFilter_module.cc:8** - Potential division by zero: RecoDataProducts not checked
- **/workspace/CosmicReco/src/CosmicShowerFilter_module.cc:9** - Potential division by zero: RecoDataProducts not checked
- **/workspace/CosmicReco/src/CosmicShowerFilter_module.cc:10** - Potential division by zero: ProditionsService not checked
- **/workspace/CosmicReco/src/CosmicShowerFilter_module.cc:11** - Potential division by zero: TrackerConditions not checked
- **/workspace/CosmicReco/src/CosmicShowerFilter_module.cc:13** - Potential division by zero: Framework not checked
- **/workspace/CosmicReco/src/CosmicShowerFilter_module.cc:14** - Potential division by zero: Framework not checked
- **/workspace/CosmicReco/src/CosmicShowerFilter_module.cc:15** - Potential division by zero: Framework not checked
- **/workspace/CosmicReco/src/CosmicShowerFilter_module.cc:16** - Potential division by zero: Framework not checked
- **/workspace/CosmicReco/src/CosmicShowerFilter_module.cc:17** - Potential division by zero: Framework not checked
- **/workspace/CosmicReco/src/CosmicShowerFilter_module.cc:18** - Potential division by zero: TFileService not checked
- ... and 674 more

#### memory_leak (37 occurrences)

- **/workspace/CosmicReco/src/CosmicShowerFilter_module.cc:88** - Potential memory leak: new TimeClusterCollection without corresponding delete
- **/workspace/CosmicReco/src/CosmicSeedFilter_module.cc:72** - Potential memory leak: new TriggerInfo without corresponding delete
- **/workspace/CosmicReco/src/CosmicTrackFit.cc:275** - Potential memory leak: new parameters without corresponding delete
- **/workspace/CosmicReco/src/CosmicTrackFit.cc:281** - Potential memory leak: new direction without corresponding delete
- **/workspace/CosmicReco/src/SimpleTimeCluster_module.cc:116** - Potential memory leak: new TimeClusterCollection without corresponding delete
- **/workspace/CosmicReco/src/CosmicFitDisplay_module.cc:152** - Potential memory leak: new TApplication without corresponding delete
- **/workspace/CosmicReco/src/CosmicFitDisplay_module.cc:310** - Potential memory leak: new TF1 without corresponding delete
- **/workspace/CosmicReco/src/CosmicFitDisplay_module.cc:352** - Potential memory leak: new TF1 without corresponding delete
- **/workspace/CosmicReco/src/CosmicFitDisplay_module.cc:407** - Potential memory leak: new TF1 without corresponding delete
- **/workspace/CosmicReco/src/CosmicFitDisplay_module.cc:446** - Potential memory leak: new TF1 without corresponding delete
- ... and 27 more

#### missing_error_handling (36 occurrences)

- **/workspace/CosmicReco/src/CosmicShowerFilter_module.cc:90** - getHandle/getValidHandle result not checked for validity
- **/workspace/CosmicReco/src/CosmicShowerFilter_module.cc:92** - getHandle/getValidHandle result not checked for validity
- **/workspace/CosmicReco/src/CosmicTrackFinder_module.cc:190** - getHandle/getValidHandle result not checked for validity
- **/workspace/CosmicReco/src/CosmicTrackFinder_module.cc:192** - getHandle/getValidHandle result not checked for validity
- **/workspace/CosmicReco/src/CosmicSeedFilter_module.cc:76** - getHandle/getValidHandle result not checked for validity
- **/workspace/CosmicReco/src/CosmicMCRecoDiff_module.cc:359** - getHandle/getValidHandle result not checked for validity
- **/workspace/CosmicReco/src/CosmicMCRecoDiff_module.cc:362** - getHandle/getValidHandle result not checked for validity
- **/workspace/CosmicReco/src/CosmicMuonInfo_module.cc:273** - getHandle/getValidHandle result not checked for validity
- **/workspace/CosmicReco/src/CosmicMuonInfo_module.cc:274** - getHandle/getValidHandle result not checked for validity
- **/workspace/CosmicReco/src/CosmicMuonInfo_module.cc:275** - getHandle/getValidHandle result not checked for validity
- ... and 26 more

#### resource_leak (1 occurrences)

- **/workspace/CosmicReco/src/CosmicAnalyzer_module.cc:264** - File handle opened but may not be closed

#### uninitialized_variable (36 occurrences)

- **/workspace/CosmicReco/src/CosmicShowerFilter_module.cc:52** - Variable _hasmaxnpanel may be used uninitialized
- **/workspace/CosmicReco/src/CosmicShowerFilter_module.cc:53** - Variable _maxnpanel may be used uninitialized
- **/workspace/CosmicReco/src/CosmicShowerFilter_module.cc:54** - Variable _maxCrossingGap may be used uninitialized
- **/workspace/CosmicReco/src/CosmicShowerFilter_module.cc:55** - Variable _maxSameGap may be used uninitialized
- **/workspace/CosmicReco/src/CosmicShowerFilter_module.cc:56** - Variable _maxTotalSameGap may be used uninitialized
- **/workspace/CosmicReco/src/CosmicShowerFilter_module.cc:57** - Variable _cutsinglelayer may be used uninitialized
- **/workspace/CosmicReco/src/CosmicSeedFilter_module.cc:49** - Variable _minnhits may be used uninitialized
- **/workspace/CosmicReco/src/CosmicSeedFilter_module.cc:50** - Variable _minFracStrawHits may be used uninitialized
- **/workspace/CosmicReco/src/CosmicSeedFilter_module.cc:51** - Variable _maxTheta may be used uninitialized
- **/workspace/CosmicReco/src/CosmicSeedFilter_module.cc:52** - Variable _minNPanelStereo may be used uninitialized
- ... and 26 more

#### unused_variable (8 occurrences)

- **/workspace/CosmicReco/src/CosmicMCRecoDiff_module.cc:202** - Variable t0 declared but possibly unused
- **/workspace/CosmicReco/src/CosmicMuonInfo_module.cc:194** - Variable _sum declared but possibly unused
- **/workspace/CosmicReco/src/CosmicMuonInfo_module.cc:195** - Variable _nbad declared but possibly unused
- **/workspace/CosmicReco/src/PDFFit.cc:46** - Variable drift_v declared but possibly unused
- **/workspace/CosmicReco/src/PDFFit.cc:55** - Variable wireradius declared but possibly unused
- **/workspace/CosmicReco/src/PDFFit.cc:56** - Variable strawradius declared but possibly unused
- **/workspace/CosmicReco/src/PDFFit.cc:502** - Variable t0 declared but possibly unused
- **/workspace/CosmicReco/src/LineFinder_module.cc:182** - Variable jts declared but possibly unused


### DAQ

Found 627 potential bugs:

#### array_bounds (171 occurrences)

- **/workspace/DAQ/src/CaloHitsFromDTCEvents_module.cc:136** - Array access peakADC2MeV_[i] without bounds check
- **/workspace/DAQ/src/CaloHitsFromDTCEvents_module.cc:137** - Array access timeCalib_[i] without bounds check
- **/workspace/DAQ/src/CaloHitsFromDTCEvents_module.cc:149** - Array access pulseMap_[crystalID] without bounds check
- **/workspace/DAQ/src/CaloHitsFromDTCEvents_module.cc:179** - Array access pulseMap_[crystalID] without bounds check
- **/workspace/DAQ/src/CaloHitsFromDTCEvents_module.cc:298** - Array access failure_counter[errorCode] without bounds check
- **/workspace/DAQ/src/CaloHitsFromDTCEvents_module.cc:322** - Array access peakADC2MeV_[SiPMID] without bounds check
- **/workspace/DAQ/src/CaloHitsFromDTCEvents_module.cc:323** - Array access timeCalib_[SiPMID] without bounds check
- **/workspace/DAQ/src/CaloHitsFromDTCEvents_module.cc:326** - Array access nhits[offlineId.crystal().disk()] without bounds check
- **/workspace/DAQ/src/CaloHitsFromDTCEvents_module.cc:361** - Array access failure_counter[errorCode] without bounds check
- **/workspace/DAQ/src/CaloHitsFromDTCEvents_module.cc:385** - Array access peakADC2MeV_[SiPMID] without bounds check
- ... and 161 more

#### assignment_in_condition (21 occurrences)

- **/workspace/DAQ/src/CaloHitsFromDTCEvents_module.cc:333** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/DAQ/src/CaloHitsFromDTCEvents_module.cc:396** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/DAQ/src/CrvDigisFromArtdaqFragments_module.cc:106** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/DAQ/src/ArtBinaryPacketsFromDigis_module.cc:466** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/DAQ/src/ArtBinaryPacketsFromDigis_module.cc:838** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/DAQ/src/ArtBinaryPacketsFromDigis_module.cc:871** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/DAQ/src/ArtBinaryPacketsFromDigis_module.cc:875** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/DAQ/src/CrvDigisFromArtdaqFragmentsFEBII_module.cc:124** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/DAQ/src/CrvGRdataFromArtdaqFragments_module.cc:116** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/DAQ/src/CrvGRdataFromArtdaqFragments_module.cc:191** - Possible assignment (=) instead of comparison (==) in condition
- ... and 11 more

#### division_by_zero (332 occurrences)

- **/workspace/DAQ/src/CaloHitsFromDTCEvents_module.cc:7** - Potential division by zero: Framework not checked
- **/workspace/DAQ/src/CaloHitsFromDTCEvents_module.cc:8** - Potential division by zero: Framework not checked
- **/workspace/DAQ/src/CaloHitsFromDTCEvents_module.cc:9** - Potential division by zero: Framework not checked
- **/workspace/DAQ/src/CaloHitsFromDTCEvents_module.cc:10** - Potential division by zero: ParameterSet not checked
- **/workspace/DAQ/src/CaloHitsFromDTCEvents_module.cc:12** - Potential division by zero: Framework not checked
- **/workspace/DAQ/src/CaloHitsFromDTCEvents_module.cc:13** - Potential division by zero: Overlays not checked
- **/workspace/DAQ/src/CaloHitsFromDTCEvents_module.cc:14** - Potential division by zero: Overlays not checked
- **/workspace/DAQ/src/CaloHitsFromDTCEvents_module.cc:15** - Potential division by zero: Overlays not checked
- **/workspace/DAQ/src/CaloHitsFromDTCEvents_module.cc:16** - Potential division by zero: Data not checked
- **/workspace/DAQ/src/CaloHitsFromDTCEvents_module.cc:18** - Potential division by zero: CaloConditions not checked
- ... and 322 more

#### memory_leak (48 occurrences)

- **/workspace/DAQ/src/CaloHitsFromDTCEvents_module.cc:212** - Potential memory leak: new mu2e without corresponding delete
- **/workspace/DAQ/src/CaloHitsFromDTCEvents_module.cc:213** - Potential memory leak: new mu2e without corresponding delete
- **/workspace/DAQ/src/CaloHitsFromDTCEvents_module.cc:216** - Potential memory leak: new mu2e without corresponding delete
- **/workspace/DAQ/src/CaloHitsFromDTCEvents_module.cc:221** - Potential memory leak: new mu2e without corresponding delete
- **/workspace/DAQ/src/CrvDigisFromArtdaqFragments_module.cc:61** - Potential memory leak: new mu2e without corresponding delete
- **/workspace/DAQ/src/CrvDigisFromArtdaqFragments_module.cc:62** - Potential memory leak: new mu2e without corresponding delete
- **/workspace/DAQ/src/CrvDigisFromArtdaqFragments_module.cc:63** - Potential memory leak: new mu2e without corresponding delete
- **/workspace/DAQ/src/ArtBinaryPacketsFromDigis_module.cc:85** - Potential memory leak: new calorimter without corresponding delete
- **/workspace/DAQ/src/ArtBinaryPacketsFromDigis_module.cc:607** - Potential memory leak: new DataBlockCollection without corresponding delete
- **/workspace/DAQ/src/ArtBinaryPacketsFromDigis_module.cc:656** - Potential memory leak: new timestamp without corresponding delete
- ... and 38 more

#### missing_error_handling (8 occurrences)

- **/workspace/DAQ/src/ArtBinaryPacketsFromDigis_module.cc:664** - getHandle/getValidHandle result not checked for validity
- **/workspace/DAQ/src/ArtBinaryPacketsFromDigis_module.cc:975** - getHandle/getValidHandle result not checked for validity
- **/workspace/DAQ/src/ArtBinaryPacketsFromDigis_module.cc:977** - getHandle/getValidHandle result not checked for validity
- **/workspace/DAQ/src/ArtBinaryPacketsFromDigis_module.cc:1025** - getHandle/getValidHandle result not checked for validity
- **/workspace/DAQ/src/PrefetchDAQData_module.cc:98** - getHandle/getValidHandle result not checked for validity
- **/workspace/DAQ/src/PrefetchDAQData_module.cc:103** - getHandle/getValidHandle result not checked for validity
- **/workspace/DAQ/src/PrefetchDAQData_module.cc:108** - getHandle/getValidHandle result not checked for validity
- **/workspace/DAQ/src/PrefetchDAQData_module.cc:113** - getHandle/getValidHandle result not checked for validity

#### missing_return (5 occurrences)

- **/workspace/DAQ/src/CaloHitsFromDTCEvents_module.cc:342** - Function may be missing return statement
- **/workspace/DAQ/src/CaloDigisFromDTCEvents_module.cc:220** - Function may be missing return statement
- **/workspace/DAQ/src/LumiStreamFilter_module.cc:301** - Function may be missing return statement
- **/workspace/DAQ/src/StrawDigiFilter_module.cc:263** - Function may be missing return statement
- **/workspace/DAQ/src/StrawDigiFilter_module.cc:392** - Function may be missing return statement

#### uninitialized_variable (33 occurrences)

- **/workspace/DAQ/src/CrvDigisFromArtdaqFragments_module.cc:45** - Variable _diagLevel may be used uninitialized
- **/workspace/DAQ/src/CrvDigisFromArtdaqFragments_module.cc:46** - Variable _useSubsystem0 may be used uninitialized
- **/workspace/DAQ/src/ArtBinaryPacketsFromDigis_module.cc:1035** - Variable rocID may be used uninitialized
- **/workspace/DAQ/src/EventHeaderFromCFOFragment_module.cc:57** - Variable diagLevel_ may be used uninitialized
- **/workspace/DAQ/src/CrvDigisFromArtdaqFragmentsFEBII_module.cc:48** - Variable _diagLevel may be used uninitialized
- **/workspace/DAQ/src/CrvDigisFromArtdaqFragmentsFEBII_module.cc:49** - Variable _useSubsystem0 may be used uninitialized
- **/workspace/DAQ/src/CrvDigisFromArtdaqFragmentsFEBII_module.cc:50** - Variable _produceZS may be used uninitialized
- **/workspace/DAQ/src/CrvDigisFromArtdaqFragmentsFEBII_module.cc:51** - Variable _produceNZS may be used uninitialized
- **/workspace/DAQ/src/CrvGRdataFromArtdaqFragments_module.cc:42** - Variable _diagLevel may be used uninitialized
- **/workspace/DAQ/src/CrvGRdataFromArtdaqFragments_module.cc:44** - Variable _writeCsvFile may be used uninitialized
- ... and 23 more

#### unused_variable (9 occurrences)

- **/workspace/DAQ/src/CaloHitsFromDTCEvents_module.cc:112** - Variable hexShiftPrint declared but possibly unused
- **/workspace/DAQ/src/ArtBinaryPacketsFromDigis_module.cc:128** - Variable NUM_PRESAMPLES declared but possibly unused
- **/workspace/DAQ/src/ArtBinaryPacketsFromDigis_module.cc:129** - Variable START_SAMPLES declared but possibly unused
- **/workspace/DAQ/src/ArtBinaryPacketsFromDigis_module.cc:130** - Variable NUM_SAMPLES declared but possibly unused
- **/workspace/DAQ/src/ArtBinaryPacketsFromDigis_module.cc:131** - Variable LOWER_TDC declared but possibly unused
- **/workspace/DAQ/src/ArtBinaryPacketsFromDigis_module.cc:132** - Variable UPPER_TDC declared but possibly unused
- **/workspace/DAQ/src/CaloDigisFromDTCEvents_module.cc:77** - Variable hexShiftPrint declared but possibly unused
- **/workspace/DAQ/src/LumiStreamFilter_module.cc:264** - Variable icopy declared but possibly unused
- **/workspace/DAQ/src/DummyLumiInfoProducer_module.cc:69** - Variable ihit declared but possibly unused


### DAQConditions

Found 3 potential bugs:

#### division_by_zero (3 occurrences)

- **/workspace/DAQConditions/src/EventTiming.cc:2** - Potential division by zero: DAQConditions not checked
- **/workspace/DAQConditions/src/EventTimingMaker.cc:1** - Potential division by zero: DAQConditions not checked
- **/workspace/DAQConditions/src/EventTimingMaker.cc:2** - Potential division by zero: exception not checked


### DataProducts

Found 52 potential bugs:

#### array_bounds (20 occurrences)

- **/workspace/DataProducts/src/STMChannel.cc:22** - Array access _name[i] without bounds check
- **/workspace/DataProducts/src/STMChannel.cc:30** - Array access _name[i] without bounds check
- **/workspace/DataProducts/src/StrawId.cc:46** - Array access v[0] without bounds check
- **/workspace/DataProducts/src/StrawId.cc:50** - Array access v[1] without bounds check
- **/workspace/DataProducts/src/StrawId.cc:54** - Array access v[2] without bounds check
- **/workspace/DataProducts/src/StrawStatus.cc:22** - Array access bitnames[std::string("Absent")] without bounds check
- **/workspace/DataProducts/src/StrawStatus.cc:23** - Array access bitnames[std::string("NoWire")] without bounds check
- **/workspace/DataProducts/src/StrawStatus.cc:24** - Array access bitnames[std::string("NoHV")] without bounds check
- **/workspace/DataProducts/src/StrawStatus.cc:25** - Array access bitnames[std::string("NoLV")] without bounds check
- **/workspace/DataProducts/src/StrawStatus.cc:26** - Array access bitnames[std::string("NoGas")] without bounds check
- ... and 10 more

#### assignment_in_condition (1 occurrences)

- **/workspace/DataProducts/src/VirtualDetectorId.cc:31** - Possible assignment (=) instead of comparison (==) in condition

#### division_by_zero (27 occurrences)

- **/workspace/DataProducts/src/STMChannel.cc:7** - Potential division by zero: DataProducts not checked
- **/workspace/DataProducts/src/STMChannel.cc:9** - Potential division by zero: static_assert not checked
- **/workspace/DataProducts/src/STMChannel.cc:17** - Potential division by zero: sizeof not checked
- **/workspace/DataProducts/src/StrawId.cc:5** - Potential division by zero: exception not checked
- **/workspace/DataProducts/src/StrawId.cc:7** - Potential division by zero: DataProducts not checked
- **/workspace/DataProducts/src/StrawId.cc:8** - Potential division by zero: GeneralUtilities not checked
- **/workspace/DataProducts/src/StrawId.cc:90** - Potential division by zero: 2 not checked
- **/workspace/DataProducts/src/StrawId.cc:91** - Potential division by zero: 2 not checked
- **/workspace/DataProducts/src/StrawId.cc:92** - Potential division by zero: 2 not checked
- **/workspace/DataProducts/src/CompressedPDGCode.cc:1** - Potential division by zero: DataProducts not checked
- ... and 17 more

#### missing_return (4 occurrences)

- **/workspace/DataProducts/src/GenVector.cc:4** - Function may be missing return statement
- **/workspace/DataProducts/src/GenVector.cc:6** - Function may be missing return statement
- **/workspace/DataProducts/src/GenVector.cc:8** - Function may be missing return statement
- **/workspace/DataProducts/src/GenVector.cc:10** - Function may be missing return statement


### DbService

Found 757 potential bugs:

#### array_bounds (344 occurrences)

- **/workspace/DbService/src/DbEngine.cc:94** - Array access _override[iover] without bounds check
- **/workspace/DbService/src/DbEngine.cc:223** - Array access _overrideTids[lt.table().name()] without bounds check
- **/workspace/DbService/src/DbEngine.cc:226** - Array access _overrideTids[lt.table().name()] without bounds check
- **/workspace/DbService/src/DbEngine.cc:240** - Array access _override[i] without bounds check
- **/workspace/DbService/src/DbEngine.cc:242** - Array access _override[j] without bounds check
- **/workspace/DbService/src/openTool_main.cc:89** - Array access unregistered[0] without bounds check
- **/workspace/DbService/src/openTool_main.cc:99** - Array access words[0] without bounds check
- **/workspace/DbService/src/DbIdList.cc:49** - Array access words[0] without bounds check
- **/workspace/DbService/src/DbIdList.cc:50** - Array access words[1] without bounds check
- **/workspace/DbService/src/DbIdList.cc:51** - Array access words[0] without bounds check
- ... and 334 more

#### assignment_in_condition (145 occurrences)

- **/workspace/DbService/src/epicsTool_main.cc:81** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/DbService/src/DbEngine.cc:148** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/DbService/src/DbEngine.cc:273** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/DbService/src/DbTool.cc:74** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/DbService/src/DbTool.cc:97** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/DbService/src/DbTool.cc:173** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/DbService/src/DbTool.cc:221** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/DbService/src/DbTool.cc:238** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/DbService/src/DbTool.cc:277** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/DbService/src/DbTool.cc:284** - Possible assignment (=) instead of comparison (==) in condition
- ... and 135 more

#### division_by_zero (133 occurrences)

- **/workspace/DbService/src/GrlHeader.cc:1** - Potential division by zero: DbService not checked
- **/workspace/DbService/src/GrlHeader.cc:2** - Potential division by zero: GeneralUtilities not checked
- **/workspace/DbService/src/epicsTool_main.cc:6** - Potential division by zero: DbService not checked
- **/workspace/DbService/src/epicsTool_main.cc:7** - Potential division by zero: program_options not checked
- **/workspace/DbService/src/epicsTool_main.cc:47** - Potential division by zero: TIME2 not checked
- **/workspace/DbService/src/epicsTool_main.cc:62** - Potential division by zero: 2022 not checked
- **/workspace/DbService/src/DbEngine.cc:1** - Potential division by zero: DbService not checked
- **/workspace/DbService/src/DbEngine.cc:2** - Potential division by zero: DbService not checked
- **/workspace/DbService/src/DbEngine.cc:3** - Potential division by zero: DbTables not checked
- **/workspace/DbService/src/DbEngine.cc:4** - Potential division by zero: exception not checked
- ... and 123 more

#### memory_leak (83 occurrences)

- **/workspace/DbService/src/DbEngine.cc:265** - Potential memory leak: new table without corresponding delete
- **/workspace/DbService/src/DbIdList.cc:12** - Potential memory leak: new connections without corresponding delete
- **/workspace/DbService/src/DbIdList.cc:33** - Potential memory leak: new database without corresponding delete
- **/workspace/DbService/src/DbTool.cc:1091** - Potential memory leak: new cid without corresponding delete
- **/workspace/DbService/src/DbTool.cc:1094** - Potential memory leak: new cid without corresponding delete
- **/workspace/DbService/src/DbTool.cc:1137** - Potential memory leak: new IoVs without corresponding delete
- **/workspace/DbService/src/DbTool.cc:1206** - Potential memory leak: new IID without corresponding delete
- **/workspace/DbService/src/DbTool.cc:1209** - Potential memory leak: new IID without corresponding delete
- **/workspace/DbService/src/DbTool.cc:1299** - Potential memory leak: new GID without corresponding delete
- **/workspace/DbService/src/DbTool.cc:1314** - Potential memory leak: new GID without corresponding delete
- ... and 73 more

#### missing_return (26 occurrences)

- **/workspace/DbService/src/DbIdList.cc:51** - Function may be missing return statement
- **/workspace/DbService/src/DbIdList.cc:53** - Function may be missing return statement
- **/workspace/DbService/src/DbIdList.cc:55** - Function may be missing return statement
- **/workspace/DbService/src/DbIdList.cc:57** - Function may be missing return statement
- **/workspace/DbService/src/DbTool.cc:2268** - Function may be missing return statement
- **/workspace/DbService/src/DbTool.cc:2276** - Function may be missing return statement
- **/workspace/DbService/src/DbTool.cc:2322** - Function may be missing return statement
- **/workspace/DbService/src/DbTool.cc:2892** - Function may be missing return statement
- **/workspace/DbService/src/DbTool.cc:2908** - Function may be missing return statement
- **/workspace/DbService/src/DbTool.cc:2922** - Function may be missing return statement
- ... and 16 more

#### resource_leak (9 occurrences)

- **/workspace/DbService/src/GrlList.cc:23** - File handle opened but may not be closed
- **/workspace/DbService/src/GrlList.cc:24** - File handle opened but may not be closed
- **/workspace/DbService/src/DbTool.cc:2566** - File handle opened but may not be closed
- **/workspace/DbService/src/DbTool.cc:3232** - File handle opened but may not be closed
- **/workspace/DbService/src/DbTool.cc:3233** - File handle opened but may not be closed
- **/workspace/DbService/src/DbTool.cc:3287** - File handle opened but may not be closed
- **/workspace/DbService/src/DbTool.cc:3288** - File handle opened but may not be closed
- **/workspace/DbService/src/GrlTool.cc:361** - File handle opened but may not be closed
- **/workspace/DbService/src/GrlTool.cc:362** - File handle opened but may not be closed

#### uninitialized_variable (15 occurrences)

- **/workspace/DbService/src/DbTool.cc:1125** - Variable iid may be used uninitialized
- **/workspace/DbService/src/DbTool.cc:1143** - Variable gid may be used uninitialized
- **/workspace/DbService/src/DbTool.cc:1393** - Variable rc may be used uninitialized
- **/workspace/DbService/src/DbTool.cc:2311** - Variable iid may be used uninitialized
- **/workspace/DbService/src/DbTool.cc:2348** - Variable gid may be used uninitialized
- **/workspace/DbService/src/DbTool.cc:2379** - Variable eid may be used uninitialized
- **/workspace/DbService/src/DbReader.cc:27** - Variable rc may be used uninitialized
- **/workspace/DbService/src/RunTool.cc:22** - Variable rc may be used uninitialized
- **/workspace/DbService/src/RunTool.cc:241** - Variable rc may be used uninitialized
- **/workspace/DbService/src/RunTool.cc:383** - Variable rc may be used uninitialized
- ... and 5 more

#### unused_variable (2 occurrences)

- **/workspace/DbService/src/epicsTool_main.cc:16** - Variable doHelp declared but possibly unused
- **/workspace/DbService/src/grlTool_main.cc:18** - Variable flags declared but possibly unused


### DbTables

Found 132 potential bugs:

#### array_bounds (21 occurrences)

- **/workspace/DbTables/src/DbUtil.cc:73** - Array access words[1] without bounds check
- **/workspace/DbTables/src/DbUtil.cc:82** - Array access words[i] without bounds check
- **/workspace/DbTables/src/DbUtil.cc:151** - Array access dv[i] without bounds check
- **/workspace/DbTables/src/DbUtil.cc:152** - Array access coll[i] without bounds check
- **/workspace/DbTables/src/DbUtil.cc:157** - Array access coll[j] without bounds check
- **/workspace/DbTables/src/DbUtil.cc:160** - Array access dv[j] without bounds check
- **/workspace/DbTables/src/DbUtil.cc:201** - Array access line[j] without bounds check
- **/workspace/DbTables/src/DbUtil.cc:206** - Array access line[j - 1] without bounds check
- **/workspace/DbTables/src/DbUtil.cc:215** - Array access line[j] without bounds check
- **/workspace/DbTables/src/DbIoV.cc:180** - Array access words[0] without bounds check
- ... and 11 more

#### assignment_in_condition (7 occurrences)

- **/workspace/DbTables/src/DbUtil.cc:101** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/DbTables/src/DbIoV.cc:199** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/DbTables/src/DbIoV.cc:204** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/DbTables/src/DbIoV.cc:212** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/DbTables/src/DbIoV.cc:217** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/DbTables/src/DbCache.cc:18** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/DbTables/src/DbCache.cc:33** - Possible assignment (=) instead of comparison (==) in condition

#### division_by_zero (58 occurrences)

- **/workspace/DbTables/src/DbTableFactory.cc:1** - Potential division by zero: DbTables not checked
- **/workspace/DbTables/src/DbTableFactory.cc:2** - Potential division by zero: DbTables not checked
- **/workspace/DbTables/src/DbTableFactory.cc:3** - Potential division by zero: DbTables not checked
- **/workspace/DbTables/src/DbTableFactory.cc:4** - Potential division by zero: DbTables not checked
- **/workspace/DbTables/src/DbTableFactory.cc:5** - Potential division by zero: DbTables not checked
- **/workspace/DbTables/src/DbTableFactory.cc:6** - Potential division by zero: DbTables not checked
- **/workspace/DbTables/src/DbTableFactory.cc:7** - Potential division by zero: DbTables not checked
- **/workspace/DbTables/src/DbTableFactory.cc:8** - Potential division by zero: DbTables not checked
- **/workspace/DbTables/src/DbTableFactory.cc:9** - Potential division by zero: DbTables not checked
- **/workspace/DbTables/src/DbTableFactory.cc:10** - Potential division by zero: DbTables not checked
- ... and 48 more

#### memory_leak (40 occurrences)

- **/workspace/DbTables/src/DbTableFactory.cc:40** - Potential memory leak: new mu2e without corresponding delete
- **/workspace/DbTables/src/DbTableFactory.cc:42** - Potential memory leak: new mu2e without corresponding delete
- **/workspace/DbTables/src/DbTableFactory.cc:44** - Potential memory leak: new mu2e without corresponding delete
- **/workspace/DbTables/src/DbTableFactory.cc:46** - Potential memory leak: new mu2e without corresponding delete
- **/workspace/DbTables/src/DbTableFactory.cc:48** - Potential memory leak: new mu2e without corresponding delete
- **/workspace/DbTables/src/DbTableFactory.cc:50** - Potential memory leak: new mu2e without corresponding delete
- **/workspace/DbTables/src/DbTableFactory.cc:52** - Potential memory leak: new mu2e without corresponding delete
- **/workspace/DbTables/src/DbTableFactory.cc:54** - Potential memory leak: new mu2e without corresponding delete
- **/workspace/DbTables/src/DbTableFactory.cc:56** - Potential memory leak: new mu2e without corresponding delete
- **/workspace/DbTables/src/DbTableFactory.cc:58** - Potential memory leak: new mu2e without corresponding delete
- ... and 30 more

#### missing_return (6 occurrences)

- **/workspace/DbTables/src/DbUtil.cc:215** - Function may be missing return statement
- **/workspace/DbTables/src/DbIoV.cc:26** - Function may be missing return statement
- **/workspace/DbTables/src/DbIoV.cc:28** - Function may be missing return statement
- **/workspace/DbTables/src/DbIoV.cc:52** - Function may be missing return statement
- **/workspace/DbTables/src/DbIoV.cc:87** - Function may be missing return statement
- **/workspace/DbTables/src/DbIoV.cc:89** - Function may be missing return statement


### DetectorSolenoidGeom

Found 1 potential bugs:

#### division_by_zero (1 occurrences)

- **/workspace/DetectorSolenoidGeom/src/DetectorSolenoid.cc:1** - Potential division by zero: DetectorSolenoidGeom not checked


### EventDisplay

Found 679 potential bugs:

#### array_bounds (171 occurrences)

- **/workspace/EventDisplay/src/EventDisplay_module.cc:181** - Array access msg[300] without bounds check
- **/workspace/EventDisplay/src/EventDisplayFrame.cc:81** - Array access _legendText[i] without bounds check
- **/workspace/EventDisplay/src/EventDisplayFrame.cc:82** - Array access _legendBox[i] without bounds check
- **/workspace/EventDisplay/src/EventDisplayFrame.cc:86** - Array access _legendParticleGroup[i] without bounds check
- **/workspace/EventDisplay/src/EventDisplayFrame.cc:87** - Array access _legendParticleText[i] without bounds check
- **/workspace/EventDisplay/src/EventDisplayFrame.cc:88** - Array access _legendParticleLine[i] without bounds check
- **/workspace/EventDisplay/src/EventDisplayFrame.cc:231** - Array access _eventInfo[i] without bounds check
- **/workspace/EventDisplay/src/EventDisplayFrame.cc:232** - Array access _eventInfo[i] without bounds check
- **/workspace/EventDisplay/src/EventDisplayFrame.cc:233** - Array access _eventInfo[i] without bounds check
- **/workspace/EventDisplay/src/EventDisplayFrame.cc:575** - Array access min[3] without bounds check
- ... and 161 more

#### assignment_in_condition (61 occurrences)

- **/workspace/EventDisplay/src/EventDisplayFrame.cc:473** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/EventDisplay/src/EventDisplayFrame.cc:484** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/EventDisplay/src/EventDisplayFrame.cc:491** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/EventDisplay/src/EventDisplayFrame.cc:499** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/EventDisplay/src/EventDisplayFrame.cc:505** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/EventDisplay/src/EventDisplayFrame.cc:511** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/EventDisplay/src/EventDisplayFrame.cc:517** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/EventDisplay/src/EventDisplayFrame.cc:523** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/EventDisplay/src/EventDisplayFrame.cc:550** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/EventDisplay/src/EventDisplayFrame.cc:730** - Possible assignment (=) instead of comparison (==) in condition
- ... and 51 more

#### division_by_zero (199 occurrences)

- **/workspace/EventDisplay/src/EventDisplay_module.cc:10** - Potential division by zero: CRVConditions not checked
- **/workspace/EventDisplay/src/EventDisplay_module.cc:11** - Potential division by zero: MCDataProducts not checked
- **/workspace/EventDisplay/src/EventDisplay_module.cc:12** - Potential division by zero: ProditionsService not checked
- **/workspace/EventDisplay/src/EventDisplay_module.cc:13** - Potential division by zero: RecoDataProducts not checked
- **/workspace/EventDisplay/src/EventDisplay_module.cc:14** - Potential division by zero: Framework not checked
- **/workspace/EventDisplay/src/EventDisplay_module.cc:15** - Potential division by zero: Framework not checked
- **/workspace/EventDisplay/src/EventDisplay_module.cc:16** - Potential division by zero: TFileService not checked
- **/workspace/EventDisplay/src/EventDisplay_module.cc:17** - Potential division by zero: Framework not checked
- **/workspace/EventDisplay/src/EventDisplay_module.cc:18** - Potential division by zero: ParameterSet not checked
- **/workspace/EventDisplay/src/EventDisplay_module.cc:23** - Potential division by zero: EventDisplay not checked
- ... and 189 more

#### memory_leak (240 occurrences)

- **/workspace/EventDisplay/src/EventDisplay_module.cc:73** - Potential memory leak: new TApplication without corresponding delete
- **/workspace/EventDisplay/src/EventDisplay_module.cc:91** - Potential memory leak: new mu2e_eventdisplay without corresponding delete
- **/workspace/EventDisplay/src/EventDisplay_module.cc:183** - Potential memory leak: new TGMsgBox without corresponding delete
- **/workspace/EventDisplay/src/EventDisplayFrame.cc:70** - Potential memory leak: new TTimer without corresponding delete
- **/workspace/EventDisplay/src/EventDisplayFrame.cc:94** - Potential memory leak: new TGHorizontalFrame without corresponding delete
- **/workspace/EventDisplay/src/EventDisplayFrame.cc:95** - Potential memory leak: new TRootEmbeddedCanvas without corresponding delete
- **/workspace/EventDisplay/src/EventDisplayFrame.cc:96** - Potential memory leak: new TGVerticalFrame without corresponding delete
- **/workspace/EventDisplay/src/EventDisplayFrame.cc:99** - Potential memory leak: new TGLayoutHints without corresponding delete
- **/workspace/EventDisplay/src/EventDisplayFrame.cc:100** - Potential memory leak: new TGLayoutHints without corresponding delete
- **/workspace/EventDisplay/src/EventDisplayFrame.cc:101** - Potential memory leak: new TGLayoutHints without corresponding delete
- ... and 230 more

#### uninitialized_variable (1 occurrences)

- **/workspace/EventDisplay/src/EventDisplay_module.cc:49** - Variable _firstLoop may be used uninitialized

#### unused_variable (1 occurrences)

- **/workspace/EventDisplay/src/DataInterface.cc:1593** - Variable i declared but possibly unused

#### use_after_free (6 occurrences)

- **/workspace/EventDisplay/src/EventDisplayFrame.cc:709** - Potential use after free: _legendBox deleted but may be used later
- **/workspace/EventDisplay/src/EventDisplayFrame.cc:710** - Potential use after free: _legendText deleted but may be used later
- **/workspace/EventDisplay/src/EventDisplayFrame.cc:744** - Potential use after free: _legendParticleGroup deleted but may be used later
- **/workspace/EventDisplay/src/EventDisplayFrame.cc:745** - Potential use after free: _legendParticleLine deleted but may be used later
- **/workspace/EventDisplay/src/EventDisplayFrame.cc:746** - Potential use after free: _legendParticleText deleted but may be used later
- **/workspace/EventDisplay/src/DataInterface.cc:1624** - Potential use after free: _geometrymanager deleted but may be used later


### EventGenerator

Found 1714 potential bugs:

#### array_bounds (152 occurrences)

- **/workspace/EventGenerator/src/ParticleGunImpl.cc:292** - Array access par[0] without bounds check
- **/workspace/EventGenerator/src/ParticleGunImpl.cc:296** - Array access par[0] without bounds check
- **/workspace/EventGenerator/src/ParticleGunImpl.cc:298** - Array access par[0] without bounds check
- **/workspace/EventGenerator/src/ParticleGunImpl.cc:299** - Array access par[0] without bounds check
- **/workspace/EventGenerator/src/ParticleGunImpl.cc:327** - Array access _momentumParameters[i] without bounds check
- **/workspace/EventGenerator/src/ParticleGunImpl.cc:332** - Array access _momentumParameters[i] without bounds check
- **/workspace/EventGenerator/src/ParticleGunImpl.cc:342** - Array access _momentumParameters[i] without bounds check
- **/workspace/EventGenerator/src/ParticleGunImpl.cc:355** - Array access _momentumParameters[0] without bounds check
- **/workspace/EventGenerator/src/ParticleGunImpl.cc:372** - Array access histogramRange[0] without bounds check
- **/workspace/EventGenerator/src/ParticleGunImpl.cc:373** - Array access histogramRange[1] without bounds check
- ... and 142 more

#### assignment_in_condition (38 occurrences)

- **/workspace/EventGenerator/src/Pileup_module.cc:151** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/EventGenerator/src/ParticleGunImpl.cc:280** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/EventGenerator/src/ParticleGunImpl.cc:335** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/EventGenerator/src/ParticleGunImpl.cc:355** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/EventGenerator/src/ParticleGunImpl.cc:392** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/EventGenerator/src/ParticleGunImpl.cc:433** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/EventGenerator/src/ParticleGunImpl.cc:497** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/EventGenerator/src/ParticleGunImpl.cc:535** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/EventGenerator/src/ParticleGunImpl.cc:565** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/EventGenerator/src/ParticleGunImpl.cc:590** - Possible assignment (=) instead of comparison (==) in condition
- ... and 28 more

#### division_by_zero (1281 occurrences)

- **/workspace/EventGenerator/src/Pileup_module.cc:14** - Potential division by zero: Vector not checked
- **/workspace/EventGenerator/src/Pileup_module.cc:15** - Potential division by zero: Random not checked
- **/workspace/EventGenerator/src/Pileup_module.cc:16** - Potential division by zero: Random not checked
- **/workspace/EventGenerator/src/Pileup_module.cc:17** - Potential division by zero: Random not checked
- **/workspace/EventGenerator/src/Pileup_module.cc:18** - Potential division by zero: Units not checked
- **/workspace/EventGenerator/src/Pileup_module.cc:20** - Potential division by zero: types not checked
- **/workspace/EventGenerator/src/Pileup_module.cc:21** - Potential division by zero: types not checked
- **/workspace/EventGenerator/src/Pileup_module.cc:22** - Potential division by zero: ParameterSet not checked
- **/workspace/EventGenerator/src/Pileup_module.cc:24** - Potential division by zero: MessageLogger not checked
- **/workspace/EventGenerator/src/Pileup_module.cc:26** - Potential division by zero: Framework not checked
- ... and 1271 more

#### memory_leak (108 occurrences)

- **/workspace/EventGenerator/src/InFlightParticleSampler_module.cc:91** - Potential memory leak: new GenParticleCollection without corresponding delete
- **/workspace/EventGenerator/src/CRYEventGenerator_module.cc:61** - Potential memory leak: new GenParticleCollection without corresponding delete
- **/workspace/EventGenerator/src/CRYEventGenerator_module.cc:78** - Potential memory leak: new CosmicLivetime without corresponding delete
- **/workspace/EventGenerator/src/CosmicDYB.cc:167** - Potential memory leak: new DYBGenerator without corresponding delete
- **/workspace/EventGenerator/src/CosmicDYB.cc:168** - Potential memory leak: new DYBGenerator without corresponding delete
- **/workspace/EventGenerator/src/CosmicDYB.cc:169** - Potential memory leak: new DYBGenerator without corresponding delete
- **/workspace/EventGenerator/src/CosmicDYB.cc:170** - Potential memory leak: new DYBGenerator without corresponding delete
- **/workspace/EventGenerator/src/CosmicDYB.cc:171** - Potential memory leak: new DYBGenerator without corresponding delete
- **/workspace/EventGenerator/src/CosmicDYB.cc:175** - Potential memory leak: new DYBGenerator without corresponding delete
- **/workspace/EventGenerator/src/PionFilter_module.cc:121** - Potential memory leak: new SumOfWeights without corresponding delete
- ... and 98 more

#### missing_error_handling (10 occurrences)

- **/workspace/EventGenerator/src/Pileup_module.cc:128** - getHandle/getValidHandle result not checked for validity
- **/workspace/EventGenerator/src/PionFilter_module.cc:82** - getHandle/getValidHandle result not checked for validity
- **/workspace/EventGenerator/src/GenFilter_module.cc:113** - getHandle/getValidHandle result not checked for validity
- **/workspace/EventGenerator/src/DecayInOrbitWeight_module.cc:101** - getHandle/getValidHandle result not checked for validity
- **/workspace/EventGenerator/src/FromStepPointMCsRotateTarget_module.cc:145** - getHandle/getValidHandle result not checked for validity
- **/workspace/EventGenerator/src/GeneratorPlots_module.cc:105** - getHandle/getValidHandle result not checked for validity
- **/workspace/EventGenerator/src/SingleProcessGenerator_module.cc:113** - getHandle/getValidHandle result not checked for validity
- **/workspace/EventGenerator/src/FromStepPointMCs_module.cc:99** - getHandle/getValidHandle result not checked for validity
- **/workspace/EventGenerator/src/GammaConversion_module.cc:116** - getHandle/getValidHandle result not checked for validity
- **/workspace/EventGenerator/src/CORSIKAEventGenerator_module.cc:142** - getHandle/getValidHandle result not checked for validity

#### missing_return (32 occurrences)

- **/workspace/EventGenerator/src/ParticleGunImpl.cc:181** - Function may be missing return statement
- **/workspace/EventGenerator/src/ParticleGunImpl.cc:184** - Function may be missing return statement
- **/workspace/EventGenerator/src/ParticleGunImpl.cc:187** - Function may be missing return statement
- **/workspace/EventGenerator/src/ParticleGunImpl.cc:190** - Function may be missing return statement
- **/workspace/EventGenerator/src/ParticleGunImpl.cc:205** - Function may be missing return statement
- **/workspace/EventGenerator/src/ParticleGunImpl.cc:208** - Function may be missing return statement
- **/workspace/EventGenerator/src/ParticleGunImpl.cc:211** - Function may be missing return statement
- **/workspace/EventGenerator/src/ParticleGunImpl.cc:214** - Function may be missing return statement
- **/workspace/EventGenerator/src/ParticleGunImpl.cc:315** - Function may be missing return statement
- **/workspace/EventGenerator/src/ParticleGunImpl.cc:346** - Function may be missing return statement
- ... and 22 more

#### resource_leak (2 occurrences)

- **/workspace/EventGenerator/src/FromAsciiMomentumAndPosition_module.cc:129** - File handle opened but may not be closed
- **/workspace/EventGenerator/src/FromG4BLFile.cc:138** - File handle opened but may not be closed

#### uninitialized_variable (76 occurrences)

- **/workspace/EventGenerator/src/Pileup_module.cc:69** - Variable muonLifeTime_ may be used uninitialized
- **/workspace/EventGenerator/src/Pileup_module.cc:70** - Variable decayFraction_ may be used uninitialized
- **/workspace/EventGenerator/src/Pileup_module.cc:74** - Variable verbosity_ may be used uninitialized
- **/workspace/EventGenerator/src/ParticleGunImpl.cc:406** - Variable passed may be used uninitialized
- **/workspace/EventGenerator/src/PionFilter_module.cc:51** - Variable diagLevel_ may be used uninitialized
- **/workspace/EventGenerator/src/PionFilter_module.cc:52** - Variable tmin_ may be used uninitialized
- **/workspace/EventGenerator/src/PionFilter_module.cc:53** - Variable tmax_ may be used uninitialized
- **/workspace/EventGenerator/src/PionFilter_module.cc:54** - Variable maxPions_ may be used uninitialized
- **/workspace/EventGenerator/src/PionFilter_module.cc:55** - Variable processCode_ may be used uninitialized
- **/workspace/EventGenerator/src/PionFilter_module.cc:57** - Variable isNull_ may be used uninitialized
- ... and 66 more

#### unused_variable (15 occurrences)

- **/workspace/EventGenerator/src/ParticleGunImpl.cc:402** - Variable j declared but possibly unused
- **/workspace/EventGenerator/src/CosmicDYB.cc:316** - Variable i declared but possibly unused
- **/workspace/EventGenerator/src/MuCapDeuteronGenerator_tool.cc:51** - Variable _rate declared but possibly unused
- **/workspace/EventGenerator/src/MuCapDeuteronGenerator_tool.cc:66** - Variable i_gen declared but possibly unused
- **/workspace/EventGenerator/src/CaloCalibGun_module.cc:189** - Variable xmanifold declared but possibly unused
- **/workspace/EventGenerator/src/MuCapNeutronGenerator_tool.cc:51** - Variable _rate declared but possibly unused
- **/workspace/EventGenerator/src/MuCapNeutronGenerator_tool.cc:65** - Variable i_gen declared but possibly unused
- **/workspace/EventGenerator/src/MuCapProtonGenerator_tool.cc:51** - Variable _rate declared but possibly unused
- **/workspace/EventGenerator/src/MuCapProtonGenerator_tool.cc:65** - Variable i_gen declared but possibly unused
- **/workspace/EventGenerator/src/MuCapPhotonGenerator_tool.cc:43** - Variable _rate declared but possibly unused
- ... and 5 more


### EventMixing

Found 143 potential bugs:

#### array_bounds (38 occurrences)

- **/workspace/EventMixing/src/Mu2eProductMixer.cc:212** - Array access subrunVolumes_[stage] without bounds check
- **/workspace/EventMixing/src/Mu2eProductMixer.cc:267** - Array access simOffsets_[inputEventIndex] without bounds check
- **/workspace/EventMixing/src/Mu2eProductMixer.cc:284** - Array access genOffsets_[inputEventIndex] without bounds check
- **/workspace/EventMixing/src/Mu2eProductMixer.cc:305** - Array access out[i] without bounds check
- **/workspace/EventMixing/src/Mu2eProductMixer.cc:306** - Array access simOffsets_[ie] without bounds check
- **/workspace/EventMixing/src/Mu2eProductMixer.cc:323** - Array access in[ieIndex] without bounds check
- **/workspace/EventMixing/src/Mu2eProductMixer.cc:324** - Array access in[ieIndex] without bounds check
- **/workspace/EventMixing/src/Mu2eProductMixer.cc:326** - Array access simOffsets_[ieIndex] without bounds check
- **/workspace/EventMixing/src/Mu2eProductMixer.cc:327** - Array access simOffsets_[ieIndex] without bounds check
- **/workspace/EventMixing/src/Mu2eProductMixer.cc:334** - Array access simOffsets_[ieIndex] without bounds check
- ... and 28 more

#### assignment_in_condition (6 occurrences)

- **/workspace/EventMixing/src/ProtonBunchIntensityLogNormal_module.cc:93** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/EventMixing/src/ProtonBunchIntensityLogNormal_module.cc:157** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/EventMixing/src/ProtonBunchIntensityLogNormal_module.cc:161** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/EventMixing/src/Mu2eProductMixer.cc:323** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/EventMixing/src/Mu2eProductMixer.cc:600** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/EventMixing/src/Mu2eProductMixer.cc:601** - Possible assignment (=) instead of comparison (==) in condition

#### division_by_zero (90 occurrences)

- **/workspace/EventMixing/src/ResamplingMixer_module.cc:6** - Potential division by zero: Framework not checked
- **/workspace/EventMixing/src/ResamplingMixer_module.cc:7** - Potential division by zero: Framework not checked
- **/workspace/EventMixing/src/ResamplingMixer_module.cc:8** - Potential division by zero: Framework not checked
- **/workspace/EventMixing/src/ResamplingMixer_module.cc:9** - Potential division by zero: RootIOPolicy not checked
- **/workspace/EventMixing/src/ResamplingMixer_module.cc:11** - Potential division by zero: types not checked
- **/workspace/EventMixing/src/ResamplingMixer_module.cc:12** - Potential division by zero: types not checked
- **/workspace/EventMixing/src/ResamplingMixer_module.cc:13** - Potential division by zero: types not checked
- **/workspace/EventMixing/src/ResamplingMixer_module.cc:14** - Potential division by zero: types not checked
- **/workspace/EventMixing/src/ResamplingMixer_module.cc:15** - Potential division by zero: Utilities not checked
- **/workspace/EventMixing/src/ResamplingMixer_module.cc:17** - Potential division by zero: SeedService not checked
- ... and 80 more

#### memory_leak (1 occurrences)

- **/workspace/EventMixing/src/MixingFilter_module.cc:50** - Potential memory leak: new collection without corresponding delete

#### missing_error_handling (3 occurrences)

- **/workspace/EventMixing/src/ProtonBunchIntensityLogNormal_module.cc:124** - getHandle/getValidHandle result not checked for validity
- **/workspace/EventMixing/src/Mu2eProductMixer.cc:168** - getHandle/getValidHandle result not checked for validity
- **/workspace/EventMixing/src/MixingFilter_module.cc:111** - getHandle/getValidHandle result not checked for validity

#### uninitialized_variable (5 occurrences)

- **/workspace/EventMixing/src/ProtonBunchIntensityFlat_module.cc:45** - Variable mean_ may be used uninitialized
- **/workspace/EventMixing/src/ProtonBunchIntensityLogNormal_module.cc:59** - Variable debug_ may be used uninitialized
- **/workspace/EventMixing/src/ProtonBunchIntensityLogNormal_module.cc:60** - Variable mean_ may be used uninitialized
- **/workspace/EventMixing/src/ProtonBunchIntensityLogNormal_module.cc:61** - Variable cutMin_ may be used uninitialized
- **/workspace/EventMixing/src/ProtonBunchIntensityLogNormal_module.cc:62** - Variable cutMax_ may be used uninitialized


### ExternalShieldingGeom

Found 3 potential bugs:

#### division_by_zero (3 occurrences)

- **/workspace/ExternalShieldingGeom/src/ExtShieldUpstream.cc:1** - Potential division by zero: ExternalShieldingGeom not checked
- **/workspace/ExternalShieldingGeom/src/ExtShieldDownstream.cc:1** - Potential division by zero: ExternalShieldingGeom not checked
- **/workspace/ExternalShieldingGeom/src/Saddle.cc:1** - Potential division by zero: ExternalShieldingGeom not checked


### Filters

Found 727 potential bugs:

#### array_bounds (111 occurrences)

- **/workspace/Filters/src/EMFPixelHitsFilter_module.cc:102** - Array access particles[ip] without bounds check
- **/workspace/Filters/src/EMFPixelHitsFilter_module.cc:132** - Array access oldParticles[ipart] without bounds check
- **/workspace/Filters/src/EMFPixelHitsFilter_module.cc:136** - Array access oldBits[ipart] without bounds check
- **/workspace/Filters/src/VetoIncorrectHits_module.cc:136** - Array access seenHitsMap_[crvStepPoints_] without bounds check
- **/workspace/Filters/src/VetoIncorrectHits_module.cc:208** - Array access passedHitsMap_[crvStepPoints_] without bounds check
- **/workspace/Filters/src/VetoIncorrectHits_module.cc:212** - Array access passedEventsMap_[crvStepPoints_] without bounds check
- **/workspace/Filters/src/VetoIncorrectHits_module.cc:236** - Array access seenHitsMap_[trackerStepPoints_] without bounds check
- **/workspace/Filters/src/VetoIncorrectHits_module.cc:309** - Array access passedHitsMap_[trackerStepPoints_] without bounds check
- **/workspace/Filters/src/VetoIncorrectHits_module.cc:313** - Array access passedEventsMap_[trackerStepPoints_] without bounds check
- **/workspace/Filters/src/VetoIncorrectHits_module.cc:339** - Array access seenHitsMap_[i.first] without bounds check
- ... and 101 more

#### assignment_in_condition (13 occurrences)

- **/workspace/Filters/src/CosmicMixingFilter_module.cc:147** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Filters/src/TrackSummaryTruthUpdater_module.cc:53** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Filters/src/SelectStepPointsByTime_module.cc:68** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Filters/src/TrkPatRecFilter_module.cc:67** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Filters/src/DetectorStepFilter_module.cc:153** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Filters/src/DetectorStepFilter_module.cc:178** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Filters/src/DetectorStepFilter_module.cc:204** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Filters/src/StrawDigiMCFilter_module.cc:93** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Filters/src/StepPointMCCollectionUpdater_module.cc:86** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Filters/src/FilterG4Out_module.cc:62** - Possible assignment (=) instead of comparison (==) in condition
- ... and 3 more

#### division_by_zero (459 occurrences)

- **/workspace/Filters/src/EMFPixelHitsFilter_module.cc:11** - Potential division by zero: ParameterSet not checked
- **/workspace/Filters/src/EMFPixelHitsFilter_module.cc:12** - Potential division by zero: Framework not checked
- **/workspace/Filters/src/EMFPixelHitsFilter_module.cc:13** - Potential division by zero: Framework not checked
- **/workspace/Filters/src/EMFPixelHitsFilter_module.cc:14** - Potential division by zero: Framework not checked
- **/workspace/Filters/src/EMFPixelHitsFilter_module.cc:15** - Potential division by zero: Persistency not checked
- **/workspace/Filters/src/EMFPixelHitsFilter_module.cc:16** - Potential division by zero: TFileService not checked
- **/workspace/Filters/src/EMFPixelHitsFilter_module.cc:17** - Potential division by zero: MessageLogger not checked
- **/workspace/Filters/src/EMFPixelHitsFilter_module.cc:19** - Potential division by zero: RecoDataProducts not checked
- **/workspace/Filters/src/EMFPixelHitsFilter_module.cc:20** - Potential division by zero: MCDataProducts not checked
- **/workspace/Filters/src/EMFPixelHitsFilter_module.cc:22** - Potential division by zero: Mu2eUtilities not checked
- ... and 449 more

#### memory_leak (51 occurrences)

- **/workspace/Filters/src/EMFPixelHitsFilter_module.cc:77** - Potential memory leak: new SimParticleCollection without corresponding delete
- **/workspace/Filters/src/EMFPixelHitsFilter_module.cc:78** - Potential memory leak: new ExtMonFNALHitTruthAssn without corresponding delete
- **/workspace/Filters/src/EMFPixelHitsFilter_module.cc:123** - Potential memory leak: new particle without corresponding delete
- **/workspace/Filters/src/KilledEventFilter_module.cc:177** - Potential memory leak: new std without corresponding delete
- **/workspace/Filters/src/KilledEventFilter_module.cc:178** - Potential memory leak: new std without corresponding delete
- **/workspace/Filters/src/KilledEventFilter_module.cc:179** - Potential memory leak: new std without corresponding delete
- **/workspace/Filters/src/KilledEventFilter_module.cc:180** - Potential memory leak: new std without corresponding delete
- **/workspace/Filters/src/KilledEventFilter_module.cc:181** - Potential memory leak: new std without corresponding delete
- **/workspace/Filters/src/KilledEventFilter_module.cc:182** - Potential memory leak: new std without corresponding delete
- **/workspace/Filters/src/KilledEventFilter_module.cc:183** - Potential memory leak: new std without corresponding delete
- ... and 41 more

#### missing_error_handling (23 occurrences)

- **/workspace/Filters/src/StepPointFilter_module.cc:36** - getHandle/getValidHandle result not checked for validity
- **/workspace/Filters/src/CompressPhysicalVolumes_module.cc:95** - getHandle/getValidHandle result not checked for validity
- **/workspace/Filters/src/CompressPhysicalVolumes_module.cc:108** - getHandle/getValidHandle result not checked for validity
- **/workspace/Filters/src/CompressPhysicalVolumes_module.cc:124** - getHandle/getValidHandle result not checked for validity
- **/workspace/Filters/src/FilterStatusG4_module.cc:64** - getHandle/getValidHandle result not checked for validity
- **/workspace/Filters/src/TrkQualFilter_module.cc:81** - getHandle/getValidHandle result not checked for validity
- **/workspace/Filters/src/TrackSummaryTruthUpdater_module.cc:45** - getHandle/getValidHandle result not checked for validity
- **/workspace/Filters/src/TrackSummaryTruthUpdater_module.cc:46** - getHandle/getValidHandle result not checked for validity
- **/workspace/Filters/src/FilterStepPointAngleVsTarget_module.cc:131** - getHandle/getValidHandle result not checked for validity
- **/workspace/Filters/src/FilterStepPointPDG_module.cc:130** - getHandle/getValidHandle result not checked for validity
- ... and 13 more

#### missing_return (1 occurrences)

- **/workspace/Filters/src/CompressStepPointMCs_module.cc:76** - Function may be missing return statement

#### uninitialized_variable (69 occurrences)

- **/workspace/Filters/src/EMFPixelHitsFilter_module.cc:53** - Variable cutMinHits_ may be used uninitialized
- **/workspace/Filters/src/EMFPixelHitsFilter_module.cc:55** - Variable nPassed_ may be used uninitialized
- **/workspace/Filters/src/CosmicMixingFilter_module.cc:77** - Variable diagLevel_ may be used uninitialized
- **/workspace/Filters/src/CosmicMixingFilter_module.cc:80** - Variable maxImpact_ may be used uninitialized
- **/workspace/Filters/src/CosmicMixingFilter_module.cc:81** - Variable timecut_ may be used uninitialized
- **/workspace/Filters/src/TrkQualFilter_module.cc:51** - Variable _effRequest may be used uninitialized
- **/workspace/Filters/src/ParticleCodeFilter_module.cc:49** - Variable printLevel_ may be used uninitialized
- **/workspace/Filters/src/SelectStepPointsByTime_module.cc:30** - Variable cutTimeMin_ may be used uninitialized
- **/workspace/Filters/src/SelectStepPointsByTime_module.cc:31** - Variable cutTimeMax_ may be used uninitialized
- **/workspace/Filters/src/SelectStepPointsByTime_module.cc:34** - Variable numInputHits_ may be used uninitialized
- ... and 59 more


### GeneralUtilities

Found 229 potential bugs:

#### array_bounds (86 occurrences)

- **/workspace/GeneralUtilities/src/VMInfo.cc:43** - Array access values[name] without bounds check
- **/workspace/GeneralUtilities/src/VMInfo.cc:49** - Array access values["VmPeak"] without bounds check
- **/workspace/GeneralUtilities/src/VMInfo.cc:50** - Array access values["VmSize"] without bounds check
- **/workspace/GeneralUtilities/src/VMInfo.cc:51** - Array access values["VmHWM"] without bounds check
- **/workspace/GeneralUtilities/src/VMInfo.cc:52** - Array access values["VmRSS"] without bounds check
- **/workspace/GeneralUtilities/src/ParseCLI.cc:98** - Array access args_span[0] without bounds check
- **/workspace/GeneralUtilities/src/ParseCLI.cc:105** - Array access args_span[i] without bounds check
- **/workspace/GeneralUtilities/src/ParseCLI.cc:111** - Array access a[0] without bounds check
- **/workspace/GeneralUtilities/src/ParseCLI.cc:124** - Array access p1[i] without bounds check
- **/workspace/GeneralUtilities/src/ParseCLI.cc:151** - Array access a1[i] without bounds check
- ... and 76 more

#### assignment_in_condition (44 occurrences)

- **/workspace/GeneralUtilities/src/NUBinning.cc:12** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/GeneralUtilities/src/VMInfo.cc:19** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/GeneralUtilities/src/ParseCLI.cc:101** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/GeneralUtilities/src/ParseCLI.cc:115** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/GeneralUtilities/src/ParseCLI.cc:154** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/GeneralUtilities/src/ParseCLI.cc:208** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/GeneralUtilities/src/ParseCLI.cc:229** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/GeneralUtilities/src/ParseCLI.cc:295** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/GeneralUtilities/src/RMS.cc:32** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/GeneralUtilities/src/OrientationResolver.cc:80** - Possible assignment (=) instead of comparison (==) in condition
- ... and 34 more

#### division_by_zero (73 occurrences)

- **/workspace/GeneralUtilities/src/NUBinning.cc:1** - Potential division by zero: GeneralUtilities not checked
- **/workspace/GeneralUtilities/src/VMInfo.cc:1** - Potential division by zero: GeneralUtilities not checked
- **/workspace/GeneralUtilities/src/VMInfo.cc:34** - Potential division by zero: proc not checked
- **/workspace/GeneralUtilities/src/toHex.cc:8** - Potential division by zero: GeneralUtilities not checked
- **/workspace/GeneralUtilities/src/ParseCLI.cc:1** - Potential division by zero: GeneralUtilities not checked
- **/workspace/GeneralUtilities/src/ParameterSetHelpers.cc:3** - Potential division by zero: GeneralUtilities not checked
- **/workspace/GeneralUtilities/src/ParameterSetHelpers.cc:10** - Potential division by zero: Vector not checked
- **/workspace/GeneralUtilities/src/ParameterSetHelpers.cc:12** - Potential division by zero: GeneralUtilities not checked
- **/workspace/GeneralUtilities/src/ParameterSetHelpers.cc:13** - Potential division by zero: GeneralUtilities not checked
- **/workspace/GeneralUtilities/src/ParameterSetHelpers.cc:15** - Potential division by zero: Utilities not checked
- ... and 63 more

#### memory_leak (1 occurrences)

- **/workspace/GeneralUtilities/src/CsvReader.cc:104** - Potential memory leak: new column without corresponding delete

#### missing_return (19 occurrences)

- **/workspace/GeneralUtilities/src/OrientationResolver.cc:89** - Function may be missing return statement
- **/workspace/GeneralUtilities/src/OrientationResolver.cc:91** - Function may be missing return statement
- **/workspace/GeneralUtilities/src/OrientationResolver.cc:93** - Function may be missing return statement
- **/workspace/GeneralUtilities/src/OrientationResolver.cc:96** - Function may be missing return statement
- **/workspace/GeneralUtilities/src/OrientationResolver.cc:101** - Function may be missing return statement
- **/workspace/GeneralUtilities/src/OrientationResolver.cc:103** - Function may be missing return statement
- **/workspace/GeneralUtilities/src/OrientationResolver.cc:105** - Function may be missing return statement
- **/workspace/GeneralUtilities/src/OrientationResolver.cc:108** - Function may be missing return statement
- **/workspace/GeneralUtilities/src/OrientationResolver.cc:113** - Function may be missing return statement
- **/workspace/GeneralUtilities/src/OrientationResolver.cc:115** - Function may be missing return statement
- ... and 9 more

#### uninitialized_variable (6 occurrences)

- **/workspace/GeneralUtilities/src/SplineInterpolation.cc:88** - Variable ibin may be used uninitialized
- **/workspace/GeneralUtilities/src/SplineInterpolation.cc:89** - Variable t may be used uninitialized
- **/workspace/GeneralUtilities/src/SplineInterpolation.cc:106** - Variable ibin may be used uninitialized
- **/workspace/GeneralUtilities/src/SplineInterpolation.cc:107** - Variable t may be used uninitialized
- **/workspace/GeneralUtilities/src/TwoDPointTest_main.cc:32** - Variable opt may be used uninitialized
- **/workspace/GeneralUtilities/src/TwoDPoint.cc:10** - Variable det may be used uninitialized


### GeomPrimitives

Found 6 potential bugs:

#### division_by_zero (6 occurrences)

- **/workspace/GeomPrimitives/src/Tube.cc:10** - Potential division by zero: GeomPrimitives not checked
- **/workspace/GeomPrimitives/src/Polyhedra.cc:10** - Potential division by zero: GeomPrimitives not checked
- **/workspace/GeomPrimitives/src/Polyhedra.cc:15** - Potential division by zero: exception not checked
- **/workspace/GeomPrimitives/src/PlacedTubs.cc:11** - Potential division by zero: GeomPrimitives not checked
- **/workspace/GeomPrimitives/src/Polycone.cc:8** - Potential division by zero: GeomPrimitives not checked
- **/workspace/GeomPrimitives/src/Polycone.cc:13** - Potential division by zero: exception not checked


### GeometryService

Found 1192 potential bugs:

#### array_bounds (390 occurrences)

- **/workspace/GeometryService/src/StoppingTargetMaker.cc:53** - Array access _halfThicknesses[size-1] without bounds check
- **/workspace/GeometryService/src/StoppingTargetMaker.cc:59** - Array access _xVars[size-1] without bounds check
- **/workspace/GeometryService/src/StoppingTargetMaker.cc:65** - Array access _yVars[size-1] without bounds check
- **/workspace/GeometryService/src/StoppingTargetMaker.cc:71** - Array access _zVars[size-1] without bounds check
- **/workspace/GeometryService/src/StoppingTargetMaker.cc:77** - Array access _xCos[size-1] without bounds check
- **/workspace/GeometryService/src/StoppingTargetMaker.cc:83** - Array access _yCos[size-1] without bounds check
- **/workspace/GeometryService/src/StoppingTargetMaker.cc:167** - Array access _zVars[i] without bounds check
- **/workspace/GeometryService/src/StoppingTargetMaker.cc:172** - Array access _xCos[i] without bounds check
- **/workspace/GeometryService/src/StoppingTargetMaker.cc:181** - Array access _xVars[i] without bounds check
- **/workspace/GeometryService/src/StoppingTargetMaker.cc:182** - Array access _yVars[i] without bounds check
- ... and 380 more

#### assignment_in_condition (46 occurrences)

- **/workspace/GeometryService/src/MBSMaker.cc:174** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/GeometryService/src/MBSMaker.cc:204** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/GeometryService/src/MBSMaker.cc:235** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/GeometryService/src/MBSMaker.cc:264** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/GeometryService/src/MBSMaker.cc:326** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/GeometryService/src/MBSMaker.cc:401** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/GeometryService/src/MBSMaker.cc:442** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/GeometryService/src/MBSMaker.cc:477** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/GeometryService/src/MBSMaker.cc:535** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/GeometryService/src/VirtualDetectorMaker.cc:204** - Possible assignment (=) instead of comparison (==) in condition
- ... and 36 more

#### division_by_zero (587 occurrences)

- **/workspace/GeometryService/src/StoppingTargetMaker.cc:13** - Potential division by zero: MessageLogger not checked
- **/workspace/GeometryService/src/StoppingTargetMaker.cc:16** - Potential division by zero: GlobalConstantsService not checked
- **/workspace/GeometryService/src/StoppingTargetMaker.cc:17** - Potential division by zero: GlobalConstantsService not checked
- **/workspace/GeometryService/src/StoppingTargetMaker.cc:18** - Potential division by zero: GeometryService not checked
- **/workspace/GeometryService/src/StoppingTargetMaker.cc:19** - Potential division by zero: StoppingTargetGeom not checked
- **/workspace/GeometryService/src/StoppingTargetMaker.cc:20** - Potential division by zero: Vector not checked
- **/workspace/GeometryService/src/StoppingTargetMaker.cc:21** - Potential division by zero: Vector not checked
- **/workspace/GeometryService/src/StoppingTargetMaker.cc:22** - Potential division by zero: Vector not checked
- **/workspace/GeometryService/src/StoppingTargetMaker.cc:23** - Potential division by zero: ConfigTools not checked
- **/workspace/GeometryService/src/StoppingTargetMaker.cc:91** - Potential division by zero: test not checked
- ... and 577 more

#### memory_leak (140 occurrences)

- **/workspace/GeometryService/src/StoppingTargetMaker.cc:153** - Potential memory leak: new StoppingTarget without corresponding delete
- **/workspace/GeometryService/src/BFieldConfigMaker.cc:44** - Potential memory leak: new BFieldConfig without corresponding delete
- **/workspace/GeometryService/src/PTMMaker.cc:150** - Potential memory leak: new PTMPWC without corresponding delete
- **/workspace/GeometryService/src/PTMMaker.cc:158** - Potential memory leak: new PTMPWC without corresponding delete
- **/workspace/GeometryService/src/PTMMaker.cc:167** - Potential memory leak: new Box without corresponding delete
- **/workspace/GeometryService/src/PTMMaker.cc:169** - Potential memory leak: new Box without corresponding delete
- **/workspace/GeometryService/src/PTMMaker.cc:172** - Potential memory leak: new Box without corresponding delete
- **/workspace/GeometryService/src/PTMMaker.cc:177** - Potential memory leak: new PTMHead without corresponding delete
- **/workspace/GeometryService/src/PTMMaker.cc:213** - Potential memory leak: new ExtrudedSolid without corresponding delete
- **/workspace/GeometryService/src/PTMMaker.cc:216** - Potential memory leak: new Box without corresponding delete
- ... and 130 more

#### missing_return (15 occurrences)

- **/workspace/GeometryService/src/BFieldConfigMaker.cc:74** - Function may be missing return statement
- **/workspace/GeometryService/src/BFieldConfigMaker.cc:105** - Function may be missing return statement
- **/workspace/GeometryService/src/MBSMaker.cc:544** - Function may be missing return statement
- **/workspace/GeometryService/src/TrackerMaker.cc:295** - Function may be missing return statement
- **/workspace/GeometryService/src/TrackerMaker.cc:311** - Function may be missing return statement
- **/workspace/GeometryService/src/TrackerMaker.cc:325** - Function may be missing return statement
- **/workspace/GeometryService/src/TrackerMaker.cc:342** - Function may be missing return statement
- **/workspace/GeometryService/src/TrackerMaker.cc:367** - Function may be missing return statement
- **/workspace/GeometryService/src/TrackerMaker.cc:1375** - Function may be missing return statement
- **/workspace/GeometryService/src/TrackerMaker.cc:1420** - Function may be missing return statement
- ... and 5 more

#### resource_leak (1 occurrences)

- **/workspace/GeometryService/src/BFieldManagerMaker.cc:418** - File handle opened but may not be closed

#### uninitialized_variable (5 occurrences)

- **/workspace/GeometryService/src/BFieldManagerMaker.cc:168** - Variable value may be used uninitialized
- **/workspace/GeometryService/src/BFieldManagerMaker.cc:175** - Variable value may be used uninitialized
- **/workspace/GeometryService/src/BFieldManagerMaker.cc:182** - Variable value may be used uninitialized
- **/workspace/GeometryService/src/BFieldManagerMaker.cc:193** - Variable value may be used uninitialized
- **/workspace/GeometryService/src/BFieldManagerMaker.cc:385** - Variable extendYFound may be used uninitialized

#### unused_variable (8 occurrences)

- **/workspace/GeometryService/src/StoppingTargetMaker.cc:82** - Variable ii declared but possibly unused
- **/workspace/GeometryService/src/VirtualDetectorMaker.cc:819** - Variable i declared but possibly unused
- **/workspace/GeometryService/src/ElectronicRackMaker.cc:62** - Variable itmp declared but possibly unused
- **/workspace/GeometryService/src/BFieldManagerMaker.cc:673** - Variable i declared but possibly unused
- **/workspace/GeometryService/src/ProductionTargetMaker.cc:236** - Variable iSpk declared but possibly unused
- **/workspace/GeometryService/src/MECOStyleProtonAbsorberMaker.cc:280** - Variable iSlat declared but possibly unused
- **/workspace/GeometryService/src/MECOStyleProtonAbsorberMaker.cc:339** - Variable iSup declared but possibly unused
- **/workspace/GeometryService/src/ExtShieldDownstreamMaker.cc:276** - Variable idummy declared but possibly unused


### GlobalConstantsService

Found 75 potential bugs:

#### array_bounds (39 occurrences)

- **/workspace/GlobalConstantsService/src/GlobalConstantsService.cc:51** - Array access makers_[typeid(mu2e::PhysicsParams).name()] without bounds check
- **/workspace/GlobalConstantsService/src/GlobalConstantsService.cc:52** - Array access makers_[typeid(mu2e::ParticleDataList).name()] without bounds check
- **/workspace/GlobalConstantsService/src/ParticleDataList.cc:53** - Array access words[0] without bounds check
- **/workspace/GlobalConstantsService/src/ParticleDataList.cc:55** - Array access words[2] without bounds check
- **/workspace/GlobalConstantsService/src/ParticleDataList.cc:56** - Array access words[1] without bounds check
- **/workspace/GlobalConstantsService/src/ParticleDataList.cc:57** - Array access words[5] without bounds check
- **/workspace/GlobalConstantsService/src/ParticleDataList.cc:58** - Array access words[1] without bounds check
- **/workspace/GlobalConstantsService/src/ParticleDataList.cc:60** - Array access words[3] without bounds check
- **/workspace/GlobalConstantsService/src/ParticleDataList.cc:61** - Array access words[4] without bounds check
- **/workspace/GlobalConstantsService/src/PhysicsParams.cc:54** - Array access freeLifetime_[PDGCode::type(tmpPDGId[i] without bounds check
- ... and 29 more

#### assignment_in_condition (4 occurrences)

- **/workspace/GlobalConstantsService/src/ParticleDataList.cc:60** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/GlobalConstantsService/src/ParticleDataList.cc:61** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/GlobalConstantsService/src/ParticleDataList.cc:72** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/GlobalConstantsService/src/ParticleDataList.cc:76** - Possible assignment (=) instead of comparison (==) in condition

#### division_by_zero (29 occurrences)

- **/workspace/GlobalConstantsService/src/MassCache.cc:4** - Potential division by zero: GlobalConstantsService not checked
- **/workspace/GlobalConstantsService/src/MassCache.cc:5** - Potential division by zero: GlobalConstantsService not checked
- **/workspace/GlobalConstantsService/src/MassCache.cc:6** - Potential division by zero: GlobalConstantsService not checked
- **/workspace/GlobalConstantsService/src/MassCache.cc:8** - Potential division by zero: Units not checked
- **/workspace/GlobalConstantsService/src/ParticleData.cc:1** - Potential division by zero: GlobalConstantsService not checked
- **/workspace/GlobalConstantsService/src/GlobalConstantsService_service.cc:5** - Potential division by zero: Framework not checked
- **/workspace/GlobalConstantsService/src/GlobalConstantsService_service.cc:6** - Potential division by zero: GlobalConstantsService not checked
- **/workspace/GlobalConstantsService/src/GlobalConstantsService.cc:10** - Potential division by zero: GlobalConstantsService not checked
- **/workspace/GlobalConstantsService/src/GlobalConstantsService.cc:16** - Potential division by zero: exception not checked
- **/workspace/GlobalConstantsService/src/GlobalConstantsService.cc:18** - Potential division by zero: ConfigTools not checked
- ... and 19 more

#### memory_leak (3 occurrences)

- **/workspace/GlobalConstantsService/src/MassCache.cc:26** - Potential memory leak: new entry without corresponding delete
- **/workspace/GlobalConstantsService/src/GlobalConstantsService.cc:1** - Potential memory leak: new entity without corresponding delete
- **/workspace/GlobalConstantsService/src/GlobalConstantsService.cc:29** - Potential memory leak: new T without corresponding delete


### HelloWorld

Found 12 potential bugs:

#### division_by_zero (10 occurrences)

- **/workspace/HelloWorld/src/HelloWorld_module.cc:12** - Potential division by zero: Framework not checked
- **/workspace/HelloWorld/src/HelloWorld_module.cc:13** - Potential division by zero: Framework not checked
- **/workspace/HelloWorld/src/HelloWorld2_module.cc:12** - Potential division by zero: Framework not checked
- **/workspace/HelloWorld/src/HelloWorld2_module.cc:13** - Potential division by zero: Framework not checked
- **/workspace/HelloWorld/src/HelloWorld2_module.cc:14** - Potential division by zero: Framework not checked
- **/workspace/HelloWorld/src/HelloWorld2_module.cc:15** - Potential division by zero: Framework not checked
- **/workspace/HelloWorld/src/HelloWorld2_module.cc:16** - Potential division by zero: ParameterSet not checked
- **/workspace/HelloWorld/src/HelloProducer_module.cc:12** - Potential division by zero: Framework not checked
- **/workspace/HelloWorld/src/HelloProducer_module.cc:13** - Potential division by zero: Framework not checked
- **/workspace/HelloWorld/src/HelloProducer_module.cc:16** - Potential division by zero: MCDataProducts not checked

#### memory_leak (1 occurrences)

- **/workspace/HelloWorld/src/HelloProducer_module.cc:39** - Potential memory leak: new GenParticleCollection without corresponding delete

#### uninitialized_variable (1 occurrences)

- **/workspace/HelloWorld/src/HelloWorld2_module.cc:47** - Variable _magicNumber may be used uninitialized


### KinKalGeom

Found 9 potential bugs:

#### division_by_zero (9 occurrences)

- **/workspace/KinKalGeom/src/StoppingTarget.cc:1** - Potential division by zero: KinKalGeom not checked
- **/workspace/KinKalGeom/src/StoppingTarget.cc:16** - Potential division by zero: 36 not checked
- **/workspace/KinKalGeom/src/SurfaceMap.cc:1** - Potential division by zero: KinKalGeom not checked
- **/workspace/KinKalGeom/src/SurfaceMap.cc:2** - Potential division by zero: exception not checked
- **/workspace/KinKalGeom/src/DetectorSolenoid.cc:1** - Potential division by zero: KinKalGeom not checked
- **/workspace/KinKalGeom/src/CRV.cc:1** - Potential division by zero: KinKalGeom not checked
- **/workspace/KinKalGeom/src/CRV.cc:4** - Potential division by zero: 04 not checked
- **/workspace/KinKalGeom/src/TestCRV.cc:1** - Potential division by zero: KinKalGeom not checked
- **/workspace/KinKalGeom/src/Tracker.cc:1** - Potential division by zero: KinKalGeom not checked


### Lumi

Found 78 potential bugs:

#### array_bounds (7 occurrences)

- **/workspace/Lumi/src/NPOTAnalysis_module.cc:125** - Array access _EventHists[kNEventHistsSets] without bounds check
- **/workspace/Lumi/src/NPOTAnalysis_module.cc:255** - Array access folder_name[20] without bounds check
- **/workspace/Lumi/src/NPOTAnalysis_module.cc:264** - Array access _EventHists[i] without bounds check
- **/workspace/Lumi/src/NPOTAnalysis_module.cc:265** - Array access _EventHists[i] without bounds check
- **/workspace/Lumi/src/NPOTAnalysis_module.cc:278** - Array access E[MeV] without bounds check
- **/workspace/Lumi/src/NPOTAnalysis_module.cc:305** - Array access E[MeV] without bounds check
- **/workspace/Lumi/src/NPOTAnalysis_module.cc:359** - Array access _EventHists[0] without bounds check

#### assignment_in_condition (2 occurrences)

- **/workspace/Lumi/src/RecoNPOTFilter_module.cc:79** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Lumi/src/RecoNPOTFilter_module.cc:100** - Possible assignment (=) instead of comparison (==) in condition

#### division_by_zero (60 occurrences)

- **/workspace/Lumi/src/RecoNPOTFilter_module.cc:4** - Potential division by zero: Framework not checked
- **/workspace/Lumi/src/RecoNPOTFilter_module.cc:5** - Potential division by zero: Framework not checked
- **/workspace/Lumi/src/RecoNPOTFilter_module.cc:6** - Potential division by zero: Framework not checked
- **/workspace/Lumi/src/RecoNPOTFilter_module.cc:7** - Potential division by zero: Framework not checked
- **/workspace/Lumi/src/RecoNPOTFilter_module.cc:8** - Potential division by zero: Framework not checked
- **/workspace/Lumi/src/RecoNPOTFilter_module.cc:10** - Potential division by zero: ParameterSet not checked
- **/workspace/Lumi/src/RecoNPOTFilter_module.cc:12** - Potential division by zero: Random not checked
- **/workspace/Lumi/src/RecoNPOTFilter_module.cc:13** - Potential division by zero: Random not checked
- **/workspace/Lumi/src/RecoNPOTFilter_module.cc:16** - Potential division by zero: SeedService not checked
- **/workspace/Lumi/src/RecoNPOTFilter_module.cc:17** - Potential division by zero: ConfigTools not checked
- ... and 50 more

#### memory_leak (1 occurrences)

- **/workspace/Lumi/src/NPOTAnalysis_module.cc:264** - Potential memory leak: new EventHists without corresponding delete

#### missing_error_handling (1 occurrences)

- **/workspace/Lumi/src/RecoNPOTFilter_module.cc:111** - getHandle/getValidHandle result not checked for validity

#### missing_return (5 occurrences)

- **/workspace/Lumi/src/RecoNPOTMaker_module.cc:190** - Function may be missing return statement
- **/workspace/Lumi/src/RecoNPOTMaker_module.cc:198** - Function may be missing return statement
- **/workspace/Lumi/src/RecoNPOTMaker_module.cc:206** - Function may be missing return statement
- **/workspace/Lumi/src/RecoNPOTMaker_module.cc:214** - Function may be missing return statement
- **/workspace/Lumi/src/RecoNPOTMaker_module.cc:239** - Function may be missing return statement

#### uninitialized_variable (2 occurrences)

- **/workspace/Lumi/src/RecoNPOTFilter_module.cc:56** - Variable _minWeight may be used uninitialized
- **/workspace/Lumi/src/RecoNPOTFilter_module.cc:58** - Variable _debugLevel may be used uninitialized


### MCDataProducts

Found 62 potential bugs:

#### array_bounds (16 occurrences)

- **/workspace/MCDataProducts/src/StepFilterMode.cc:63** - Array access nam[i] without bounds check
- **/workspace/MCDataProducts/src/StrawDigiMC.cc:51** - Array access _sgspa[strawend] without bounds check
- **/workspace/MCDataProducts/src/StrawDigiMC.cc:52** - Array access _sgspa[strawend] without bounds check
- **/workspace/MCDataProducts/src/StrawDigiMC.cc:58** - Array access _sgspa[0] without bounds check
- **/workspace/MCDataProducts/src/StrawDigiMC.cc:59** - Array access _sgspa[0] without bounds check
- **/workspace/MCDataProducts/src/StrawDigiMC.cc:61** - Array access _sgspa[0] without bounds check
- **/workspace/MCDataProducts/src/StrawDigiMC.cc:65** - Array access _sgspa[strawend] without bounds check
- **/workspace/MCDataProducts/src/StrawDigiMC.cc:71** - Array access _ctime[0] without bounds check
- **/workspace/MCDataProducts/src/ProcessCode.cc:32** - Array access _name[i] without bounds check
- **/workspace/MCDataProducts/src/ProcessCode.cc:40** - Array access _name[i] without bounds check
- ... and 6 more

#### assignment_in_condition (5 occurrences)

- **/workspace/MCDataProducts/src/CaloClusterMC.cc:18** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/MCDataProducts/src/MCRelationship.cc:53** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/MCDataProducts/src/MCRelationship.cc:56** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/MCDataProducts/src/MCRelationship.cc:62** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/MCDataProducts/src/MCRelationship.cc:70** - Possible assignment (=) instead of comparison (==) in condition

#### division_by_zero (38 occurrences)

- **/workspace/MCDataProducts/src/StageParticle.cc:1** - Potential division by zero: MCDataProducts not checked
- **/workspace/MCDataProducts/src/SimParticle.cc:1** - Potential division by zero: MCDataProducts not checked
- **/workspace/MCDataProducts/src/DigiProvenance.cc:5** - Potential division by zero: MCDataProducts not checked
- **/workspace/MCDataProducts/src/StepFilterMode.cc:9** - Potential division by zero: MCDataProducts not checked
- **/workspace/MCDataProducts/src/StepFilterMode.cc:11** - Potential division by zero: static_assert not checked
- **/workspace/MCDataProducts/src/StepFilterMode.cc:41** - Potential division by zero: sizeof not checked
- **/workspace/MCDataProducts/src/StrawDigiMC.cc:7** - Potential division by zero: MCDataProducts not checked
- **/workspace/MCDataProducts/src/StrawDigiMC.cc:8** - Potential division by zero: DataProducts not checked
- **/workspace/MCDataProducts/src/StrawDigiMC.cc:10** - Potential division by zero: exception not checked
- **/workspace/MCDataProducts/src/MARSInfo.cc:1** - Potential division by zero: MCDataProducts not checked
- ... and 28 more

#### memory_leak (2 occurrences)

- **/workspace/MCDataProducts/src/GenId.cc:70** - Potential memory leak: new
 enum without corresponding delete
- **/workspace/MCDataProducts/src/GenId.cc:71** - Potential memory leak: new type without corresponding delete

#### unused_variable (1 occurrences)

- **/workspace/MCDataProducts/src/PhysicalVolumeInfo.cc:18** - Variable operator declared but possibly unused


### MECOStyleProtonAbsorberGeom

Found 1 potential bugs:

#### division_by_zero (1 occurrences)

- **/workspace/MECOStyleProtonAbsorberGeom/src/MECOStyleProtonAbsorber.cc:9** - Potential division by zero: MECOStyleProtonAbsorberGeom not checked


### Mu2e

Found 5 potential bugs:

#### division_by_zero (4 occurrences)

- **/workspace/Mu2e/src/mu2e_main.cc:5** - Potential division by zero: Framework not checked
- **/workspace/Mu2e/src/mu2e_main.cc:10** - Potential division by zero: Framework not checked
- **/workspace/Mu2e/src/mu2e_main.cc:11** - Potential division by zero: MessageLogger not checked
- **/workspace/Mu2e/src/mu2e_main.cc:44** - Potential division by zero: build not checked

#### missing_return (1 occurrences)

- **/workspace/Mu2e/src/mu2e_main.cc:32** - Function may be missing return statement


### Mu2eBTrk

Found 25 potential bugs:

#### array_bounds (3 occurrences)

- **/workspace/Mu2eBTrk/src/ParticleInfo.cc:79** - Array access table_[id] without bounds check
- **/workspace/Mu2eBTrk/src/DetStrawElem.cc:65** - Array access pathrange[0] without bounds check
- **/workspace/Mu2eBTrk/src/DetStrawElem.cc:66** - Array access pathrange[1] without bounds check

#### assignment_in_condition (2 occurrences)

- **/workspace/Mu2eBTrk/src/ParticleInfo.cc:15** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Mu2eBTrk/src/DetStrawElem.cc:55** - Possible assignment (=) instead of comparison (==) in condition

#### division_by_zero (18 occurrences)

- **/workspace/Mu2eBTrk/src/BaBarMu2eField.cc:3** - Potential division by zero: BaBar not checked
- **/workspace/Mu2eBTrk/src/BaBarMu2eField.cc:4** - Potential division by zero: Mu2eBTrk not checked
- **/workspace/Mu2eBTrk/src/BaBarMu2eField.cc:5** - Potential division by zero: GeometryService not checked
- **/workspace/Mu2eBTrk/src/BaBarMu2eField.cc:6** - Potential division by zero: BFieldGeom not checked
- **/workspace/Mu2eBTrk/src/BaBarMu2eField.cc:7** - Potential division by zero: GeometryService not checked
- **/workspace/Mu2eBTrk/src/ParticleInfo.cc:1** - Potential division by zero: Mu2eBTrk not checked
- **/workspace/Mu2eBTrk/src/ParticleInfo.cc:2** - Potential division by zero: DataProducts not checked
- **/workspace/Mu2eBTrk/src/ParticleInfo.cc:4** - Potential division by zero: GlobalConstantsService not checked
- **/workspace/Mu2eBTrk/src/ParticleInfo.cc:5** - Potential division by zero: GlobalConstantsService not checked
- **/workspace/Mu2eBTrk/src/DetStrawElem.cc:8** - Potential division by zero: Mu2eBTrk not checked
- ... and 8 more

#### memory_leak (1 occurrences)

- **/workspace/Mu2eBTrk/src/DetStrawElem.cc:30** - Potential memory leak: new TrkLineTraj without corresponding delete

#### use_after_free (1 occurrences)

- **/workspace/Mu2eBTrk/src/DetStrawElem.cc:34** - Potential use after free: _wtraj deleted but may be used later


### Mu2eG4

Found 5145 potential bugs:

#### array_bounds (766 occurrences)

- **/workspace/Mu2eG4/src/Mu2eG4DSGradientMagneticField.cc:27** - Array access Point[4] without bounds check
- **/workspace/Mu2eG4/src/Mu2eG4DSGradientMagneticField.cc:33** - Array access Point[0] without bounds check
- **/workspace/Mu2eG4/src/Mu2eG4DSGradientMagneticField.cc:35** - Array access Bfield[2] without bounds check
- **/workspace/Mu2eG4/src/Mu2eG4DSGradientMagneticField.cc:40** - Array access Bfield[0] without bounds check
- **/workspace/Mu2eG4/src/Mu2eG4DSGradientMagneticField.cc:41** - Array access Bfield[0] without bounds check
- **/workspace/Mu2eG4/src/Mu2eG4DSGradientMagneticField.cc:42** - Array access Bfield[1] without bounds check
- **/workspace/Mu2eG4/src/Mu2eG4DSGradientMagneticField.cc:46** - Array access Bfield[0] without bounds check
- **/workspace/Mu2eG4/src/constructSTM.cc:142** - Array access stmMagnetHoleHalfLengths[3] without bounds check
- **/workspace/Mu2eG4/src/constructSTM.cc:146** - Array access stmMagnetHoleHalfLengths[0] without bounds check
- **/workspace/Mu2eG4/src/constructSTM.cc:147** - Array access stmMagnetHoleHalfLengths[1] without bounds check
- ... and 756 more

#### assignment_in_condition (60 occurrences)

- **/workspace/Mu2eG4/src/Mu2eG4Cuts.cc:72** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Mu2eG4/src/Mu2eG4Cuts.cc:85** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Mu2eG4/src/IonProducer_module.cc:69** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Mu2eG4/src/constructVirtualDetectors.cc:1798** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Mu2eG4/src/ConstructTrackerDetail5.cc:333** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Mu2eG4/src/Mu2eG4SensitiveDetector.cc:120** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Mu2eG4/src/constructDS.cc:406** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Mu2eG4/src/Mu2eG4WorkerRunManager.cc:229** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Mu2eG4/src/generateFieldMap.cc:38** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Mu2eG4/src/constructProtonAbsorber.cc:1631** - Possible assignment (=) instead of comparison (==) in condition
- ... and 50 more

#### division_by_zero (3203 occurrences)

- **/workspace/Mu2eG4/src/CaloReadoutCardSD.cc:10** - Potential division by zero: MessageLogger not checked
- **/workspace/Mu2eG4/src/CaloReadoutCardSD.cc:11** - Potential division by zero: exception not checked
- **/workspace/Mu2eG4/src/CaloReadoutCardSD.cc:14** - Potential division by zero: Mu2eG4 not checked
- **/workspace/Mu2eG4/src/CaloReadoutCardSD.cc:15** - Potential division by zero: Mu2eG4 not checked
- **/workspace/Mu2eG4/src/CaloReadoutCardSD.cc:16** - Potential division by zero: Mu2eG4 not checked
- **/workspace/Mu2eG4/src/CaloReadoutCardSD.cc:17** - Potential division by zero: Mu2eG4 not checked
- **/workspace/Mu2eG4/src/CaloReadoutCardSD.cc:18** - Potential division by zero: GeometryService not checked
- **/workspace/Mu2eG4/src/CaloReadoutCardSD.cc:19** - Potential division by zero: CalorimeterGeom not checked
- **/workspace/Mu2eG4/src/CaloReadoutCardSD.cc:22** - Potential division by zero: G4Step not checked
- **/workspace/Mu2eG4/src/physicsListDecider.cc:29** - Potential division by zero: exception not checked
- ... and 3193 more

#### memory_leak (1021 occurrences)

- **/workspace/Mu2eG4/src/physicsListDecider.cc:75** - Potential memory leak: new Mu2eG4MinimalModularPhysicsList without corresponding delete
- **/workspace/Mu2eG4/src/physicsListDecider.cc:79** - Potential memory leak: new Mu2eG4MinDEDXModularPhysicsList without corresponding delete
- **/workspace/Mu2eG4/src/physicsListDecider.cc:86** - Potential memory leak: new G4ErrorPhysicsList without corresponding delete
- **/workspace/Mu2eG4/src/physicsListDecider.cc:122** - Potential memory leak: new Mu2eG4StepLimiterPhysicsConstructor without corresponding delete
- **/workspace/Mu2eG4/src/physicsListDecider.cc:125** - Potential memory leak: new Mu2eG4CustomizationPhysicsConstructor without corresponding delete
- **/workspace/Mu2eG4/src/physicsListDecider.cc:153** - Potential memory leak: new G4RadioactiveDecayPhysics without corresponding delete
- **/workspace/Mu2eG4/src/physicsListDecider.cc:158** - Potential memory leak: new Mu2eG4BiasedRDPhysics without corresponding delete
- **/workspace/Mu2eG4/src/physicsListDecider.cc:162** - Potential memory leak: new G4ThermalNeutrons without corresponding delete
- **/workspace/Mu2eG4/src/physicsListDecider.cc:205** - Potential memory leak: new Mu2eG4DecayMuonsWithSpinPhysicsConstructor without corresponding delete
- **/workspace/Mu2eG4/src/Mu2eWorld.cc:283** - Potential memory leak: new G4Region without corresponding delete
- ... and 1011 more

#### missing_error_handling (8 occurrences)

- **/workspace/Mu2eG4/src/writePhysicalVolumes.cc:24** - getHandle/getValidHandle result not checked for validity
- **/workspace/Mu2eG4/src/Mu2eG4Cuts.cc:86** - getHandle/getValidHandle result not checked for validity
- **/workspace/Mu2eG4/src/Mu2eG4TrackingAction.cc:373** - getHandle/getValidHandle result not checked for validity
- **/workspace/Mu2eG4/src/SensitiveDetectorHelper.cc:195** - getHandle/getValidHandle result not checked for validity
- **/workspace/Mu2eG4/src/Mu2eG4PrimaryGeneratorAction.cc:80** - getHandle/getValidHandle result not checked for validity
- **/workspace/Mu2eG4/src/Mu2eG4PrimaryGeneratorAction.cc:99** - getHandle/getValidHandle result not checked for validity
- **/workspace/Mu2eG4/src/Mu2eG4PrimaryGeneratorAction.cc:117** - getHandle/getValidHandle result not checked for validity
- **/workspace/Mu2eG4/src/Mu2eG4PrimaryGeneratorAction.cc:140** - getHandle/getValidHandle result not checked for validity

#### missing_return (43 occurrences)

- **/workspace/Mu2eG4/src/Mu2eWorld.cc:445** - Function may be missing return statement
- **/workspace/Mu2eG4/src/Mu2eWorld.cc:454** - Function may be missing return statement
- **/workspace/Mu2eG4/src/Mu2eWorld.cc:464** - Function may be missing return statement
- **/workspace/Mu2eG4/src/Mu2eWorld.cc:473** - Function may be missing return statement
- **/workspace/Mu2eG4/src/Mu2eWorld.cc:475** - Function may be missing return statement
- **/workspace/Mu2eG4/src/Mu2eWorld.cc:477** - Function may be missing return statement
- **/workspace/Mu2eG4/src/Mu2eWorld.cc:479** - Function may be missing return statement
- **/workspace/Mu2eG4/src/Mu2eWorld.cc:481** - Function may be missing return statement
- **/workspace/Mu2eG4/src/Mu2eWorld.cc:484** - Function may be missing return statement
- **/workspace/Mu2eG4/src/Mu2eWorld.cc:486** - Function may be missing return statement
- ... and 33 more

#### resource_leak (1 occurrences)

- **/workspace/Mu2eG4/src/scorerFTDTable.cc:28** - File handle opened but may not be closed

#### uninitialized_variable (17 occurrences)

- **/workspace/Mu2eG4/src/customizeChargedPionDecay.cc:79** - Variable ok may be used uninitialized
- **/workspace/Mu2eG4/src/customizeChargedPionDecay.cc:129** - Variable b may be used uninitialized
- **/workspace/Mu2eG4/src/customizeChargedPionDecay.cc:167** - Variable addENu may be used uninitialized
- **/workspace/Mu2eG4/src/Mu2eG4Cuts.cc:64** - Variable overflowWarningPrinted_ may be used uninitialized
- **/workspace/Mu2eG4/src/Mu2eG4Cuts.cc:340** - Variable offset_ may be used uninitialized
- **/workspace/Mu2eG4/src/Mu2eG4Cuts.cc:416** - Variable doNotCut_ may be used uninitialized
- **/workspace/Mu2eG4/src/Mu2eG4Cuts.cc:452** - Variable negate_ may be used uninitialized
- **/workspace/Mu2eG4/src/Mu2eG4Cuts.cc:510** - Variable negate_ may be used uninitialized
- **/workspace/Mu2eG4/src/Mu2eG4Cuts.cc:609** - Variable cut_ may be used uninitialized
- **/workspace/Mu2eG4/src/Mu2eG4Cuts.cc:644** - Variable cut_ may be used uninitialized
- ... and 7 more

#### unused_variable (15 occurrences)

- **/workspace/Mu2eG4/src/constructHaymanRings.cc:53** - Variable psVacuumSensitive declared but possibly unused
- **/workspace/Mu2eG4/src/constructVirtualDetectors.cc:1469** - Variable y_vd_halflength declared but possibly unused
- **/workspace/Mu2eG4/src/constructVirtualDetectors.cc:1798** - Variable i declared but possibly unused
- **/workspace/Mu2eG4/src/constructDS.cc:415** - Variable ds2HalfLength declared but possibly unused
- **/workspace/Mu2eG4/src/constructDS.cc:723** - Variable cableRunSensitive declared but possibly unused
- **/workspace/Mu2eG4/src/constructProtonAbsorber.cc:129** - Variable addSD declared but possibly unused
- **/workspace/Mu2eG4/src/CaloReadoutSD.cc:56** - Variable i declared but possibly unused
- **/workspace/Mu2eG4/src/constructTargetPS.cc:95** - Variable psVacuumSensitive declared but possibly unused
- **/workspace/Mu2eG4/src/constructHall.cc:554** - Variable vertices declared but possibly unused
- **/workspace/Mu2eG4/src/HelicalProtonAbsorber.cc:57** - Variable step_length_z declared but possibly unused
- ... and 5 more

#### use_after_free (11 occurrences)

- **/workspace/Mu2eG4/src/Mu2eWorld.cc:446** - Potential use after free: _rhs deleted but may be used later
- **/workspace/Mu2eG4/src/Mu2eWorld.cc:455** - Potential use after free: _rhs deleted but may be used later
- **/workspace/Mu2eG4/src/Mu2eWorld.cc:465** - Potential use after free: _rhs deleted but may be used later
- **/workspace/Mu2eG4/src/Mu2eWorld.cc:797** - Potential use after free: the deleted but may be used later
- **/workspace/Mu2eG4/src/Mu2eG4WorkerRunManager.cc:205** - Potential use after free: currentRun deleted but may be used later
- **/workspace/Mu2eG4/src/Mu2eG4WorkerRunManager.cc:279** - Potential use after free: anEvent deleted but may be used later
- **/workspace/Mu2eG4/src/Mu2eG4MTRunManager.cc:98** - Potential use after free: currentRun deleted but may be used later
- **/workspace/Mu2eG4/src/HelicalProtonAbsorber.cc:137** - Potential use after free: pabs_phys deleted but may be used later
- **/workspace/Mu2eG4/src/HelicalProtonAbsorber.cc:138** - Potential use after free: pabs_logic deleted but may be used later
- **/workspace/Mu2eG4/src/HelicalProtonAbsorber.cc:139** - Potential use after free: pabs_solid deleted but may be used later
- ... and 1 more


### Mu2eG4Helper

Found 10 potential bugs:

#### array_bounds (1 occurrences)

- **/workspace/Mu2eG4Helper/src/Mu2eG4Helper.cc:47** - Array access _volumeInfoList[info.name] without bounds check

#### assignment_in_condition (1 occurrences)

- **/workspace/Mu2eG4Helper/src/Mu2eG4Helper.cc:41** - Possible assignment (=) instead of comparison (==) in condition

#### division_by_zero (8 occurrences)

- **/workspace/Mu2eG4Helper/src/Mu2eG4Helper.cc:11** - Potential division by zero: Mu2eG4Helper not checked
- **/workspace/Mu2eG4Helper/src/Mu2eG4Helper.cc:12** - Potential division by zero: Framework not checked
- **/workspace/Mu2eG4Helper/src/Mu2eG4Helper_service.cc:5** - Potential division by zero: Framework not checked
- **/workspace/Mu2eG4Helper/src/Mu2eG4Helper_service.cc:6** - Potential division by zero: Mu2eG4Helper not checked
- **/workspace/Mu2eG4Helper/src/VolumeInfo.cc:10** - Potential division by zero: Mu2eG4Helper not checked
- **/workspace/Mu2eG4Helper/src/VolumeInfo.cc:12** - Potential division by zero: GeometryService not checked
- **/workspace/Mu2eG4Helper/src/VolumeInfo.cc:13** - Potential division by zero: GeometryService not checked
- **/workspace/Mu2eG4Helper/src/AntiLeakRegistry.cc:12** - Potential division by zero: Mu2eG4Helper not checked


### Mu2eHallGeom

Found 7 potential bugs:

#### array_bounds (1 occurrences)

- **/workspace/Mu2eHallGeom/src/Mu2eHall.cc:71** - Array access verts[i] without bounds check

#### division_by_zero (6 occurrences)

- **/workspace/Mu2eHallGeom/src/Mu2eHall.cc:7** - Potential division by zero: Mu2eHallGeom not checked
- **/workspace/Mu2eHallGeom/src/Mu2eHall.cc:15** - Potential division by zero: GeomPrimitives not checked
- **/workspace/Mu2eHallGeom/src/Mu2eHall.cc:18** - Potential division by zero: Units not checked
- **/workspace/Mu2eHallGeom/src/Mu2eHall.cc:19** - Potential division by zero: Vector not checked
- **/workspace/Mu2eHallGeom/src/Mu2eHall.cc:20** - Potential division by zero: Vector not checked
- **/workspace/Mu2eHallGeom/src/Mu2eHall.cc:22** - Potential division by zero: exception not checked


### Mu2eKinKal

Found 455 potential bugs:

#### array_bounds (68 occurrences)

- **/workspace/Mu2eKinKal/src/CentralHelixFit_module.cc:209** - Array access seedcov_[ipar] without bounds check
- **/workspace/Mu2eKinKal/src/CentralHelixFit_module.cc:213** - Array access paramconstraints_[ipar] without bounds check
- **/workspace/Mu2eKinKal/src/CentralHelixFit_module.cc:266** - Array access cseedcol[index] without bounds check
- **/workspace/Mu2eKinKal/src/DriftANNSHU.cc:42** - Array access spars[0] without bounds check
- **/workspace/Mu2eKinKal/src/DriftANNSHU.cc:43** - Array access spars[1] without bounds check
- **/workspace/Mu2eKinKal/src/DriftANNSHU.cc:44** - Array access spars[2] without bounds check
- **/workspace/Mu2eKinKal/src/DriftANNSHU.cc:45** - Array access spars[3] without bounds check
- **/workspace/Mu2eKinKal/src/DriftANNSHU.cc:49** - Array access spars[4] without bounds check
- **/workspace/Mu2eKinKal/src/DriftANNSHU.cc:51** - Array access cpars[0] without bounds check
- **/workspace/Mu2eKinKal/src/DriftANNSHU.cc:52** - Array access cpars[1] without bounds check
- ... and 58 more

#### assignment_in_condition (7 occurrences)

- **/workspace/Mu2eKinKal/src/CentralHelixFit_module.cc:314** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Mu2eKinKal/src/Chi2SHU.cc:71** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Mu2eKinKal/src/KinematicLineFit_module.cc:294** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Mu2eKinKal/src/RegrowKinematicLine_module.cc:254** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Mu2eKinKal/src/LoopHelixFit_module.cc:285** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Mu2eKinKal/src/LoopHelixFit_module.cc:341** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Mu2eKinKal/src/RegrowLoopHelix_module.cc:264** - Possible assignment (=) instead of comparison (==) in condition

#### division_by_zero (337 occurrences)

- **/workspace/Mu2eKinKal/src/KKFitSettings.cc:1** - Potential division by zero: Mu2eKinKal not checked
- **/workspace/Mu2eKinKal/src/KKFitSettings.cc:2** - Potential division by zero: Mu2eKinKal not checked
- **/workspace/Mu2eKinKal/src/KKFitSettings.cc:3** - Potential division by zero: Mu2eKinKal not checked
- **/workspace/Mu2eKinKal/src/KKFitSettings.cc:4** - Potential division by zero: GeneralUtilities not checked
- **/workspace/Mu2eKinKal/src/CentralHelixFit_module.cc:4** - Potential division by zero: 18 not checked
- **/workspace/Mu2eKinKal/src/CentralHelixFit_module.cc:7** - Potential division by zero: types not checked
- **/workspace/Mu2eKinKal/src/CentralHelixFit_module.cc:8** - Potential division by zero: types not checked
- **/workspace/Mu2eKinKal/src/CentralHelixFit_module.cc:9** - Potential division by zero: types not checked
- **/workspace/Mu2eKinKal/src/CentralHelixFit_module.cc:10** - Potential division by zero: types not checked
- **/workspace/Mu2eKinKal/src/CentralHelixFit_module.cc:11** - Potential division by zero: types not checked
- ... and 327 more

#### memory_leak (14 occurrences)

- **/workspace/Mu2eKinKal/src/CentralHelixFit_module.cc:256** - Potential memory leak: new KKTRKCOL without corresponding delete
- **/workspace/Mu2eKinKal/src/CentralHelixFit_module.cc:257** - Potential memory leak: new KalSeedCollection without corresponding delete
- **/workspace/Mu2eKinKal/src/KinematicLineFit_module.cc:270** - Potential memory leak: new KKTRKCOL without corresponding delete
- **/workspace/Mu2eKinKal/src/KinematicLineFit_module.cc:271** - Potential memory leak: new KalSeedCollection without corresponding delete
- **/workspace/Mu2eKinKal/src/KinematicLineFit_module.cc:272** - Potential memory leak: new KalLineAssns without corresponding delete
- **/workspace/Mu2eKinKal/src/RegrowKinematicLine_module.cc:199** - Potential memory leak: new KKTRKCOL without corresponding delete
- **/workspace/Mu2eKinKal/src/RegrowKinematicLine_module.cc:200** - Potential memory leak: new KalSeedCollection without corresponding delete
- **/workspace/Mu2eKinKal/src/RegrowKinematicLine_module.cc:206** - Potential memory leak: new KalSeedMCAssns without corresponding delete
- **/workspace/Mu2eKinKal/src/LoopHelixFit_module.cc:389** - Potential memory leak: new KKTRKCOL without corresponding delete
- **/workspace/Mu2eKinKal/src/LoopHelixFit_module.cc:390** - Potential memory leak: new KalSeedCollection without corresponding delete
- ... and 4 more

#### missing_error_handling (16 occurrences)

- **/workspace/Mu2eKinKal/src/CentralHelixFit_module.cc:252** - getHandle/getValidHandle result not checked for validity
- **/workspace/Mu2eKinKal/src/CentralHelixFit_module.cc:253** - getHandle/getValidHandle result not checked for validity
- **/workspace/Mu2eKinKal/src/CentralHelixFit_module.cc:261** - getHandle/getValidHandle result not checked for validity
- **/workspace/Mu2eKinKal/src/KinematicLineFit_module.cc:266** - getHandle/getValidHandle result not checked for validity
- **/workspace/Mu2eKinKal/src/KinematicLineFit_module.cc:267** - getHandle/getValidHandle result not checked for validity
- **/workspace/Mu2eKinKal/src/KinematicLineFit_module.cc:278** - getHandle/getValidHandle result not checked for validity
- **/workspace/Mu2eKinKal/src/RegrowKinematicLine_module.cc:189** - getHandle/getValidHandle result not checked for validity
- **/workspace/Mu2eKinKal/src/RegrowKinematicLine_module.cc:191** - getHandle/getValidHandle result not checked for validity
- **/workspace/Mu2eKinKal/src/RegrowKinematicLine_module.cc:193** - getHandle/getValidHandle result not checked for validity
- **/workspace/Mu2eKinKal/src/LoopHelixFit_module.cc:308** - getHandle/getValidHandle result not checked for validity
- ... and 6 more

#### missing_return (8 occurrences)

- **/workspace/Mu2eKinKal/src/KKFitSettings.cc:48** - Function may be missing return statement
- **/workspace/Mu2eKinKal/src/KKFitSettings.cc:50** - Function may be missing return statement
- **/workspace/Mu2eKinKal/src/KKFitSettings.cc:52** - Function may be missing return statement
- **/workspace/Mu2eKinKal/src/KKFitSettings.cc:54** - Function may be missing return statement
- **/workspace/Mu2eKinKal/src/DriftANNSHU.cc:104** - Function may be missing return statement
- **/workspace/Mu2eKinKal/src/BkgANNSHU.cc:49** - Function may be missing return statement
- **/workspace/Mu2eKinKal/src/CADSHU.cc:52** - Function may be missing return statement
- **/workspace/Mu2eKinKal/src/RegrowLoopHelix_module.cc:274** - Function may be missing return statement

#### uninitialized_variable (5 occurrences)

- **/workspace/Mu2eKinKal/src/RegrowKinematicLine_module.cc:140** - Variable debug_ may be used uninitialized
- **/workspace/Mu2eKinKal/src/RegrowKinematicLine_module.cc:151** - Variable fillMCAssns_ may be used uninitialized
- **/workspace/Mu2eKinKal/src/RegrowLoopHelix_module.cc:143** - Variable debug_ may be used uninitialized
- **/workspace/Mu2eKinKal/src/RegrowLoopHelix_module.cc:155** - Variable fillMCAssns_ may be used uninitialized
- **/workspace/Mu2eKinKal/src/RegrowLoopHelix_module.cc:156** - Variable extend_ may be used uninitialized


### Mu2eUtilities

Found 555 potential bugs:

#### array_bounds (79 occurrences)

- **/workspace/Mu2eUtilities/src/MVATools.cc:371** - Array access synapsessPerLayer[iLayer-1] without bounds check
- **/workspace/Mu2eUtilities/src/MVATools.cc:374** - Array access layerToNeurons[iLayer-1] without bounds check
- **/workspace/Mu2eUtilities/src/MVATools.cc:435** - Array access fv_[i] without bounds check
- **/workspace/Mu2eUtilities/src/MVATools.cc:448** - Array access x_[ival] without bounds check
- **/workspace/Mu2eUtilities/src/MVATools.cc:452** - Array access x_[ival] without bounds check
- **/workspace/Mu2eUtilities/src/MVATools.cc:454** - Array access links_[0] without bounds check
- **/workspace/Mu2eUtilities/src/MVATools.cc:455** - Array access links_[0] without bounds check
- **/workspace/Mu2eUtilities/src/MVATools.cc:463** - Array access links_[k+1] without bounds check
- **/workspace/Mu2eUtilities/src/MVATools.cc:465** - Array access y_[j] without bounds check
- **/workspace/Mu2eUtilities/src/MVATools.cc:466** - Array access links_[k] without bounds check
- ... and 69 more

#### assignment_in_condition (16 occurrences)

- **/workspace/Mu2eUtilities/src/MVATools.cc:339** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Mu2eUtilities/src/MVATools.cc:454** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Mu2eUtilities/src/GammaPairConversionSpectrum.cc:75** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Mu2eUtilities/src/CaloPulseShape.cc:72** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Mu2eUtilities/src/EjectedProtonSpectrum.cc:32** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Mu2eUtilities/src/EjectedProtonSpectrum.cc:37** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Mu2eUtilities/src/VectorVolume.cc:45** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Mu2eUtilities/src/ReSeedByEventID.cc:42** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Mu2eUtilities/src/PoissonHistogramBinning.cc:45** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Mu2eUtilities/src/TrackCuts.cc:104** - Possible assignment (=) instead of comparison (==) in condition
- ... and 6 more

#### division_by_zero (410 occurrences)

- **/workspace/Mu2eUtilities/src/Table.cc:12** - Potential division by zero: Mu2eUtilities not checked
- **/workspace/Mu2eUtilities/src/Table.cc:78** - Potential division by zero: integral not checked
- **/workspace/Mu2eUtilities/src/PointLinePCA_XYZ.cc:3** - Potential division by zero: GenVector not checked
- **/workspace/Mu2eUtilities/src/PointLinePCA_XYZ.cc:4** - Potential division by zero: GenVector not checked
- **/workspace/Mu2eUtilities/src/PointLinePCA_XYZ.cc:6** - Potential division by zero: Mu2eUtilities not checked
- **/workspace/Mu2eUtilities/src/MVATools.cc:5** - Potential division by zero: parsers not checked
- **/workspace/Mu2eUtilities/src/MVATools.cc:6** - Potential division by zero: util not checked
- **/workspace/Mu2eUtilities/src/MVATools.cc:14** - Potential division by zero: ConfigTools not checked
- **/workspace/Mu2eUtilities/src/MVATools.cc:15** - Potential division by zero: DataProducts not checked
- **/workspace/Mu2eUtilities/src/MVATools.cc:16** - Potential division by zero: exception not checked
- ... and 400 more

#### memory_leak (3 occurrences)

- **/workspace/Mu2eUtilities/src/MVATools.cc:281** - Potential memory leak: new XercesDOMParser without corresponding delete
- **/workspace/Mu2eUtilities/src/ProtonPulseRandPDF.cc:136** - Potential memory leak: new vector without corresponding delete
- **/workspace/Mu2eUtilities/src/PionCaptureSpectrum.cc:103** - Potential memory leak: new fit without corresponding delete

#### missing_return (34 occurrences)

- **/workspace/Mu2eUtilities/src/PoissonHistogramBinning.cc:51** - Function may be missing return statement
- **/workspace/Mu2eUtilities/src/PoissonHistogramBinning.cc:56** - Function may be missing return statement
- **/workspace/Mu2eUtilities/src/PoissonHistogramBinning.cc:61** - Function may be missing return statement
- **/workspace/Mu2eUtilities/src/BinnedSpectrum.cc:37** - Function may be missing return statement
- **/workspace/Mu2eUtilities/src/BinnedSpectrum.cc:42** - Function may be missing return statement
- **/workspace/Mu2eUtilities/src/BinnedSpectrum.cc:45** - Function may be missing return statement
- **/workspace/Mu2eUtilities/src/BinnedSpectrum.cc:50** - Function may be missing return statement
- **/workspace/Mu2eUtilities/src/BinnedSpectrum.cc:63** - Function may be missing return statement
- **/workspace/Mu2eUtilities/src/BinnedSpectrum.cc:70** - Function may be missing return statement
- **/workspace/Mu2eUtilities/src/BinnedSpectrum.cc:82** - Function may be missing return statement
- ... and 24 more

#### uninitialized_variable (6 occurrences)

- **/workspace/Mu2eUtilities/src/EjectedProtonSpectrum.cc:30** - Variable spectrumWeight may be used uninitialized
- **/workspace/Mu2eUtilities/src/LsqSums4.cc:120** - Variable x may be used uninitialized
- **/workspace/Mu2eUtilities/src/LsqSums4.cc:126** - Variable y may be used uninitialized
- **/workspace/Mu2eUtilities/src/LsqSums4.cc:190** - Variable chi2 may be used uninitialized
- **/workspace/Mu2eUtilities/src/MuonCaptureSpectrum.cc:112** - Variable kMax may be used uninitialized
- **/workspace/Mu2eUtilities/src/compressPdgId.cc:100** - Variable ind may be used uninitialized

#### unused_variable (7 occurrences)

- **/workspace/Mu2eUtilities/src/MVATools.cc:374** - Variable iIn declared but possibly unused
- **/workspace/Mu2eUtilities/src/MVATools.cc:543** - Variable i declared but possibly unused
- **/workspace/Mu2eUtilities/src/GammaPairConversionSpectrum.cc:217** - Variable uMax declared but possibly unused
- **/workspace/Mu2eUtilities/src/CaloPulseShape.cc:47** - Variable j declared but possibly unused
- **/workspace/Mu2eUtilities/src/CaloPulseShape.cc:62** - Variable i declared but possibly unused
- **/workspace/Mu2eUtilities/src/rm48.cc:31** - Variable i declared but possibly unused
- **/workspace/Mu2eUtilities/src/TwoLinePCA_XYZ.cc:73** - Variable ambig_sign declared but possibly unused


### PTMGeom

Found 12 potential bugs:

#### division_by_zero (7 occurrences)

- **/workspace/PTMGeom/src/PTMStand.cc:1** - Potential division by zero: PTMGeom not checked
- **/workspace/PTMGeom/src/PTMPWC.cc:1** - Potential division by zero: PTMGeom not checked
- **/workspace/PTMGeom/src/PTMPWC.cc:2** - Potential division by zero: GeomPrimitives not checked
- **/workspace/PTMGeom/src/PTMPWC.cc:61** - Potential division by zero: numVertWires not checked
- **/workspace/PTMGeom/src/PTMPWC.cc:64** - Potential division by zero: numHorizWires not checked
- **/workspace/PTMGeom/src/PTM.cc:1** - Potential division by zero: PTMGeom not checked
- **/workspace/PTMGeom/src/PTMHead.cc:1** - Potential division by zero: PTMGeom not checked

#### memory_leak (5 occurrences)

- **/workspace/PTMGeom/src/PTMPWC.cc:60** - Potential memory leak: new Box without corresponding delete
- **/workspace/PTMGeom/src/PTMPWC.cc:63** - Potential memory leak: new Box without corresponding delete
- **/workspace/PTMGeom/src/PTMPWC.cc:66** - Potential memory leak: new Box without corresponding delete
- **/workspace/PTMGeom/src/PTMPWC.cc:68** - Potential memory leak: new Box without corresponding delete
- **/workspace/PTMGeom/src/PTMPWC.cc:70** - Potential memory leak: new Box without corresponding delete


### ParticleID

Found 258 potential bugs:

#### array_bounds (116 occurrences)

- **/workspace/ParticleID/src/ParticleID_module.cc:74** - Array access y[i] without bounds check
- **/workspace/ParticleID/src/ParticleID_module.cc:75** - Array access ey[i] without bounds check
- **/workspace/ParticleID/src/ParticleID_module.cc:80** - Array access pathbounds[nbounds] without bounds check
- **/workspace/ParticleID/src/ParticleID_module.cc:84** - Array access pathbounds[0] without bounds check
- **/workspace/ParticleID/src/ParticleID_module.cc:86** - Array access pathbounds[0] without bounds check
- **/workspace/ParticleID/src/ParticleID_module.cc:87** - Array access pathbounds[1] without bounds check
- **/workspace/ParticleID/src/ParticleID_module.cc:88** - Array access pathbounds[2] without bounds check
- **/workspace/ParticleID/src/ParticleID_module.cc:89** - Array access pathbounds[3] without bounds check
- **/workspace/ParticleID/src/ParticleID_module.cc:90** - Array access pathbounds[4] without bounds check
- **/workspace/ParticleID/src/ParticleID_module.cc:91** - Array access pathbounds[5] without bounds check
- ... and 106 more

#### assignment_in_condition (52 occurrences)

- **/workspace/ParticleID/src/ParticleID_module.cc:84** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/ParticleID/src/ParticleID_module.cc:86** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/ParticleID/src/ParticleID_module.cc:87** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/ParticleID/src/ParticleID_module.cc:88** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/ParticleID/src/ParticleID_module.cc:89** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/ParticleID/src/ParticleID_module.cc:90** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/ParticleID/src/ParticleID_module.cc:91** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/ParticleID/src/ParticleID_module.cc:92** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/ParticleID/src/ParticleID_module.cc:93** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/ParticleID/src/ParticleID_module.cc:94** - Possible assignment (=) instead of comparison (==) in condition
- ... and 42 more

#### division_by_zero (59 occurrences)

- **/workspace/ParticleID/src/ParticleID_module.cc:8** - Potential division by zero: fcl not checked
- **/workspace/ParticleID/src/ParticleID_module.cc:16** - Potential division by zero: Framework not checked
- **/workspace/ParticleID/src/ParticleID_module.cc:17** - Potential division by zero: Framework not checked
- **/workspace/ParticleID/src/ParticleID_module.cc:18** - Potential division by zero: Framework not checked
- **/workspace/ParticleID/src/ParticleID_module.cc:19** - Potential division by zero: Framework not checked
- **/workspace/ParticleID/src/ParticleID_module.cc:20** - Potential division by zero: TFileService not checked
- **/workspace/ParticleID/src/ParticleID_module.cc:21** - Potential division by zero: ParameterSet not checked
- **/workspace/ParticleID/src/ParticleID_module.cc:37** - Potential division by zero: RecoDataProducts not checked
- **/workspace/ParticleID/src/ParticleID_module.cc:38** - Potential division by zero: TrkBase not checked
- **/workspace/ParticleID/src/ParticleID_module.cc:39** - Potential division by zero: TrkBase not checked
- ... and 49 more

#### memory_leak (13 occurrences)

- **/workspace/ParticleID/src/ParticleID_module.cc:232** - Potential memory leak: new TApplication without corresponding delete
- **/workspace/ParticleID/src/ParticleID_module.cc:240** - Potential memory leak: new TCanvas without corresponding delete
- **/workspace/ParticleID/src/ParticleID_module.cc:272** - Potential memory leak: new PIDProductCollection without corresponding delete
- **/workspace/ParticleID/src/ParticleID_module.cc:406** - Potential memory leak: new TGraphErrors without corresponding delete
- **/workspace/ParticleID/src/ParticleID_module.cc:408** - Potential memory leak: new TMinuit without corresponding delete
- **/workspace/ParticleID/src/PIDUtilities.cc:137** - Potential memory leak: new TH1D without corresponding delete
- **/workspace/ParticleID/src/PIDUtilities.cc:156** - Potential memory leak: new double[1+nb1] without corresponding delete
- **/workspace/ParticleID/src/PIDUtilities.cc:157** - Potential memory leak: new double[1+nb2] without corresponding delete
- **/workspace/ParticleID/src/PIDUtilities.cc:158** - Potential memory leak: new double[2+nb1+nb2] without corresponding delete
- **/workspace/ParticleID/src/PIDUtilities.cc:159** - Potential memory leak: new double[2+nb1+nb2] without corresponding delete
- ... and 3 more

#### missing_return (7 occurrences)

- **/workspace/ParticleID/src/PIDLogLEp.cc:72** - Function may be missing return statement
- **/workspace/ParticleID/src/PIDLogL1D.cc:63** - Function may be missing return statement
- **/workspace/ParticleID/src/PIDUtilities.cc:79** - Function may be missing return statement
- **/workspace/ParticleID/src/PIDUtilities.cc:122** - Function may be missing return statement
- **/workspace/ParticleID/src/PIDUtilities.cc:303** - Function may be missing return statement
- **/workspace/ParticleID/src/PIDUtilities.cc:440** - Function may be missing return statement
- **/workspace/ParticleID/src/PIDUtilities.cc:450** - Function may be missing return statement

#### resource_leak (2 occurrences)

- **/workspace/ParticleID/src/PIDLogLEp.cc:47** - File handle opened but may not be closed
- **/workspace/ParticleID/src/PIDLogL1D.cc:40** - File handle opened but may not be closed

#### uninitialized_variable (7 occurrences)

- **/workspace/ParticleID/src/PIDLogLEp.cc:91** - Variable val may be used uninitialized
- **/workspace/ParticleID/src/ParticleIDRead_module.cc:52** - Variable _verbosity may be used uninitialized
- **/workspace/ParticleID/src/ParticleIDRead_module.cc:53** - Variable _maxPrint may be used uninitialized
- **/workspace/ParticleID/src/ParticleIDRead_module.cc:55** - Variable _processEmpty may be used uninitialized
- **/workspace/ParticleID/src/PIDLogL1D.cc:67** - Variable nbins may be used uninitialized
- **/workspace/ParticleID/src/PIDLogL1D.cc:80** - Variable val may be used uninitialized
- **/workspace/ParticleID/src/PIDUtilities.cc:95** - Variable wtmin may be used uninitialized

#### use_after_free (2 occurrences)

- **/workspace/ParticleID/src/PIDUtilities.cc:136** - Potential use after free: morphedhist deleted but may be used later
- **/workspace/ParticleID/src/PIDUtilities.cc:473** - Potential use after free: morphedhist deleted but may be used later


### Print

Found 283 potential bugs:

#### array_bounds (2 occurrences)

- **/workspace/Print/src/STMWaveformDigiPrinter.cc:74** - Array access adcs[i] without bounds check
- **/workspace/Print/src/BkgQualPrinter.cc:48** - Array access coll[0] without bounds check

#### assignment_in_condition (37 occurrences)

- **/workspace/Print/src/StepPointMCPrinter.cc:69** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Print/src/STMWaveformDigiPrinter.cc:64** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Print/src/BkgClusterPrinter.cc:63** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Print/src/StrawHitPrinter.cc:65** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Print/src/CaloRecoDigiPrinter.cc:64** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Print/src/CrvDigiMCPrinter.cc:63** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Print/src/MCTrajectoryPrinter.cc:67** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Print/src/CaloHitMCPrinter.cc:65** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Print/src/ComboHitPrinter.cc:63** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Print/src/TimeClusterPrinter.cc:64** - Possible assignment (=) instead of comparison (==) in condition
- ... and 27 more

#### division_by_zero (192 occurrences)

- **/workspace/Print/src/StepPointMCPrinter.cc:2** - Potential division by zero: Print not checked
- **/workspace/Print/src/StepPointMCPrinter.cc:3** - Potential division by zero: Framework not checked
- **/workspace/Print/src/STMWaveformDigiPrinter.cc:1** - Potential division by zero: Print not checked
- **/workspace/Print/src/STMWaveformDigiPrinter.cc:2** - Potential division by zero: Framework not checked
- **/workspace/Print/src/BkgClusterPrinter.cc:2** - Potential division by zero: Print not checked
- **/workspace/Print/src/BkgClusterPrinter.cc:3** - Potential division by zero: Framework not checked
- **/workspace/Print/src/TriggerResultsPrinter.cc:2** - Potential division by zero: Print not checked
- **/workspace/Print/src/TriggerResultsPrinter.cc:3** - Potential division by zero: Mu2eUtilities not checked
- **/workspace/Print/src/TriggerResultsPrinter.cc:4** - Potential division by zero: Framework not checked
- **/workspace/Print/src/StrawHitPrinter.cc:2** - Potential division by zero: Print not checked
- ... and 182 more

#### missing_error_handling (46 occurrences)

- **/workspace/Print/src/StepPointMCPrinter.cc:18** - getHandle/getValidHandle result not checked for validity
- **/workspace/Print/src/STMWaveformDigiPrinter.cc:17** - getHandle/getValidHandle result not checked for validity
- **/workspace/Print/src/BkgClusterPrinter.cc:17** - getHandle/getValidHandle result not checked for validity
- **/workspace/Print/src/TriggerResultsPrinter.cc:20** - getHandle/getValidHandle result not checked for validity
- **/workspace/Print/src/StrawHitPrinter.cc:17** - getHandle/getValidHandle result not checked for validity
- **/workspace/Print/src/CaloRecoDigiPrinter.cc:18** - getHandle/getValidHandle result not checked for validity
- **/workspace/Print/src/CrvDigiMCPrinter.cc:17** - getHandle/getValidHandle result not checked for validity
- **/workspace/Print/src/MCTrajectoryPrinter.cc:18** - getHandle/getValidHandle result not checked for validity
- **/workspace/Print/src/CaloHitMCPrinter.cc:17** - getHandle/getValidHandle result not checked for validity
- **/workspace/Print/src/ComboHitPrinter.cc:17** - getHandle/getValidHandle result not checked for validity
- ... and 36 more

#### uninitialized_variable (5 occurrences)

- **/workspace/Print/src/PrintModule_module.cc:174** - Variable _verbose may be used uninitialized
- **/workspace/Print/src/KalSeedPrinter.cc:65** - Variable t0 may be used uninitialized
- **/workspace/Print/src/RunSubrunEvent_module.cc:70** - Variable _runCount may be used uninitialized
- **/workspace/Print/src/RunSubrunEvent_module.cc:71** - Variable _subrunCount may be used uninitialized
- **/workspace/Print/src/RunSubrunEvent_module.cc:72** - Variable _eventCount may be used uninitialized

#### unused_variable (1 occurrences)

- **/workspace/Print/src/TrackSummaryPrinter.cc:167** - Variable maxd declared but possibly unused


### ProditionsService

Found 61 potential bugs:

#### array_bounds (21 occurrences)

- **/workspace/ProditionsService/src/ProditionsService.cc:54** - Array access _caches[cor->name()] without bounds check
- **/workspace/ProditionsService/src/ProditionsService.cc:56** - Array access _caches[csy->name()] without bounds check
- **/workspace/ProditionsService/src/ProditionsService.cc:58** - Array access _caches[cst->name()] without bounds check
- **/workspace/ProditionsService/src/ProditionsService.cc:60** - Array access _caches[cca->name()] without bounds check
- **/workspace/ProditionsService/src/ProditionsService.cc:62** - Array access _caches[etc->name()] without bounds check
- **/workspace/ProditionsService/src/ProditionsService.cc:65** - Array access _caches[sep->name()] without bounds check
- **/workspace/ProditionsService/src/ProditionsService.cc:68** - Array access _caches[frc->name()] without bounds check
- **/workspace/ProditionsService/src/ProditionsService.cc:70** - Array access _caches[tsc->name()] without bounds check
- **/workspace/ProditionsService/src/ProditionsService.cc:72** - Array access _caches[tpm->name()] without bounds check
- **/workspace/ProditionsService/src/ProditionsService.cc:74** - Array access _caches[sdc->name()] without bounds check
- ... and 11 more

#### division_by_zero (40 occurrences)

- **/workspace/ProditionsService/src/ProditionsTest_module.cc:11** - Potential division by zero: Framework not checked
- **/workspace/ProditionsService/src/ProditionsTest_module.cc:12** - Potential division by zero: Framework not checked
- **/workspace/ProditionsService/src/ProditionsTest_module.cc:13** - Potential division by zero: ParameterSet not checked
- **/workspace/ProditionsService/src/ProditionsTest_module.cc:14** - Potential division by zero: types not checked
- **/workspace/ProditionsService/src/ProditionsTest_module.cc:15** - Potential division by zero: types not checked
- **/workspace/ProditionsService/src/ProditionsTest_module.cc:17** - Potential division by zero: CRVConditions not checked
- **/workspace/ProditionsService/src/ProditionsTest_module.cc:18** - Potential division by zero: CRVConditions not checked
- **/workspace/ProditionsService/src/ProditionsTest_module.cc:19** - Potential division by zero: CRVConditions not checked
- **/workspace/ProditionsService/src/ProditionsTest_module.cc:20** - Potential division by zero: ProditionsService not checked
- **/workspace/ProditionsService/src/ProditionsService.cc:4** - Potential division by zero: AnalysisConditions not checked
- ... and 30 more


### ProductionSolenoidGeom

Found 3 potential bugs:

#### division_by_zero (3 occurrences)

- **/workspace/ProductionSolenoidGeom/src/PSExternalShielding.cc:1** - Potential division by zero: ProductionSolenoidGeom not checked
- **/workspace/ProductionSolenoidGeom/src/PSEnclosure.cc:1** - Potential division by zero: ProductionSolenoidGeom not checked
- **/workspace/ProductionSolenoidGeom/src/PSShield.cc:3** - Potential division by zero: ProductionSolenoidGeom not checked


### ProductionTargetGeom

Found 2 potential bugs:

#### division_by_zero (1 occurrences)

- **/workspace/ProductionTargetGeom/src/ProductionTarget.cc:1** - Potential division by zero: ProductionTargetGeom not checked

#### unused_variable (1 occurrences)

- **/workspace/ProductionTargetGeom/src/ProductionTarget.cc:7** - Variable nFins declared but possibly unused


### ProtonBeamDumpGeom

Found 1 potential bugs:

#### division_by_zero (1 occurrences)

- **/workspace/ProtonBeamDumpGeom/src/ProtonBeamDump.cc:1** - Potential division by zero: ProtonBeamDumpGeom not checked


### RecoDataProducts

Found 282 potential bugs:

#### array_bounds (193 occurrences)

- **/workspace/RecoDataProducts/src/StrawHitFlag.cc:24** - Array access bitnames[std::string("Stereo")] without bounds check
- **/workspace/RecoDataProducts/src/StrawHitFlag.cc:25** - Array access bitnames[std::string("PanelCombo")] without bounds check
- **/workspace/RecoDataProducts/src/StrawHitFlag.cc:26** - Array access bitnames[std::string("ResolvedPhi")] without bounds check
- **/workspace/RecoDataProducts/src/StrawHitFlag.cc:27** - Array access bitnames[std::string("TimeDivision")] without bounds check
- **/workspace/RecoDataProducts/src/StrawHitFlag.cc:28** - Array access bitnames[std::string("EnergySelection")] without bounds check
- **/workspace/RecoDataProducts/src/StrawHitFlag.cc:29** - Array access bitnames[std::string("RadiusSelection")] without bounds check
- **/workspace/RecoDataProducts/src/StrawHitFlag.cc:30** - Array access bitnames[std::string("TimeSelection")] without bounds check
- **/workspace/RecoDataProducts/src/StrawHitFlag.cc:31** - Array access bitnames[std::string("BackgroundCluster")] without bounds check
- **/workspace/RecoDataProducts/src/StrawHitFlag.cc:32** - Array access bitnames[std::string("Background")] without bounds check
- **/workspace/RecoDataProducts/src/StrawHitFlag.cc:33** - Array access bitnames[std::string("Isolated")] without bounds check
- ... and 183 more

#### assignment_in_condition (9 occurrences)

- **/workspace/RecoDataProducts/src/KalSegment.cc:8** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/RecoDataProducts/src/IntensityInfoCalo.cc:29** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/RecoDataProducts/src/IntensityInfoCalo.cc:35** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/RecoDataProducts/src/TrkExtTraj.cc:72** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/RecoDataProducts/src/TrkExtTraj.cc:77** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/RecoDataProducts/src/TrkExtTraj.cc:184** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/RecoDataProducts/src/TrkExtTraj.cc:201** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/RecoDataProducts/src/TrkExtTraj.cc:252** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/RecoDataProducts/src/TrkExtTraj.cc:264** - Possible assignment (=) instead of comparison (==) in condition

#### division_by_zero (69 occurrences)

- **/workspace/RecoDataProducts/src/StrawHitFlag.cc:8** - Potential division by zero: RecoDataProducts not checked
- **/workspace/RecoDataProducts/src/ExtMonFNALTrkFitQuality.cc:1** - Potential division by zero: RecoDataProducts not checked
- **/workspace/RecoDataProducts/src/ExtMonUCITofHit.cc:7** - Potential division by zero: RecoDataProducts not checked
- **/workspace/RecoDataProducts/src/ExtMonFNALRawHit.cc:1** - Potential division by zero: RecoDataProducts not checked
- **/workspace/RecoDataProducts/src/ExtMonFNALRecoClusterCollection.cc:1** - Potential division by zero: RecoDataProducts not checked
- **/workspace/RecoDataProducts/src/CosmicTrack.cc:2** - Potential division by zero: RecoDataProducts not checked
- **/workspace/RecoDataProducts/src/TrkExtTrajPoint.cc:14** - Potential division by zero: exception not checked
- **/workspace/RecoDataProducts/src/TrkExtTrajPoint.cc:15** - Potential division by zero: Vector not checked
- **/workspace/RecoDataProducts/src/TrkExtTrajPoint.cc:16** - Potential division by zero: Matrix not checked
- **/workspace/RecoDataProducts/src/TrkExtTrajPoint.cc:17** - Potential division by zero: RecoDataProducts not checked
- ... and 59 more

#### memory_leak (3 occurrences)

- **/workspace/RecoDataProducts/src/KalSeed.cc:10** - Potential memory leak: new KalSeed without corresponding delete
- **/workspace/RecoDataProducts/src/KalSeed.cc:27** - Potential memory leak: new KalSeed without corresponding delete
- **/workspace/RecoDataProducts/src/KalSeed.cc:44** - Potential memory leak: new KalSeed without corresponding delete

#### missing_return (2 occurrences)

- **/workspace/RecoDataProducts/src/TrkExtTraj.cc:173** - Function may be missing return statement
- **/workspace/RecoDataProducts/src/TrkExtTraj.cc:203** - Function may be missing return statement

#### uninitialized_variable (5 occurrences)

- **/workspace/RecoDataProducts/src/KalSeed.cc:141** - Variable t0 may be used uninitialized
- **/workspace/RecoDataProducts/src/KalSeed.cc:147** - Variable t0 may be used uninitialized
- **/workspace/RecoDataProducts/src/KalSeed.cc:155** - Variable t0 may be used uninitialized
- **/workspace/RecoDataProducts/src/TrkExtTraj.cc:167** - Variable p may be used uninitialized
- **/workspace/RecoDataProducts/src/TrkExtTraj.cc:212** - Variable volid may be used uninitialized

#### unused_variable (1 occurrences)

- **/workspace/RecoDataProducts/src/TrkToCaloExtrapol.cc:136** - Variable fltlen declared but possibly unused


### STMConditions

Found 8 potential bugs:

#### array_bounds (6 occurrences)

- **/workspace/STMConditions/src/STMEnergyCalibMaker.cc:17** - Array access cmap[STMChannel(STMChannel::enum_type::HPGe)] without bounds check
- **/workspace/STMConditions/src/STMEnergyCalibMaker.cc:18** - Array access cmap[STMChannel(STMChannel::enum_type::LaBr)] without bounds check
- **/workspace/STMConditions/src/STMEnergyCalibMaker.cc:29** - Array access pmap[channel] without bounds check
- **/workspace/STMConditions/src/STMEnergyCalibMaker.cc:41** - Array access sfmap[channel] without bounds check
- **/workspace/STMConditions/src/STMEnergyCalibMaker.cc:65** - Array access cmap[row.channel()] without bounds check
- **/workspace/STMConditions/src/STMEnergyCalibMaker.cc:76** - Array access pmap[row.channel()] without bounds check

#### division_by_zero (2 occurrences)

- **/workspace/STMConditions/src/STMEnergyCalibMaker.cc:1** - Potential division by zero: STMConditions not checked
- **/workspace/STMConditions/src/STMEnergyCalibMaker.cc:2** - Potential division by zero: exception not checked


### STMMC

Found 220 potential bugs:

#### array_bounds (23 occurrences)

- **/workspace/STMMC/src/VirtualDetectorTree_module.cc:108** - Array access pdgIds[pdgId] without bounds check
- **/workspace/STMMC/src/HPGeTree_module.cc:184** - Array access EDeps[topParentId] without bounds check
- **/workspace/STMMC/src/HPGeTree_module.cc:198** - Array access pdgIds[pdgId] without bounds check
- **/workspace/STMMC/src/HPGeTree_module.cc:205** - Array access topParentIds[i] without bounds check
- **/workspace/STMMC/src/HPGeTree_module.cc:206** - Array access EDeps[topParentId] without bounds check
- **/workspace/STMMC/src/HPGeTree_module.cc:207** - Array access times[topParentId] without bounds check
- **/workspace/STMMC/src/ConcatenateDigitizedWaveforms_module.cc:93** - Array access waveforms[0] without bounds check
- **/workspace/STMMC/src/ConcatenateDigitizedWaveforms_module.cc:94** - Array access waveforms[0] without bounds check
- **/workspace/STMMC/src/ConcatenateDigitizedWaveforms_module.cc:103** - Array access outputADCs[i] without bounds check
- **/workspace/STMMC/src/HPGeWaveformsFromStepPointMCs_module.cc:310** - Array access _chargeCollected[i] without bounds check
- ... and 13 more

#### assignment_in_condition (4 occurrences)

- **/workspace/STMMC/src/HPGeTree_module.cc:182** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/STMMC/src/HPGeTree_module.cc:197** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/STMMC/src/HPGeWaveformsFromStepPointMCs_module.cc:424** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/STMMC/src/HPGeWaveformsFromStepPointMCs_module.cc:431** - Possible assignment (=) instead of comparison (==) in condition

#### division_by_zero (176 occurrences)

- **/workspace/STMMC/src/VirtualDetectorTree_module.cc:11** - Potential division by zero: Framework not checked
- **/workspace/STMMC/src/VirtualDetectorTree_module.cc:12** - Potential division by zero: Framework not checked
- **/workspace/STMMC/src/VirtualDetectorTree_module.cc:13** - Potential division by zero: Framework not checked
- **/workspace/STMMC/src/VirtualDetectorTree_module.cc:14** - Potential division by zero: Framework not checked
- **/workspace/STMMC/src/VirtualDetectorTree_module.cc:17** - Potential division by zero: exception not checked
- **/workspace/STMMC/src/VirtualDetectorTree_module.cc:20** - Potential division by zero: Utilities not checked
- **/workspace/STMMC/src/VirtualDetectorTree_module.cc:21** - Potential division by zero: types not checked
- **/workspace/STMMC/src/VirtualDetectorTree_module.cc:24** - Potential division by zero: MessageLogger not checked
- **/workspace/STMMC/src/VirtualDetectorTree_module.cc:27** - Potential division by zero: GlobalConstantsService not checked
- **/workspace/STMMC/src/VirtualDetectorTree_module.cc:28** - Potential division by zero: GlobalConstantsService not checked
- ... and 166 more

#### memory_leak (15 occurrences)

- **/workspace/STMMC/src/HPGeTree_module.cc:6** - Potential memory leak: new entry without corresponding delete
- **/workspace/STMMC/src/HPGeTree_module.cc:8** - Potential memory leak: new entry without corresponding delete
- **/workspace/STMMC/src/ShiftVirtualDetectorStepPointMCs_module.cc:1** - Potential memory leak: new location without corresponding delete
- **/workspace/STMMC/src/ShiftVirtualDetectorStepPointMCs_module.cc:2** - Potential memory leak: new location without corresponding delete
- **/workspace/STMMC/src/ShiftVirtualDetectorStepPointMCs_module.cc:103** - Potential memory leak: new StepPointMCCollection without corresponding delete
- **/workspace/STMMC/src/ShiftVirtualDetectorStepPointMCs_module.cc:124** - Potential memory leak: new offset without corresponding delete
- **/workspace/STMMC/src/ShiftVirtualDetectorStepPointMCs_module.cc:125** - Potential memory leak: new distribution without corresponding delete
- **/workspace/STMMC/src/ShiftVirtualDetectorStepPointMCs_module.cc:156** - Potential memory leak: new offset without corresponding delete
- **/workspace/STMMC/src/ShiftVirtualDetectorStepPointMCs_module.cc:157** - Potential memory leak: new distribution without corresponding delete
- **/workspace/STMMC/src/ConcatenateDigitizedWaveforms_module.cc:91** - Potential memory leak: new STMWaveformDigiCollection without corresponding delete
- ... and 5 more

#### missing_return (1 occurrences)

- **/workspace/STMMC/src/HPGeWaveformsFromStepPointMCs_module.cc:431** - Function may be missing return statement

#### unused_variable (1 occurrences)

- **/workspace/STMMC/src/DetectorEfficiency_module.cc:43** - Variable verbose declared but possibly unused


### STMReco

Found 243 potential bugs:

#### array_bounds (63 occurrences)

- **/workspace/STMReco/src/STMAnalyzeDigis_module.cc:182** - Array access p[0] without bounds check
- **/workspace/STMReco/src/STMAnalyzeDigis_module.cc:183** - Array access p[1] without bounds check
- **/workspace/STMReco/src/STMAnalyzeDigis_module.cc:184** - Array access p[2] without bounds check
- **/workspace/STMReco/src/STMAnalyzeDigis_module.cc:185** - Array access p[3] without bounds check
- **/workspace/STMReco/src/STMAnalyzeDigis_module.cc:186** - Array access t[0] without bounds check
- **/workspace/STMReco/src/STMAnalyzeDigis_module.cc:193** - Array access p[0] without bounds check
- **/workspace/STMReco/src/STMAnalyzeDigis_module.cc:194** - Array access p[1] without bounds check
- **/workspace/STMReco/src/STMAnalyzeDigis_module.cc:195** - Array access p[2] without bounds check
- **/workspace/STMReco/src/STMAnalyzeDigis_module.cc:196** - Array access p[3] without bounds check
- **/workspace/STMReco/src/STMAnalyzeDigis_module.cc:197** - Array access p[4] without bounds check
- ... and 53 more

#### assignment_in_condition (7 occurrences)

- **/workspace/STMReco/src/STMAnalyzeDigis_module.cc:404** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/STMReco/src/STMAnalyzeDigis_module.cc:460** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/STMReco/src/STMZeroSuppression_module.cc:225** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/STMReco/src/STMZeroSuppression_module.cc:365** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/STMReco/src/STMMovingWindowDeconvolution_module.cc:185** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/STMReco/src/STMMovingWindowDeconvolution_module.cc:186** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/STMReco/src/STMMovingWindowDeconvolution_module.cc:278** - Possible assignment (=) instead of comparison (==) in condition

#### division_by_zero (152 occurrences)

- **/workspace/STMReco/src/STMAnalyzeDigis_module.cc:7** - Potential division by zero: Framework not checked
- **/workspace/STMReco/src/STMAnalyzeDigis_module.cc:8** - Potential division by zero: Framework not checked
- **/workspace/STMReco/src/STMAnalyzeDigis_module.cc:9** - Potential division by zero: Framework not checked
- **/workspace/STMReco/src/STMAnalyzeDigis_module.cc:10** - Potential division by zero: Framework not checked
- **/workspace/STMReco/src/STMAnalyzeDigis_module.cc:11** - Potential division by zero: Framework not checked
- **/workspace/STMReco/src/STMAnalyzeDigis_module.cc:12** - Potential division by zero: exception not checked
- **/workspace/STMReco/src/STMAnalyzeDigis_module.cc:13** - Potential division by zero: Utilities not checked
- **/workspace/STMReco/src/STMAnalyzeDigis_module.cc:14** - Potential division by zero: MessageLogger not checked
- **/workspace/STMReco/src/STMAnalyzeDigis_module.cc:16** - Potential division by zero: ParameterSet not checked
- **/workspace/STMReco/src/STMAnalyzeDigis_module.cc:17** - Potential division by zero: types not checked
- ... and 142 more

#### memory_leak (9 occurrences)

- **/workspace/STMReco/src/STMAnalyzeDigis_module.cc:238** - Potential memory leak: new TSpline3 without corresponding delete
- **/workspace/STMReco/src/STMAnalyzeDigis_module.cc:252** - Potential memory leak: new TF1 without corresponding delete
- **/workspace/STMReco/src/STMAnalyzeDigis_module.cc:266** - Potential memory leak: new TF1 without corresponding delete
- **/workspace/STMReco/src/STMAnalyzeDigis_module.cc:287** - Potential memory leak: new TF1 without corresponding delete
- **/workspace/STMReco/src/STMAnalyzeDigis_module.cc:294** - Potential memory leak: new TGraph without corresponding delete
- **/workspace/STMReco/src/STMZeroSuppression_module.cc:182** - Potential memory leak: new STMWaveformDigiCollection without corresponding delete
- **/workspace/STMReco/src/STMMovingWindowDeconvolution_module.cc:210** - Potential memory leak: new STMMWDDigiCollection without corresponding delete
- **/workspace/STMReco/src/STMMovingWindowDeconvolution_module.cc:382** - Potential memory leak: new peak without corresponding delete
- **/workspace/STMReco/src/MakeSTMHits_module.cc:64** - Potential memory leak: new STMHitCollection without corresponding delete

#### missing_error_handling (6 occurrences)

- **/workspace/STMReco/src/STMZeroSuppression_module.cc:181** - getHandle/getValidHandle result not checked for validity
- **/workspace/STMReco/src/PlotSTMWaveformDigis_module.cc:66** - getHandle/getValidHandle result not checked for validity
- **/workspace/STMReco/src/PlotSTMEnergySpectrum_module.cc:67** - getHandle/getValidHandle result not checked for validity
- **/workspace/STMReco/src/PlotSTMMWDSpectrum_module.cc:63** - getHandle/getValidHandle result not checked for validity
- **/workspace/STMReco/src/STMMovingWindowDeconvolution_module.cc:211** - getHandle/getValidHandle result not checked for validity
- **/workspace/STMReco/src/MakeSTMHits_module.cc:65** - getHandle/getValidHandle result not checked for validity

#### missing_return (3 occurrences)

- **/workspace/STMReco/src/STMZeroSuppression_module.cc:365** - Function may be missing return statement
- **/workspace/STMReco/src/STMZeroSuppression_module.cc:368** - Function may be missing return statement
- **/workspace/STMReco/src/STMMovingWindowDeconvolution_module.cc:379** - Function may be missing return statement

#### resource_leak (1 occurrences)

- **/workspace/STMReco/src/STMAnalyzeDigis_module.cc:159** - File handle opened but may not be closed

#### uninitialized_variable (2 occurrences)

- **/workspace/STMReco/src/PlotSTMWaveformDigis_module.cc:47** - Variable _subtractPedestal may be used uninitialized
- **/workspace/STMReco/src/PlotSTMWaveformDigis_module.cc:49** - Variable _verbosityLevel may be used uninitialized


### SeedService

Found 30 potential bugs:

#### array_bounds (6 occurrences)

- **/workspace/SeedService/src/SeedTest01_module.cc:53** - Array access instanceNames_[i] without bounds check
- **/workspace/SeedService/src/SeedTest01_module.cc:70** - Array access instanceNames_[i] without bounds check
- **/workspace/SeedService/src/SeedTest01_module.cc:72** - Array access instanceNames_[i] without bounds check
- **/workspace/SeedService/src/SeedTest01_module.cc:77** - Array access instanceNames_[i] without bounds check
- **/workspace/SeedService/src/SeedTest01_module.cc:79** - Array access instanceNames_[i] without bounds check
- **/workspace/SeedService/src/SeedService.cc:46** - Array access cnames[0] without bounds check

#### assignment_in_condition (3 occurrences)

- **/workspace/SeedService/src/SeedService.cc:148** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/SeedService/src/SeedService.cc:166** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/SeedService/src/SeedService.cc:279** - Possible assignment (=) instead of comparison (==) in condition

#### division_by_zero (20 occurrences)

- **/workspace/SeedService/src/SeedTest01_module.cc:9** - Potential division by zero: SeedService not checked
- **/workspace/SeedService/src/SeedTest01_module.cc:12** - Potential division by zero: Framework not checked
- **/workspace/SeedService/src/SeedTest01_module.cc:13** - Potential division by zero: Framework not checked
- **/workspace/SeedService/src/SeedTest01_module.cc:14** - Potential division by zero: Framework not checked
- **/workspace/SeedService/src/SeedTest01_module.cc:15** - Potential division by zero: Framework not checked
- **/workspace/SeedService/src/SeedTest01_module.cc:16** - Potential division by zero: Framework not checked
- **/workspace/SeedService/src/SeedTest01_module.cc:17** - Potential division by zero: Framework not checked
- **/workspace/SeedService/src/SeedService.cc:15** - Potential division by zero: SeedService not checked
- **/workspace/SeedService/src/SeedService.cc:18** - Potential division by zero: Framework not checked
- **/workspace/SeedService/src/SeedService.cc:19** - Potential division by zero: Framework not checked
- ... and 10 more

#### uninitialized_variable (1 occurrences)

- **/workspace/SeedService/src/SeedTest01_module.cc:38** - Variable testMode_ may be used uninitialized


### ServicesGeom

Found 2 potential bugs:

#### division_by_zero (2 occurrences)

- **/workspace/ServicesGeom/src/ElectronicRack.cc:1** - Potential division by zero: ServicesGeom not checked
- **/workspace/ServicesGeom/src/Pipe.cc:1** - Potential division by zero: ServicesGeom not checked


### SimulationConditions

Found 4 potential bugs:

#### division_by_zero (4 occurrences)

- **/workspace/SimulationConditions/src/SimBookkeeperMaker.cc:5** - Potential division by zero: SimulationConditions not checked
- **/workspace/SimulationConditions/src/SimBookkeeper.cc:2** - Potential division by zero: SimulationConditions not checked
- **/workspace/SimulationConditions/src/SimBookkeeperCache.cc:5** - Potential division by zero: Framework not checked
- **/workspace/SimulationConditions/src/SimBookkeeperCache.cc:7** - Potential division by zero: SimulationConditions not checked


### Sources

Found 309 potential bugs:

#### array_bounds (76 occurrences)

- **/workspace/Sources/src/FromSTMTestBeamData_source.cc:172** - Array access unixtime[4] without bounds check
- **/workspace/Sources/src/FromSTMTestBeamData_source.cc:173** - Array access unixtime[0] without bounds check
- **/workspace/Sources/src/FromSTMTestBeamData_source.cc:174** - Array access unixtime[3] without bounds check
- **/workspace/Sources/src/FromSTMTestBeamData_source.cc:190** - Array access slice_header[1] without bounds check
- **/workspace/Sources/src/FromSTMTestBeamData_source.cc:192** - Array access slice_header[0] without bounds check
- **/workspace/Sources/src/FromSTMTestBeamData_source.cc:194** - Array access slice_header[0] without bounds check
- **/workspace/Sources/src/FromSTMTestBeamData_source.cc:198** - Array access slice_header[0] without bounds check
- **/workspace/Sources/src/FromSTMTestBeamData_source.cc:203** - Array access adc[1] without bounds check
- **/workspace/Sources/src/FromSTMTestBeamData_source.cc:205** - Array access adc[0] without bounds check
- **/workspace/Sources/src/FromSTMTestBeamData_source.cc:206** - Array access adc[0] without bounds check
- ... and 66 more

#### assignment_in_condition (15 occurrences)

- **/workspace/Sources/src/FromEMFMARSFileWeighted_source.cc:127** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Sources/src/FromEMFMARSFileWeighted_source.cc:194** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Sources/src/FromSTMTestBeamData_source.cc:248** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Sources/src/FromCorsikaBinary_source.cc:180** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Sources/src/CosmicCORSIKA.cc:164** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Sources/src/CosmicCORSIKA.cc:167** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Sources/src/CosmicCORSIKA.cc:182** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Sources/src/CosmicCORSIKA.cc:235** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Sources/src/FromExtMonFNALMARSFile_source.cc:142** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Sources/src/FromExtMonFNALMARSFile_source.cc:200** - Possible assignment (=) instead of comparison (==) in condition
- ... and 5 more

#### division_by_zero (160 occurrences)

- **/workspace/Sources/src/FromEMFMARSFileWeighted_source.cc:9** - Potential division by zero: Sources not checked
- **/workspace/Sources/src/FromEMFMARSFileWeighted_source.cc:13** - Potential division by zero: utility not checked
- **/workspace/Sources/src/FromEMFMARSFileWeighted_source.cc:17** - Potential division by zero: Vector not checked
- **/workspace/Sources/src/FromEMFMARSFileWeighted_source.cc:18** - Potential division by zero: Vector not checked
- **/workspace/Sources/src/FromEMFMARSFileWeighted_source.cc:20** - Potential division by zero: Framework not checked
- **/workspace/Sources/src/FromEMFMARSFileWeighted_source.cc:21** - Potential division by zero: Framework not checked
- **/workspace/Sources/src/FromEMFMARSFileWeighted_source.cc:22** - Potential division by zero: Framework not checked
- **/workspace/Sources/src/FromEMFMARSFileWeighted_source.cc:23** - Potential division by zero: Framework not checked
- **/workspace/Sources/src/FromEMFMARSFileWeighted_source.cc:24** - Potential division by zero: Framework not checked
- **/workspace/Sources/src/FromEMFMARSFileWeighted_source.cc:25** - Potential division by zero: Framework not checked
- ... and 150 more

#### memory_leak (44 occurrences)

- **/workspace/Sources/src/FromEMFMARSFileWeighted_source.cc:146** - Potential memory leak: new art without corresponding delete
- **/workspace/Sources/src/FromEMFMARSFileWeighted_source.cc:183** - Potential memory leak: new GenParticleCollection without corresponding delete
- **/workspace/Sources/src/FromEMFMARSFileWeighted_source.cc:184** - Potential memory leak: new MARSInfoCollection without corresponding delete
- **/workspace/Sources/src/FromEMFMARSFileWeighted_source.cc:185** - Potential memory leak: new GenParticleMARSAssns without corresponding delete
- **/workspace/Sources/src/FromSTMTestBeamData_source.cc:132** - Potential memory leak: new art without corresponding delete
- **/workspace/Sources/src/FromSTMTestBeamData_source.cc:155** - Potential memory leak: new mu2e without corresponding delete
- **/workspace/Sources/src/FromSTMTestBeamData_source.cc:156** - Potential memory leak: new mu2e without corresponding delete
- **/workspace/Sources/src/FromSTMTestBeamData_source.cc:184** - Potential memory leak: new mu2e without corresponding delete
- **/workspace/Sources/src/FromSTMTestBeamData_source.cc:235** - Potential memory leak: new run without corresponding delete
- **/workspace/Sources/src/FromSTMTestBeamData_source.cc:235** - Potential memory leak: new subRun without corresponding delete
- ... and 34 more

#### missing_return (1 occurrences)

- **/workspace/Sources/src/FromSTMTestBeamData_source.cc:214** - Function may be missing return statement

#### resource_leak (1 occurrences)

- **/workspace/Sources/src/FromSTMTestBeamData_source.cc:121** - File handle opened but may not be closed

#### uninitialized_variable (4 occurrences)

- **/workspace/Sources/src/FromExtMonFNALMARSFile_source.cc:48** - Variable remainingWeight may be used uninitialized
- **/workspace/Sources/src/PBISequence_source.cc:165** - Variable protons may be used uninitialized
- **/workspace/Sources/src/PBISequence_source.cc:199** - Variable protons may be used uninitialized
- **/workspace/Sources/src/PBISequence_source.cc:259** - Variable protons may be used uninitialized

#### unused_variable (3 occurrences)

- **/workspace/Sources/src/FromSTMTestBeamData_source.cc:64** - Variable currentFileNumber_ declared but possibly unused
- **/workspace/Sources/src/FromSTMTestBeamData_source.cc:189** - Variable i_slice declared but possibly unused
- **/workspace/Sources/src/FromSTMTestBeamData_source.cc:204** - Variable i_adc_sample declared but possibly unused

#### use_after_free (5 occurrences)

- **/workspace/Sources/src/FromSTMTestBeamData_source.cc:250** - Potential use after free: it deleted but may be used later
- **/workspace/Sources/src/FromCorsikaBinary_source.cc:181** - Potential use after free: it deleted but may be used later
- **/workspace/Sources/src/PBISequence_source.cc:188** - Potential use after free: currentFile_ deleted but may be used later
- **/workspace/Sources/src/PBISequence_source.cc:227** - Potential use after free: it deleted but may be used later
- **/workspace/Sources/src/FromTrackerPrototypeData_source.cc:305** - Potential use after free: it deleted but may be used later


### StoppingTargetGeom

Found 4 potential bugs:

#### division_by_zero (4 occurrences)

- **/workspace/StoppingTargetGeom/src/zBinningForFoils.cc:12** - Potential division by zero: exception not checked
- **/workspace/StoppingTargetGeom/src/zBinningForFoils.cc:14** - Potential division by zero: StoppingTargetGeom not checked
- **/workspace/StoppingTargetGeom/src/zBinningForFoils.cc:15** - Potential division by zero: StoppingTargetGeom not checked
- **/workspace/StoppingTargetGeom/src/zBinningForFoils.cc:45** - Potential division by zero: nBinsDZ not checked


### TEveEventDisplay

Found 531 potential bugs:

#### array_bounds (104 occurrences)

- **/workspace/TEveEventDisplay/src/TEveMu2eProjectionInterface.cc:191** - Array access orthodetlist[i] without bounds check
- **/workspace/TEveEventDisplay/src/TEveMu2eProjectionInterface.cc:195** - Array access orthodetlist[i] without bounds check
- **/workspace/TEveEventDisplay/src/TEveMu2eHit.cc:25** - Array access allStraws[i] without bounds check
- **/workspace/TEveEventDisplay/src/TEveMu2eHit.cc:80** - Array access colors[energylevel] without bounds check
- **/workspace/TEveEventDisplay/src/TEveMu2eHit.cc:127** - Array access colors[energylevel] without bounds check
- **/workspace/TEveEventDisplay/src/TEveMu2eHit.cc:169** - Array access colors[energylevel] without bounds check
- **/workspace/TEveEventDisplay/src/TEveMu2eCRVEvent.cc:32** - Array access sibarposition[3] without bounds check
- **/workspace/TEveEventDisplay/src/TEveMu2eCRVEvent.cc:33** - Array access sibarposition[0] without bounds check
- **/workspace/TEveEventDisplay/src/TEveMu2eCRVEvent.cc:34** - Array access sibarposition[1] without bounds check
- **/workspace/TEveEventDisplay/src/TEveMu2eCRVEvent.cc:35** - Array access sibarposition[2] without bounds check
- ... and 94 more

#### assignment_in_condition (40 occurrences)

- **/workspace/TEveEventDisplay/src/TEveMu2eMCInterface.cc:12** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TEveEventDisplay/src/TEveMu2eMCInterface.cc:16** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TEveEventDisplay/src/TEveMu2eMCInterface.cc:21** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TEveEventDisplay/src/TEveMu2eMCInterface.cc:29** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TEveEventDisplay/src/TEveMu2eMCInterface.cc:59** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TEveEventDisplay/src/TEveMu2eMCInterface.cc:170** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TEveEventDisplay/src/TEveMu2eMCTraj.cc:11** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TEveEventDisplay/src/TEveMu2eDataInterface.cc:13** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TEveEventDisplay/src/TEveMu2eDataInterface.cc:17** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TEveEventDisplay/src/TEveMu2eDataInterface.cc:22** - Possible assignment (=) instead of comparison (==) in condition
- ... and 30 more

#### division_by_zero (96 occurrences)

- **/workspace/TEveEventDisplay/src/TEveMu2eProjectionInterface.cc:1** - Potential division by zero: TEveEventDisplay not checked
- **/workspace/TEveEventDisplay/src/TEveMu2eProjectionInterface.cc:12** - Potential division by zero: RZ not checked
- **/workspace/TEveEventDisplay/src/TEveMu2eProjectionInterface.cc:19** - Potential division by zero: evt not checked
- **/workspace/TEveEventDisplay/src/TEveMu2eProjectionInterface.cc:45** - Potential division by zero: RZ not checked
- **/workspace/TEveEventDisplay/src/TEveMu2eProjectionInterface.cc:58** - Potential division by zero: evt not checked
- **/workspace/TEveEventDisplay/src/TEveMu2eProjectionInterface.cc:91** - Potential division by zero: RZ not checked
- **/workspace/TEveEventDisplay/src/TEveMu2eProjectionInterface.cc:104** - Potential division by zero: evt not checked
- **/workspace/TEveEventDisplay/src/TEveMu2eHit.cc:1** - Potential division by zero: GeometryService not checked
- **/workspace/TEveEventDisplay/src/TEveMu2eHit.cc:2** - Potential division by zero: GeometryService not checked
- **/workspace/TEveEventDisplay/src/TEveMu2eHit.cc:3** - Potential division by zero: TEveEventDisplay not checked
- ... and 86 more

#### memory_leak (283 occurrences)

- **/workspace/TEveEventDisplay/src/TEveMu2eProjectionInterface.cc:13** - Potential memory leak: new TEveProjectionManager without corresponding delete
- **/workspace/TEveEventDisplay/src/TEveMu2eProjectionInterface.cc:14** - Potential memory leak: new TEveProjectionAxes without corresponding delete
- **/workspace/TEveEventDisplay/src/TEveMu2eProjectionInterface.cc:19** - Potential memory leak: new tab without corresponding delete
- **/workspace/TEveEventDisplay/src/TEveMu2eProjectionInterface.cc:46** - Potential memory leak: new TEveProjectionManager without corresponding delete
- **/workspace/TEveEventDisplay/src/TEveMu2eProjectionInterface.cc:47** - Potential memory leak: new TEveProjectionAxes without corresponding delete
- **/workspace/TEveEventDisplay/src/TEveMu2eProjectionInterface.cc:52** - Potential memory leak: new TEveProjectionManager without corresponding delete
- **/workspace/TEveEventDisplay/src/TEveMu2eProjectionInterface.cc:53** - Potential memory leak: new TEveProjectionAxes without corresponding delete
- **/workspace/TEveEventDisplay/src/TEveMu2eProjectionInterface.cc:58** - Potential memory leak: new tab without corresponding delete
- **/workspace/TEveEventDisplay/src/TEveMu2eProjectionInterface.cc:92** - Potential memory leak: new TEveProjectionManager without corresponding delete
- **/workspace/TEveEventDisplay/src/TEveMu2eProjectionInterface.cc:93** - Potential memory leak: new TEveProjectionAxes without corresponding delete
- ... and 273 more

#### missing_error_handling (3 occurrences)

- **/workspace/TEveEventDisplay/src/Collection_Filler.cc:75** - getHandle/getValidHandle result not checked for validity
- **/workspace/TEveEventDisplay/src/Collection_Filler.cc:91** - getHandle/getValidHandle result not checked for validity
- **/workspace/TEveEventDisplay/src/Collection_Filler.cc:99** - getHandle/getValidHandle result not checked for validity

#### uninitialized_variable (3 occurrences)

- **/workspace/TEveEventDisplay/src/TEveNonGDMLTest_module.cc:77** - Variable _diagLevel may be used uninitialized
- **/workspace/TEveEventDisplay/src/TEveNonGDMLTest_module.cc:140** - Variable enter may be used uninitialized
- **/workspace/TEveEventDisplay/src/TEveGDMLTest_module.cc:76** - Variable _diagLevel may be used uninitialized

#### unused_variable (2 occurrences)

- **/workspace/TEveEventDisplay/src/TEveNonGDMLTest_module.cc:78** - Variable isFirstEvent declared but possibly unused
- **/workspace/TEveEventDisplay/src/TEveEventDisplay_module.cc:72** - Variable subrunn declared but possibly unused


### TestTools

Found 1 potential bugs:

#### division_by_zero (1 occurrences)

- **/workspace/TestTools/src/TestClass.cc:12** - Potential division by zero: TestTools not checked


### TrackCaloMatching

Found 504 potential bugs:

#### array_bounds (172 occurrences)

- **/workspace/TrackCaloMatching/src/TrackCaloIntersectionMVA_module.cc:147** - Array access _trksection[128] without bounds check
- **/workspace/TrackCaloMatching/src/TrackCaloIntersectionMVA_module.cc:148** - Array access _trkmomx[128] without bounds check
- **/workspace/TrackCaloMatching/src/TrackCaloIntersectionMVA_module.cc:168** - Array access trksection[trkint] without bounds check
- **/workspace/TrackCaloMatching/src/TrackCaloIntersectionMVA_module.cc:169** - Array access trkpath[trkint] without bounds check
- **/workspace/TrackCaloMatching/src/TrackCaloIntersectionMVA_module.cc:170** - Array access trktof[trkint] without bounds check
- **/workspace/TrackCaloMatching/src/TrackCaloIntersectionMVA_module.cc:171** - Array access trkx[trkint] without bounds check
- **/workspace/TrackCaloMatching/src/TrackCaloIntersectionMVA_module.cc:172** - Array access trky[trkint] without bounds check
- **/workspace/TrackCaloMatching/src/TrackCaloIntersectionMVA_module.cc:173** - Array access trkz[trkint] without bounds check
- **/workspace/TrackCaloMatching/src/TrackCaloIntersectionMVA_module.cc:174** - Array access trkmomx[trkint] without bounds check
- **/workspace/TrackCaloMatching/src/TrackCaloIntersectionMVA_module.cc:175** - Array access trkmomy[trkint] without bounds check
- ... and 162 more

#### division_by_zero (309 occurrences)

- **/workspace/TrackCaloMatching/src/TrackCaloIntersectionMVA_module.cc:21** - Potential division by zero: Framework not checked
- **/workspace/TrackCaloMatching/src/TrackCaloIntersectionMVA_module.cc:22** - Potential division by zero: Framework not checked
- **/workspace/TrackCaloMatching/src/TrackCaloIntersectionMVA_module.cc:23** - Potential division by zero: Framework not checked
- **/workspace/TrackCaloMatching/src/TrackCaloIntersectionMVA_module.cc:24** - Potential division by zero: TFileDirectory not checked
- **/workspace/TrackCaloMatching/src/TrackCaloIntersectionMVA_module.cc:25** - Potential division by zero: Framework not checked
- **/workspace/TrackCaloMatching/src/TrackCaloIntersectionMVA_module.cc:26** - Potential division by zero: TFileService not checked
- **/workspace/TrackCaloMatching/src/TrackCaloIntersectionMVA_module.cc:27** - Potential division by zero: Framework not checked
- **/workspace/TrackCaloMatching/src/TrackCaloIntersectionMVA_module.cc:30** - Potential division by zero: ParameterSet not checked
- **/workspace/TrackCaloMatching/src/TrackCaloIntersectionMVA_module.cc:31** - Potential division by zero: MessageLogger not checked
- **/workspace/TrackCaloMatching/src/TrackCaloIntersectionMVA_module.cc:34** - Potential division by zero: GeometryService not checked
- ... and 299 more

#### memory_leak (9 occurrences)

- **/workspace/TrackCaloMatching/src/TrackCaloIntersectionMVA_module.cc:219** - Potential memory leak: new TrkCaloIntersectCollection without corresponding delete
- **/workspace/TrackCaloMatching/src/TrackCaloMatchingExtend_module.cc:137** - Potential memory leak: new TrkCaloMatchCollection without corresponding delete
- **/workspace/TrackCaloMatching/src/TrackCaloMatching_module.cc:211** - Potential memory leak: new TrackClusterMatchCollection without corresponding delete
- **/workspace/TrackCaloMatching/src/TrackCaloMatching_module.cc:472** - Potential memory leak: new best without corresponding delete
- **/workspace/TrackCaloMatching/src/TrkExtrapol_module.cc:274** - Potential memory leak: new double[nSections] without corresponding delete
- **/workspace/TrackCaloMatching/src/TrkExtrapol_module.cc:275** - Potential memory leak: new double[nSections] without corresponding delete
- **/workspace/TrackCaloMatching/src/TrkExtrapol_module.cc:276** - Potential memory leak: new bool[nSections] without corresponding delete
- **/workspace/TrackCaloMatching/src/TrkExtrapol_module.cc:457** - Potential memory leak: new TrkToCaloExtrapolCollection without corresponding delete
- **/workspace/TrackCaloMatching/src/TrackCaloMatchingMVA_module.cc:154** - Potential memory leak: new TrkCaloMatchCollection without corresponding delete

#### missing_error_handling (3 occurrences)

- **/workspace/TrackCaloMatching/src/TrackCaloIntersection_module.cc:188** - getHandle/getValidHandle result not checked for validity
- **/workspace/TrackCaloMatching/src/TrackCaloMatching_module.cc:196** - getHandle/getValidHandle result not checked for validity
- **/workspace/TrackCaloMatching/src/TrackCaloMatching_module.cc:199** - getHandle/getValidHandle result not checked for validity

#### missing_return (3 occurrences)

- **/workspace/TrackCaloMatching/src/TrackCaloMatching_module.cc:258** - Function may be missing return statement
- **/workspace/TrackCaloMatching/src/TrkExtrapol_module.cc:330** - Function may be missing return statement
- **/workspace/TrackCaloMatching/src/TrkExtrapol_module.cc:501** - Function may be missing return statement

#### uninitialized_variable (4 occurrences)

- **/workspace/TrackCaloMatching/src/TrackCaloIntersection_module.cc:130** - Variable _outputNtup may be used uninitialized
- **/workspace/TrackCaloMatching/src/TrackCaloMatching_module.cc:92** - Variable _firstEvent may be used uninitialized
- **/workspace/TrackCaloMatching/src/TrkExtrapol_module.cc:267** - Variable circleRadius may be used uninitialized
- **/workspace/TrackCaloMatching/src/TrkExtrapol_module.cc:366** - Variable lrange may be used uninitialized

#### unused_variable (4 occurrences)

- **/workspace/TrackCaloMatching/src/TrackCaloIntersectionMVA_module.cc:254** - Variable iSec declared but possibly unused
- **/workspace/TrackCaloMatching/src/TrackCaloIntersection_module.cc:225** - Variable iSec declared but possibly unused
- **/workspace/TrackCaloMatching/src/TrkExtrapol_module.cc:301** - Variable iStep declared but possibly unused
- **/workspace/TrackCaloMatching/src/TrackCaloMatchingMVA_module.cc:397** - Variable i declared but possibly unused


### TrackerConditions

Found 420 potential bugs:

#### array_bounds (237 occurrences)

- **/workspace/TrackerConditions/src/Mu2eDetectorMaker.cc:36** - Array access _strawmap[straw->id()] without bounds check
- **/workspace/TrackerConditions/src/TrackerPanelMapMaker.cc:31** - Array access mnid[i] without bounds check
- **/workspace/TrackerConditions/src/StrawElectronics.cc:27** - Array access poles[i] without bounds check
- **/workspace/TrackerConditions/src/StrawElectronics.cc:28** - Array access poles[i] without bounds check
- **/workspace/TrackerConditions/src/StrawElectronics.cc:31** - Array access zeros[i] without bounds check
- **/workspace/TrackerConditions/src/StrawElectronics.cc:32** - Array access zeros[i] without bounds check
- **/workspace/TrackerConditions/src/StrawElectronics.cc:53** - Array access response[i] without bounds check
- **/workspace/TrackerConditions/src/StrawElectronics.cc:56** - Array access response[i] without bounds check
- **/workspace/TrackerConditions/src/StrawElectronics.cc:61** - Array access response[i] without bounds check
- **/workspace/TrackerConditions/src/StrawElectronics.cc:67** - Array access response[i] without bounds check
- ... and 227 more

#### assignment_in_condition (15 occurrences)

- **/workspace/TrackerConditions/src/StrawElectronics.cc:27** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrackerConditions/src/StrawElectronics.cc:31** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrackerConditions/src/StrawElectronics.cc:55** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrackerConditions/src/StrawElectronics.cc:60** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrackerConditions/src/StrawElectronics.cc:72** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrackerConditions/src/StrawElectronics.cc:80** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrackerConditions/src/StrawElectronics.cc:112** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrackerConditions/src/StrawElectronics.cc:338** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrackerConditions/src/StrawElectronics.cc:353** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrackerConditions/src/StrawPhysicsMaker.cc:48** - Possible assignment (=) instead of comparison (==) in condition
- ... and 5 more

#### division_by_zero (158 occurrences)

- **/workspace/TrackerConditions/src/Mu2eDetectorMaker.cc:4** - Potential division by zero: GeometryService not checked
- **/workspace/TrackerConditions/src/Mu2eDetectorMaker.cc:5** - Potential division by zero: TrackerGeom not checked
- **/workspace/TrackerConditions/src/Mu2eDetectorMaker.cc:6** - Potential division by zero: TrackerConditions not checked
- **/workspace/TrackerConditions/src/Mu2eDetectorMaker.cc:7** - Potential division by zero: TrackerConditions not checked
- **/workspace/TrackerConditions/src/TrackerPanelMapMaker.cc:2** - Potential division by zero: TrackerConditions not checked
- **/workspace/TrackerConditions/src/TrackerPanelMapMaker.cc:3** - Potential division by zero: TrackerConditions not checked
- **/workspace/TrackerConditions/src/TrackerPanelMapMaker.cc:4** - Potential division by zero: exception not checked
- **/workspace/TrackerConditions/src/DriftInfo.cc:1** - Potential division by zero: TrackerConditions not checked
- **/workspace/TrackerConditions/src/DriftInfo.cc:3** - Potential division by zero: 3 not checked
- **/workspace/TrackerConditions/src/StrawElectronics.cc:8** - Potential division by zero: TrackerConditions not checked
- ... and 148 more

#### memory_leak (1 occurrences)

- **/workspace/TrackerConditions/src/Mu2eDetectorMaker.cc:34** - Potential memory leak: new DetStrawElem without corresponding delete

#### missing_return (7 occurrences)

- **/workspace/TrackerConditions/src/StrawPhysicsMaker.cc:50** - Function may be missing return statement
- **/workspace/TrackerConditions/src/TrackerStatus.cc:30** - Function may be missing return statement
- **/workspace/TrackerConditions/src/TrackerStatus.cc:34** - Function may be missing return statement
- **/workspace/TrackerConditions/src/TrackerStatus.cc:40** - Function may be missing return statement
- **/workspace/TrackerConditions/src/TrackerStatus.cc:48** - Function may be missing return statement
- **/workspace/TrackerConditions/src/TrackerStatus.cc:56** - Function may be missing return statement
- **/workspace/TrackerConditions/src/TrackerStatus.cc:62** - Function may be missing return statement

#### uninitialized_variable (2 occurrences)

- **/workspace/TrackerConditions/src/StrawPhysics.cc:55** - Variable aval may be used uninitialized
- **/workspace/TrackerConditions/src/StrawResponseMaker.cc:29** - Variable x may be used uninitialized


### TrackerGeom

Found 23 potential bugs:

#### array_bounds (14 occurrences)

- **/workspace/TrackerGeom/src/SupportModel.cc:23** - Array access nam[unknown] without bounds check
- **/workspace/TrackerGeom/src/SupportModel.cc:24** - Array access nam[simple] without bounds check
- **/workspace/TrackerGeom/src/SupportModel.cc:25** - Array access nam[detailedv0] without bounds check
- **/workspace/TrackerGeom/src/Panel.cc:33** - Array access _straws[straw.id().straw()] without bounds check
- **/workspace/TrackerGeom/src/Panel.cc:43** - Array access _straws[straw.id().straw()] without bounds check
- **/workspace/TrackerGeom/src/Panel.cc:49** - Array access _straws[StrawId::_nstraws-2] without bounds check
- **/workspace/TrackerGeom/src/Panel.cc:52** - Array access _straws[47] without bounds check
- **/workspace/TrackerGeom/src/Plane.cc:31** - Array access _panels[panel.id().panel()] without bounds check
- **/workspace/TrackerGeom/src/Plane.cc:39** - Array access _panels[0] without bounds check
- **/workspace/TrackerGeom/src/SupportStructure.cc:39** - Array access _stiffRings[i] without bounds check
- ... and 4 more

#### division_by_zero (9 occurrences)

- **/workspace/TrackerGeom/src/SupportModel.cc:9** - Potential division by zero: TrackerGeom not checked
- **/workspace/TrackerGeom/src/Panel.cc:7** - Potential division by zero: TrackerGeom not checked
- **/workspace/TrackerGeom/src/Panel.cc:8** - Potential division by zero: exception not checked
- **/workspace/TrackerGeom/src/Plane.cc:10** - Potential division by zero: TrackerGeom not checked
- **/workspace/TrackerGeom/src/Plane.cc:37** - Potential division by zero: 6 not checked
- **/workspace/TrackerGeom/src/Manifold.cc:3** - Potential division by zero: TrackerGeom not checked
- **/workspace/TrackerGeom/src/SupportStructure.cc:8** - Potential division by zero: TrackerGeom not checked
- **/workspace/TrackerGeom/src/Tracker.cc:10** - Potential division by zero: TrackerGeom not checked
- **/workspace/TrackerGeom/src/Straw.cc:8** - Potential division by zero: TrackerGeom not checked


### TrackerMC

Found 446 potential bugs:

#### array_bounds (157 occurrences)

- **/workspace/TrackerMC/src/StrawWaveform.cc:191** - Array access times[0] without bounds check
- **/workspace/TrackerMC/src/StrawWaveform.cc:218** - Array access volts[j] without bounds check
- **/workspace/TrackerMC/src/MakeStrawGasSteps_module.cc:339** - Array access steps[ispmc] without bounds check
- **/workspace/TrackerMC/src/MakeStrawGasSteps_module.cc:405** - Array access dmap[dkey] without bounds check
- **/workspace/TrackerMC/src/PoissonTrackerNoise_module.cc:200** - Array access crTimesPhysical[StrawEnd::cal] without bounds check
- **/workspace/TrackerMC/src/PoissonTrackerNoise_module.cc:201** - Array access crTimesPhysical[StrawEnd::hv] without bounds check
- **/workspace/TrackerMC/src/PoissonTrackerNoise_module.cc:213** - Array access atTimesDigital[StrawEnd::cal] without bounds check
- **/workspace/TrackerMC/src/PoissonTrackerNoise_module.cc:216** - Array access atTimesDigital[StrawEnd::hv] without bounds check
- **/workspace/TrackerMC/src/PoissonTrackerNoise_module.cc:220** - Array access crTimesPhysical[0] without bounds check
- **/workspace/TrackerMC/src/StrawDigiBundleCollection.cc:39** - Array access _bundles[i] without bounds check
- ... and 147 more

#### assignment_in_condition (16 occurrences)

- **/workspace/TrackerMC/src/StrawWaveform.cc:31** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrackerMC/src/StrawWaveform.cc:72** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrackerMC/src/StrawWaveform.cc:89** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrackerMC/src/StrawWaveform.cc:134** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrackerMC/src/StrawWaveform.cc:169** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrackerMC/src/MakeStrawGasSteps_module.cc:372** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrackerMC/src/MakeStrawGasSteps_module.cc:414** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrackerMC/src/StrawClusterSequence.cc:31** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrackerMC/src/StrawClusterSequencePair.cc:24** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrackerMC/src/StrawDigisFromStrawGasSteps_module.cc:967** - Possible assignment (=) instead of comparison (==) in condition
- ... and 6 more

#### division_by_zero (247 occurrences)

- **/workspace/TrackerMC/src/StrawWaveform.cc:8** - Potential division by zero: TrackerMC not checked
- **/workspace/TrackerMC/src/StrawWaveform.cc:10** - Potential division by zero: math not checked
- **/workspace/TrackerMC/src/StrawWaveform.cc:202** - Potential division by zero: strawele not checked
- **/workspace/TrackerMC/src/MakeStrawGasSteps_module.cc:7** - Potential division by zero: Framework not checked
- **/workspace/TrackerMC/src/MakeStrawGasSteps_module.cc:8** - Potential division by zero: Framework not checked
- **/workspace/TrackerMC/src/MakeStrawGasSteps_module.cc:9** - Potential division by zero: Framework not checked
- **/workspace/TrackerMC/src/MakeStrawGasSteps_module.cc:10** - Potential division by zero: exception not checked
- **/workspace/TrackerMC/src/MakeStrawGasSteps_module.cc:11** - Potential division by zero: types not checked
- **/workspace/TrackerMC/src/MakeStrawGasSteps_module.cc:12** - Potential division by zero: Utilities not checked
- **/workspace/TrackerMC/src/MakeStrawGasSteps_module.cc:13** - Potential division by zero: MessageLogger not checked
- ... and 237 more

#### memory_leak (13 occurrences)

- **/workspace/TrackerMC/src/MakeStrawGasSteps_module.cc:190** - Potential memory leak: new StrawGasStepCollection without corresponding delete
- **/workspace/TrackerMC/src/MakeStrawGasSteps_module.cc:191** - Potential memory leak: new StrawGasStepAssns without corresponding delete
- **/workspace/TrackerMC/src/PoissonTrackerNoise_module.cc:222** - Potential memory leak: new digi without corresponding delete
- **/workspace/TrackerMC/src/StrawClusterSequence.cc:38** - Potential memory leak: new clust without corresponding delete
- **/workspace/TrackerMC/src/StrawDigiBundleCollection.cc:48** - Potential memory leak: new StrawDigiBundles without corresponding delete
- **/workspace/TrackerMC/src/StrawDigiBundleCollection.cc:80** - Potential memory leak: new StrawDigiBundles without corresponding delete
- **/workspace/TrackerMC/src/StrawDigisFromStrawGasSteps_module.cc:522** - Potential memory leak: new StrawDigiCollection without corresponding delete
- **/workspace/TrackerMC/src/StrawDigisFromStrawGasSteps_module.cc:523** - Potential memory leak: new StrawDigiADCWaveformCollection without corresponding delete
- **/workspace/TrackerMC/src/StrawDigisFromStrawGasSteps_module.cc:524** - Potential memory leak: new StrawDigiMCCollection without corresponding delete
- **/workspace/TrackerMC/src/StrawDigisFromStrawGasSteps_module.cc:555** - Potential memory leak: new digis without corresponding delete
- ... and 3 more

#### missing_error_handling (2 occurrences)

- **/workspace/TrackerMC/src/PoissonTrackerNoise_module.cc:123** - getHandle/getValidHandle result not checked for validity
- **/workspace/TrackerMC/src/StrawDigisFromStrawGasSteps_module.cc:485** - getHandle/getValidHandle result not checked for validity

#### missing_return (1 occurrences)

- **/workspace/TrackerMC/src/StrawDigisFromStrawGasSteps_module.cc:633** - Function may be missing return statement

#### uninitialized_variable (10 occurrences)

- **/workspace/TrackerMC/src/PoissonTrackerNoise_module.cc:77** - Variable _rate may be used uninitialized
- **/workspace/TrackerMC/src/PoissonTrackerNoise_module.cc:79** - Variable _crtime_spacing may be used uninitialized
- **/workspace/TrackerMC/src/PoissonTrackerNoise_module.cc:80** - Variable _crtime_tolerance may be used uninitialized
- **/workspace/TrackerMC/src/AnalogWireSignal.cc:35** - Variable tmp may be used uninitialized
- **/workspace/TrackerMC/src/AnalogWireSignal.cc:84** - Variable crTime may be used uninitialized
- **/workspace/TrackerMC/src/StrawDigisFromStrawGasSteps_module.cc:77** - Variable _charge may be used uninitialized
- **/workspace/TrackerMC/src/StrawDigisFromStrawGasSteps_module.cc:78** - Variable _time may be used uninitialized
- **/workspace/TrackerMC/src/StrawDigisFromStrawGasSteps_module.cc:937** - Variable digitize may be used uninitialized
- **/workspace/TrackerMC/src/StrawDigisFromStrawGasSteps_module.cc:1028** - Variable ns may be used uninitialized
- **/workspace/TrackerMC/src/MakeMCKalSeed_module.cc:150** - Variable t0 may be used uninitialized


### Trigger

Found 527 potential bugs:

#### array_bounds (243 occurrences)

- **/workspace/Trigger/src/EvalWeightedEventCounts_module.cc:48** - Array access _hOccInfo[kNOcc] without bounds check
- **/workspace/Trigger/src/EvalWeightedEventCounts_module.cc:53** - Array access _hOccInfo[i] without bounds check
- **/workspace/Trigger/src/EvalWeightedEventCounts_module.cc:101** - Array access _hOccInfo[index_last] without bounds check
- **/workspace/Trigger/src/EvalWeightedEventCounts_module.cc:104** - Array access _hOccInfo[index_last] without bounds check
- **/workspace/Trigger/src/EvalWeightedEventCounts_module.cc:117** - Array access _wgSum[0] without bounds check
- **/workspace/Trigger/src/EvalWeightedEventCounts_module.cc:118** - Array access _wgSum[1] without bounds check
- **/workspace/Trigger/src/EvalWeightedEventCounts_module.cc:119** - Array access _wgSum[2] without bounds check
- **/workspace/Trigger/src/EvalWeightedEventCounts_module.cc:144** - Array access _wgSum[0] without bounds check
- **/workspace/Trigger/src/EvalWeightedEventCounts_module.cc:162** - Array access _wgSum[1] without bounds check
- **/workspace/Trigger/src/EvalWeightedEventCounts_module.cc:163** - Array access _hOccInfo[0] without bounds check
- ... and 233 more

#### assignment_in_condition (16 occurrences)

- **/workspace/Trigger/src/ReadTriggerInfo_module.cc:506** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Trigger/src/ReadTriggerInfo_module.cc:540** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Trigger/src/ReadTriggerInfo_module.cc:544** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Trigger/src/ReadTriggerInfo_module.cc:554** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Trigger/src/ReadTriggerInfo_module.cc:558** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Trigger/src/ReadTriggerInfo_module.cc:568** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Trigger/src/ReadTriggerInfo_module.cc:572** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Trigger/src/ReadTriggerInfo_module.cc:648** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Trigger/src/ReadTriggerInfo_module.cc:656** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Trigger/src/ReadTriggerInfo_module.cc:689** - Possible assignment (=) instead of comparison (==) in condition
- ... and 6 more

#### division_by_zero (242 occurrences)

- **/workspace/Trigger/src/EvalWeightedEventCounts_module.cc:7** - Potential division by zero: Framework not checked
- **/workspace/Trigger/src/EvalWeightedEventCounts_module.cc:8** - Potential division by zero: Framework not checked
- **/workspace/Trigger/src/EvalWeightedEventCounts_module.cc:9** - Potential division by zero: Framework not checked
- **/workspace/Trigger/src/EvalWeightedEventCounts_module.cc:10** - Potential division by zero: Framework not checked
- **/workspace/Trigger/src/EvalWeightedEventCounts_module.cc:11** - Potential division by zero: TFileDirectory not checked
- **/workspace/Trigger/src/EvalWeightedEventCounts_module.cc:12** - Potential division by zero: TFileService not checked
- **/workspace/Trigger/src/EvalWeightedEventCounts_module.cc:13** - Potential division by zero: exception not checked
- **/workspace/Trigger/src/EvalWeightedEventCounts_module.cc:14** - Potential division by zero: ParameterSet not checked
- **/workspace/Trigger/src/EvalWeightedEventCounts_module.cc:15** - Potential division by zero: ParameterSetRegistry not checked
- **/workspace/Trigger/src/EvalWeightedEventCounts_module.cc:18** - Potential division by zero: MCDataProducts not checked
- ... and 232 more

#### memory_leak (4 occurrences)

- **/workspace/Trigger/src/MergeTriggerInfo_module.cc:57** - Potential memory leak: new TriggerInfoCollection without corresponding delete
- **/workspace/Trigger/src/MergeTriggerInfo_module.cc:58** - Potential memory leak: new KalSeedCollection without corresponding delete
- **/workspace/Trigger/src/MergeTriggerInfo_module.cc:59** - Potential memory leak: new HelixSeedCollection without corresponding delete
- **/workspace/Trigger/src/MergeTriggerInfo_module.cc:60** - Potential memory leak: new TimeClusterCollection without corresponding delete

#### missing_error_handling (5 occurrences)

- **/workspace/Trigger/src/EvalWeightedEventCounts_module.cc:140** - getHandle/getValidHandle result not checked for validity
- **/workspace/Trigger/src/ReadTriggerInfo_module.cc:786** - getHandle/getValidHandle result not checked for validity
- **/workspace/Trigger/src/DigiFilter_module.cc:75** - getHandle/getValidHandle result not checked for validity
- **/workspace/Trigger/src/DigiFilter_module.cc:81** - getHandle/getValidHandle result not checked for validity
- **/workspace/Trigger/src/PrescaleEvent_module.cc:83** - getHandle/getValidHandle result not checked for validity

#### missing_return (2 occurrences)

- **/workspace/Trigger/src/DigiFilter_module.cc:102** - Function may be missing return statement
- **/workspace/Trigger/src/DigiFilter_module.cc:104** - Function may be missing return statement

#### uninitialized_variable (15 occurrences)

- **/workspace/Trigger/src/EvalWeightedEventCounts_module.cc:73** - Variable _diagLevel may be used uninitialized
- **/workspace/Trigger/src/ReadTriggerInfo_module.cc:90** - Variable counts may be used uninitialized
- **/workspace/Trigger/src/ReadTriggerInfo_module.cc:91** - Variable exclusive_counts may be used uninitialized
- **/workspace/Trigger/src/DigiFilter_module.cc:34** - Variable _useSD may be used uninitialized
- **/workspace/Trigger/src/DigiFilter_module.cc:35** - Variable _useCD may be used uninitialized
- **/workspace/Trigger/src/DigiFilter_module.cc:38** - Variable _minnsd may be used uninitialized
- **/workspace/Trigger/src/DigiFilter_module.cc:39** - Variable _maxnsd may be used uninitialized
- **/workspace/Trigger/src/DigiFilter_module.cc:40** - Variable _minncd may be used uninitialized
- **/workspace/Trigger/src/DigiFilter_module.cc:41** - Variable _maxncd may be used uninitialized
- **/workspace/Trigger/src/DigiFilter_module.cc:42** - Variable _maxcaloE may be used uninitialized
- ... and 5 more


### TrkDiag

Found 972 potential bugs:

#### array_bounds (202 occurrences)

- **/workspace/TrkDiag/src/TrkMCTools.cc:48** - Array access spmap[spp] without bounds check
- **/workspace/TrkDiag/src/TrkMCTools.cc:76** - Array access sct[0] without bounds check
- **/workspace/TrkDiag/src/BkgDiag_module.cc:132** - Array access _icontrib[512] without bounds check
- **/workspace/TrkDiag/src/BkgDiag_module.cc:138** - Array access _hitPdg[8192] without bounds check
- **/workspace/TrkDiag/src/BkgDiag_module.cc:140** - Array access _hitTime[8192] without bounds check
- **/workspace/TrkDiag/src/BkgDiag_module.cc:234** - Array access icontrib[ncontrib] without bounds check
- **/workspace/TrkDiag/src/BkgDiag_module.cc:241** - Array access hitTime[nhits] without bounds check
- **/workspace/TrkDiag/src/BkgDiag_module.cc:242** - Array access hitnch[nhits] without bounds check
- **/workspace/TrkDiag/src/BkgDiag_module.cc:243** - Array access hitnsh[nhits] without bounds check
- **/workspace/TrkDiag/src/BkgDiag_module.cc:245** - Array access hitPdg[nhits] without bounds check
- ... and 192 more

#### assignment_in_condition (27 occurrences)

- **/workspace/TrkDiag/src/TrkMCTools.cc:45** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkDiag/src/BkgDiag_module.cc:303** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkDiag/src/BkgDiag_module.cc:582** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkDiag/src/BkgDiag_module.cc:597** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkDiag/src/TrackPID_module.cc:107** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkDiag/src/StrawHitDiag_module.cc:356** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkDiag/src/StrawHitDiag_module.cc:427** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkDiag/src/StrawHitDiag_module.cc:435** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkDiag/src/ComboHitDiag_module.cc:376** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkDiag/src/ComboHitDiag_module.cc:392** - Possible assignment (=) instead of comparison (==) in condition
- ... and 17 more

#### division_by_zero (669 occurrences)

- **/workspace/TrkDiag/src/ProtonBunchTimeDiag_module.cc:6** - Potential division by zero: 1 not checked
- **/workspace/TrkDiag/src/ProtonBunchTimeDiag_module.cc:9** - Potential division by zero: Framework not checked
- **/workspace/TrkDiag/src/ProtonBunchTimeDiag_module.cc:10** - Potential division by zero: TFileService not checked
- **/workspace/TrkDiag/src/ProtonBunchTimeDiag_module.cc:11** - Potential division by zero: Framework not checked
- **/workspace/TrkDiag/src/ProtonBunchTimeDiag_module.cc:12** - Potential division by zero: RecoDataProducts not checked
- **/workspace/TrkDiag/src/ProtonBunchTimeDiag_module.cc:13** - Potential division by zero: MCDataProducts not checked
- **/workspace/TrkDiag/src/ProtonBunchTimeDiag_module.cc:14** - Potential division by zero: DataProducts not checked
- **/workspace/TrkDiag/src/ProtonBunchTimeDiag_module.cc:59** - Potential division by zero: I not checked
- **/workspace/TrkDiag/src/ProtonBunchTimeDiag_module.cc:60** - Potential division by zero: F not checked
- **/workspace/TrkDiag/src/ProtonBunchTimeDiag_module.cc:61** - Potential division by zero: F not checked
- ... and 659 more

#### memory_leak (19 occurrences)

- **/workspace/TrkDiag/src/TrackPID_module.cc:87** - Potential memory leak: new MVAResultCollection without corresponding delete
- **/workspace/TrkDiag/src/TimeClusterDiag_module.cc:423** - Potential memory leak: new TMarker without corresponding delete
- **/workspace/TrkDiag/src/TimeClusterDiag_module.cc:431** - Potential memory leak: new TMarker without corresponding delete
- **/workspace/TrkDiag/src/TrackQuality_module.cc:85** - Potential memory leak: new MVAResultCollection without corresponding delete
- **/workspace/TrkDiag/src/HelixDiag_module.cc:455** - Potential memory leak: new TEllipse without corresponding delete
- **/workspace/TrkDiag/src/HelixDiag_module.cc:495** - Potential memory leak: new TEllipse without corresponding delete
- **/workspace/TrkDiag/src/HelixDiag_module.cc:511** - Potential memory leak: new TEllipse without corresponding delete
- **/workspace/TrkDiag/src/HelixDiag_module.cc:517** - Potential memory leak: new TEllipse without corresponding delete
- **/workspace/TrkDiag/src/HelixDiag_module.cc:533** - Potential memory leak: new TMarker without corresponding delete
- **/workspace/TrkDiag/src/HelixDiag_module.cc:627** - Potential memory leak: new TArc without corresponding delete
- ... and 9 more

#### missing_error_handling (39 occurrences)

- **/workspace/TrkDiag/src/ProtonBunchTimeDiag_module.cc:67** - getHandle/getValidHandle result not checked for validity
- **/workspace/TrkDiag/src/ProtonBunchTimeDiag_module.cc:69** - getHandle/getValidHandle result not checked for validity
- **/workspace/TrkDiag/src/ProtonBunchTimeDiag_module.cc:71** - getHandle/getValidHandle result not checked for validity
- **/workspace/TrkDiag/src/BkgDiag_module.cc:497** - getHandle/getValidHandle result not checked for validity
- **/workspace/TrkDiag/src/BkgDiag_module.cc:498** - getHandle/getValidHandle result not checked for validity
- **/workspace/TrkDiag/src/BkgDiag_module.cc:500** - getHandle/getValidHandle result not checked for validity
- **/workspace/TrkDiag/src/BkgDiag_module.cc:505** - getHandle/getValidHandle result not checked for validity
- **/workspace/TrkDiag/src/BkgDiag_module.cc:507** - getHandle/getValidHandle result not checked for validity
- **/workspace/TrkDiag/src/RobustMultiHelixAnalyzer_module.cc:115** - getHandle/getValidHandle result not checked for validity
- **/workspace/TrkDiag/src/RobustMultiHelixAnalyzer_module.cc:118** - getHandle/getValidHandle result not checked for validity
- ... and 29 more

#### missing_return (5 occurrences)

- **/workspace/TrkDiag/src/TrkMCTools.cc:138** - Function may be missing return statement
- **/workspace/TrkDiag/src/BkgDiag_module.cc:546** - Function may be missing return statement
- **/workspace/TrkDiag/src/BkgDiag_module.cc:548** - Function may be missing return statement
- **/workspace/TrkDiag/src/TrackPID_module.cc:130** - Function may be missing return statement
- **/workspace/TrkDiag/src/TrkRecoDiag_module.cc:605** - Function may be missing return statement

#### uninitialized_variable (9 occurrences)

- **/workspace/TrkDiag/src/StrawResponseTest_module.cc:48** - Variable nbins_ may be used uninitialized
- **/workspace/TrkDiag/src/StrawResponseTest_module.cc:50** - Variable first_ may be used uninitialized
- **/workspace/TrkDiag/src/TrkGeomTest_module.cc:46** - Variable first_ may be used uninitialized
- **/workspace/TrkDiag/src/TrkGeomTest_module.cc:47** - Variable teststation_ may be used uninitialized
- **/workspace/TrkDiag/src/TrackPID_module.cc:64** - Variable _printMVA may be used uninitialized
- **/workspace/TrkDiag/src/TrackPID_module.cc:65** - Variable _debug may be used uninitialized
- **/workspace/TrkDiag/src/TimeClusterDiag_module.cc:75** - Variable _count may be used uninitialized
- **/workspace/TrkDiag/src/TrackQuality_module.cc:64** - Variable _printMVA may be used uninitialized
- **/workspace/TrkDiag/src/TrackQuality_module.cc:65** - Variable _debug may be used uninitialized

#### unused_variable (2 occurrences)

- **/workspace/TrkDiag/src/BkgDiag_module.cc:471** - Variable iz declared but possibly unused
- **/workspace/TrkDiag/src/TrkGeomTest_module.cc:184** - Variable iz declared but possibly unused


### TrkExt

Found 942 potential bugs:

#### array_bounds (570 occurrences)

- **/workspace/TrkExt/src/TrkExtDiag.cc:66** - Array access hotx[nhots] without bounds check
- **/workspace/TrkExt/src/TrkExtDiag.cc:67** - Array access hoty[nhots] without bounds check
- **/workspace/TrkExt/src/TrkExtDiag.cc:68** - Array access hotz[nhots] without bounds check
- **/workspace/TrkExt/src/TrkExtDiag.cc:69** - Array access hott0[nhots] without bounds check
- **/workspace/TrkExt/src/TrkExtDiag.cc:74** - Array access trkl[ntrks] without bounds check
- **/workspace/TrkExt/src/TrkExtDiag.cc:75** - Array access trkx[ntrks] without bounds check
- **/workspace/TrkExt/src/TrkExtDiag.cc:76** - Array access trky[ntrks] without bounds check
- **/workspace/TrkExt/src/TrkExtDiag.cc:77** - Array access trkz[ntrks] without bounds check
- **/workspace/TrkExt/src/TrkExtDiag.cc:78** - Array access trkpx[ntrks] without bounds check
- **/workspace/TrkExt/src/TrkExtDiag.cc:79** - Array access trkpy[ntrks] without bounds check
- ... and 560 more

#### assignment_in_condition (39 occurrences)

- **/workspace/TrkExt/src/TrkExtDiag.cc:224** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkExt/src/TrkExtDiag.cc:236** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkExt/src/TrkExtDiag.cc:335** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkExt/src/TrkExtDiag.cc:492** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkExt/src/TrkExtDiag.cc:668** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkExt/src/TrkExtDiag.cc:689** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkExt/src/TrkExtDiag.cc:749** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkExt/src/TrkExtDiag.cc:764** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkExt/src/TrkExtMaterial.cc:131** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkExt/src/TrkExtStoppingTarget.cc:69** - Possible assignment (=) instead of comparison (==) in condition
- ... and 29 more

#### division_by_zero (294 occurrences)

- **/workspace/TrkExt/src/TrkExtDiag.cc:4** - Potential division by zero: Framework not checked
- **/workspace/TrkExt/src/TrkExtDiag.cc:5** - Potential division by zero: Framework not checked
- **/workspace/TrkExt/src/TrkExtDiag.cc:6** - Potential division by zero: Framework not checked
- **/workspace/TrkExt/src/TrkExtDiag.cc:7** - Potential division by zero: Framework not checked
- **/workspace/TrkExt/src/TrkExtDiag.cc:8** - Potential division by zero: Framework not checked
- **/workspace/TrkExt/src/TrkExtDiag.cc:9** - Potential division by zero: TFileService not checked
- **/workspace/TrkExt/src/TrkExtDiag.cc:10** - Potential division by zero: ParameterSet not checked
- **/workspace/TrkExt/src/TrkExtDiag.cc:12** - Potential division by zero: BFieldGeom not checked
- **/workspace/TrkExt/src/TrkExtDiag.cc:13** - Potential division by zero: TrkExt not checked
- **/workspace/TrkExt/src/TrkExtDiag.cc:14** - Potential division by zero: TrkExt not checked
- ... and 284 more

#### memory_leak (2 occurrences)

- **/workspace/TrkExt/src/TrkExt_module.cc:376** - Potential memory leak: new TrkExtTrajCollection without corresponding delete
- **/workspace/TrkExt/src/TrkExt_module.cc:812** - Potential memory leak: new step without corresponding delete

#### missing_return (5 occurrences)

- **/workspace/TrkExt/src/TrkExtDetectors.cc:70** - Function may be missing return statement
- **/workspace/TrkExt/src/TrkExt_module.cc:900** - Function may be missing return statement
- **/workspace/TrkExt/src/TrkExt_module.cc:928** - Function may be missing return statement
- **/workspace/TrkExt/src/TrkExt_module.cc:929** - Function may be missing return statement
- **/workspace/TrkExt/src/TrkExtShape.cc:46** - Function may be missing return statement

#### uninitialized_variable (26 occurrences)

- **/workspace/TrkExt/src/TrkExtDiag.cc:354** - Variable i may be used uninitialized
- **/workspace/TrkExt/src/TrkExtDiag.cc:544** - Variable sign may be used uninitialized
- **/workspace/TrkExt/src/TrkExtDiag.cc:553** - Variable index may be used uninitialized
- **/workspace/TrkExt/src/TrkExtDiag.cc:723** - Variable i may be used uninitialized
- **/workspace/TrkExt/src/TrkExtDiag.cc:801** - Variable sign may be used uninitialized
- **/workspace/TrkExt/src/TrkExtDiag.cc:808** - Variable index may be used uninitialized
- **/workspace/TrkExt/src/TrkExtDiag.cc:842** - Variable index may be used uninitialized
- **/workspace/TrkExt/src/TrkExtDiag.cc:875** - Variable index may be used uninitialized
- **/workspace/TrkExt/src/TrkExtDiag.cc:908** - Variable index may be used uninitialized
- **/workspace/TrkExt/src/TrkExtDiag.cc:941** - Variable index may be used uninitialized
- ... and 16 more

#### unused_variable (6 occurrences)

- **/workspace/TrkExt/src/TrkExt_module.cc:63** - Variable MAXSIM declared but possibly unused
- **/workspace/TrkExt/src/TrkExt_module.cc:1103** - Variable a2 declared but possibly unused
- **/workspace/TrkExt/src/TrkExt_module.cc:1104** - Variable a3 declared but possibly unused
- **/workspace/TrkExt/src/TrkExt_module.cc:1105** - Variable a4 declared but possibly unused
- **/workspace/TrkExt/src/TrkExt_module.cc:1106** - Variable a5 declared but possibly unused
- **/workspace/TrkExt/src/TrkExt_module.cc:1107** - Variable a6 declared but possibly unused


### TrkFilters

Found 137 potential bugs:

#### array_bounds (14 occurrences)

- **/workspace/TrkFilters/src/TimeClusterFilter_module.cc:106** - Array access pmap[iplane] without bounds check
- **/workspace/TrkFilters/src/MultiHelixFilter_module.cc:269** - Array access _hists[10] without bounds check
- **/workspace/TrkFilters/src/MultiHelixFilter_module.cc:321** - Array access _hists[index] without bounds check
- **/workspace/TrkFilters/src/MultiHelixFilter_module.cc:322** - Array access _hists[index] without bounds check
- **/workspace/TrkFilters/src/MultiHelixFilter_module.cc:404** - Array access h1_hits[index] without bounds check
- **/workspace/TrkFilters/src/MultiHelixFilter_module.cc:445** - Array access indices[0] without bounds check
- **/workspace/TrkFilters/src/MultiHelixFilter_module.cc:447** - Array access indices[index] without bounds check
- **/workspace/TrkFilters/src/MultiHelixFilter_module.cc:448** - Array access _helixCuts[index] without bounds check
- **/workspace/TrkFilters/src/MultiHelixFilter_module.cc:462** - Array access indices[i] without bounds check
- **/workspace/TrkFilters/src/MultiHelixFilter_module.cc:463** - Array access indices[j] without bounds check
- ... and 4 more

#### assignment_in_condition (3 occurrences)

- **/workspace/TrkFilters/src/TimeClusterFilter_module.cc:112** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkFilters/src/HelixFilter_module.cc:160** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkFilters/src/HelixFilter_module.cc:244** - Possible assignment (=) instead of comparison (==) in condition

#### division_by_zero (81 occurrences)

- **/workspace/TrkFilters/src/TimeClusterFilter_module.cc:3** - Potential division by zero: 1 not checked
- **/workspace/TrkFilters/src/TimeClusterFilter_module.cc:6** - Potential division by zero: Framework not checked
- **/workspace/TrkFilters/src/TimeClusterFilter_module.cc:7** - Potential division by zero: Framework not checked
- **/workspace/TrkFilters/src/TimeClusterFilter_module.cc:8** - Potential division by zero: Framework not checked
- **/workspace/TrkFilters/src/TimeClusterFilter_module.cc:9** - Potential division by zero: Framework not checked
- **/workspace/TrkFilters/src/TimeClusterFilter_module.cc:10** - Potential division by zero: types not checked
- **/workspace/TrkFilters/src/TimeClusterFilter_module.cc:11** - Potential division by zero: types not checked
- **/workspace/TrkFilters/src/TimeClusterFilter_module.cc:14** - Potential division by zero: RecoDataProducts not checked
- **/workspace/TrkFilters/src/TimeClusterFilter_module.cc:15** - Potential division by zero: RecoDataProducts not checked
- **/workspace/TrkFilters/src/TimeClusterFilter_module.cc:16** - Potential division by zero: RecoDataProducts not checked
- ... and 71 more

#### memory_leak (5 occurrences)

- **/workspace/TrkFilters/src/TimeClusterFilter_module.cc:79** - Potential memory leak: new TriggerInfo without corresponding delete
- **/workspace/TrkFilters/src/MultiHelixFilter_module.cc:321** - Potential memory leak: new Hist_t without corresponding delete
- **/workspace/TrkFilters/src/MultiHelixFilter_module.cc:519** - Potential memory leak: new TriggerInfo without corresponding delete
- **/workspace/TrkFilters/src/HelixFilter_module.cc:287** - Potential memory leak: new TriggerInfo without corresponding delete
- **/workspace/TrkFilters/src/KalSeedFilter_module.cc:146** - Potential memory leak: new TriggerInfo without corresponding delete

#### missing_error_handling (1 occurrences)

- **/workspace/TrkFilters/src/TimeClusterFilter_module.cc:83** - getHandle/getValidHandle result not checked for validity

#### missing_return (1 occurrences)

- **/workspace/TrkFilters/src/KalSeedFilter_module.cc:274** - Function may be missing return statement

#### uninitialized_variable (15 occurrences)

- **/workspace/TrkFilters/src/TimeClusterFilter_module.cc:51** - Variable _hascc may be used uninitialized
- **/workspace/TrkFilters/src/TimeClusterFilter_module.cc:52** - Variable _minnhits may be used uninitialized
- **/workspace/TrkFilters/src/TimeClusterFilter_module.cc:53** - Variable _minnplanes may be used uninitialized
- **/workspace/TrkFilters/src/TimeClusterFilter_module.cc:54** - Variable _minplanespan may be used uninitialized
- **/workspace/TrkFilters/src/TimeClusterFilter_module.cc:55** - Variable _debug may be used uninitialized
- **/workspace/TrkFilters/src/TimeClusterFilter_module.cc:58** - Variable _noFilter may be used uninitialized
- **/workspace/TrkFilters/src/HelixFilter_module.cc:92** - Variable val may be used uninitialized
- **/workspace/TrkFilters/src/HelixFilter_module.cc:221** - Variable _debug may be used uninitialized
- **/workspace/TrkFilters/src/HelixFilter_module.cc:224** - Variable _noFilter may be used uninitialized
- **/workspace/TrkFilters/src/HelixFilter_module.cc:225** - Variable _minNHelices may be used uninitialized
- ... and 5 more

#### unused_variable (17 occurrences)

- **/workspace/TrkFilters/src/MultiHelixFilter_module.cc:167** - Variable _minMomentum declared but possibly unused
- **/workspace/TrkFilters/src/MultiHelixFilter_module.cc:168** - Variable _maxMomentum declared but possibly unused
- **/workspace/TrkFilters/src/MultiHelixFilter_module.cc:169** - Variable _minPt declared but possibly unused
- **/workspace/TrkFilters/src/MultiHelixFilter_module.cc:170** - Variable _requireCaloCluster declared but possibly unused
- **/workspace/TrkFilters/src/MultiHelixFilter_module.cc:171** - Variable _minNStrawHits declared but possibly unused
- **/workspace/TrkFilters/src/MultiHelixFilter_module.cc:172** - Variable _minHitRatio declared but possibly unused
- **/workspace/TrkFilters/src/MultiHelixFilter_module.cc:173** - Variable _maxChi2XY declared but possibly unused
- **/workspace/TrkFilters/src/MultiHelixFilter_module.cc:174** - Variable _maxChi2PhiZ declared but possibly unused
- **/workspace/TrkFilters/src/MultiHelixFilter_module.cc:175** - Variable _minD0 declared but possibly unused
- **/workspace/TrkFilters/src/MultiHelixFilter_module.cc:176** - Variable _maxD0 declared but possibly unused
- ... and 7 more


### TrkHitReco

Found 501 potential bugs:

#### array_bounds (235 occurrences)

- **/workspace/TrkHitReco/src/FlagBkgHits_module.cc:166** - Array access chcol[ich] without bounds check
- **/workspace/TrkHitReco/src/FlagBkgHits_module.cc:168** - Array access bkgccol[icl] without bounds check
- **/workspace/TrkHitReco/src/FlagBkgHits_module.cc:182** - Array access chfcol[ich] without bounds check
- **/workspace/TrkHitReco/src/FlagBkgHits_module.cc:185** - Array access chcol[ich] without bounds check
- **/workspace/TrkHitReco/src/FlagBkgHits_module.cc:198** - Array access chfcol[ich] without bounds check
- **/workspace/TrkHitReco/src/FlagBkgHits_module.cc:203** - Array access chcol_p[ishi] without bounds check
- **/workspace/TrkHitReco/src/FlagBkgHits_module.cc:240** - Array access chfcol[chit] without bounds check
- **/workspace/TrkHitReco/src/FlagBkgHits_module.cc:250** - Array access bkgccol[icl] without bounds check
- **/workspace/TrkHitReco/src/StereoLine.cc:7** - Array access pars_[posx] without bounds check
- **/workspace/TrkHitReco/src/StereoLine.cc:11** - Array access pars_[dxdz] without bounds check
- ... and 225 more

#### assignment_in_condition (14 occurrences)

- **/workspace/TrkHitReco/src/MakeStereoHits_module.cc:359** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkHitReco/src/ComboPeakFitRoot.cc:102** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkHitReco/src/TNTClusterer.cc:167** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkHitReco/src/TNTClusterer.cc:168** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkHitReco/src/TNTClusterer.cc:170** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkHitReco/src/TNTClusterer.cc:176** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkHitReco/src/PeakFitFunction.cc:162** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkHitReco/src/StrawHitRecoUtils.cc:29** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkHitReco/src/CombineStereoPoints.cc:39** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkHitReco/src/CombineStereoPoints.cc:56** - Possible assignment (=) instead of comparison (==) in condition
- ... and 4 more

#### division_by_zero (213 occurrences)

- **/workspace/TrkHitReco/src/FlagBkgHits_module.cc:1** - Potential division by zero: Framework not checked
- **/workspace/TrkHitReco/src/FlagBkgHits_module.cc:2** - Potential division by zero: Framework not checked
- **/workspace/TrkHitReco/src/FlagBkgHits_module.cc:3** - Potential division by zero: Framework not checked
- **/workspace/TrkHitReco/src/FlagBkgHits_module.cc:4** - Potential division by zero: TFileService not checked
- **/workspace/TrkHitReco/src/FlagBkgHits_module.cc:5** - Potential division by zero: Utilities not checked
- **/workspace/TrkHitReco/src/FlagBkgHits_module.cc:6** - Potential division by zero: types not checked
- **/workspace/TrkHitReco/src/FlagBkgHits_module.cc:7** - Potential division by zero: types not checked
- **/workspace/TrkHitReco/src/FlagBkgHits_module.cc:8** - Potential division by zero: types not checked
- **/workspace/TrkHitReco/src/FlagBkgHits_module.cc:10** - Potential division by zero: ConditionsService not checked
- **/workspace/TrkHitReco/src/FlagBkgHits_module.cc:11** - Potential division by zero: ConfigTools not checked
- ... and 203 more

#### memory_leak (14 occurrences)

- **/workspace/TrkHitReco/src/MakeStereoHits_module.cc:162** - Potential memory leak: new hit without corresponding delete
- **/workspace/TrkHitReco/src/ProtonBunchTimeFromStrawDigis_module.cc:89** - Potential memory leak: new ProtonBunchTime without corresponding delete
- **/workspace/TrkHitReco/src/Chi2Clusterer.cc:118** - Potential memory leak: new cluster without corresponding delete
- **/workspace/TrkHitReco/src/Chi2Clusterer.cc:118** - Potential memory leak: new hits without corresponding delete
- **/workspace/TrkHitReco/src/Chi2Clusterer.cc:118** - Potential memory leak: new hit without corresponding delete
- **/workspace/TrkHitReco/src/Chi2Clusterer.cc:119** - Potential memory leak: new cluster without corresponding delete
- **/workspace/TrkHitReco/src/Chi2Clusterer.cc:152** - Potential memory leak: new cluster without corresponding delete
- **/workspace/TrkHitReco/src/StrawHitReco_module.cc:193** - Potential memory leak: new StrawHitCollection without corresponding delete
- **/workspace/TrkHitReco/src/StrawHitReco_module.cc:196** - Potential memory leak: new ComboHitCollection without corresponding delete
- **/workspace/TrkHitReco/src/StrawHitReco_module.cc:197** - Potential memory leak: new IntensityInfoTrackerHits without corresponding delete
- ... and 4 more

#### missing_error_handling (11 occurrences)

- **/workspace/TrkHitReco/src/FlagBkgHits_module.cc:143** - getHandle/getValidHandle result not checked for validity
- **/workspace/TrkHitReco/src/MakeStereoHits_module.cc:133** - getHandle/getValidHandle result not checked for validity
- **/workspace/TrkHitReco/src/ProtonBunchTimeFromStrawDigis_module.cc:87** - getHandle/getValidHandle result not checked for validity
- **/workspace/TrkHitReco/src/CombineStrawHits_module.cc:124** - getHandle/getValidHandle result not checked for validity
- **/workspace/TrkHitReco/src/CombineStrawHits_module.cc:126** - getHandle/getValidHandle result not checked for validity
- **/workspace/TrkHitReco/src/StrawHitReco_module.cc:170** - getHandle/getValidHandle result not checked for validity
- **/workspace/TrkHitReco/src/StrawHitReco_module.cc:175** - getHandle/getValidHandle result not checked for validity
- **/workspace/TrkHitReco/src/StrawHitReco_module.cc:181** - getHandle/getValidHandle result not checked for validity
- **/workspace/TrkHitReco/src/StrawHitReco_module.cc:185** - getHandle/getValidHandle result not checked for validity
- **/workspace/TrkHitReco/src/StrawHitReco_module.cc:188** - getHandle/getValidHandle result not checked for validity
- ... and 1 more

#### missing_return (2 occurrences)

- **/workspace/TrkHitReco/src/Chi2Clusterer.cc:155** - Function may be missing return statement
- **/workspace/TrkHitReco/src/TNTClusterer.cc:154** - Function may be missing return statement

#### uninitialized_variable (8 occurrences)

- **/workspace/TrkHitReco/src/FlagBkgHits_module.cc:58** - Variable filter_ may be used uninitialized
- **/workspace/TrkHitReco/src/FlagBkgHits_module.cc:59** - Variable savebkg_ may be used uninitialized
- **/workspace/TrkHitReco/src/FlagBkgHits_module.cc:65** - Variable kerasQ_ may be used uninitialized
- **/workspace/TrkHitReco/src/FlagBkgHits_module.cc:66** - Variable iev_ may be used uninitialized
- **/workspace/TrkHitReco/src/MakeStereoHits_module.cc:176** - Variable dt may be used uninitialized
- **/workspace/TrkHitReco/src/StereoLineTest_main.cc:36** - Variable opt may be used uninitialized
- **/workspace/TrkHitReco/src/StrawHitRecoUtils.cc:143** - Variable halfpv may be used uninitialized
- **/workspace/TrkHitReco/src/CombineStereoPoints.cc:125** - Variable inv may be used uninitialized

#### unused_variable (3 occurrences)

- **/workspace/TrkHitReco/src/StereoLineTest_main.cc:85** - Variable ievt declared but possibly unused
- **/workspace/TrkHitReco/src/TNTClusterer.cc:251** - Variable tdist declared but possibly unused
- **/workspace/TrkHitReco/src/TNTClusterer.cc:293** - Variable i declared but possibly unused

#### use_after_free (1 occurrences)

- **/workspace/TrkHitReco/src/PeakFitFunction.cc:13** - Potential use after free: _tf1 deleted but may be used later


### TrkPatRec

Found 987 potential bugs:

#### array_bounds (462 occurrences)

- **/workspace/TrkPatRec/src/TimeAndPhiClusterFinderDiag_tool.cc:79** - Array access chSel[Nch] without bounds check
- **/workspace/TrkPatRec/src/TimeAndPhiClusterFinderDiag_tool.cc:80** - Array access chNhit[Nch] without bounds check
- **/workspace/TrkPatRec/src/TimeAndPhiClusterFinderDiag_tool.cc:81** - Array access chPdg[Nch] without bounds check
- **/workspace/TrkPatRec/src/TimeAndPhiClusterFinderDiag_tool.cc:82** - Array access chCrCode[Nch] without bounds check
- **/workspace/TrkPatRec/src/TimeAndPhiClusterFinderDiag_tool.cc:83** - Array access chSimId[Nch] without bounds check
- **/workspace/TrkPatRec/src/TimeAndPhiClusterFinderDiag_tool.cc:84** - Array access chTime[Nch] without bounds check
- **/workspace/TrkPatRec/src/TimeAndPhiClusterFinderDiag_tool.cc:85** - Array access chPhi[Nch] without bounds check
- **/workspace/TrkPatRec/src/TimeAndPhiClusterFinderDiag_tool.cc:86** - Array access chRad[Nch] without bounds check
- **/workspace/TrkPatRec/src/TimeAndPhiClusterFinderDiag_tool.cc:87** - Array access chX[Nch] without bounds check
- **/workspace/TrkPatRec/src/TimeAndPhiClusterFinderDiag_tool.cc:88** - Array access chY[Nch] without bounds check
- ... and 452 more

#### assignment_in_condition (38 occurrences)

- **/workspace/TrkPatRec/src/TimeClusterFinder_module.cc:327** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkPatRec/src/TimeClusterFinder_module.cc:431** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkPatRec/src/RobustHelixFinder_module.cc:297** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkPatRec/src/RobustHelixFinder_module.cc:443** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkPatRec/src/RobustHelixFinder_module.cc:704** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkPatRec/src/RobustHelixFinder_module.cc:719** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkPatRec/src/RobustHelixFinder_module.cc:1043** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkPatRec/src/KalFinalFit_module.cc:165** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkPatRec/src/KalFinalFit_module.cc:228** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkPatRec/src/KalFinalFit_module.cc:232** - Possible assignment (=) instead of comparison (==) in condition
- ... and 28 more

#### division_by_zero (427 occurrences)

- **/workspace/TrkPatRec/src/TimeAndPhiClusterFinderDiag_tool.cc:4** - Potential division by zero: Utilities not checked
- **/workspace/TrkPatRec/src/TimeAndPhiClusterFinderDiag_tool.cc:5** - Potential division by zero: Utilities not checked
- **/workspace/TrkPatRec/src/TimeAndPhiClusterFinderDiag_tool.cc:6** - Potential division by zero: ParameterSet not checked
- **/workspace/TrkPatRec/src/TimeAndPhiClusterFinderDiag_tool.cc:8** - Potential division by zero: MCDataProducts not checked
- **/workspace/TrkPatRec/src/TimeAndPhiClusterFinderDiag_tool.cc:9** - Potential division by zero: MCDataProducts not checked
- **/workspace/TrkPatRec/src/TimeAndPhiClusterFinderDiag_tool.cc:10** - Potential division by zero: Mu2eUtilities not checked
- **/workspace/TrkPatRec/src/TimeAndPhiClusterFinderDiag_tool.cc:11** - Potential division by zero: TrkPatRec not checked
- **/workspace/TrkPatRec/src/TimeAndPhiClusterFinderDiag_tool.cc:12** - Potential division by zero: RecoDataProducts not checked
- **/workspace/TrkPatRec/src/TimeAndPhiClusterFinderDiag_tool.cc:17** - Potential division by zero: Framework not checked
- **/workspace/TrkPatRec/src/TimeAndPhiClusterFinderDiag_tool.cc:18** - Potential division by zero: ParameterSet not checked
- ... and 417 more

#### memory_leak (22 occurrences)

- **/workspace/TrkPatRec/src/TimeClusterFinder_module.cc:226** - Potential memory leak: new TimeClusterCollection without corresponding delete
- **/workspace/TrkPatRec/src/RobustHelixFinder_module.cc:351** - Potential memory leak: new HelixSeedCollection without corresponding delete
- **/workspace/TrkPatRec/src/RobustHelixFinder_module.cc:356** - Potential memory leak: new HelixSeedCollection without corresponding delete
- **/workspace/TrkPatRec/src/KalFinalFit_module.cc:168** - Potential memory leak: new DoubletAmbigResolver without corresponding delete
- **/workspace/TrkPatRec/src/KalFinalFit_module.cc:169** - Potential memory leak: new std without corresponding delete
- **/workspace/TrkPatRec/src/KalFinalFit_module.cc:215** - Potential memory leak: new KalRepCollection without corresponding delete
- **/workspace/TrkPatRec/src/KalFinalFit_module.cc:216** - Potential memory leak: new KalRepPtrCollection without corresponding delete
- **/workspace/TrkPatRec/src/KalFinalFit_module.cc:217** - Potential memory leak: new KalSeedCollection without corresponding delete
- **/workspace/TrkPatRec/src/KalFinalFit_module.cc:218** - Potential memory leak: new KalHelixAssns without corresponding delete
- **/workspace/TrkPatRec/src/KalFinalFit_module.cc:219** - Potential memory leak: new StrawHitFlagCollection without corresponding delete
- ... and 12 more

#### missing_error_handling (17 occurrences)

- **/workspace/TrkPatRec/src/TimeAndPhiClusterFinderDiag_tool.cc:109** - getHandle/getValidHandle result not checked for validity
- **/workspace/TrkPatRec/src/TimeClusterFinder_module.cc:217** - getHandle/getValidHandle result not checked for validity
- **/workspace/TrkPatRec/src/TimeClusterFinder_module.cc:222** - getHandle/getValidHandle result not checked for validity
- **/workspace/TrkPatRec/src/RobustHelixFinder_module.cc:339** - getHandle/getValidHandle result not checked for validity
- **/workspace/TrkPatRec/src/RobustHelixFinder_module.cc:342** - getHandle/getValidHandle result not checked for validity
- **/workspace/TrkPatRec/src/KalFinalFit_module.cc:213** - getHandle/getValidHandle result not checked for validity
- **/workspace/TrkPatRec/src/KalFinalFit_module.cc:455** - getHandle/getValidHandle result not checked for validity
- **/workspace/TrkPatRec/src/KalFinalFit_module.cc:457** - getHandle/getValidHandle result not checked for validity
- **/workspace/TrkPatRec/src/KalFinalFit_module.cc:470** - getHandle/getValidHandle result not checked for validity
- **/workspace/TrkPatRec/src/TimeAndPhiClusterFinder_module.cc:201** - getHandle/getValidHandle result not checked for validity
- ... and 7 more

#### missing_return (4 occurrences)

- **/workspace/TrkPatRec/src/RobustHelixFinder_module.cc:450** - Function may be missing return statement
- **/workspace/TrkPatRec/src/KalFinalFit_module.cc:331** - Function may be missing return statement
- **/workspace/TrkPatRec/src/RobustMultiHelixFinder_module.cc:53** - Function may be missing return statement
- **/workspace/TrkPatRec/src/RobustMultiHelixFinder_module.cc:477** - Function may be missing return statement

#### uninitialized_variable (12 occurrences)

- **/workspace/TrkPatRec/src/TimeAndPhiClusterFinderDiag_tool.cc:47** - Variable treeInit_ may be used uninitialized
- **/workspace/TrkPatRec/src/TimeAndPhiClusterFinderDiag_tool.cc:50** - Variable mcdiag_ may be used uninitialized
- **/workspace/TrkPatRec/src/KalFinalFit_module.cc:577** - Variable rdrift may be used uninitialized
- **/workspace/TrkPatRec/src/RobustMultiHelixFinderDiag_tool.cc:47** - Variable treeInit_ may be used uninitialized
- **/workspace/TrkPatRec/src/RobustMultiHelixFinderDiag_tool.cc:50** - Variable mcdiag_ may be used uninitialized
- **/workspace/TrkPatRec/src/KalFinalFitDiag_tool.cc:77** - Variable doca may be used uninitialized
- **/workspace/TrkPatRec/src/KalFinalFitDiag_tool.cc:80** - Variable dtCls may be used uninitialized
- **/workspace/TrkPatRec/src/KalSeedFit_module.cc:373** - Variable locflt may be used uninitialized
- **/workspace/TrkPatRec/src/KalSeedFitDiag_tool.cc:32** - Variable nactive may be used uninitialized
- **/workspace/TrkPatRec/src/KalSeedFitDiag_tool.cc:33** - Variable ndeactivated may be used uninitialized
- ... and 2 more

#### unused_variable (3 occurrences)

- **/workspace/TrkPatRec/src/RobustHelixFinder_module.cc:832** - Variable nTotalStations declared but possibly unused
- **/workspace/TrkPatRec/src/RobustHelixFinder_module.cc:882** - Variable panelId declared but possibly unused
- **/workspace/TrkPatRec/src/RobustMultiHelixFinder_module.cc:808** - Variable iter declared but possibly unused

#### use_after_free (2 occurrences)

- **/workspace/TrkPatRec/src/KalFinalFit_module.cc:183** - Potential use after free: _data deleted but may be used later
- **/workspace/TrkPatRec/src/KalFinalFit_module.cc:184** - Potential use after free: _data deleted but may be used later


### TrkReco

Found 913 potential bugs:

#### array_bounds (352 occurrences)

- **/workspace/TrkReco/src/TrkPrintUtils.cc:64** - Array access Message[0] without bounds check
- **/workspace/TrkReco/src/TrkPrintUtils.cc:89** - Array access momvec[i] without bounds check
- **/workspace/TrkReco/src/PanelAmbigStructs.cc:75** - Array access _state[ihit] without bounds check
- **/workspace/TrkReco/src/PanelAmbigStructs.cc:76** - Array access _state[jhit] without bounds check
- **/workspace/TrkReco/src/PanelAmbigStructs.cc:122** - Array access pstate[ihit] without bounds check
- **/workspace/TrkReco/src/KalFit.cc:145** - Array access _maxpardif[0] without bounds check
- **/workspace/TrkReco/src/KalFit.cc:179** - Array access _ambigstrategy[iter] without bounds check
- **/workspace/TrkReco/src/KalFit.cc:181** - Array access _herr[iter] without bounds check
- **/workspace/TrkReco/src/KalFit.cc:184** - Array access _herr[iter] without bounds check
- **/workspace/TrkReco/src/KalFit.cc:187** - Array access _herr[iter] without bounds check
- ... and 342 more

#### assignment_in_condition (52 occurrences)

- **/workspace/TrkReco/src/TrkPrintUtils.cc:34** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkReco/src/TrkPrintUtils.cc:64** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkReco/src/TrkPrintUtils.cc:174** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkReco/src/TrkPrintUtils.cc:256** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkReco/src/PanelAmbigStructs.cc:45** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkReco/src/KalFitData.cc:49** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkReco/src/AmbigResolver.cc:52** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkReco/src/HitAmbigResolver.cc:45** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkReco/src/KalFit.cc:195** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/TrkReco/src/KalFit.cc:273** - Possible assignment (=) instead of comparison (==) in condition
- ... and 42 more

#### division_by_zero (415 occurrences)

- **/workspace/TrkReco/src/TrkPrintUtils.cc:4** - Potential division by zero: Mu2eUtilities not checked
- **/workspace/TrkReco/src/TrkPrintUtils.cc:5** - Potential division by zero: TrkReco not checked
- **/workspace/TrkReco/src/TrkPrintUtils.cc:6** - Potential division by zero: RecoDataProducts not checked
- **/workspace/TrkReco/src/TrkPrintUtils.cc:8** - Potential division by zero: BTrkData not checked
- **/workspace/TrkReco/src/TrkPrintUtils.cc:9** - Potential division by zero: BTrkData not checked
- **/workspace/TrkReco/src/TrkPrintUtils.cc:11** - Potential division by zero: KalmanTrack not checked
- **/workspace/TrkReco/src/TrkPrintUtils.cc:12** - Potential division by zero: TrkBase not checked
- **/workspace/TrkReco/src/TrkPrintUtils.cc:13** - Potential division by zero: TrkBase not checked
- **/workspace/TrkReco/src/TrkPrintUtils.cc:14** - Potential division by zero: ProbTools not checked
- **/workspace/TrkReco/src/TrkPrintUtils.cc:15** - Potential division by zero: BbrGeom not checked
- ... and 405 more

#### memory_leak (29 occurrences)

- **/workspace/TrkReco/src/KalFitData.cc:30** - Potential memory leak: new vector without corresponding delete
- **/workspace/TrkReco/src/HitAmbigResolver.cc:59** - Potential memory leak: new ambig without corresponding delete
- **/workspace/TrkReco/src/KalFit.cc:149** - Potential memory leak: new TrkPrintUtils without corresponding delete
- **/workspace/TrkReco/src/KalFit.cc:181** - Potential memory leak: new FixedAmbigResolver without corresponding delete
- **/workspace/TrkReco/src/KalFit.cc:184** - Potential memory leak: new HitAmbigResolver without corresponding delete
- **/workspace/TrkReco/src/KalFit.cc:187** - Potential memory leak: new PanelAmbig without corresponding delete
- **/workspace/TrkReco/src/KalFit.cc:190** - Potential memory leak: new DoubletAmbigResolver without corresponding delete
- **/workspace/TrkReco/src/KalFit.cc:278** - Potential memory leak: new KalRep without corresponding delete
- **/workspace/TrkReco/src/KalFit.cc:334** - Potential memory leak: new TrkStrawHit without corresponding delete
- **/workspace/TrkReco/src/KalFit.cc:492** - Potential memory leak: new TrkStrawHit without corresponding delete
- ... and 19 more

#### missing_error_handling (5 occurrences)

- **/workspace/TrkReco/src/TrkPrintUtils.cc:168** - getHandle/getValidHandle result not checked for validity
- **/workspace/TrkReco/src/MergeHelices_module.cc:93** - getHandle/getValidHandle result not checked for validity
- **/workspace/TrkReco/src/SelectSameTrack_module.cc:93** - getHandle/getValidHandle result not checked for validity
- **/workspace/TrkReco/src/TrkRecoMcUtils_tool.cc:203** - getHandle/getValidHandle result not checked for validity
- **/workspace/TrkReco/src/SelectReflections_module.cc:75** - getHandle/getValidHandle result not checked for validity

#### missing_return (16 occurrences)

- **/workspace/TrkReco/src/MergeHelices_module.cc:109** - Function may be missing return statement
- **/workspace/TrkReco/src/TrkUtilities.cc:367** - Function may be missing return statement
- **/workspace/TrkReco/src/RobustHelixFit.cc:341** - Function may be missing return statement
- **/workspace/TrkReco/src/RobustHelixFit.cc:538** - Function may be missing return statement
- **/workspace/TrkReco/src/RobustHelixFit.cc:999** - Function may be missing return statement
- **/workspace/TrkReco/src/RobustHelixFit.cc:1322** - Function may be missing return statement
- **/workspace/TrkReco/src/PanelAmbigResolver.cc:265** - Function may be missing return statement
- **/workspace/TrkReco/src/SelectSameTrack_module.cc:171** - Function may be missing return statement
- **/workspace/TrkReco/src/SelectSameTrack_module.cc:174** - Function may be missing return statement
- **/workspace/TrkReco/src/SelectSameTrack_module.cc:177** - Function may be missing return statement
- ... and 6 more

#### uninitialized_variable (30 occurrences)

- **/workspace/TrkReco/src/TrkPrintUtils.cc:163** - Variable ihit may be used uninitialized
- **/workspace/TrkReco/src/AmbigResolver.cc:63** - Variable locdist may be used uninitialized
- **/workspace/TrkReco/src/KalFit.cc:75** - Variable _flt may be used uninitialized
- **/workspace/TrkReco/src/KalFit.cc:83** - Variable _maxdiff may be used uninitialized
- **/workspace/TrkReco/src/KalFit.cc:340** - Variable iambig may be used uninitialized
- **/workspace/TrkReco/src/MergeHelices_module.cc:49** - Variable _debug may be used uninitialized
- **/workspace/TrkReco/src/MergeHelices_module.cc:50** - Variable _deltanh may be used uninitialized
- **/workspace/TrkReco/src/MergeHelices_module.cc:52** - Variable _minnover may be used uninitialized
- **/workspace/TrkReco/src/MergeHelices_module.cc:53** - Variable _minoverfrac may be used uninitialized
- **/workspace/TrkReco/src/TrkUtilities.cc:289** - Variable loclen may be used uninitialized
- ... and 20 more

#### unused_variable (11 occurrences)

- **/workspace/TrkReco/src/KalFit.cc:947** - Variable worst declared but possibly unused
- **/workspace/TrkReco/src/PanelAmbigResolver.cc:307** - Variable g11 declared but possibly unused
- **/workspace/TrkReco/src/PanelAmbigResolver.cc:308** - Variable g22 declared but possibly unused
- **/workspace/TrkReco/src/PanelAmbigResolver.cc:309** - Variable g12 declared but possibly unused
- **/workspace/TrkReco/src/PanelAmbigResolver.cc:310** - Variable g21 declared but possibly unused
- **/workspace/TrkReco/src/PanelAmbigResolver.cc:311** - Variable b1 declared but possibly unused
- **/workspace/TrkReco/src/PanelAmbigResolver.cc:312** - Variable b2 declared but possibly unused
- **/workspace/TrkReco/src/PanelAmbigResolver.cc:313** - Variable d1 declared but possibly unused
- **/workspace/TrkReco/src/PanelAmbigResolver.cc:314** - Variable d2 declared but possibly unused
- **/workspace/TrkReco/src/PanelAmbigResolver.cc:316** - Variable test declared but possibly unused
- ... and 1 more

#### use_after_free (3 occurrences)

- **/workspace/TrkReco/src/KalFitData.cc:35** - Potential use after free: helixTraj deleted but may be used later
- **/workspace/TrkReco/src/KalFitData.cc:42** - Potential use after free: krep deleted but may be used later
- **/workspace/TrkReco/src/KalFitData.cc:50** - Potential use after free: krep deleted but may be used later


### UtilityModules

Found 55 potential bugs:

#### array_bounds (1 occurrences)

- **/workspace/UtilityModules/src/StopSelection_module.cc:241** - Array access selected[index] without bounds check

#### assignment_in_condition (1 occurrences)

- **/workspace/UtilityModules/src/ReadTrackSPM_module.cc:43** - Possible assignment (=) instead of comparison (==) in condition

#### division_by_zero (42 occurrences)

- **/workspace/UtilityModules/src/ModifyTrackSPM_module.cc:7** - Potential division by zero: Framework not checked
- **/workspace/UtilityModules/src/ModifyTrackSPM_module.cc:8** - Potential division by zero: Framework not checked
- **/workspace/UtilityModules/src/ModifyTrackSPM_module.cc:9** - Potential division by zero: Utilities not checked
- **/workspace/UtilityModules/src/ModifyTrackSPM_module.cc:11** - Potential division by zero: MCDataProducts not checked
- **/workspace/UtilityModules/src/NullProducer_module.cc:13** - Potential division by zero: SeedService not checked
- **/workspace/UtilityModules/src/NullProducer_module.cc:15** - Potential division by zero: Framework not checked
- **/workspace/UtilityModules/src/NullProducer_module.cc:16** - Potential division by zero: Framework not checked
- **/workspace/UtilityModules/src/NullProducer_module.cc:17** - Potential division by zero: Utilities not checked
- **/workspace/UtilityModules/src/NullProducer_module.cc:19** - Potential division by zero: Random not checked
- **/workspace/UtilityModules/src/RecoNullProducer_module.cc:11** - Potential division by zero: Framework not checked
- ... and 32 more

#### memory_leak (4 occurrences)

- **/workspace/UtilityModules/src/StopSelection_module.cc:222** - Potential memory leak: new sim without corresponding delete
- **/workspace/UtilityModules/src/StopSelection_module.cc:283** - Potential memory leak: new EventWeight without corresponding delete
- **/workspace/UtilityModules/src/StopSelection_module.cc:298** - Potential memory leak: new SumOfWeights without corresponding delete
- **/workspace/UtilityModules/src/StopSelection_module.cc:299** - Potential memory leak: new SumOfWeights without corresponding delete

#### missing_error_handling (3 occurrences)

- **/workspace/UtilityModules/src/ModifyTrackSPM_module.cc:41** - getHandle/getValidHandle result not checked for validity
- **/workspace/UtilityModules/src/StopSelection_module.cc:227** - getHandle/getValidHandle result not checked for validity
- **/workspace/UtilityModules/src/StopSelection_module.cc:228** - getHandle/getValidHandle result not checked for validity

#### uninitialized_variable (3 occurrences)

- **/workspace/UtilityModules/src/StopSelection_module.cc:104** - Variable acceptReject_ may be used uninitialized
- **/workspace/UtilityModules/src/StopSelection_module.cc:105** - Variable diagLevel_ may be used uninitialized
- **/workspace/UtilityModules/src/StopSelection_module.cc:110** - Variable nempty_ may be used uninitialized

#### unused_variable (1 occurrences)

- **/workspace/UtilityModules/src/NullProducer_module.cc:55** - Variable i declared but possibly unused


### Validation

Found 153 potential bugs:

#### array_bounds (12 occurrences)

- **/workspace/Validation/src/ValKalSeed.cc:15** - Array access _vdmap[VirtualDetectorId(VirtualDetectorId::TT_FrontHollow)] without bounds check
- **/workspace/Validation/src/ValKalSeed.cc:16** - Array access _vdmap[VirtualDetectorId(VirtualDetectorId::TT_Mid)] without bounds check
- **/workspace/Validation/src/ValKalSeed.cc:17** - Array access _vdmap[VirtualDetectorId(VirtualDetectorId::TT_MidInner)] without bounds check
- **/workspace/Validation/src/ValKalSeed.cc:18** - Array access _vdmap[VirtualDetectorId(VirtualDetectorId::TT_Back)] without bounds check
- **/workspace/Validation/src/ValKalSeed.cc:19** - Array access _vdmap[VirtualDetectorId(VirtualDetectorId::TT_OutSurf)] without bounds check
- **/workspace/Validation/src/ValKalSeed.cc:20** - Array access _vdmap[VirtualDetectorId(VirtualDetectorId::TT_InSurf)] without bounds check
- **/workspace/Validation/src/ValKalSeed.cc:143** - Array access _vdmap[vdid] without bounds check
- **/workspace/Validation/src/ValKalSeed.cc:244** - Array access ppv[0] without bounds check
- **/workspace/Validation/src/ValSTMWaveformDigi.cc:27** - Array access adcs[0] without bounds check
- **/workspace/Validation/src/valCompare_main.cc:191** - Array access argv[optind] without bounds check
- ... and 2 more

#### assignment_in_condition (3 occurrences)

- **/workspace/Validation/src/ValTrackSummary.cc:171** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Validation/src/ValTrackSummary.cc:212** - Possible assignment (=) instead of comparison (==) in condition
- **/workspace/Validation/src/valCompare_main.cc:178** - Possible assignment (=) instead of comparison (==) in condition

#### division_by_zero (122 occurrences)

- **/workspace/Validation/src/ValCaloHit.cc:2** - Potential division by zero: Validation not checked
- **/workspace/Validation/src/ValBkgCluster.cc:2** - Potential division by zero: Validation not checked
- **/workspace/Validation/src/ValHelixSeed.cc:1** - Potential division by zero: Validation not checked
- **/workspace/Validation/src/ValHelixSeed.cc:2** - Potential division by zero: GeometryService not checked
- **/workspace/Validation/src/ValHelixSeed.cc:3** - Potential division by zero: Mu2eUtilities not checked
- **/workspace/Validation/src/ValHelixSeed.cc:4** - Potential division by zero: TrackerGeom not checked
- **/workspace/Validation/src/ValKalSeed.cc:1** - Potential division by zero: Validation not checked
- **/workspace/Validation/src/ValKalSeed.cc:2** - Potential division by zero: MCDataProducts not checked
- **/workspace/Validation/src/ValKalSeed.cc:3** - Potential division by zero: MCDataProducts not checked
- **/workspace/Validation/src/ValKalSeed.cc:4** - Potential division by zero: MCDataProducts not checked
- ... and 112 more

#### memory_leak (1 occurrences)

- **/workspace/Validation/src/Validation_module.cc:213** - Potential memory leak: new set without corresponding delete

#### missing_return (11 occurrences)

- **/workspace/Validation/src/ValId.cc:29** - Function may be missing return statement
- **/workspace/Validation/src/ValId.cc:31** - Function may be missing return statement
- **/workspace/Validation/src/ValId.cc:33** - Function may be missing return statement
- **/workspace/Validation/src/ValId.cc:35** - Function may be missing return statement
- **/workspace/Validation/src/ValId.cc:37** - Function may be missing return statement
- **/workspace/Validation/src/ValId.cc:39** - Function may be missing return statement
- **/workspace/Validation/src/ValId.cc:41** - Function may be missing return statement
- **/workspace/Validation/src/ValId.cc:43** - Function may be missing return statement
- **/workspace/Validation/src/ValId.cc:45** - Function may be missing return statement
- **/workspace/Validation/src/ValId.cc:50** - Function may be missing return statement
- ... and 1 more

#### uninitialized_variable (3 occurrences)

- **/workspace/Validation/src/ValKalSeed.cc:130** - Variable t0 may be used uninitialized
- **/workspace/Validation/src/ValStatusG4.cc:29** - Variable logx may be used uninitialized
- **/workspace/Validation/src/valCompare_main.cc:97** - Variable c may be used uninitialized

#### unused_variable (1 occurrences)

- **/workspace/Validation/src/ValId.cc:18** - Variable jj declared but possibly unused


