# Real Bugs Found in Mu2e Offline Framework

Total real bugs found: 12387

## Summary by Type

- **array_bounds**: 6724 occurrences
- **assignment_in_condition**: 27 occurrences
- **division_by_zero**: 2277 occurrences
- **memory_leak**: 1296 occurrences
- **missing_return**: 362 occurrences
- **uninitialized_variable**: 1676 occurrences
- **use_after_free**: 25 occurrences

## Detailed Findings

### array_bounds (6724 occurrences)

**/workspace/Analyses/src/TSTrackAna_module.cc:266**
- Severity: medium
- Code: `TH2F* h2YvsR = _maph2YvsR[h2Id];`
- Description: Array access _maph2YvsR[h2Id] without bounds check

**/workspace/Analyses/src/CountVirtualDetectorHits_module.cc:78**
- Severity: medium
- Code: `counter[index]++;`
- Description: Array access counter[index] without bounds check

**/workspace/Analyses/src/CountVirtualDetectorHits_module.cc:88**
- Severity: medium
- Code: `log << "VD" << enabledVDs[i] << ": " << counter[i] << "\n";`
- Description: Array access enabledVDs[i] without bounds check

**/workspace/Analyses/src/G4ReactionAnalyzer_module.cc:73**
- Severity: medium
- Code: `++ccount[pp.str()];`
- Description: Array access ccount[pp.str()] without bounds check

**/workspace/Analyses/src/KineticFracAnalysis_module.cc:394**
- Severity: medium
- Code: `_Ntup->Branch("mTrkId",    &_mTrkId,    "mTrkId[nMatch]/I");`
- Description: Array access mTrkId[nMatch] without bounds check

**/workspace/Analyses/src/KineticFracAnalysis_module.cc:395**
- Severity: medium
- Code: `_Ntup->Branch("mCluId",    &_mCluId,    "mCluId[nMatch]/I");`
- Description: Array access mCluId[nMatch] without bounds check

**/workspace/Analyses/src/KineticFracAnalysis_module.cc:396**
- Severity: medium
- Code: `_Ntup->Branch("mChi2",     &_mChi2,     "mChi2[nMatch]/F");`
- Description: Array access mChi2[nMatch] without bounds check

**/workspace/Analyses/src/KineticFracAnalysis_module.cc:397**
- Severity: medium
- Code: `_Ntup->Branch("mChi2Pos",  &_mChi2Pos,  "mChi2Pos[nMatch]/F");`
- Description: Array access mChi2Pos[nMatch] without bounds check

**/workspace/Analyses/src/KineticFracAnalysis_module.cc:398**
- Severity: medium
- Code: `_Ntup->Branch("mChi2Time", &_mChi2Time, "mChi2Time[nMatch]/F");`
- Description: Array access mChi2Time[nMatch] without bounds check

**/workspace/Analyses/src/KineticFracAnalysis_module.cc:401**
- Severity: medium
- Code: `_Ntup->Branch("genId",        &_genPdgId,     "genId[nGen]/I");`
- Description: Array access genId[nGen] without bounds check

**/workspace/Analyses/src/KineticFracAnalysis_module.cc:402**
- Severity: medium
- Code: `_Ntup->Branch("genCrCode",    &_genCrCode,    "genCrCode[nGen]/I");`
- Description: Array access genCrCode[nGen] without bounds check

**/workspace/Analyses/src/KineticFracAnalysis_module.cc:403**
- Severity: medium
- Code: `_Ntup->Branch("genMomX",      &_genmomX,      "genMomX[nGen]/F");`
- Description: Array access genMomX[nGen] without bounds check

**/workspace/Analyses/src/KineticFracAnalysis_module.cc:404**
- Severity: medium
- Code: `_Ntup->Branch("genMomY",      &_genmomY,      "genMomY[nGen]/F");`
- Description: Array access genMomY[nGen] without bounds check

**/workspace/Analyses/src/KineticFracAnalysis_module.cc:405**
- Severity: medium
- Code: `_Ntup->Branch("genMomZ",      &_genmomZ,      "genMomZ[nGen]/F");`
- Description: Array access genMomZ[nGen] without bounds check

