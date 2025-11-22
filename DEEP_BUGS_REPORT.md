# Deep Bug Analysis Report

Total bugs found: 5404

## Summary by Type

- **art_api_misuse**: 62 occurrences
- **buffer_overflow**: 63 occurrences
- **infinite_loop**: 4 occurrences
- **iterator_invalidation**: 478 occurrences
- **logic_error**: 9 occurrences
- **pointer_arithmetic**: 795 occurrences
- **resource_leak**: 42 occurrences
- **stl_container_misuse**: 175 occurrences
- **string_handling**: 311 occurrences
- **type_mismatch**: 6 occurrences
- **undefined_behavior**: 3459 occurrences

## Detailed Findings

### art_api_misuse (62 occurrences)

**/workspace/CalPatRec/src/ComboHitFilter_module.cc:107**
- Severity: high
- Code: `produces<ComboHitCollection>();`
- Description: produces() declared but no corresponding event.put() found

**/workspace/CalPatRec/src/ComboHitFilter_module.cc:108**
- Severity: high
- Code: `produces<StrawHitFlagCollection>();`
- Description: produces() declared but no corresponding event.put() found

**/workspace/CalPatRec/src/MergeHelixFinder_module.cc:101**
- Severity: high
- Code: `produces<AlgorithmIDCollection>  ();`
- Description: produces() declared but no corresponding event.put() found

**/workspace/CalPatRec/src/MergeHelixFinder_module.cc:102**
- Severity: high
- Code: `produces<HelixSeedCollection>    ();`
- Description: produces() declared but no corresponding event.put() found

**/workspace/CalPatRec/src/DeltaFinder_module.cc:151**
- Severity: high
- Code: `produces<IntensityInfoTimeCluster>();`
- Description: produces() declared but no corresponding event.put() found

**/workspace/CalPatRec/src/DeltaFinder_module.cc:153**
- Severity: high
- Code: `produces<ComboHitCollection>("");`
- Description: produces() declared but no corresponding event.put() found

**/workspace/CalPatRec/src/DeltaFinder_module.cc:154**
- Severity: high
- Code: `if (_writeStrawHits         == 1) produces<ComboHitCollection>("StrawHits");`
- Description: produces() declared but no corresponding event.put() found

**/workspace/CalPatRec/src/DeltaFinder_module.cc:157**
- Severity: high
- Code: `produces<TimeClusterCollection>();`
- Description: produces() declared but no corresponding event.put() found

**/workspace/CaloCluster/src/CaloProtoClusterMaker_module.cc:92**
- Severity: high
- Code: `art::Handle<CaloHitCollection> CaloHitsHandle = event.getHandle<CaloHitCollection>(caloCrystalToken_);`
- Description: getHandle() result not checked with isValid() - may dereference invalid handle

**/workspace/CaloCluster/src/CaloClusterFast_module.cc:78**
- Severity: high
- Code: `art::Handle<CaloHitCollection> caloHitsHandle = event.getHandle<CaloHitCollection>(caloHitToken_);`
- Description: getHandle() result not checked with isValid() - may dereference invalid handle

**/workspace/CaloFilters/src/FilterEcalNNTrigger_module.cc:70**
- Severity: high
- Code: `art::Handle<CaloClusterCollection> caloClustersHandle = event.getHandle<CaloClusterCollection>(caloClusterToken_);`
- Description: getHandle() result not checked with isValid() - may dereference invalid handle

**/workspace/CaloFilters/src/CaloCosmicCalib_module.cc:97**
- Severity: high
- Code: `produces<TriggerInfo>();`
- Description: produces() declared but no corresponding event.put() found

**/workspace/CommonMC/src/ProtonBunchTimeMCFromProtonBunchTime_module.cc:45**
- Severity: high
- Code: `auto pbt = event.getHandle<ProtonBunchTime>(pbttag_);`
- Description: getHandle() result not checked with isValid() - may dereference invalid handle

**/workspace/CosmicReco/src/CosmicSeedFilter_module.cc:68**
- Severity: high
- Code: `produces<TriggerInfo>();`
- Description: produces() declared but no corresponding event.put() found

**/workspace/DAQ/src/ArtBinaryPacketsFromDigis_module.cc:567**
- Severity: high
- Code: `produces<timestamp>();`
- Description: produces() declared but no corresponding event.put() found

**/workspace/EventGenerator/src/CRYEventGenerator_module.cc:52**
- Severity: high
- Code: `produces<GenParticleCollection>();`
- Description: produces() declared but no corresponding event.put() found

**/workspace/EventGenerator/src/CRYEventGenerator_module.cc:53**
- Severity: high
- Code: `produces<CosmicLivetime,art::InSubRun>();`
- Description: produces() declared but no corresponding event.put() found

**/workspace/EventGenerator/src/PionFilter_module.cc:72**
- Severity: high
- Code: `produces<SumOfWeights, art::InSubRun>("total");`
- Description: produces() declared but no corresponding event.put() found

**/workspace/EventGenerator/src/PionFilter_module.cc:73**
- Severity: high
- Code: `produces<SumOfWeights, art::InSubRun>("selected");`
- Description: produces() declared but no corresponding event.put() found

**/workspace/EventGenerator/src/EventGenerator_module.cc:120**
- Severity: high
- Code: `produces<GenParticleCollection>();`
- Description: produces() declared but no corresponding event.put() found

**/workspace/EventGenerator/src/EventGenerator_module.cc:122**
- Severity: high
- Code: `produces<G4BeamlineInfoCollection>();`
- Description: produces() declared but no corresponding event.put() found

**/workspace/EventGenerator/src/G4BeamlineGenerator_module.cc:89**
- Severity: high
- Code: `produces<GenParticleCollection>();`
- Description: produces() declared but no corresponding event.put() found

**/workspace/EventGenerator/src/G4BeamlineGenerator_module.cc:90**
- Severity: high
- Code: `produces<G4BeamlineInfoCollection>();`
- Description: produces() declared but no corresponding event.put() found

**/workspace/EventGenerator/src/RanTest_module.cc:39**
- Severity: high
- Code: `produces<GenParticleCollection>();`
- Description: produces() declared but no corresponding event.put() found

**/workspace/EventGenerator/src/PrimaryProtonGun_module.cc:68**
- Severity: high
- Code: `produces<GenParticleCollection>();`
- Description: produces() declared but no corresponding event.put() found

**/workspace/EventGenerator/src/GenEventCounter_module.cc:41**
- Severity: high
- Code: `produces<mu2e::GenEventCount, art::InSubRun>();`
- Description: produces() declared but no corresponding event.put() found

**/workspace/EventGenerator/src/CORSIKAEventGenerator_module.cc:118**
- Severity: high
- Code: `produces<GenParticleCollection>();`
- Description: produces() declared but no corresponding event.put() found

**/workspace/EventGenerator/src/CORSIKAEventGenerator_module.cc:119**
- Severity: high
- Code: `produces<CosmicLivetime,art::InSubRun>();`
- Description: produces() declared but no corresponding event.put() found

**/workspace/EventMixing/src/Mu2eProductMixer.cc:136**
- Severity: high
- Code: `helper.produces<PhysicalVolumeInfoMultiCollection, art::InSubRun>(subrunVolInstanceName_);`
- Description: produces() declared but no corresponding event.put() found

**/workspace/EventMixing/src/Mu2eProductMixer.cc:155**
- Severity: high
- Code: `helper.produces<CosmicLivetime, art::InSubRun>(subrunLivetimeInstanceName_);`
- Description: produces() declared but no corresponding event.put() found

... and 32 more

### buffer_overflow (63 occurrences)

**/workspace/CalPatRec/src/AgnosticHelixFinderDiag_tool.cc:125**
- Severity: high
- Code: `sprintf(folder_name, "evt_%i", i);`
- Description: sprintf used - consider snprintf to prevent buffer overflow