**/workspace/Analyses/src/KineticFracAnalysis_module.cc:406**
- Severity: medium
- Code: `_Ntup->Branch("genStartX",    &_genStartX,    "genStartX[nGen]/F");`
- Description: Array access genStartX[nGen] without bounds check

**/workspace/Analyses/src/KineticFracAnalysis_module.cc:407**
- Severity: medium
- Code: `_Ntup->Branch("genStartY",    &_genStartY,    "genStartY[nGen]/F");`
- Description: Array access genStartY[nGen] without bounds check

**/workspace/Analyses/src/KineticFracAnalysis_module.cc:408**
- Severity: medium
- Code: `_Ntup->Branch("genStartZ",    &_genStartZ,    "genStartZ[nGen]/F");`
- Description: Array access genStartZ[nGen] without bounds check

**/workspace/Analyses/src/KineticFracAnalysis_module.cc:409**
- Severity: medium
- Code: `_Ntup->Branch("genStartT",    &_genStartT,    "genStartT[nGen]/F");`
- Description: Array access genStartT[nGen] without bounds check

**/workspace/Analyses/src/KineticFracAnalysis_module.cc:412**
- Severity: medium
- Code: `_Ntup->Branch("cryId",        &_cryId ,       "cryId[nCry]/I");`
- Description: Array access cryId[nCry] without bounds check

**/workspace/Analyses/src/KineticFracAnalysis_module.cc:413**
- Severity: medium
- Code: `_Ntup->Branch("crySectionId", &_crySectionId, "crySectionId[nCry]/I");`
- Description: Array access crySectionId[nCry] without bounds check

... and 6704 more

### assignment_in_condition (27 occurrences)

**/workspace/DbService/src/DbTool.cc:97**
- Severity: high
- Code: `if ((rc = getArgs(args))) return rc;`
- Description: Possible assignment (=) instead of comparison (==)

**/workspace/DbService/src/DbTool.cc:173**
- Severity: high
- Code: `if ((rc = getArgs(args))) return rc;`
- Description: Possible assignment (=) instead of comparison (==)

**/workspace/DbService/src/DbTool.cc:238**
- Severity: high
- Code: `if ((rc = getArgs(args))) return rc;`
- Description: Possible assignment (=) instead of comparison (==)

**/workspace/DbService/src/DbTool.cc:300**
- Severity: high
- Code: `if ((rc = getArgs(args))) return rc;`
- Description: Possible assignment (=) instead of comparison (==)

**/workspace/DbService/src/DbTool.cc:343**
- Severity: high
- Code: `if ((rc = getArgs(args))) return rc;`
- Description: Possible assignment (=) instead of comparison (==)

**/workspace/DbService/src/DbTool.cc:392**
- Severity: high
- Code: `if ((rc = getArgs(args))) return rc;`
- Description: Possible assignment (=) instead of comparison (==)

**/workspace/DbService/src/DbTool.cc:443**
- Severity: high
- Code: `if ((rc = getArgs(args))) return rc;`
- Description: Possible assignment (=) instead of comparison (==)

**/workspace/DbService/src/DbTool.cc:514**
- Severity: high
- Code: `if ((rc = getArgs(args))) return rc;`
- Description: Possible assignment (=) instead of comparison (==)

**/workspace/DbService/src/DbTool.cc:556**
- Severity: high
- Code: `if ((rc = getArgs(args))) return rc;`
- Description: Possible assignment (=) instead of comparison (==)

**/workspace/DbService/src/DbTool.cc:616**
- Severity: high
- Code: `if ((rc = getArgs(args))) return rc;`
- Description: Possible assignment (=) instead of comparison (==)

**/workspace/DbService/src/DbTool.cc:710**
- Severity: high
- Code: `if ((rc = getArgs(args))) return rc;`
- Description: Possible assignment (=) instead of comparison (==)

**/workspace/DbService/src/DbTool.cc:946**
- Severity: high
- Code: `if ((rc = getArgs(args))) return rc;`
- Description: Possible assignment (=) instead of comparison (==)

**/workspace/DbService/src/DbTool.cc:1160**
- Severity: high
- Code: `if ((rc = getArgs(args))) return rc;`
- Description: Possible assignment (=) instead of comparison (==)

**/workspace/DbService/src/DbTool.cc:1230**
- Severity: high
- Code: `if ((rc = getArgs(args))) return rc;`
- Description: Possible assignment (=) instead of comparison (==)

**/workspace/DbService/src/DbTool.cc:1355**
- Severity: high
- Code: `if ((rc = getArgs(args))) return rc;`
- Description: Possible assignment (=) instead of comparison (==)

**/workspace/DbService/src/DbTool.cc:1494**
- Severity: high
- Code: `if ((rc = getArgs(args))) return rc;`
- Description: Possible assignment (=) instead of comparison (==)

**/workspace/DbService/src/DbTool.cc:1738**
- Severity: high
- Code: `if ((rc = getArgs(args))) return rc;`
- Description: Possible assignment (=) instead of comparison (==)

**/workspace/DbService/src/DbTool.cc:1897**
- Severity: high
- Code: `if ((rc = getArgs(args))) return rc;`
- Description: Possible assignment (=) instead of comparison (==)

**/workspace/DbService/src/DbTool.cc:1956**
- Severity: high
- Code: `if ((rc = getArgs(args))) return rc;`
- Description: Possible assignment (=) instead of comparison (==)

**/workspace/DbService/src/DbTool.cc:2093**
- Severity: high
- Code: `if ((rc = getArgs(args))) return rc;`
- Description: Possible assignment (=) instead of comparison (==)

... and 7 more

### division_by_zero (2277 occurrences)

**/workspace/Analyses/src/DiskCal00_module.cc:272**
- Severity: high
- Code: `cout << "Number of Readouts: " << nSiPM << " "  << CaloConst::_nSiPMPerCrystal << " " << nSiPM/CaloConst::_nSiPMPerCrystal << endl;`
- Description: Division by CaloConst without zero check

**/workspace/Analyses/src/StatusG4Analyzer_module.cc:59**
- Severity: high
- Code: `hRealTime_        = tfs->make<TH1D>( "hRealTime",      "Wall Clock time/event (10 ms ticks);(ms)",  50,  0.,   500.   );`
- Description: Division by event without zero check

**/workspace/Analyses/src/StatusG4Analyzer_module.cc:60**
- Severity: high
- Code: `hRealTimeWide_    = tfs->make<TH1D>( "hRealTimeWide",  "Wall Clock time/event (10 ms ticks);(ms)", 100,  0., 10000.   );`
- Description: Division by event without zero check