**/workspace/CalPatRec/src/AgnosticHelixFinderDiag_tool.cc:138**
- Severity: high
- Code: `sprintf(folder_name, "tcl_%i", i);`
- Description: sprintf used - consider snprintf to prevent buffer overflow

**/workspace/CalPatRec/src/AgnosticHelixFinderDiag_tool.cc:152**
- Severity: high
- Code: `sprintf(folder_name, "hs_%i", i);`
- Description: sprintf used - consider snprintf to prevent buffer overflow

**/workspace/CalPatRec/src/AgnosticHelixFinderDiag_tool.cc:165**
- Severity: high
- Code: `sprintf(folder_name, "li_%i", i);`
- Description: sprintf used - consider snprintf to prevent buffer overflow

**/workspace/CalPatRec/src/AgnosticHelixFinderDiag_tool.cc:178**
- Severity: high
- Code: `sprintf(folder_name, "ls_%i", i);`
- Description: sprintf used - consider snprintf to prevent buffer overflow

**/workspace/CalPatRec/src/AgnosticHelixFinderDiag_tool.cc:194**
- Severity: high
- Code: `sprintf(folder_name, "tp_%i", i);`
- Description: sprintf used - consider snprintf to prevent buffer overflow

**/workspace/CalPatRec/src/MergePatRecDiag_tool.cc:137**
- Severity: high
- Code: `sprintf(folder_name,"evt_%i",i);`
- Description: sprintf used - consider snprintf to prevent buffer overflow

**/workspace/CalPatRec/src/MergePatRecDiag_tool.cc:154**
- Severity: high
- Code: `sprintf(folder_name,"tpr_%i",i);`
- Description: sprintf used - consider snprintf to prevent buffer overflow

**/workspace/CalPatRec/src/MergePatRecDiag_tool.cc:171**
- Severity: high
- Code: `sprintf(folder_name,"cpr_%i",i);`
- Description: sprintf used - consider snprintf to prevent buffer overflow

**/workspace/CalPatRec/src/CalTimePeakFinderDiag_tool.cc:160**
- Severity: high
- Code: `sprintf(folder_name,"evt_%i",i);`
- Description: sprintf used - consider snprintf to prevent buffer overflow

**/workspace/CalPatRec/src/CalTimePeakFinderDiag_tool.cc:178**
- Severity: high
- Code: `sprintf(folder_name,"cl_%i",i);`
- Description: sprintf used - consider snprintf to prevent buffer overflow

**/workspace/CalPatRec/src/CalTimePeakFinderDiag_tool.cc:196**
- Severity: high
- Code: `sprintf(folder_name,"tcl_%i",i);`
- Description: sprintf used - consider snprintf to prevent buffer overflow

**/workspace/CalPatRec/src/TZClusterFinderDiag_tool.cc:125**
- Severity: high
- Code: `sprintf(folder_name,"evt_%i",i);`
- Description: sprintf used - consider snprintf to prevent buffer overflow

**/workspace/CalPatRec/src/TZClusterFinderDiag_tool.cc:135**
- Severity: high
- Code: `sprintf(folder_name,"tcl_%i",i);`
- Description: sprintf used - consider snprintf to prevent buffer overflow

**/workspace/CalPatRec/src/DeltaFinderDiag_tool.cc:565**
- Severity: high
- Code: `sprintf(folder_name,"evt_%i",i);`
- Description: sprintf used - consider snprintf to prevent buffer overflow

**/workspace/CalPatRec/src/DeltaFinderDiag_tool.cc:610**
- Severity: high
- Code: `sprintf(folder_name,"seed_%i",i);`
- Description: sprintf used - consider snprintf to prevent buffer overflow

**/workspace/CalPatRec/src/DeltaFinderDiag_tool.cc:628**
- Severity: high
- Code: `sprintf(folder_name,"seed2_%i",i);`
- Description: sprintf used - consider snprintf to prevent buffer overflow

**/workspace/CalPatRec/src/DeltaFinderDiag_tool.cc:659**
- Severity: high
- Code: `sprintf(folder_name,"delta_%i",i);`
- Description: sprintf used - consider snprintf to prevent buffer overflow

**/workspace/CalPatRec/src/DeltaFinderDiag_tool.cc:689**
- Severity: high
- Code: `sprintf(folder_name,"mc_%i",i);`
- Description: sprintf used - consider snprintf to prevent buffer overflow

**/workspace/CalPatRec/src/DeltaFinderDiag_tool.cc:708**
- Severity: high
- Code: `sprintf(folder_name,"proton_%i",i);`
- Description: sprintf used - consider snprintf to prevent buffer overflow

**/workspace/CalPatRec/src/DeltaFinderAna_module.cc:425**
- Severity: high
- Code: `sprintf(folder_name,"evt_%i",i);`
- Description: sprintf used - consider snprintf to prevent buffer overflow

**/workspace/CalPatRec/src/DeltaFinderAna_module.cc:490**
- Severity: high
- Code: `sprintf(folder_name,"ch_%i",i);`
- Description: sprintf used - consider snprintf to prevent buffer overflow

**/workspace/CalPatRec/src/DeltaFinderAna_module.cc:535**
- Severity: high
- Code: `sprintf(folder_name,"sh_%i",i);`
- Description: sprintf used - consider snprintf to prevent buffer overflow

**/workspace/CalPatRec/src/DeltaFinderAna_module.cc:574**
- Severity: high
- Code: `sprintf(folder_name,"mc_%i",i);`
- Description: sprintf used - consider snprintf to prevent buffer overflow

**/workspace/EventDisplay/src/EventDisplay_module.cc:182**
- Severity: high
- Code: `sprintf(msg,"The end of file has been reached, but the event #%i has not been found.",eventToFind);`
- Description: sprintf used - consider snprintf to prevent buffer overflow

**/workspace/Lumi/src/NPOTAnalysis_module.cc:262**
- Severity: high
- Code: `sprintf(folder_name,"evt_%i",i);`
- Description: sprintf used - consider snprintf to prevent buffer overflow

**/workspace/ParticleID/src/ParticleID_module.cc:195**
- Severity: high
- Code: `sprintf(name,"htempe%d",i);`
- Description: sprintf used - consider snprintf to prevent buffer overflow

**/workspace/ParticleID/src/ParticleID_module.cc:201**
- Severity: high
- Code: `sprintf(name,"htempm%d",i);`
- Description: sprintf used - consider snprintf to prevent buffer overflow

**/workspace/TEveEventDisplay/src/TEveMu2eMainWindow.cc:752**
- Severity: high
- Code: `sprintf(msg, "Error #%i : Cluster minimum energy larger than maximum", true);`
- Description: sprintf used - consider snprintf to prevent buffer overflow

**/workspace/TEveEventDisplay/src/TEveMu2eMainWindow.cc:764**
- Severity: high
- Code: `sprintf(msg, "Error #%i : Hit minimum energy larger than maximum", true);`
- Description: sprintf used - consider snprintf to prevent buffer overflow

... and 33 more

### infinite_loop (4 occurrences)

**/workspace/CRVReco/src/CrvWidebandTriggerFilter_module.cc:86**
- Severity: high
- Code: `while(true)`
- Description: Potential infinite loop without break statement

**/workspace/CRVResponse/src/MakeCrvSiPMCharges.cc:203**
- Severity: high
- Code: `} //while(1)`
- Description: Potential infinite loop without break statement

**/workspace/Mu2eG4/src/MTMasterThread.cc:54**
- Severity: high
- Code: `while (true) {`
- Description: Potential infinite loop without break statement

**/workspace/Sources/src/FromTrackerPrototypeData_source.cc:215**
- Severity: high
- Code: `while (true) {`
- Description: Potential infinite loop without break statement

### iterator_invalidation (478 occurrences)

**/workspace/Analyses/src/TSTrackAna_module.cc:98**
- Severity: high
- Code: `for(const auto& i : stepStrings) {`
- Description: Potential iterator invalidation: container modified during iteration

**/workspace/Analyses/src/DiskCal00_module.cc:166**
- Severity: high
- Code: `for ( CaloHitCollection::const_iterator i=cryHits.begin(), e=cryHits.end(); i != e; ++i ){`
- Description: Potential iterator invalidation: container modified during iteration

**/workspace/Analyses/src/PtrTest0_module.cc:56**
- Severity: high
- Code: `for ( GenParticleCollection::const_iterator i=gens.begin();`
- Description: Potential iterator invalidation: container modified during iteration

**/workspace/Analyses/src/PtrTest0_module.cc:82**
- Severity: high
- Code: `for ( SimParticleCollection::const_iterator i = sims.begin();`
- Description: Potential iterator invalidation: container modified during iteration

**/workspace/Analyses/src/KineticFracAnalysis_module.cc:782**
- Severity: high
- Code: `for (auto cryPtr : cluster.caloHitsPtrVector()) cryList.push_back(int(cryPtr.get()- &CaloHits.at(0)));`
- Description: Potential iterator invalidation: container modified during iteration

**/workspace/Analyses/src/KineticFracAnalysis_module.cc:791**
- Severity: high
- Code: `for (auto& edep : eDepMCs)`
- Description: Potential iterator invalidation: container modified during iteration

**/workspace/Analyses/src/CaloHitFinderInspect_module.cc:222**
- Severity: high
- Code: `for (const auto & showerSim : caloShowerSims) if (std::abs(showerSim->time()+20.0-x[i]) < 5.0) {peakFound=true; break;}`
- Description: Potential iterator invalidation: container modified during iteration

**/workspace/Analyses/src/TrackSummaryTruthMaker_module.cc:64**
- Severity: high
- Code: `for(const auto& recoMapEntry: *ireco) {`
- Description: Potential iterator invalidation: container modified during iteration

**/workspace/Analyses/src/TrackSummaryTruthMaker_module.cc:66**
- Severity: high
- Code: `for(const auto hot : krep.hitVector()) {`
- Description: Potential iterator invalidation: container modified during iteration

**/workspace/Analyses/src/SelectPiMinusAtTS5_module.cc:123**
- Severity: high
- Code: `for(StepPointMCCollection::const_iterator i=inhits.begin(); i!=inhits.end(); ++i) {`
- Description: Potential iterator invalidation: container modified during iteration

**/workspace/Analyses/src/SelectPiMinusAtTS5_module.cc:160**
- Severity: high
- Code: `for(TrackSet::const_iterator i=particlesWithHits.begin(); i!=particlesWithHits.end(); ++i) {`
- Description: Potential iterator invalidation: container modified during iteration

**/workspace/Analyses/src/CaloCalibAna_module.cc:313**
- Severity: high
- Code: `for (auto& edep : eDepMCs)`
- Description: Potential iterator invalidation: container modified during iteration

**/workspace/Analyses/src/CaloCalibAna_module.cc:409**
- Severity: high
- Code: `for (auto cryPtr : cluster.caloHitsPtrVector()) cryList.push_back(std::distance(&CaloHits.at(0),cryPtr.get()));`
- Description: Potential iterator invalidation: container modified during iteration

**/workspace/Analyses/src/CaloCalibAna_module.cc:417**
- Severity: high
- Code: `for (auto& edep : eDepMCs)`
- Description: Potential iterator invalidation: container modified during iteration

**/workspace/Analyses/src/StepPointMCDumperCompact_module.cc:100**
- Severity: high
- Code: `for(const auto& i : stepStrings) {`
- Description: Potential iterator invalidation: container modified during iteration

**/workspace/Analyses/src/SensitiveTargetEnergyDumper_module.cc:281**
- Severity: high
- Code: `for ( const auto& iColl : tauHitCollections_ ){`
- Description: Potential iterator invalidation: container modified during iteration

**/workspace/Analyses/src/ReadBack_module.cc:384**
- Severity: high
- Code: `for (const auto& step : steps )`
- Description: Potential iterator invalidation: container modified during iteration

**/workspace/Analyses/src/ReadBack_module.cc:398**
- Severity: high
- Code: `for (const auto& iter : stepPtMap) _hCaStepEdep->Fill(iter.first,iter.second);`
- Description: Potential iterator invalidation: container modified during iteration

**/workspace/Analyses/src/ReadBack_module.cc:399**
- Severity: high
- Code: `for (const auto& iter : stepPtMap2) _hCaStepNum->Fill(iter.first,iter.second);`
- Description: Potential iterator invalidation: container modified during iteration

**/workspace/Analyses/src/ReadBack_module.cc:407**
- Severity: high
- Code: `for (const auto& showerSim : caloShowerSims)`
- Description: Potential iterator invalidation: container modified during iteration

**/workspace/Analyses/src/ReadBack_module.cc:410**
- Severity: high
- Code: `for (const auto& step : showerSim.caloShowerSteps()) showerMap2[showerSim.crystalID()] += step->nCompress();`
- Description: Potential iterator invalidation: container modified during iteration

**/workspace/Analyses/src/ReadBack_module.cc:418**
- Severity: high
- Code: `for (const auto& iter : showerMap)  _hCaShowerEdep->Fill(iter.first,iter.second);`
- Description: Potential iterator invalidation: container modified during iteration

**/workspace/Analyses/src/ReadBack_module.cc:419**
- Severity: high
- Code: `for (const auto& iter : showerMap2) _hCaShowerNum->Fill(iter.first,iter.second);`
- Description: Potential iterator invalidation: container modified during iteration

**/workspace/Analyses/src/FilterVDHits_module.cc:122**
- Severity: high
- Code: `for(StepPointMCCollection::const_iterator i=inhits.begin(); i!=inhits.end(); ++i) {`
- Description: Potential iterator invalidation: container modified during iteration

**/workspace/Analyses/src/FilterVDHits_module.cc:154**
- Severity: high
- Code: `for(TrackSet::const_iterator i=particlesWithHits.begin(); i!=particlesWithHits.end(); ++i) {`
- Description: Potential iterator invalidation: container modified during iteration

**/workspace/Analyses/src/PbarAnalysis2_module.cc:812**
- Severity: high
- Code: `for (auto cryPtr : cluster.caloHitsPtrVector()) cryList.push_back(int(cryPtr.get()- &CaloHits.at(0)));`
- Description: Potential iterator invalidation: container modified during iteration

**/workspace/Analyses/src/PbarAnalysis2_module.cc:822**
- Severity: high
- Code: `for (auto& edep : eDepMCs)`
- Description: Potential iterator invalidation: container modified during iteration

**/workspace/Analyses/src/CaloTrackMatchExample_module.cc:262**
- Severity: high
- Code: `for (CaloClusterCollection::const_iterator clusterIt = caloClusters.begin(); clusterIt != caloClusters.end(); ++clusterIt)`
- Description: Potential iterator invalidation: container modified during iteration

**/workspace/Analyses/src/StepPointMC1stHitDumper_module.cc:187**
- Severity: high
- Code: `for ( const auto& iColl : tauHitCollections_ ){`
- Description: Potential iterator invalidation: container modified during iteration

**/workspace/Analyses/src/SimParticleCheck00_module.cc:87**
- Severity: high
- Code: `for ( HandleVector::const_iterator i=allSims.begin(), e=allSims.end(); i != e; ++i ){`
- Description: Potential iterator invalidation: container modified during iteration

... and 448 more

### logic_error (9 occurrences)

**/workspace/Analyses/src/GeomVis_module.cc:144**
- Severity: high
- Code: `if (0) { cout<< "center " << endl;  center.Print(); }`
- Description: Condition always true/false - dead code or logic error