**/workspace/Analyses/src/StatusG4Analyzer_module.cc:61**
- Severity: high
- Code: `hCPUTime_         = tfs->make<TH1D>( "hCPUTime",       "CPU  time/event(10 ms ticks);(ms)",         50,  0.,   500.   );`
- Description: Division by event(10 without zero check

**/workspace/Analyses/src/StatusG4Analyzer_module.cc:62**
- Severity: high
- Code: `hCPUTimeWide_     = tfs->make<TH1D>( "hCPUTimeWide",   "CPU  time/event(10 ms ticks);(ms)",        100,  0., 10000.   );`
- Description: Division by event(10 without zero check

**/workspace/Analyses/src/ReadTrackerSteps_module.cc:102**
- Severity: high
- Code: `"Number/ID of the detector with step",`
- Description: Division by ID without zero check

**/workspace/Analyses/src/CRYGenPlots_module.cc:111**
- Severity: high
- Code: `_cosmicTree->Branch("x", &_x, "x/F");`
- Description: Division by F without zero check

**/workspace/Analyses/src/CRYGenPlots_module.cc:112**
- Severity: high
- Code: `_cosmicTree->Branch("y", &_y, "y/F");`
- Description: Division by F without zero check

**/workspace/Analyses/src/CRYGenPlots_module.cc:113**
- Severity: high
- Code: `_cosmicTree->Branch("z", &_z, "z/F");`
- Description: Division by F without zero check

**/workspace/Analyses/src/CRYGenPlots_module.cc:114**
- Severity: high
- Code: `_cosmicTree->Branch("px", &_px, "px/F");`
- Description: Division by F without zero check

**/workspace/Analyses/src/CRYGenPlots_module.cc:115**
- Severity: high
- Code: `_cosmicTree->Branch("py", &_py, "py/F");`
- Description: Division by F without zero check

**/workspace/Analyses/src/CRYGenPlots_module.cc:116**
- Severity: high
- Code: `_cosmicTree->Branch("pz", &_pz, "pz/F");`
- Description: Division by F without zero check

**/workspace/Analyses/src/CRYGenPlots_module.cc:117**
- Severity: high
- Code: `_cosmicTree->Branch("theta", &_theta, "theta/F");`
- Description: Division by F without zero check

**/workspace/Analyses/src/CRYGenPlots_module.cc:118**
- Severity: high
- Code: `_cosmicTree->Branch("phi", &_phi, "phi/F");`
- Description: Division by F without zero check

**/workspace/Analyses/src/CRYGenPlots_module.cc:119**
- Severity: high
- Code: `_cosmicTree->Branch("KE", &_KE, "KE/F");`
- Description: Division by F without zero check

**/workspace/Analyses/src/CRYGenPlots_module.cc:120**
- Severity: high
- Code: `_cosmicTree->Branch("p", &_p, "p/F");`
- Description: Division by F without zero check

**/workspace/Analyses/src/CRYGenPlots_module.cc:121**
- Severity: high
- Code: `_cosmicTree->Branch("t", &_t, "t/F");`
- Description: Division by F without zero check

**/workspace/Analyses/src/CRYGenPlots_module.cc:122**
- Severity: high
- Code: `_cosmicTree->Branch("pdgId", &_pdgId, "pdgId/I");`
- Description: Division by I without zero check

**/workspace/Analyses/src/CRYGenPlots_module.cc:219**
- Severity: high
- Code: `_hPyOverPmag = tfs->make<TH1F>("PyOverPmag", "Py/Pmag", 200, -20., 20.);`
- Description: Division by Pmag without zero check

**/workspace/Analyses/src/KineticFracAnalysis_module.cc:389**
- Severity: high
- Code: `_Ntup->Branch("evt",          &_evt ,        "evt/I");`
- Description: Division by I without zero check

... and 2257 more

### memory_leak (1296 occurrences)

**/workspace/Analyses/src/TSTrackAna_module.cc:170**
- Severity: high
- Code: `TGeoMaterial* vacuum = new TGeoMaterial("vacuum",200,100,20);`
- Description: Memory allocated with new but not deleted: vacuum

**/workspace/Analyses/src/TSTrackAna_module.cc:171**
- Severity: high
- Code: `_trkMat = new TGeoMedium("TrkMat",1,vacuum);`
- Description: Memory allocated with new but not deleted: _trkMat

**/workspace/Analyses/src/TSTrackAna_module.cc:190**
- Severity: high
- Code: `//if (!gApplication) gApplication = new TApplication("TSTrackAna",0,0);`
- Description: Memory allocated with new but not deleted: gApplication

**/workspace/Analyses/src/KineticFracAnalysis_module.cc:616**
- Severity: high
- Code: `// TF1* func = new TF1("timeFit",timeFit,0.,50.,3);`
- Description: Memory allocated with new but not deleted: func

**/workspace/Analyses/src/KineticFracAnalysis_module.cc:628**
- Severity: high
- Code: `_hTanDipVsMomentumLoFrac = new TH2F("_hTanDipVsMomentumLoFrac","Tan Dip vs Momentum LoFrac",300,0.,300.,100,0.,3.);`
- Description: Memory allocated with new but not deleted: _hTanDipVsMomentumLoFrac

**/workspace/Analyses/src/KineticFracAnalysis_module.cc:634**
- Severity: high
- Code: `_hTanDipVsMomentumMuon = new TH2F("_hTanDipVsMomentumMuon","Tan Dip vs Momentum Muon",300,0.,300.,100,0.,3.);`
- Description: Memory allocated with new but not deleted: _hTanDipVsMomentumMuon

**/workspace/Analyses/src/ReadPSVacuum_module.cc:63**
- Severity: high
- Code: `nt = new float[1000];`
- Description: Memory allocated with new but not deleted: nt

**/workspace/Analyses/src/ReadPTM_module.cc:60**
- Severity: high
- Code: `nt = new float[1000];`
- Description: Memory allocated with new but not deleted: nt

**/workspace/Analyses/src/GeomVis_module.cc:101**
- Severity: high
- Code: `TGeoMaterial* vacuum = new TGeoMaterial("vacuum",200,100,20);`
- Description: Memory allocated with new but not deleted: vacuum

**/workspace/Analyses/src/GeomVis_module.cc:102**
- Severity: high
- Code: `_trkMat = new TGeoMedium("TrkMat",1,vacuum);`
- Description: Memory allocated with new but not deleted: _trkMat

**/workspace/Analyses/src/GeomVis_module.cc:164**
- Severity: high
- Code: `TGeoArb8 *arb = new TGeoArb8(dz);`
- Description: Memory allocated with new but not deleted: arb

**/workspace/Analyses/src/GeomVis_module.cc:174**
- Severity: high
- Code: `TGeoVolume *vol = new TGeoVolume(name, arb, _trkMat);`
- Description: Memory allocated with new but not deleted: vol

**/workspace/Analyses/src/GeomVis_module.cc:186**
- Severity: high
- Code: `TGeoTube *tube = new TGeoTube(0.0, dr, dz);`
- Description: Memory allocated with new but not deleted: tube

**/workspace/Analyses/src/GeomVis_module.cc:188**
- Severity: high
- Code: `TGeoRotation *rot = new TGeoRotation();`
- Description: Memory allocated with new but not deleted: rot

**/workspace/Analyses/src/GeomVis_module.cc:192**
- Severity: high
- Code: `TGeoVolume *vol = new TGeoVolume(name, tube, 0);`
- Description: Memory allocated with new but not deleted: vol

**/workspace/Analyses/src/GeomVis_module.cc:201**
- Severity: high
- Code: `if (!gApplication) gApplication = new TApplication("GeomVis",0,0);`
- Description: Memory allocated with new but not deleted: gApplication

**/workspace/Analyses/src/GeomVis_module.cc:212**
- Severity: high
- Code: `_frame = new TGMainFrame(gClient->GetRoot(), width, height);`
- Description: Memory allocated with new but not deleted: _frame

**/workspace/Analyses/src/GeomVis_module.cc:213**
- Severity: high
- Code: `_mainFrame = new TGHorizontalFrame(_frame, _frame->GetWidth(), _frame->GetHeight());`
- Description: Memory allocated with new but not deleted: _mainFrame

**/workspace/Analyses/src/GeomVis_module.cc:214**
- Severity: high
- Code: `_mainCanvas = new TRootEmbeddedCanvas("GeomVisCanvas",_mainFrame,width-200, height-100);`
- Description: Memory allocated with new but not deleted: _mainCanvas

**/workspace/Analyses/src/GeomVis_module.cc:218**
- Severity: high
- Code: `_mainPad = new TPad("mainPad","Detector", 0, 0, 1, 1, 5,1,1);`
- Description: Memory allocated with new but not deleted: _mainPad

... and 1276 more

### missing_return (362 occurrences)

**/workspace/Analyses/src/SelectPiMinusAtTS5_module.cc:72**
- Severity: high
- Code: `virtual bool beginRun(art::Run& run) { std::cout<<"AG: beginRun() called"<<std::endl; return true; }`
- Description: Function beginRun missing return statement

**/workspace/Analyses/src/ReadCaloDigi_module.cc:685**
- Severity: high
- Code: `}else if (diskId == 1){`
- Description: Function if missing return statement

**/workspace/Analyses/src/VMMonitor_module.cc:59**
- Severity: high
- Code: `} else if ( _everyEvent ){`
- Description: Function if missing return statement

**/workspace/Analyses/src/SensitiveTargetEnergyDumper_module.cc:340**
- Severity: high
- Code: `} else if (hitInputTagInstance == "ProductionTargetPositiveEndRing"){`
- Description: Function if missing return statement

**/workspace/Analyses/src/SensitiveTargetEnergyDumper_module.cc:347**
- Severity: high
- Code: `} else if (hitInputTagInstance == "ProductionTargetNegativeEndRing"){`
- Description: Function if missing return statement

**/workspace/Analyses/src/SensitiveTargetEnergyDumper_module.cc:354**
- Severity: high
- Code: `} else if (hitInputTagInstance == "ProductionTargetStartingCoreSection"){`
- Description: Function if missing return statement

**/workspace/Analyses/src/SensitiveTargetEnergyDumper_module.cc:361**
- Severity: high
- Code: `} else if (hitInputTagInstance == "ProductionTargetFinSection"){`
- Description: Function if missing return statement

**/workspace/Analyses/src/SensitiveTargetEnergyDumper_module.cc:368**
- Severity: high
- Code: `} else if (hitInputTagInstance == "ProductionTargetFinStartingSection"){`
- Description: Function if missing return statement

**/workspace/Analyses/src/SensitiveTargetEnergyDumper_module.cc:375**
- Severity: high
- Code: `} else if (hitInputTagInstance == "ProductionTargetFinTopSection" || hitInputTagInstance == "ProductionTargetFinTopStartingSection"){`
- Description: Function if missing return statement

**/workspace/Analyses/src/PrimaryProtonEnergyDumper_module.cc:300**
- Severity: high
- Code: `} else if (hitInputTagInstance == "ProductionTargetPositiveEndRing"){`
- Description: Function if missing return statement

**/workspace/Analyses/src/PrimaryProtonEnergyDumper_module.cc:308**
- Severity: high
- Code: `} else if (hitInputTagInstance == "ProductionTargetNegativeEndRing"){`
- Description: Function if missing return statement

**/workspace/Analyses/src/PrimaryProtonEnergyDumper_module.cc:315**
- Severity: high
- Code: `} else if (hitInputTagInstance == "ProductionTargetStartingCoreSection"){`
- Description: Function if missing return statement

**/workspace/Analyses/src/PrimaryProtonEnergyDumper_module.cc:322**
- Severity: high
- Code: `} else if (hitInputTagInstance == "ProductionTargetFinSection"){`
- Description: Function if missing return statement

**/workspace/Analyses/src/PrimaryProtonEnergyDumper_module.cc:329**
- Severity: high
- Code: `} else if (hitInputTagInstance == "ProductionTargetFinStartingSection"){`
- Description: Function if missing return statement

**/workspace/Analyses/src/PrimaryProtonEnergyDumper_module.cc:336**
- Severity: high
- Code: `} else if (hitInputTagInstance == "ProductionTargetFinTopSection" || hitInputTagInstance == "ProductionTargetFinTopStartingSection"){`
- Description: Function if missing return statement

**/workspace/Analyses/src/FilterVDHits_module.cc:71**
- Severity: high
- Code: `virtual bool beginRun(art::Run& run) { std::cout<<"AG: beginRun() called"<<std::endl; return true; }`
- Description: Function beginRun missing return statement

**/workspace/Analyses/src/pbars1hist_module.cc:49**
- Severity: high
- Code: `CLHEP::Hep3Vector mu2eToTarget_momentum(const CLHEP::Hep3Vector& mu2emom) {`
- Description: Function mu2eToTarget_momentum missing return statement

**/workspace/Analyses/src/CountPionDecays_module.cc:120**
- Severity: high
- Code: `} else if ( hasMu && !hasE ){`
- Description: Function if missing return statement

**/workspace/BTrkData/src/Doublet.cc:81**
- Severity: high
- Code: `else if (fNStrawHits < kMaxNHits) {`
- Description: Function if missing return statement

**/workspace/BTrkData/src/TrkStrawHit.cc:159**
- Severity: high
- Code: `} else if( _rdrift > _rstraw){`
- Description: Function if missing return statement

... and 342 more

### uninitialized_variable (1676 occurrences)

**/workspace/Analyses/src/TSTrackAna_module.cc:251**
- Severity: medium
- Code: `if (fabs(delta) < _mapTrkDelta[id]) {`
- Description: Member variable _mapTrkDelta may be uninitialized

**/workspace/Analyses/src/KineticFracAnalysis_module.cc:936**
- Severity: medium
- Code: `if (_cluCogZ[bestCluster[trackNumber]] > 1800.) {break;}`
- Description: Member variable _cluCogZ may be uninitialized

**/workspace/Analyses/src/KineticFracAnalysis_module.cc:1010**
- Severity: medium
- Code: `if (bestZ < 2000.){_hFracOnEdgeFaceAndClusterInFront->Fill(_cluEnergy[bestCluster[trackNumber]]/trk.momentum(pathLength).mag());}`
- Description: Member variable _hFracOnEdgeFaceAndClusterInFront may be uninitialized

**/workspace/Analyses/src/KineticFracAnalysis_module.cc:1011**
- Severity: medium
- Code: `if (bestZ > 2000.){_hFracOnEdgeFaceAndClusterInBack->Fill(_cluEnergy[bestCluster[trackNumber]]/trk.momentum(pathLength).mag());`
- Description: Member variable _hFracOnEdgeFaceAndClusterInBack may be uninitialized

**/workspace/Analyses/src/KineticFracAnalysis_module.cc:1185**
- Severity: medium
- Code: `if (event.getByLabel(_shLabel,strawhitsH)) {`
- Description: Member variable _shLabel may be uninitialized

**/workspace/Analyses/src/KineticFracAnalysis_module.cc:1195**
- Severity: medium
- Code: `if (event.getByLabel(_shpLabel,shposH)) {`
- Description: Member variable _shpLabel may be uninitialized

**/workspace/Analyses/src/KineticFracAnalysis_module.cc:1205**
- Severity: medium
- Code: `if (event.getByLabel(_shfLabel,shflagH)) {`
- Description: Member variable _shfLabel may be uninitialized

**/workspace/Analyses/src/KineticFracAnalysis_module.cc:1215**
- Severity: medium
- Code: `if (event.getByLabel(_bkfLabel,bkflagH)) {`
- Description: Member variable _bkfLabel may be uninitialized

**/workspace/Analyses/src/ReadPSVacuum_module.cc:57**
- Severity: medium
- Code: `pdg_save.insert(pdg_ids[i]);`
- Description: Member variable _save may be uninitialized

**/workspace/Analyses/src/CaloDigiAna_module.cc:42**
- Severity: medium
- Code: `TH1F*       _hNCaloDigi;`
- Description: Member variable _hNCaloDigi may be uninitialized

**/workspace/Analyses/src/CaloDigiAna_module.cc:43**
- Severity: medium
- Code: `TH1F*       _hCDT0;`
- Description: Member variable _hCDT0 may be uninitialized

**/workspace/Analyses/src/CaloDigiAna_module.cc:44**
- Severity: medium
- Code: `TH1F*       _hCDROId;`
- Description: Member variable _hCDROId may be uninitialized

**/workspace/Analyses/src/CaloDigiAna_module.cc:45**
- Severity: medium
- Code: `TH1F*       _hCDPeakPos;`
- Description: Member variable _hCDPeakPos may be uninitialized

**/workspace/Analyses/src/CaloDigiAna_module.cc:46**
- Severity: medium
- Code: `TH1F*       _hCDAmp;`
- Description: Member variable _hCDAmp may be uninitialized

**/workspace/Analyses/src/CaloDigiAna_module.cc:47**
- Severity: medium
- Code: `TH1F*       _hNSamplesPerDigi ;`
- Description: Member variable _hNSamplesPerDigi may be uninitialized

**/workspace/Analyses/src/CaloDigiAna_module.cc:48**
- Severity: medium
- Code: `TH1F*       _hNSamplesPerEvent;`
- Description: Member variable _hNSamplesPerEvent may be uninitialized

**/workspace/Analyses/src/CaloDigiAna_module.cc:50**
- Severity: medium
- Code: `// TH2F*       _hNSamplesVsRadius;`
- Description: Member variable _hNSamplesVsRadius may be uninitialized

**/workspace/Analyses/src/CaloDigiAna_module.cc:51**
- Severity: medium
- Code: `// TH2F*       _hNHitsVsRadius   ;`
- Description: Member variable _hNHitsVsRadius may be uninitialized

**/workspace/Analyses/src/CaloDigiAna_module.cc:149**
- Severity: medium
- Code: `_histDisk[diskId]._hCDT0           ->Fill(caloDigi->t0());`
- Description: Member variable _histDisk may be uninitialized

**/workspace/Analyses/src/CaloDigiAna_module.cc:150**
- Severity: medium
- Code: `_histDisk[diskId]._hCDROId         ->Fill(roId);`
- Description: Member variable _histDisk may be uninitialized

... and 1656 more

### use_after_free (25 occurrences)

**/workspace/Analyses/src/InteractiveRoot_module.cc:13**
- Severity: high
- Code: `//    delete the TApplication at end of job.  In this module, the test`
- Description: Pointer the deleted but may be used later

**/workspace/BTrkData/src/TrkCaloHit.cc:42**
- Severity: high
- Code: `// delete the trajectory`
- Description: Pointer the deleted but may be used later

**/workspace/BTrkData/src/TrkCaloHit.cc:43**
- Severity: high
- Code: `delete _hittraj;`
- Description: Pointer _hittraj deleted but may be used later

**/workspace/BTrkData/src/TrkStrawHit.cc:70**
- Severity: high
- Code: `// delete the trajectory`
- Description: Pointer the deleted but may be used later

**/workspace/CalPatRec/src/HlPrint_ComboHit.cc:52**
- Severity: high
- Code: `delete HlPrint::_Instance;`
- Description: Pointer HlPrint deleted but may be used later

**/workspace/CalPatRec/src/DeltaFinderAlg_findProtons.cc:173**
- Severity: high
- Code: `printf("* DeltaFinderAlg::%s:001: overlapping hits hits proton segments %3i:%3i, delete them from %3i\n",`
- Description: Pointer them deleted but may be used later

**/workspace/EventDisplay/src/EventDisplayFrame.cc:709**
- Severity: high
- Code: `delete _legendBox[i];`
- Description: Pointer _legendBox deleted but may be used later

**/workspace/EventDisplay/src/EventDisplayFrame.cc:710**
- Severity: high
- Code: `delete _legendText[i];`
- Description: Pointer _legendText deleted but may be used later

**/workspace/EventDisplay/src/EventDisplayFrame.cc:744**
- Severity: high
- Code: `delete _legendParticleGroup[i];`
- Description: Pointer _legendParticleGroup deleted but may be used later

**/workspace/EventDisplay/src/EventDisplayFrame.cc:745**
- Severity: high
- Code: `delete _legendParticleLine[i];`
- Description: Pointer _legendParticleLine deleted but may be used later

**/workspace/EventDisplay/src/EventDisplayFrame.cc:746**
- Severity: high
- Code: `delete _legendParticleText[i];`
- Description: Pointer _legendParticleText deleted but may be used later

**/workspace/Mu2eBTrk/src/DetStrawElem.cc:34**
- Severity: high
- Code: `delete _wtraj;`
- Description: Pointer _wtraj deleted but may be used later

**/workspace/Mu2eG4/src/Mu2eWorld.cc:797**
- Severity: high
- Code: `// G4 takes ownership and will delete the detectors at the job end`
- Description: Pointer the deleted but may be used later

**/workspace/Mu2eG4/src/Mu2eG4WorkerRunManager.cc:279**
- Severity: high
- Code: `delete anEvent;`
- Description: Pointer anEvent deleted but may be used later

**/workspace/Mu2eG4/src/HelicalProtonAbsorber.cc:137**
- Severity: high
- Code: `delete pabs_phys;`
- Description: Pointer pabs_phys deleted but may be used later

**/workspace/Mu2eG4/src/HelicalProtonAbsorber.cc:138**
- Severity: high
- Code: `delete pabs_logic;`
- Description: Pointer pabs_logic deleted but may be used later

**/workspace/Mu2eG4/src/HelicalProtonAbsorber.cc:139**
- Severity: high
- Code: `delete pabs_solid;`
- Description: Pointer pabs_solid deleted but may be used later

**/workspace/Sources/src/FromSTMTestBeamData_source.cc:250**
- Severity: high
- Code: `// art takes ownership of the object pointed to by outSR and will delete it at the appropriate time.`
- Description: Pointer it deleted but may be used later

**/workspace/Sources/src/FromCorsikaBinary_source.cc:181**
- Severity: high
- Code: `// art takes ownership of the object pointed to by outSR and will delete it at the appropriate time.`
- Description: Pointer it deleted but may be used later

**/workspace/Sources/src/PBISequence_source.cc:227**
- Severity: high
- Code: `// art takes ownership of the object pointed to by outSR and will delete it at the appropriate time.`
- Description: Pointer it deleted but may be used later

... and 5 more