**/workspace/Analyses/src/GeomVis_module.cc:176**
- Severity: high
- Code: `if (0) cout << "x " << center.x() << " y " << center.y() << endl;`
- Description: Condition always true/false - dead code or logic error

**/workspace/CalPatRec/src/AgnosticHelixFinderDiagDisplay.cc:882**
- Severity: high
- Code: `if(false) {`
- Description: Condition always true/false - dead code or logic error

**/workspace/GeometryService/src/VirtualDetectorMaker.cc:308**
- Severity: high
- Code: `if(true) {`
- Description: Condition always true/false - dead code or logic error

**/workspace/Mu2eG4/src/constructExtMonFNALBuilding.cc:892**
- Severity: high
- Code: `if (false) {`
- Description: Condition always true/false - dead code or logic error

**/workspace/Mu2eHallGeom/src/Mu2eHall.cc:84**
- Severity: high
- Code: `if ( z < neg2nd && z > negHigh ) {`
- Description: Impossible condition: variable cannot be both < and > something

**/workspace/TrkHitReco/src/MakeStereoHits_module.cc:194**
- Severity: high
- Code: `if(rho < _maxrho && rho > _minrho ){`
- Description: Impossible condition: variable cannot be both < and > something

**/workspace/TrkHitReco/src/MakeStereoHits_module.cc:218**
- Severity: high
- Code: `if(rho < _maxrho && rho > _minrho ){`
- Description: Impossible condition: variable cannot be both < and > something

**/workspace/TrkHitReco/src/MakeStereoHits_module.cc:224**
- Severity: high
- Code: `if( energy < _maxE && energy > _minE ) {`
- Description: Impossible condition: variable cannot be both < and > something

### pointer_arithmetic (795 occurrences)

**/workspace/Analyses/src/CRYGenPlots_module.cc:214**
- Severity: medium
- Code: `200, -M_PI - 0.5, M_PI + 0.5);`
- Description: Raw pointer arithmetic - verify bounds and alignment

**/workspace/Analyses/src/CRYGenPlots_module.cc:216**
- Severity: medium
- Code: `200, -M_PI - 0.5, M_PI + 0.5);`
- Description: Raw pointer arithmetic - verify bounds and alignment

**/workspace/Analyses/src/KineticFracAnalysis_module.cc:521**
- Severity: medium
- Code: `_hfitpar_d0omega    = tfs->make<TH1F>("_hfitpar_d0omega","d0 + 2/om",120,-200.,1000.);`
- Description: Raw pointer arithmetic - verify bounds and alignment

**/workspace/Analyses/src/CaloHitFinderInspect_module.cc:143**
- Severity: medium
- Code: `int    roId                   = caloFromDigi.at(index+1);`
- Description: Raw pointer arithmetic - verify bounds and alignment

**/workspace/Analyses/src/CaloHitFinderInspect_module.cc:151**
- Severity: medium
- Code: `int wfOffset           = index+2;`
- Description: Raw pointer arithmetic - verify bounds and alignment

**/workspace/Analyses/src/CaloHitFinderInspect_module.cc:180**
- Severity: medium
- Code: `double t0      = waveform.at(index+1);`
- Description: Raw pointer arithmetic - verify bounds and alignment

**/workspace/Analyses/src/CaloHitFinderInspect_module.cc:182**
- Severity: medium
- Code: `int    wfindex = index+2;`
- Description: Raw pointer arithmetic - verify bounds and alignment

**/workspace/Analyses/src/CaloHitFinderInspect_module.cc:188**
- Severity: medium
- Code: `x.push_back(t0 + (i+0.5)*_digiSampling);`
- Description: Raw pointer arithmetic - verify bounds and alignment

**/workspace/Analyses/src/ReadCaloDigi_module.cc:256**
- Severity: medium
- Code: `Form("Disk0: N caloDigis @ %i MeV threshold",i+1), 1e4, 0, 1e4);`
- Description: Raw pointer arithmetic - verify bounds and alignment

**/workspace/Analyses/src/ReadCaloDigi_module.cc:258**
- Severity: medium
- Code: `Form("Disk0: N of words per caloDigi @ %i MeV threshold",i+1),`
- Description: Raw pointer arithmetic - verify bounds and alignment

**/workspace/Analyses/src/ReadCaloDigi_module.cc:261**
- Severity: medium
- Code: `Form("Disk0: N of words per event @ %i MeV threshold",i+1),`
- Description: Raw pointer arithmetic - verify bounds and alignment

**/workspace/Analyses/src/ReadCaloDigi_module.cc:264**
- Severity: medium
- Code: `Form("Disk1: N caloDigis @ %i MeV threshold",i+1), 1e4, 0, 1e4);`
- Description: Raw pointer arithmetic - verify bounds and alignment

**/workspace/Analyses/src/ReadCaloDigi_module.cc:266**
- Severity: medium
- Code: `Form("Disk1: N of words per caloDigi @ %i MeV threshold",i+1),`
- Description: Raw pointer arithmetic - verify bounds and alignment

**/workspace/Analyses/src/ReadCaloDigi_module.cc:269**
- Severity: medium
- Code: `Form("Disk1: N of words per event @ %i MeV threshold",i+1),`
- Description: Raw pointer arithmetic - verify bounds and alignment

**/workspace/Analyses/src/ReadCaloDigi_module.cc:272**
- Severity: medium
- Code: `Form("N of words per event vs crystal Id @ %i MeV threshold",i+1),`
- Description: Raw pointer arithmetic - verify bounds and alignment

**/workspace/Analyses/src/SensitiveTargetEnergyDumper_module.cc:246**
- Severity: medium
- Code: `_hEnergyVsZ = tfs->make<TH1F>("_hEnergyVsZ","Energy vs Z",nbins+10`
- Description: Raw pointer arithmetic - verify bounds and alignment

**/workspace/Analyses/src/SensitiveTargetEnergyDumper_module.cc:253**
- Severity: medium
- Code: `_hHitZCore = tfs->make<TH1F>("_hHitZCore","Internal Z Position of Hit, Core Section, Energy Weighted",nbins+10`
- Description: Raw pointer arithmetic - verify bounds and alignment

**/workspace/Analyses/src/SensitiveTargetEnergyDumper_module.cc:256**
- Severity: medium
- Code: `_hHitZStartingCore = tfs->make<TH1F>("_hHitZStartingCore","Internal Z Position of Hit, Starting Core Section, Energy Weighted",nbins+10`
- Description: Raw pointer arithmetic - verify bounds and alignment

**/workspace/Analyses/src/SensitiveTargetEnergyDumper_module.cc:259**
- Severity: medium
- Code: `_hHitZFin = tfs->make<TH1F>("_hHitZFin","Internal Z Position of Hit, Fin Section, Energy Weighted",nbins+10`
- Description: Raw pointer arithmetic - verify bounds and alignment

**/workspace/Analyses/src/SensitiveTargetEnergyDumper_module.cc:262**
- Severity: medium
- Code: `_hHitZStartingFin = tfs->make<TH1F>("_hHitZStartingFin","Internal Z Position of Hit, Starting Fin Section, Energy Weighted",nbins+10`
- Description: Raw pointer arithmetic - verify bounds and alignment

**/workspace/Analyses/src/SensitiveTargetEnergyDumper_module.cc:268**
- Severity: medium
- Code: `_hEnergyVsZAll = tfs->make<TH1F>("_hEnergyVsZAll","Energy vs Z",nbins+10`
- Description: Raw pointer arithmetic - verify bounds and alignment

**/workspace/Analyses/src/PrimaryProtonEnergyDumper_module.cc:234**
- Severity: medium
- Code: `_hEnergyVsZ = tfs->make<TH1F>("_hEnergyVsZ","Energy vs Z",nbins+10`
- Description: Raw pointer arithmetic - verify bounds and alignment

**/workspace/Analyses/src/PrimaryProtonEnergyDumper_module.cc:241**
- Severity: medium
- Code: `_hHitZCore = tfs->make<TH1F>("_hHitZCore","Internal Z Position of Hit, Core Section, Energy Weighted",nbins+10`
- Description: Raw pointer arithmetic - verify bounds and alignment

**/workspace/Analyses/src/PrimaryProtonEnergyDumper_module.cc:244**
- Severity: medium
- Code: `_hHitZStartingCore = tfs->make<TH1F>("_hHitZStartingCore","Internal Z Position of Hit, Starting Core Section, Energy Weighted",nbins+10`
- Description: Raw pointer arithmetic - verify bounds and alignment

**/workspace/Analyses/src/PrimaryProtonEnergyDumper_module.cc:247**
- Severity: medium
- Code: `_hHitZFin = tfs->make<TH1F>("_hHitZFin","Internal Z Position of Hit, Fin Section, Energy Weighted",nbins+10`
- Description: Raw pointer arithmetic - verify bounds and alignment

**/workspace/Analyses/src/PrimaryProtonEnergyDumper_module.cc:250**
- Severity: medium
- Code: `_hHitZStartingFin = tfs->make<TH1F>("_hHitZStartingFin","Internal Z Position of Hit, Starting Fin Section, Energy Weighted",nbins+10`
- Description: Raw pointer arithmetic - verify bounds and alignment

**/workspace/Analyses/src/CORSIKAGenPlots_module.cc:152**
- Severity: medium
- Code: `for (GenParticleCollection::const_iterator j = i+1; j != particles.end(); ++j)`
- Description: Raw pointer arithmetic - verify bounds and alignment

**/workspace/Analyses/src/CORSIKAGenPlots_module.cc:237**
- Severity: medium
- Code: `200, -M_PI - 0.5, M_PI + 0.5);`
- Description: Raw pointer arithmetic - verify bounds and alignment

**/workspace/Analyses/src/CORSIKAGenPlots_module.cc:239**
- Severity: medium
- Code: `200, -M_PI - 0.5, M_PI + 0.5);`
- Description: Raw pointer arithmetic - verify bounds and alignment

**/workspace/BFieldGeom/src/BFGridMap.cc:203**
- Severity: medium
- Code: `_field(i, j + 1, k),     _field(i + 1, j + 1, k),`
- Description: Raw pointer arithmetic - verify bounds and alignment

... and 765 more

### resource_leak (42 occurrences)

**/workspace/Analyses/src/PbarAnalysis2_module.cc:273**
- Severity: high
- Code: `_pbarVertexOut.open(_pbarVertexOutName.c_str());`
- Description: File opened but may not be closed

**/workspace/Analyses/src/BFieldPlotter_module.cc:156**
- Severity: high
- Code: `if(fs.is_open()){`
- Description: File opened but may not be closed

**/workspace/Analyses/src/BFieldPlotter_module.cc:212**
- Severity: high
- Code: `if(_dump && fs.is_open())fs.close();`
- Description: File opened but may not be closed

**/workspace/Analyses/src/StoppedParticlesPrinter_module.cc:35**
- Severity: high
- Code: `outFile_.open(outFileName.c_str());`
- Description: File opened but may not be closed

**/workspace/Analyses/src/MTVerification_module.cc:79**
- Severity: high
- Code: `myOutFile.open("/home/goodenou/Mu2e_MT/Offline/MTVerification.txt");`
- Description: File opened but may not be closed

**/workspace/BFieldTest/src/BFieldTest_module.cc:99**
- Severity: high
- Code: `//     FILE* file = fopen(outFile.c_str(), "w");`
- Description: File opened but may not be closed

**/workspace/BFieldTest/src/BFieldTest_module.cc:119**
- Severity: high
- Code: `FILE* file = fopen(outFile.c_str(), "w");`
- Description: File opened but may not be closed

**/workspace/CRVConditions/src/CRVOrdinalMaker.cc:54**
- Severity: high
- Code: `ordFile.open(fileSpec);`
- Description: File opened but may not be closed

**/workspace/CRVConditions/src/CRVOrdinalMaker.cc:55**
- Severity: high
- Code: `if (!ordFile.is_open()) {`
- Description: File opened but may not be closed

**/workspace/CRVReco/src/CrvPedestalFinder_module.cc:112**
- Severity: high
- Code: `outputFile.open(_tmpDBfileName);`
- Description: File opened but may not be closed

**/workspace/CRVReco/src/CrvCalibration_module.cc:119**
- Severity: high
- Code: `outputFile.open(_tmpDBfileName);`
- Description: File opened but may not be closed

**/workspace/CaloConditions/src/CaloDAQMapMaker.cc:25**
- Severity: high
- Code: `ordFile.open(fileSpec);`
- Description: File opened but may not be closed

**/workspace/CaloConditions/src/CaloDAQMapMaker.cc:26**
- Severity: high
- Code: `if (!ordFile.is_open()) {`
- Description: File opened but may not be closed

**/workspace/CaloVisualizer/src/THMu2eCaloDisk.cc:271**
- Severity: high
- Code: `fmap.open(fullPath);`
- Description: File opened but may not be closed

**/workspace/CaloVisualizer/src/THMu2eCaloDisk.cc:272**
- Severity: high
- Code: `if (!fmap.is_open()) {`
- Description: File opened but may not be closed

**/workspace/CosmicReco/src/CosmicAnalyzer_module.cc:264**
- Severity: high
- Code: `outputfile.open("CosmicAnalysis.csv");`
- Description: File opened but may not be closed

**/workspace/DbService/src/GrlList.cc:23**
- Severity: high
- Code: `myfile.open(filename);`
- Description: File opened but may not be closed

**/workspace/DbService/src/GrlList.cc:24**
- Severity: high
- Code: `if (!myfile.is_open()) {`
- Description: File opened but may not be closed

**/workspace/DbService/src/DbTool.cc:2566**
- Severity: high
- Code: `myfile.open(args["file"]);`
- Description: File opened but may not be closed

**/workspace/DbService/src/DbTool.cc:3232**
- Severity: high
- Code: `myfile.open(arg);`
- Description: File opened but may not be closed

**/workspace/DbService/src/DbTool.cc:3233**
- Severity: high
- Code: `if (!myfile.is_open()) {`
- Description: File opened but may not be closed

**/workspace/DbService/src/DbTool.cc:3287**
- Severity: high
- Code: `myfile.open(arg);`
- Description: File opened but may not be closed

**/workspace/DbService/src/DbTool.cc:3288**
- Severity: high
- Code: `if (!myfile.is_open()) {`
- Description: File opened but may not be closed

**/workspace/DbService/src/GrlTool.cc:361**
- Severity: high
- Code: `myfile.open(comFile);`
- Description: File opened but may not be closed

**/workspace/DbService/src/GrlTool.cc:362**
- Severity: high
- Code: `if (!myfile.is_open()) {`
- Description: File opened but may not be closed

**/workspace/DbTables/src/DbUtil.cc:32**
- Severity: high
- Code: `myfile.open(fn);`
- Description: File opened but may not be closed

**/workspace/DbTables/src/DbUtil.cc:33**
- Severity: high
- Code: `if (!myfile.is_open()) {`
- Description: File opened but may not be closed

**/workspace/DbTables/src/DbUtil.cc:139**
- Severity: high
- Code: `myfile.open(fn);`
- Description: File opened but may not be closed

**/workspace/DbTables/src/DbUtil.cc:140**
- Severity: high
- Code: `if (!myfile.is_open()) {`
- Description: File opened but may not be closed

**/workspace/EventGenerator/src/FromAsciiMomentumAndPosition_module.cc:129**
- Severity: high
- Code: `vertexFile_.open( vertexFileString_.c_str() );`
- Description: File opened but may not be closed

... and 12 more

### stl_container_misuse (175 occurrences)

**/workspace/Analyses/src/TSTrackAna_module.cc:266**
- Severity: low
- Code: `TH2F* h2YvsR = _maph2YvsR[h2Id];`
- Description: Map access with [] may create unwanted default entry - consider using find() or at()

**/workspace/Analyses/src/CaloHitFinderInspect_module.cc:131**
- Severity: low
- Code: `for (auto const& caloShowerSim: caloShowerSims) caloShowerSimsMap[caloShowerSim.crystalID()].push_back(&caloShowerSim);`
- Description: Map access with [] may create unwanted default entry - consider using find() or at()

**/workspace/Analyses/src/CaloHitFinderInspect_module.cc:146**
- Severity: low
- Code: `CaloShowerSimVec& caloShowers = caloShowerSimsMap[crystalId];`
- Description: Map access with [] may create unwanted default entry - consider using find() or at()

**/workspace/Analyses/src/ReadBack_module.cc:386**
- Severity: low
- Code: `stepPtMap[step.volumeId()] += step.totalEDep();`
- Description: Map access with [] may create unwanted default entry - consider using find() or at()

**/workspace/Analyses/src/ReadBack_module.cc:387**
- Severity: low
- Code: `++stepPtMap2[step.volumeId()];`
- Description: Map access with [] may create unwanted default entry - consider using find() or at()

**/workspace/Analyses/src/ReadBack_module.cc:409**
- Severity: low
- Code: `showerMap[showerSim.crystalID()] += showerSim.energyDep();`
- Description: Map access with [] may create unwanted default entry - consider using find() or at()

**/workspace/Analyses/src/ReadBack_module.cc:410**
- Severity: low
- Code: `for (const auto& step : showerSim.caloShowerSteps()) showerMap2[showerSim.crystalID()] += step->nCompress();`
- Description: Map access with [] may create unwanted default entry - consider using find() or at()

**/workspace/Analyses/src/PbarAnalysis2_module.cc:496**
- Severity: low
- Code: `vdMap[hit.simParticle()] = &hit;`
- Description: Map access with [] may create unwanted default entry - consider using find() or at()

**/workspace/Analyses/src/BFieldPlotter_module.cc:149**
- Severity: low
- Code: `if(_hMap[name]) return; //already filled the maps in a previous event`
- Description: Map access with [] may create unwanted default entry - consider using find() or at()

**/workspace/Analyses/src/BFieldPlotter_module.cc:167**
- Severity: low
- Code: `_hMap[name] = tfdir.make<TH2F>(("hMap"+name).c_str()  , (name + " Magnetic field map").c_str(),`
- Description: Map access with [] may create unwanted default entry - consider using find() or at()

**/workspace/Analyses/src/BFieldPlotter_module.cc:196**
- Severity: low
- Code: `_hMap[name]->Fill(axisOne, axisTwo, field.mag()); //fill with weight of the field magnitude`
- Description: Map access with [] may create unwanted default entry - consider using find() or at()

**/workspace/Analyses/src/ReadTrackCaloMatchingMVA_module.cc:284**
- Severity: low
- Code: `vdMap[hit.simParticle()] = &hit;`
- Description: Map access with [] may create unwanted default entry - consider using find() or at()

**/workspace/BFieldGeom/src/BFGridMap.cc:88**
- Severity: low
- Code: `CLHEP::Hep3Vector BFGridMap::interpolate(CLHEP::Hep3Vector const vec[3][3][3],`
- Description: Map access with [] may create unwanted default entry - consider using find() or at()

**/workspace/BFieldGeom/src/BFGridMap.cc:141**
- Severity: low
- Code: `double BFGridMap::gmcpoly2(double const f1d[3], double const& x) const {`
- Description: Map access with [] may create unwanted default entry - consider using find() or at()

**/workspace/CRVConditions/src/CRVOrdinalMaker.cc:36**
- Severity: low
- Code: `offMap[i][j][k] = CRVId::nChannels;`
- Description: Map access with [] may create unwanted default entry - consider using find() or at()

**/workspace/CRVConditions/src/CRVStatusMaker.cc:25**
- Severity: low
- Code: `smap[channel] = stat;`
- Description: Map access with [] may create unwanted default entry - consider using find() or at()

**/workspace/CRVConditions/src/CRVStatusMaker.cc:47**
- Severity: low
- Code: `smap[row.channel()] = row.status();`
- Description: Map access with [] may create unwanted default entry - consider using find() or at()

**/workspace/CRVReco/src/CrvFPGArate_module.cc:106**
- Severity: low
- Code: `eventFPGAmap[FPGAIndex]=0;`
- Description: Map access with [] may create unwanted default entry - consider using find() or at()

**/workspace/CRVReco/src/CrvFPGArate_module.cc:107**
- Severity: low
- Code: `eventHitMultiplicityMap[FPGAIndex].clear();`
- Description: Map access with [] may create unwanted default entry - consider using find() or at()

**/workspace/CRVReco/src/CrvFPGArate_module.cc:132**
- Severity: low
- Code: `eventFPGAmap[FPGAIndex]++;`
- Description: Map access with [] may create unwanted default entry - consider using find() or at()

**/workspace/CRVReco/src/CrvFPGArate_module.cc:136**
- Severity: low
- Code: `eventHitMultiplicityMap[FPGAIndex].back()++;`
- Description: Map access with [] may create unwanted default entry - consider using find() or at()

**/workspace/CRVReco/src/CrvFPGArate_module.cc:138**
- Severity: low
- Code: `eventHitMultiplicityMap[FPGAIndex].push_back(1);`
- Description: Map access with [] may create unwanted default entry - consider using find() or at()

**/workspace/CRVReco/src/CrvCoincidenceFinder_module.cc:267**
- Severity: low
- Code: `_sectorMap[i]=s;`
- Description: Map access with [] may create unwanted default entry - consider using find() or at()

**/workspace/CRVReco/src/CrvCoincidenceFinder_module.cc:337**
- Severity: low
- Code: `sectorTypeMap[sector.sectorType].emplace_back(crvRecoPulse, crvCounterPos,`
- Description: Map access with [] may create unwanted default entry - consider using find() or at()

**/workspace/CRVReco/src/CrvCoincidenceFinder_module.cc:541**
- Severity: low
- Code: `offsetFromCounterCenter[_sectorMap.at(crvSector).lengthDirection]=distanceFromCounterCenter;`
- Description: Map access with [] may create unwanted default entry - consider using find() or at()

**/workspace/CRVResponse/src/CrvMCHelper.cc:37**
- Severity: low
- Code: `simParticleMap[step.simParticle()]+=step.visibleEDep();`
- Description: Map access with [] may create unwanted default entry - consider using find() or at()

**/workspace/CRVResponse/src/CrvPhotonGenerator_module.cc:368**
- Severity: low
- Code: `std::vector<CrvPhotons::SinglePhoton> &photons = photonMap[barIndexSiPMNumber];`
- Description: Map access with [] may create unwanted default entry - consider using find() or at()

**/workspace/CRVResponse/src/CrvStepsFromStepPointMCs_module.cc:345**
- Severity: low
- Code: `vector<SPMCPtr> &spmcptrv = stepPointMap[barIndexTrackPair];`
- Description: Map access with [] may create unwanted default entry - consider using find() or at()

**/workspace/CalPatRec/src/AgnosticHelixFinderDiag_tool.cc:741**
- Severity: low
- Code: `++pmap[id];`
- Description: Map access with [] may create unwanted default entry - consider using find() or at()

**/workspace/CaloCluster/src/CaloProtoClusterMaker_module.cc:122**
- Severity: low
- Code: `caloIdHitMap[hit.crystalID()].push_back(&hit);`
- Description: Map access with [] may create unwanted default entry - consider using find() or at()

... and 145 more

### string_handling (311 occurrences)

**/workspace/Analyses/src/G4ReactionAnalyzer_module.cc:72**
- Severity: medium
- Code: `hDaugherCreationCodes_->Fill(pp.str().c_str(), 1.);`
- Description: c_str() used - pointer may become invalid if string is modified

**/workspace/Analyses/src/G4ReactionAnalyzer_module.cc:76**
- Severity: medium
- Code: `hDaugherMultiplicity_->Fill(i.first.c_str(), i.second, 1.);`
- Description: c_str() used - pointer may become invalid if string is modified

**/workspace/Analyses/src/CosmicAnalysis_module.cc:313**
- Severity: medium
- Code: `if(filename.find(_filenameSearchPattern)!=std::string::npos) strncpy(_eventinfo.filename, filename.c_str(),199);`
- Description: c_str() used - pointer may become invalid if string is modified

**/workspace/Analyses/src/CosmicAnalysis_module.cc:353**
- Severity: medium
- Code: `strncpy(_eventinfo.cosmic_particle, HepPID::particleName(pdgId).c_str(),99);`
- Description: c_str() used - pointer may become invalid if string is modified

**/workspace/Analyses/src/CosmicAnalysis_module.cc:459**
- Severity: medium
- Code: `strncpy(_eventinfo.simreco_production_process, productionProcess.name().c_str(),99);`
- Description: c_str() used - pointer may become invalid if string is modified

**/workspace/Analyses/src/CosmicAnalysis_module.cc:462**
- Severity: medium
- Code: `strncpy(_eventinfo.simreco_particle, HepPID::particleName(pdgId).c_str(),99);`
- Description: c_str() used - pointer may become invalid if string is modified

**/workspace/Analyses/src/CosmicAnalysis_module.cc:476**
- Severity: medium
- Code: `strncpy(_eventinfo.simreco_production_volume, productionVolumeName.c_str(),99);`
- Description: c_str() used - pointer may become invalid if string is modified

**/workspace/Analyses/src/StoppedParticlesDumper_module.cc:177**
- Severity: medium
- Code: `nt_->Branch("stops", &data_, branchDesc.c_str());`
- Description: c_str() used - pointer may become invalid if string is modified

**/workspace/Analyses/src/CollectionSizeAnalyzer_module.cc:118**
- Severity: medium
- Code: `hStepPointSize_->Fill(cn.c_str(), double(c->size()));`
- Description: c_str() used - pointer may become invalid if string is modified

**/workspace/Analyses/src/CollectionSizeAnalyzer_module.cc:119**
- Severity: medium
- Code: `hStepPointSum_->Fill(cn.c_str(), double(c->size()));`
- Description: c_str() used - pointer may become invalid if string is modified

**/workspace/Analyses/src/CollectionSizeAnalyzer_module.cc:120**
- Severity: medium
- Code: `hStepPointDistLin_->Fill(cn.c_str(), double(c->size()), 1.);`
- Description: c_str() used - pointer may become invalid if string is modified

**/workspace/Analyses/src/CollectionSizeAnalyzer_module.cc:121**
- Severity: medium
- Code: `hStepPointDistLog_->Fill(cn.c_str(), log10(std::max(1., double(c->size()))), 1.);`
- Description: c_str() used - pointer may become invalid if string is modified

**/workspace/Analyses/src/CollectionSizeAnalyzer_module.cc:130**
- Severity: medium
- Code: `hSimParticleDistLin_->Fill(cn.c_str(), double(c->size()), 1.);`
- Description: c_str() used - pointer may become invalid if string is modified

**/workspace/Analyses/src/CollectionSizeAnalyzer_module.cc:131**
- Severity: medium
- Code: `hSimParticleDistLog_->Fill(cn.c_str(), log10(std::max(1., double(c->size()))), 1.);`
- Description: c_str() used - pointer may become invalid if string is modified

**/workspace/Analyses/src/PionMomentumAnalyzer_module.cc:102**
- Severity: medium
- Code: `h_p_by_parent_->Fill(parentName.c_str(), momentum, 1.0);`
- Description: c_str() used - pointer may become invalid if string is modified

**/workspace/Analyses/src/PbarAnalysis2_module.cc:273**
- Severity: medium
- Code: `_pbarVertexOut.open(_pbarVertexOutName.c_str());`
- Description: c_str() used - pointer may become invalid if string is modified

**/workspace/Analyses/src/BFieldPlotter_module.cc:103**
- Severity: medium
- Code: `<< _plane.c_str();`
- Description: c_str() used - pointer may become invalid if string is modified

**/workspace/Analyses/src/BFieldPlotter_module.cc:155**
- Severity: medium
- Code: `fs.open (dumpfile.c_str(), fstream::out);`
- Description: c_str() used - pointer may become invalid if string is modified

**/workspace/Analyses/src/BFieldPlotter_module.cc:164**
- Severity: medium
- Code: `art::TFileDirectory tfdir = tfs->mkdir( ("BFieldMapper_"+name).c_str() );`
- Description: c_str() used - pointer may become invalid if string is modified

**/workspace/Analyses/src/BFieldPlotter_module.cc:167**
- Severity: medium
- Code: `_hMap[name] = tfdir.make<TH2F>(("hMap"+name).c_str()  , (name + " Magnetic field map").c_str(),`
- Description: c_str() used - pointer may become invalid if string is modified

**/workspace/Analyses/src/StoppedParticlesPrinter_module.cc:35**
- Severity: medium
- Code: `outFile_.open(outFileName.c_str());`
- Description: c_str() used - pointer may become invalid if string is modified

**/workspace/Analyses/src/pbars1hist_module.cc:153**
- Severity: medium
- Code: `pbarParentPDG_->Fill(parentName.c_str(), 1.0);`
- Description: c_str() used - pointer may become invalid if string is modified

**/workspace/Analyses/src/pbars1hist_module.cc:154**
- Severity: medium
- Code: `pbarParentMomentum_->Fill(parentName.c_str(), parentStartMomentum, 1.0);`
- Description: c_str() used - pointer may become invalid if string is modified

**/workspace/BFieldTest/src/BFieldSymmetry_module.cc:106**
- Severity: medium
- Code: `art::TFileDirectory tfdir = tfs.mkdir(map_.getKey().c_str());`
- Description: c_str() used - pointer may become invalid if string is modified

**/workspace/BFieldTest/src/BFieldTest_module.cc:99**
- Severity: medium
- Code: `//     FILE* file = fopen(outFile.c_str(), "w");`
- Description: c_str() used - pointer may become invalid if string is modified

**/workspace/BFieldTest/src/BFieldTest_module.cc:119**
- Severity: medium
- Code: `FILE* file = fopen(outFile.c_str(), "w");`
- Description: c_str() used - pointer may become invalid if string is modified

**/workspace/Blinding/src/BigNumber.cc:13**
- Severity: medium
- Code: `auto rv = _rep.c_str();`
- Description: c_str() used - pointer may become invalid if string is modified

**/workspace/CRVReco/src/CrvFPGArate_module.cc:165**
- Severity: medium
- Code: `const std::string histName=Form("%i_%i_%i__%s_%i",rocID,rocPort,febFPGA,sectorName.c_str(),moduleNumber);`
- Description: c_str() used - pointer may become invalid if string is modified

**/workspace/CRVReco/src/CrvFPGArate_module.cc:167**
- Severity: medium
- Code: `FPGAiter = _FPGArateHists.emplace(FPGAIndex,_tfdirFPGAhitRates->make<TH1F>(histName.c_str(),histName.c_str(),100,0,100)).first;  //returns iterator to new element`
- Description: c_str() used - pointer may become invalid if string is modified

**/workspace/CRVReco/src/CrvFPGArate_module.cc:193**
- Severity: medium
- Code: `const std::string histName=Form("%i_%i_%i__%s_%i",rocID,rocPort,febFPGA,sectorName.c_str(),moduleNumber);`
- Description: c_str() used - pointer may become invalid if string is modified

... and 281 more

### type_mismatch (6 occurrences)

**/workspace/CalorimeterGeom/src/Disk.cc:179**
- Severity: medium
- Code: `if (tolerance < 0) {`
- Description: Comparing unsigned type with < 0 (always false)

**/workspace/GeometryService/src/BFieldManagerMaker.cc:533**
- Severity: medium
- Code: `if (fd < 0) {`
- Description: Comparing unsigned type with < 0 (always false)

**/workspace/GlobalConstantsService/src/PhysicsParams.cc:56**
- Severity: medium
- Code: `if(tmpPDGId[i] < 0) {`
- Description: Comparing unsigned type with < 0 (always false)

**/workspace/Mu2eUtilities/src/MedianCalculator.cc:55**
- Severity: medium
- Code: `while (sum < 0.5 * _totalWeight) {`
- Description: Comparing unsigned type with < 0 (always false)

**/workspace/TrkPatRec/src/TimeAndPhiClusterFinder_module.cc:398**
- Severity: medium
- Code: `if (deltaPhi < 0) deltaPhi += 6.2832;`
- Description: Comparing unsigned type with < 0 (always false)

**/workspace/TrkReco/src/PanelAmbigStructs.cc:77**
- Severity: medium
- Code: `if(hprod < 0){`
- Description: Comparing unsigned type with < 0 (always false)

### undefined_behavior (3459 occurrences)

**/workspace/Analyses/src/KineticFracAnalysis_module.cc:724**
- Severity: high
- Code: `//--------------------------  Do generated particles --------------------------------`
- Description: Multiple increments/decrements on same variable - undefined behavior

**/workspace/Analyses/src/KineticFracAnalysis_module.cc:731**
- Severity: high
- Code: `//--------------------------  Do calorimeter hits --------------------------------`
- Description: Multiple increments/decrements on same variable - undefined behavior

**/workspace/Analyses/src/KineticFracAnalysis_module.cc:774**
- Severity: high
- Code: `//--------------------------  Do clusters --------------------------------`
- Description: Multiple increments/decrements on same variable - undefined behavior

**/workspace/Analyses/src/KineticFracAnalysis_module.cc:1108**
- Severity: high
- Code: `//--------------------------  Do tracks  --------------------------------`
- Description: Multiple increments/decrements on same variable - undefined behavior

**/workspace/Analyses/src/KineticFracAnalysis_module.cc:1182**
- Severity: high
- Code: `//--------------------------  Do tracker hits  --------------------------------`
- Description: Multiple increments/decrements on same variable - undefined behavior

**/workspace/Analyses/src/CaloHitFinderInspect_module.cc:94**
- Severity: high
- Code: `//------------------------------------------`
- Description: Multiple increments/decrements on same variable - undefined behavior

**/workspace/Analyses/src/CaloHitFinderInspect_module.cc:111**
- Severity: high
- Code: `//-------------------------------------------------------`
- Description: Multiple increments/decrements on same variable - undefined behavior

**/workspace/Analyses/src/CaloHitFinderInspect_module.cc:275**
- Severity: high
- Code: `//------------------------------------------------------`
- Description: Multiple increments/decrements on same variable - undefined behavior

**/workspace/Analyses/src/CaloHitFinderInspect_module.cc:283**
- Severity: high
- Code: `//-----------------------------------------------`
- Description: Multiple increments/decrements on same variable - undefined behavior

**/workspace/Analyses/src/CaloHitFinderInspect_module.cc:297**
- Severity: high
- Code: `//-----------------------------------`
- Description: Multiple increments/decrements on same variable - undefined behavior

**/workspace/Analyses/src/CaloDigiAna_module.cc:131**
- Severity: high
- Code: `//--------------------------------------------------------------------------------`
- Description: Multiple increments/decrements on same variable - undefined behavior

**/workspace/Analyses/src/CaloDigiAna_module.cc:170**
- Severity: high
- Code: `//--------------------------------------------------------------------------------`
- Description: Multiple increments/decrements on same variable - undefined behavior

**/workspace/Analyses/src/CaloDigiAna_module.cc:173**
- Severity: high
- Code: `//--------------------------------------------------------------------------------`
- Description: Multiple increments/decrements on same variable - undefined behavior

**/workspace/Analyses/src/FilterEmptyEvents_module.cc:1**
- Severity: high
- Code: `/*------------------------------------------------------------`
- Description: Multiple increments/decrements on same variable - undefined behavior

**/workspace/Analyses/src/FilterEmptyEvents_module.cc:15**
- Severity: high
- Code: `-----------------------------------------------------------*/`
- Description: Multiple increments/decrements on same variable - undefined behavior

**/workspace/Analyses/src/FilterEmptyEvents_module.cc:39**
- Severity: high
- Code: `//--------------------------------------------------------------------`
- Description: Multiple increments/decrements on same variable - undefined behavior

**/workspace/Analyses/src/SelectPiMinusAtTS5_module.cc:217**
- Severity: high
- Code: `//----------------------------------------------------------------`
- Description: Multiple increments/decrements on same variable - undefined behavior

**/workspace/Analyses/src/SelectPiMinusAtTS5_module.cc:248**
- Severity: high
- Code: `//----------------------------------------------------------------`
- Description: Multiple increments/decrements on same variable - undefined behavior

**/workspace/Analyses/src/SelectPiMinusAtTS5_module.cc:277**
- Severity: high
- Code: `//----------------------------------------------------------------`
- Description: Multiple increments/decrements on same variable - undefined behavior

**/workspace/Analyses/src/EMFCSimpleDumper_module.cc:105**
- Severity: high
- Code: `//----------------------------------------------------------------`
- Description: Multiple increments/decrements on same variable - undefined behavior

**/workspace/Analyses/src/EMFCSimpleDumper_module.cc:124**
- Severity: high
- Code: `//----------------------------------------------------------------`
- Description: Multiple increments/decrements on same variable - undefined behavior

**/workspace/Analyses/src/EMFCSimpleDumper_module.cc:145**
- Severity: high
- Code: `//----------------------------------------------------------------`
- Description: Multiple increments/decrements on same variable - undefined behavior

**/workspace/Analyses/src/ReadCaloDigi_module.cc:454**
- Severity: high
- Code: `//--------------------------------------------------------------------------------`
- Description: Multiple increments/decrements on same variable - undefined behavior

**/workspace/Analyses/src/ReadCaloDigi_module.cc:492**
- Severity: high
- Code: `//--------------------------------------------------------------------------------`
- Description: Multiple increments/decrements on same variable - undefined behavior

**/workspace/Analyses/src/CaloCalibAna_module.cc:297**
- Severity: high
- Code: `//--------------------------  Do calorimeter hits --------------------------------`
- Description: Multiple increments/decrements on same variable - undefined behavior

**/workspace/Analyses/src/CaloCalibAna_module.cc:401**
- Severity: high
- Code: `//--------------------------  Do clusters --------------------------------`
- Description: Multiple increments/decrements on same variable - undefined behavior

**/workspace/Analyses/src/CaloCalibAna_module.cc:483**
- Severity: high
- Code: `//--------------------------  Do virtual detectors --------------------------------`
- Description: Multiple increments/decrements on same variable - undefined behavior

**/workspace/Analyses/src/ParticleIDScan_module.cc:44**
- Severity: high
- Code: `//----------------------------------------------------------------`
- Description: Multiple increments/decrements on same variable - undefined behavior

**/workspace/Analyses/src/StepPointMCDumperCompact_module.cc:56**
- Severity: high
- Code: `//----------------------------------------------------------------`
- Description: Multiple increments/decrements on same variable - undefined behavior

**/workspace/Analyses/src/CosmicFilter_module.cc:3**
- Severity: high
- Code: `// -------------------------`
- Description: Multiple increments/decrements on same variable - undefined behavior

... and 3429 more

