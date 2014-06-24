import FWCore.ParameterSet.Config as cms
import copy

##############################
##### List of triggers   #####
##############################

triggersJetMet = cms.vstring(
    "HLT_MonoCentralPFJet80_PFMETnoMu95_NHEF0p95_v",
    "HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_v",
    "emulateHLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95",
    "HLT_MET120_HBHENoiseCleaned_v",
    )

#triggerMonoCentralPFJet80_PFMETnoMu95_NHEF0p95 = cms.vstring(
triggersJetMet95 = cms.vstring(
    "HLT_MonoCentralPFJet80_PFMETnoMu95_NHEF0p95_v",
    
    )

triggersJetMet95Met120 = cms.vstring(
        "HLT_MonoCentralPFJet80_PFMETnoMu95_NHEF0p95_v",
        "HLT_MET120_HBHENoiseCleaned_v",    
            )
triggersJetMet105 = cms.vstring(
    "HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_v",
    "emulateHLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95",
    )

triggersJetMet105Met120 = cms.vstring(
        "HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_v",
        "emulateHLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95",
        "HLT_MET120_HBHENoiseCleaned_v",
            )

triggersJetMet95105 = cms.vstring(
        "HLT_MonoCentralPFJet80_PFMETnoMu95_NHEF0p95_v",
        "HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_v",
        "emulateHLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95",
            )
triggersMet120 = cms.vstring(
    "HLT_MET120_HBHENoiseCleaned_v",
    )

triggersMet80 = cms.vstring(
    "HLT_MonoCentralPFJet80_PFMETnoMu95_NHEF0p95_v",
    "HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_v",
    "HLT_MET120_HBHENoiseCleaned_v",
    "HLT_MET80_v", 
    )

triggersJet80 = cms.vstring(
    "HLT_PFJet80_v", 
)


triggersSinglePhoton = cms.vstring(
     "HLT_Photon135_v", 
        )
# Choose triggers by going to http://j2eeps.cern.ch/cms-project-confdb-hltdev/browser
# Select online/2012/8e33/v2.1.
# Take all the single electron triggers than are unprescaled and do not have extra strange requirements.  
triggersSingleMu = cms.vstring(
    "HLT_IsoMu24_eta2p1_v",  
    #    "HLT_IsoMu24_v",  # Not available in 2012A  
    )

triggerDoubleMu = cms.vstring(
    "HLT_Mu17_Mu8_v",  
    )

triggersJetMetOrSingleMu = copy.deepcopy(triggersJetMet)  
triggersJetMetOrSingleMu.extend(["HLT_IsoMu24_eta2p1_v"])  


triggersSingleElec = cms.vstring(
    "HLT_Ele27_WP80_v",
    )
triggersDoubleMu = cms.vstring(
    "HLT_DoubleMu11_Acoplanarity03_v",
    "HLT_DoubleMu14_Mass8_PFMET40_v",
    "HLT_DoubleMu14_Mass8_PFMET50_v",
    "HLT_DoubleMu3_4_Dimuon5_Bs_Central_v",
    "HLT_DoubleMu3p5_4_Dimuon5_Bs_Central_v",
    "HLT_DoubleMu3p5_LowMassNonResonant_Displaced_v",
    "HLT_DoubleMu3p5_LowMass_Displaced_v",
    "HLT_DoubleMu4_Acoplanarity03_v",
    "HLT_DoubleMu4_Dimuon7_Bs_Forward_v",
    "HLT_DoubleMu4_JpsiTk_Displaced_v",
    "HLT_DoubleMu4_Jpsi_Displaced_v",
    "HLT_DoubleMu5_Ele8_CaloIdT_TrkIdVL_v",
    "HLT_DoubleMu5_IsoMu5_v",
    "HLT_DoubleMu8_Ele8_CaloIdT_TrkIdVL_v",
    )
##########################
##### List of cuts   #####
##########################

##### List of valid input collections #####
# jets, muons, electrons, taus, photons, mets,
# events, tracks, primaryvertexs,
# genjets, mcparticles,
# bxlumis, superclusters 

######################
#-- Cuts on  Event --#
######################
cutEvtFilterScraping = cms.PSet (
    inputCollection = cms.string("events"),
    cutString = cms.string("FilterOutScraping > 0"),
    numberRequired = cms.string(">= 1"),
    )
cutEvtCSCHaloTight = cms.PSet (
    inputCollection = cms.string("events"),
    cutString = cms.string("CSCTightHaloId == 0"),
    numberRequired = cms.string(">= 1"),
    )
cutEvtCSCHaloLoose = cms.PSet (
    inputCollection = cms.string("events"),
    cutString = cms.string("CSCLooseHaloId == 0"),
    numberRequired = cms.string(">= 1"),
    )
cutEvtHBHENoiseFilter = cms.PSet (
    inputCollection = cms.string("events"),
    cutString = cms.string("HBHENoiseFilter == 1"),
    numberRequired = cms.string(">= 1"),
    )
cutEvtHcalNoiseFilter = cms.PSet (
    inputCollection = cms.string("events"),
    cutString = cms.string("hcalnoiseTight == 1"),
    numberRequired = cms.string(">= 1"),
    )
cutHltPt = cms.PSet (
    inputCollection = cms.string("mets"),
    cutString = cms.string("hltPt > 0"),
    numberRequired = cms.string(">= 1"),
    )
cutHlt105 = cms.PSet (
    inputCollection = cms.string("mets"),
    cutString = cms.string("hlt105 > 0"),
    numberRequired = cms.string(">= 1"),
    )


################################
#-- Cuts on Primary Vertexes --#
################################
cutVtxGood = cms.PSet (
    inputCollection = cms.string("primaryvertexs"),
    cutString = cms.string("isGood > 0"),
    numberRequired = cms.string(">= 1"),
    )
###################
#-- Cuts on MET --#
###################
cutMET220 = cms.PSet (
    inputCollection = cms.string("mets"),
    cutString = cms.string("pt > 220"),
    numberRequired = cms.string(">= 1"),
    )
cutMetSig = cms.PSet (
    inputCollection = cms.string("mets"),
    cutString = cms.string("significance > 10"),
    numberRequired = cms.string(">= 1"),
    )
cutMET = cms.PSet (
    inputCollection = cms.string("mets"),
    cutString = cms.string("pt > 100"),
    numberRequired = cms.string(">= 1"),
    )

cutL1MET = cms.PSet (
    inputCollection = cms.string("mets"),
    cutString = cms.string("l1Pt > 30"),
    numberRequired = cms.string(">= 1"),
    )

cutMetDeltaPhiMin2Jets = cms.PSet (
    inputCollection = cms.string("mets"),
    cutString = cms.string("fabs(deltaPhiMin2Jets) > 1.5"),
    numberRequired = cms.string(">= 1"),
    )
cutMetDeltaPhiMin2Jets0p5 = cms.PSet (
    inputCollection = cms.string("mets"),
    cutString = cms.string("fabs(deltaPhiMin2Jets) > 0.5"),
    numberRequired = cms.string(">= 1"),
    )
cutMETNoMu = cms.PSet (
    inputCollection = cms.string("mets"),
    cutString = cms.string("metNoMu > 100"),
    numberRequired = cms.string(">= 1"),
    )
cutMETNoMu220 = cms.PSet (
    inputCollection = cms.string("mets"),
    cutString = cms.string("metNoMu > 220"),
    numberRequired = cms.string(">= 1"),
    )
cutMETNoElec = cms.PSet (
    inputCollection = cms.string("mets"),
    cutString = cms.string("metNoElec > 220"),
    numberRequired = cms.string(">= 1"),
    )
cutMET20 = cms.PSet(
    inputCollection = cms.string("mets"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 1"),
    )
cutMET30 = cms.PSet (
    inputCollection = cms.string("mets"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 1"),
    )
cutMET40 = cms.PSet (
    inputCollection = cms.string("mets"),
    cutString = cms.string("pt > 40"),
    numberRequired = cms.string(">= 1"),
    )
cutMET50 = cms.PSet(
    inputCollection = cms.string("mets"),
    cutString = cms.string("pt > 50"),
    numberRequired = cms.string(">= 1"),
    )
cutMET75 = cms.PSet(
    inputCollection = cms.string("mets"),
    cutString = cms.string("pt > 75"),
    numberRequired = cms.string(">= 1"),
    )
cutMET90 = cms.PSet(
    inputCollection = cms.string("mets"),
    cutString = cms.string("pt > 90"),
    numberRequired = cms.string(">= 1"),
    )
cutMET100 = cms.PSet(
    inputCollection = cms.string("mets"),
    cutString = cms.string("pt > 100"),
    numberRequired = cms.string(">= 1"),
    )
cutMET200 = cms.PSet (
    inputCollection = cms.string("mets"),
    cutString = cms.string("pt > 200"),
    numberRequired = cms.string(">= 1"),
    )
cutMaxMET200 = cms.PSet (
    inputCollection = cms.string("mets"),
    cutString = cms.string("pt < 200"),
    numberRequired = cms.string(">= 1"),
    )
cutMaxMET100 = cms.PSet (
    inputCollection = cms.string("mets"),
    cutString = cms.string("pt < 100"),
    numberRequired = cms.string(">= 1"),
    )

###############################
#-- Cuts on Trigger Objects --#
###############################
cutL1MET100 = cms.PSet (
    inputCollection = cms.string("trigobjs"),
    cutString = cms.string("pt > 100"),
    numberRequired = cms.string(">= 1"),
    )
cutMaxL1MET100 = cms.PSet (
    inputCollection = cms.string("trigobjs"),
    cutString = cms.string("pt < 100"),
    numberRequired = cms.string(">= 1"),
    )
####################
#-- Cuts on Jets --#
####################
cutSubLeadingJetID = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("disappTrkSubLeadingJetID > 0"),
    numberRequired = cms.string(">= 1"),
    )
cutSubLeadingJetIDFilter = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("disappTrkSubLeadingJetID > 0"),
    numberRequired = cms.string(">= 0"),
    )
cutBTagVeto = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("btagCombinedSecVertex > 0.679"),
    numberRequired = cms.string("= 0"),
    )
cutJetPt = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("pt > 110"),
    numberRequired = cms.string(">= 1"),
    )
cutJetPt150 = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("pt > 150"),
    numberRequired = cms.string(">= 1"),
    )


cutSecJetPt150 = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("pt > 150"),
    numberRequired = cms.string(">= 1"),
    )

cutJetLeadingPt = cms.PSet(
    inputCollection = cms.string("jets"),
    cutString = cms.string("isLeadingPtJet == 1"),
    numberRequired = cms.string(">= 0"),
    )
cutSecJetLeadingPtFilter = cms.PSet(
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("isLeadingPtJet == 1"),
    numberRequired = cms.string(">= 0"),
    )
cutSecJetLeadingPt = cms.PSet(
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("isLeadingPtJet == 1"),
    numberRequired = cms.string(">= 1"),
#    numberRequired = cms.string("= 1"),
    )
cutJetPt20 = cms.PSet(
    inputCollection = cms.string("jets"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 1"),
    )
cutJetPt30Filter = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 0"),
    )
cutJetPt30 = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 1"),
    )
cutJetPt45 = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("pt > 45"),
    numberRequired = cms.string(">= 1"),
    )
cutJetPt50 = cms.PSet(
    inputCollection = cms.string("jets"),
    cutString = cms.string("pt > 50"),
    numberRequired = cms.string(">= 1"),
    )
cutJetPt75 = cms.PSet(
    inputCollection = cms.string("jets"),
    cutString = cms.string("pt > 75"),
    numberRequired = cms.string(">= 1"),
    )
cutJetPt100 = cms.PSet(
    inputCollection = cms.string("jets"),
    cutString = cms.string("pt > 100"),
    numberRequired = cms.string(">= 1"),
    )
cutJetEta = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("fabs(eta) < 2.4"),
    numberRequired = cms.string(">= 1"),
    )
cutJetEta2p5Filter = cms.PSet (  # Use to filter jet collection but not reject events  
    inputCollection = cms.string("jets"),
    cutString = cms.string("fabs(eta) < 2.5"), 
    numberRequired = cms.string(">= 0"),
    )
cutJetEta2p6Filter = cms.PSet (  # Use to filter jet collection but not reject events  
    inputCollection = cms.string("jets"),
    cutString = cms.string("fabs(eta) < 2.6"),  # take from AN2012_421_v6, p. 2  
    numberRequired = cms.string(">= 0"),
    )
cutJetEta2p4 = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("fabs(eta) < 2.4"),
    numberRequired = cms.string(">= 1"),
    )

cutJetEta4p5 = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("fabs(eta) < 4.5"),
    numberRequired = cms.string(">= 1"),
    )
cutJetEta5Filter = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("fabs(eta) < 5.0"),
    numberRequired = cms.string(">= 0"),
    )
cutJetEta2p8 = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("fabs(eta) < 2.8"),
    numberRequired = cms.string(">= 1"),
    )
cutJetVetoDPhiMet = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("fabs(dPhiMet) < 1.5"),
    numberRequired = cms.string("== 0"),
    isVeto = cms.bool(True),  
    )
cutJetEta2p4Filter = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("fabs(eta) < 2.4"),
    numberRequired = cms.string(">= 0"),
    )
cutJetIDLooseFilter = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("jetIDLoose > 0"),
    numberRequired = cms.string(">= 0"),
    )
cutJetBeta0p2Filter = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("beta > 0.2"),
    numberRequired = cms.string(">= 0"),
    )
cutJetBTagCSVMediumVeto = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("btagCombinedSecVertex > 0.679"),  # From https://twiki.cern.ch/twiki/bin/viewauth/CMS/BTagPerformanceOP#B_tagging_Operating_Points_for_5  
    numberRequired = cms.string("== 0"),
    isVeto = cms.bool(True), 
    )
cutJetPt30NJet1 = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string("== 1"),
    )
cutJetPt30NJet2 = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("pt > 30c"),
    numberRequired = cms.string("== 2"),
    )
cutJetPt30NJet3 = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string("== 3"),
    )
cutJetPt30NJet4 = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 4"),
    )
cutNJet1Min = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string(">= 1"),
    )
cutNJet1Exact = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("== 1"),
    )
cutNJet2Exact = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("== 2"),
    )
cutNJets = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("<= 2"),
    )
cutNoForwardJets = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("fabs(eta) > 3"),
    numberRequired = cms.string("= 0"),
    )
cutJetNoiseChgHad = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("chargedHadronEnergyFraction > 0.2"),
#    cutString = cms.string("chargedHadronEnergyFraction > 0"),
    numberRequired = cms.string(">= 1"),
    )
cutJetNoiseChgEM  = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("chargedEmEnergyFraction < 0.5"),
    numberRequired = cms.string(">= 1"),
    )
cutJetNoiseNeuEM = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("neutralEmEnergyFraction < 0.7"),
    numberRequired = cms.string(">= 1"),
    )
cutJetNoiseNeuHad = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("neutralHadronEnergyFraction < 0.7"),
    numberRequired = cms.string(">= 1"),
    )
cutJetNoiseNeuHad95Filter = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("neutralHadronEnergyFraction < 0.95"),
    numberRequired = cms.string(">= 0"),
    )
cutJetDeltaRMuonPt20Filter = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("deltaRMuonPt20 > 0.4"),
    numberRequired = cms.string(">= 0"),
    )
##############################
#-- Cuts on Secondary Jets --#
##############################
cutLeadingJetID = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("disappTrkLeadingJetID > 0"),
    numberRequired = cms.string(">= 1"),
    )
cutSecJetBTagVeto = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("btagCombinedSecVertex > 0.679"),
    numberRequired = cms.string("= 0"),
    )
cutSecJetPt = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("pt > 110"),
    numberRequired = cms.string(">= 1"),
    )
cutSecJetPt90 = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("pt > 90"),
    numberRequired = cms.string(">= 1"),
    )
cutSecJetPt150 = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("pt > 150"),
    numberRequired = cms.string(">= 1"),
    )
cutSecJetEta2p4 = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("fabs(eta) < 2.4"),
    numberRequired = cms.string(">= 1"),
    )
cutSecJetEta2p8 = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("fabs(eta) < 2.8"),
    numberRequired = cms.string(">= 1"),
    )
cutSecJetNoiseChgHad = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("chargedHadronEnergyFraction > 0.2"),
    numberRequired = cms.string(">= 1"),
    )
cutSecJetNoiseChgEM  = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("chargedEmEnergyFraction < 0.5"),
    numberRequired = cms.string(">= 1"),
    )
cutSecJetNoiseNeuEM = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("neutralEmEnergyFraction < 0.7"),
    numberRequired = cms.string(">= 1"),
    )
cutSecJetNoiseNeuHad = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("neutralHadronEnergyFraction < 0.7"),
    numberRequired = cms.string(">= 1"),
    )
cutSecJetPt30NJet1 = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string("== 1"),
    )
cutSecJetPt30NJet2 = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string("== 2"),
    )
cutSecJetPt30NJet3 = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string("== 3"),
    )
cutSecJetPt30NJet4 = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 4"),
    )
cutSecJetBTagVeto = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("btagCombinedSecVertex > 0.679"),
    numberRequired = cms.string("= 0"),
    )
## cutSecJetNoiseChgHad = cms.PSet (
##     inputCollection = cms.string("secondary jets"),
##     cutString = cms.string("chargedHadronEnergyFraction > 0.2"),
##     numberRequired = cms.string(">= 1"),
##     )
## cutSecJetNoiseNeuEM = cms.PSet (
##     inputCollection = cms.string("secondary jets"),
##     cutString = cms.string("neutralEmEnergyFraction < 0.7"),
##     numberRequired = cms.string(">= 1"),
##     )
## cutSecJetNoiseChgEM = cms.PSet (
##     inputCollection = cms.string("secondary jets"),
##     cutString = cms.string("chargedEmEnergyFraction < 0.5"),
##     numberRequired = cms.string(">= 1"),
##     )
## cutSecJetNoiseNeuHad = cms.PSet (
##     inputCollection = cms.string("secondary jets"),
##     cutString = cms.string("neutralHadronEnergyFraction < 0.7"),
##     numberRequired = cms.string(">= 1"),
##     )

#############################
#-- Cuts on Jet-Jet Pairs --#
#############################
cutJetJetDPhi = cms.PSet (
    inputCollection = cms.string("jet-jet pairs"),
    cutString = cms.string("deltaPhi > 2.5"),
    numberRequired = cms.string("= 0"),
    isVeto = cms.bool(True),
    )
######################
#-- Cuts on Tracks --#
######################
cutTrkPt = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("pt > 50"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkPt10 = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("pt > 10"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkPt15 = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("pt > 15"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkPt20 = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkPt30 = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkPt50 = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("pt > 50"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkPt75 = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("pt > 75"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkPtError = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("ptErrorByPt < 0.2"),
    numberRequired = cms.string(">= 1"),
    )

cutTrkDPhiMet = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(dPhiMet) < 1.5"),
    numberRequired = cms.string(">= 1"),
    )

cutMinTrkDPhiMet = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(dPhiMet) > 1.5"),
    numberRequired = cms.string(">= 1"),
    )

cutTrkChi2Norm1p6 = cms.PSet(
    # ndof is defined in:
    # https://cmssdt.cern.ch/SDT/lxr/source/RecoTracker/TrackProducer/src/TrackProducerAlgorithm.cc?v=CMSSW_5_3_3#073
    # A track with 6 hits, 3 pixel and 3 strip hits, each with weight 1.0, would have:
    # ndof = 3*3 + 3*2 - 5 = 10
    # In that case, the chi2 probability will be >10% if normalizedChi2 < 1.6:
    # root [11] TMath::Prob(16, 10)
    # (Double_t)9.96324004870459551e-02 
    inputCollection = cms.string("tracks"),
    cutString = cms.string("normChi2 < 1.6"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkEta = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("fabs(eta) < 2.1"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkEta2p3 = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("fabs(eta) < 2.3"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkEtaBarrel = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("fabs(eta) < 0.8"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkEcalGap1 = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("detectorEta > -1.14018 || detectorEta < -1.1439"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkEcalGap2 = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("detectorEta > -0.791884 || detectorEta < -0.796051"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkEcalGap3 = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("detectorEta > -0.44356 || detectorEta < -0.447911"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkEcalGap4 = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("detectorEta > 0.00238527 || detectorEta <  -0.00330793"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkEcalGap5 = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("detectorEta > 0.446183 || detectorEta < 0.441949"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkEcalGap6 = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("detectorEta > 0.793955 || detectorEta < 0.789963"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkEcalGap7 = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("detectorEta > 1.14164 || detectorEta < 1.13812"),
    numberRequired = cms.string(">= 1"),
    )


cutTrkWheel0GapVeto = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("fabs(eta) < 0.15 | fabs(eta) > 0.35"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkEtaMuonPk = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("fabs(eta) < 1.55 | fabs(eta) > 1.85"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkEtaAtlas = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("fabs(eta) < 1.9 && fabs(eta) > 0.1"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkEtaAtlasVeto = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("fabs(eta) < 1.35 || fabs(eta) > 1.75"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkD0 = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("fabs(d0wrtPV) < 0.02"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkD0Atlas = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("fabs(d0wrtPV) < 0.01"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkD0Inv = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("fabs(d0wrtPV) > 0.02 && fabs(d0wrtPV) < 0.22"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkDZ = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("fabs(dZwrtPV) < 0.5"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkDZSinTheta = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("fabs(dZSinTheta) < 0.05"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkDZInv = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("fabs(dZwrtPV) > 0.5 && fabs(dZwrtPV) < 5.5"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkNHits = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("numValidHits >= 7"),
#    cutString = cms.string("numValidHits == 7"),
    numberRequired = cms.string(">= 1"),
    )
#cutTrkNHits7 = cms.PSet(
#    inputCollection= cms.string("tracks"),
#    cutString = cms.string("numValidHits >= 7"),
#    numberRequired = cms.string(">= 1"),
#    )
cutTrkNHitsIs7 = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("numValidHits == 7"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkNHitsIs6 = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("numValidHits == 6"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkNHitsIs5 = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("numValidHits == 5"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkNHitsIs4 = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("numValidHits == 4"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkNHitsIs3 = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("numValidHits == 3"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkNHits4Min = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("numValidHits >= 4"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkNHits3Min = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("numValidHits >= 3"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkHitMissMid = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("nHitsMissingMiddle == 0"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkHitMissMidInv = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("nHitsMissingMiddle >= 1"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkHitMissIn = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("nHitsMissingInner == 0"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkHitMissInDebug = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("nHitsMissingInner >= 1"),
    numberRequired = cms.string("= 0"),
    #    isVeto = cms.bool(True),  
    )
cutTrkIso = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("isIso == 1"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkRelIsoRp3 = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("trkRelIsoRp3 < 0.05"), 
    numberRequired = cms.string(">= 1"),
    )
cutTrkRelIsoRp3Atlas = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("trkRelIsoRp3 < 0.04"), 
    numberRequired = cms.string(">= 1"),
    )
cutTrkRelIsoRp3Debug = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("trkRelIsoRp3 > 0.05"), 
    numberRequired = cms.string("= 0"),
    isVeto = cms.bool(True),  
    )
cutTrkDeadEcalVeto =  cms.PSet (
    inputCollection = cms.string("tracks"),
#    cutString = cms.string("isMatchedDeadEcal == 0"),
    cutString = cms.string("isMatchedDeadEcalDet == 0"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkBadCSCVeto =  cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("isMatchedBadCSC == 0"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkBadCSCVetoInv =  cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("isMatchedBadCSC == 1"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkCrackVeto = cms.PSet (
    inputCollection = cms.string("tracks"),
#    cutString = cms.string("fabs(eta) < 1.42 | fabs(eta) > 1.65"),
    cutString = cms.string("fabs(detectorEta) < 1.42 | fabs(detectorEta) > 1.65"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkDeadEcalMatch = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("isMatchedDeadEcal == 1"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkSumPtGT = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("depTrkRp5MinusPt > 7"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkSumPtLT = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("depTrkRp5MinusPt <= 7"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkHitMissOut = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("nHitsMissingOuter >= 3"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkHitMissOut6 = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("nHitsMissingOuter >= 6"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkHitMissOut7 = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("nHitsMissingOuter >= 7"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkHitMissOut8 = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("nHitsMissingOuter >= 8"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkHitMissOutInv = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("nHitsMissingOuter <= 2"),
    numberRequired = cms.string(">= 1"),
    )
cutMaxMissOut = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("nHitsMissingOuter <= 2"),
    numberRequired = cms.string(">= 1"),
    )
cutMaxCaloByP = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("caloTotDeltaRp5ByP < 0.1"),
    numberRequired = cms.string(">= 1"),
    )
cutMaxCaloByPLoose = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("caloTotDeltaRp5ByP < 0.5"),
    numberRequired = cms.string(">= 1"),
    )
cutMaxCaloTight = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("caloTotDeltaRp5 < 5"),
    numberRequired = cms.string(">= 1"),
    )
cutMaxCalo10 = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("caloTotDeltaRp5RhoCorr < 10"),
    numberRequired = cms.string(">= 1"),
    )
cutMaxCalo10Inv = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("caloTotDeltaRp5RhoCorr > 10"),
    numberRequired = cms.string(">= 1"),
    )
cutMaxCaloLoose = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("caloTotDeltaRp5 < 30"),
    numberRequired = cms.string(">= 1"),
    )
cutMaxCaloPUCorr = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("caloTotDeltaRp5RhoCorr < 20"),
    numberRequired = cms.string(">= 1"),
    )
cutMaxCaloPUCorrBlind = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("caloTotDeltaRp5RhoCorr > 20"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkHitMissOutCtrlReg = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("nHitsMissingOuter == 0"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkCharginoId = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedPdgId) == 1000024"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkSusyId = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedPdgId) > 1000001 && fabs(genMatchedPdgId) < 3160113"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkElectronId = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedPdgId) == 11"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkElecIdInv = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedPdgId) != 11"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkMuonId = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedPdgId) == 13"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkMuonIdInv = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedPdgId) != 13"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkTauId = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedPdgId) == 15"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkTauIdInv = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedPdgId) != 15"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkPionId =cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedPdgId) == 211"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkNotGenMatched = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedPdgId) == 0"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkNotGenMatchedInv = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedPdgId) != 0"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkLightMesonId =cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedId) == 15"),
    #  for bin indices, see OSUAnalysis::getPdgIdBinValue(int pdgId)
    numberRequired = cms.string(">= 1"),
    )
cutTrkKMesonId =cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedId) == 16"),
    #  for bin indices, see OSUAnalysis::getPdgIdBinValue(int pdgId)
    numberRequired = cms.string(">= 1"),
    )
cutTrkLightBaryonId =cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedId) == 19"),
    #  for bin indices, see OSUAnalysis::getPdgIdBinValue(int pdgId)
    numberRequired = cms.string(">= 1"),
    )
cutTrkKBaryonId =cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedId) == 20"),
    #  for bin indices, see OSUAnalysis::getPdgIdBinValue(int pdgId)
    numberRequired = cms.string(">= 1"),
    )
cutNoCuts = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string(">= 0"),
    )
cutTrkD0Side = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(d0wrtPV) > 0.1 && fabs(d0wrtPV) < 0.3"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkDZSide = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(dZwrtPV) > 0.05 && fabs(dZwrtPV) < 0.15"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkJetDeltaR = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("deltaRMinSubLeadJet > 0.5"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkJetDeltaRInv = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("deltaRMinSubLeadJet < 0.5"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkJetDeltaPhi = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("deltaPhiMaxSubLeadJet < 2.7"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkJetDeltaRAtlas = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("deltaRMinSubLeadJet > 0.4"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkJetDeltaPhi2p5 = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("deltaPhiMaxSubLeadJet < 2.5"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkJetDeltaPhi2p6 = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("deltaPhiMaxSubLeadJet < 2.6"),
    numberRequired = cms.string(">= 1"),
    )

cutTrkJetDeltaPhi2p7 = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("deltaPhiMaxSubLeadJet < 2.7"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkJetDeltaPhi2p8 = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("deltaPhiMaxSubLeadJet < 2.8"),
    numberRequired = cms.string(">= 1"),
    )

cutTrkJetDeltaPhi2p9 = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("deltaPhiMaxSubLeadJet < 2.9"),
    numberRequired = cms.string(">= 1"),
    )

###############################
#-- Cuts on Track-Jet pairs --#
###############################

#####################
#-- Cuts on Muons --#
#####################
cutMuonChgPos = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("charge == 1"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonChgNeg = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("charge == -1"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonEta = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("fabs(eta) < 2.1"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonEta2p5 = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("fabs(eta) < 2.5"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonEta2p1 = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("fabs(eta) < 2.1"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonPt20 = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonPt25 = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("pt > 25"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonTightID = cms.PSet (  # recommended by https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideMuonId#Tight_Muon 
    inputCollection = cms.string("muons"),
    cutString = cms.string("tightID > 0"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonLooseID = cms.PSet (  
    inputCollection = cms.string("muons"),
    cutString = cms.string("looseID > 0"),
    numberRequired = cms.string(">= 1"),
    )
cutOldMuonLooseIDVeto = cms.PSet (  
    inputCollection = cms.string("muons"),
    cutString = cms.string("looseID > 0"),
    numberRequired = cms.string("= 0"),
    )
## cutMuonLooseIDVeto = cms.PSet (  
##     inputCollection = cms.string("muon-track pairs"),
##     cutString = cms.string("deltaRLooseID < 0.15"),
##     numberRequired = cms.string("= 0"),
##     isVeto = cms.bool(True),  
##     )
cutMuonLooseIDVeto = cms.PSet (  
    inputCollection = cms.string("tracks"),
    cutString = cms.string("deltaRMinMuonLooseId > 0.15"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonLooseIDVetoInv = cms.PSet (  
    inputCollection = cms.string("tracks"),
    cutString = cms.string("deltaRMinMuonLooseId < 0.15"),
    numberRequired = cms.string(">= 1"),
    )
## cutMuonLooseIDVetoInv = cms.PSet ( 
##     inputCollection = cms.string("muons"),
##     cutString = cms.string("looseID > 0"),
##     numberRequired = cms.string(">= 1"),
##     )
cutMuonLooseIDOnlyOne = cms.PSet (  
    inputCollection = cms.string("muons"),
    cutString = cms.string("looseID > 0"),
    numberRequired = cms.string("= 1"),
    )
cutSecMuonLooseIDGlobalVeto = cms.PSet (  
    inputCollection = cms.string("tracks"),
    cutString = cms.string("deltaRMinSecMuonLooseIdGlobal > 0.15"), 
    numberRequired = cms.string(">= 1"),
    )
cutSecMuonLooseIDVeto = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("deltaRMinSecMuonLooseId > 0.15"),
    numberRequired = cms.string(">= 1"),
    )
## cutSecMuonLooseIDVeto = cms.PSet (  
##     inputCollection = cms.string("secondary muon-track pairs"),
##     cutString = cms.string("deltaRGlobalMuon < 0.15"), 
##     numberRequired = cms.string("= 0"),
##     isVeto = cms.bool(True),  
##     )
cutOldSecMuonLooseIDVeto = cms.PSet (  
     inputCollection = cms.string("secondary muons"),
     cutString = cms.string("looseID  > 0"),
     numberRequired = cms.string("= 0"),
     )
cutSecMuonLooseIDVetoInv = cms.PSet (  
    inputCollection = cms.string("secondary muons"),
    cutString = cms.string("isGlobalMuon  > 0"),
    numberRequired = cms.string(">= 1"),
    )
cutSecMuonLooseIDOnlyOne = cms.PSet (  
    inputCollection = cms.string("secondary muons"),
    cutString = cms.string("looseID > 0"),
    numberRequired = cms.string("= 1"),
    )
cutMuonDetIso = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("detIso < 0.05"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonPFIso = cms.PSet (  # recommended by https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideMuonId#Muon_Isolation_AN1
    inputCollection = cms.string("muons"),
    cutString = cms.string("relPFdBetaIso < 0.12"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonD0 = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("abs(correctedD0) < 0.02"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonDZ = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("abs(correctedDZ) < 0.02"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonValidHits = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("tkNumValidHits > 4"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonOneOnly = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("relPFdBetaIso < 0.12"), 
    numberRequired = cms.string("= 1"),
    )
cutMuonMetMT = cms.PSet(
    inputCollection = cms.string("muons"),
    cutString = cms.string("metMT < 40"),
    numberRequired = cms.string(">= 1"),
    )

cutMuonMetMTInverse = cms.PSet(
    inputCollection = cms.string("muons"),
    cutString = cms.string("metMT > 40"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonVeto = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("= 0"),
    )
cutMuonVetoPt10 = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("pt > 10"),
    numberRequired = cms.string("= 0"),
    )
cutSecMuonVetoPt10 = cms.PSet (
    inputCollection = cms.string("secondary muons"),
    cutString = cms.string("pt > 10"),
    numberRequired = cms.string("= 0"),
    )
cutMuonPlusMet220 = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("ptPlusMet > 220"),
    numberRequired = cms.string(">= 1"),
    )
###############################
#-- Cuts on Muon-Muon Pairs --#
###############################
cutMuonPairPt20 = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 2"),
    )
cutMuonPairPt25 = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("pt > 25"),
    numberRequired = cms.string(">= 2"),
    )
cutMuonPairEta = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("fabs(eta) < 2.5"),
    numberRequired = cms.string(">= 2"),
    )
cutMuonPairEta24 = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("fabs(eta) < 2.4"),
    numberRequired = cms.string(">= 2"),
    )
cutMuonPairTightID = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("tightID > 0"),
    numberRequired = cms.string(">= 2"),
    )
cutMuonPairDetIso = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("detIso < 0.05"),
    numberRequired = cms.string(">= 2"),
    )
cutMuonPairPFIso = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("relPFdBetaIso < 0.12"),
    numberRequired = cms.string(">= 2"),
    )
cutMuonPairPFIso15 = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("relPFdBetaIso < 0.15"),
    numberRequired = cms.string(">= 2"),
    )
cutMuonPairD0 = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("abs(correctedD0) < 0.02"),
    numberRequired = cms.string(">= 2"),
    )
cutMuonPairDZ = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("abs(correctedDZ) < 0.02"),
    numberRequired = cms.string(">= 2"),
    )
cutMuonPairValidHits = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("tkNumValidHits > 4"),
    numberRequired = cms.string(">= 2"),
    )
cutMuMuInvMass = cms.PSet (
    inputCollection = cms.string("muon-muon pairs"),
    cutString = cms.string("invMass > 80 & invMass < 100"),
    numberRequired = cms.string(">= 1"),
    )
cutMuMuInvMass81_101 = cms.PSet (
    inputCollection = cms.string("muon-muon pairs"),
    cutString = cms.string("invMass > 81 & invMass < 101"),
    numberRequired = cms.string(">= 1"),
    )
cutMuMuChargeProduct = cms.PSet (
    inputCollection = cms.string("muon-muon pairs"),
    cutString = cms.string("chargeProduct == -1"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonVetoThird =   cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("pt > 10"),
    numberRequired = cms.string("<= 2"),  
    )
################################
#-- Cuts on Muon-Track Pairs --#
################################
cutMuTrkChgOpp = cms.PSet (
    inputCollection = cms.string("muon-track pairs"),
    cutString = cms.string("chargeProduct == -1"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonTrkDRSame = cms.PSet (
    inputCollection = cms.string("muon-track pairs"),
    cutString = cms.string("deltaR < 0.15"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonTrkDRSameNone = cms.PSet (
    inputCollection = cms.string("muon-track pairs"),
    cutString = cms.string("deltaR < 0.15"),
    numberRequired = cms.string("= 0"),
    )
cutMuTrkDeltaRSame = cms.PSet(
    inputCollection = cms.string("muon-track pairs"),
    cutString = cms.string("deltaR < 0.15"),
    numberRequired = cms.string(">= 1"),
    )
cutMuTrkDeltaR = cms.PSet(
    inputCollection = cms.string("muon-track pairs"),
    cutString = cms.string("deltaR > 0.15"),
    numberRequired = cms.string(">= 1"),
    )
cutMuTrkDeltaRp5 = cms.PSet(
    inputCollection = cms.string("muon-track pairs"),
    cutString = cms.string("deltaR > 0.5"),
    numberRequired = cms.string(">= 1"),
    )
cutMuTrkInvMass = cms.PSet(
    inputCollection = cms.string("muon-track pairs"),
    cutString = cms.string("invMass > 40 & invMass < 75"),
    numberRequired = cms.string(">= 1"),
    )
cutMuTrkInvMass80To100 = cms.PSet(
    inputCollection = cms.string("muon-track pairs"),
    cutString = cms.string("invMass > 80 & invMass < 100"),
    numberRequired = cms.string(">= 1"),
    )
cutMuTrkInvMassTight = cms.PSet(
    inputCollection = cms.string("muon-track pairs"),
    cutString = cms.string("invMass > 40 & invMass < 185"),
    numberRequired = cms.string(">= 1"),
    )
cutMuTrkVeto = cms.PSet(
    inputCollection = cms.string("muon-track pairs"),
    cutString = cms.string("invMass < 80 | invMass > 100"),
    numberRequired = cms.string(">= 1"),
    )
##############################
#-- Cuts on Muon-Tau Pairs --#
##############################
cutMuTauInvMass = cms.PSet(
    inputCollection = cms.string("muon-tau pairs"),
    cutString = cms.string("invMass > 40 & invMass < 160"),
    numberRequired = cms.string(">= 1"),
    )
cutMuTauCharge = cms.PSet(
    inputCollection = cms.string("muon-tau pairs"),
    cutString = cms.string("chargeProduct == -1"),
    numberRequired = cms.string(">= 1"),
    )
cutMuTauDeltaR = cms.PSet(
    inputCollection = cms.string("muon-tau pairs"),
    cutString = cms.string("deltaR < 0.15"),
    numberRequired = cms.string(">= 1"),
    )
#########################
#-- Cuts on Electrons --#
#########################
cutElecPt20 = cms.PSet(
    inputCollection = cms.string("electrons"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 1"),
    )
cutElecPt25 = cms.PSet(
    inputCollection = cms.string("electrons"),
    cutString = cms.string("pt > 25"),
    numberRequired = cms.string(">= 1"),
    )
cutElecPt = cms.PSet(
    inputCollection = cms.string("electrons"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 1"),
    )
cutElecPt30 = cms.PSet(
    inputCollection = cms.string("electrons"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 1"),
    )
cutElecPt40 = cms.PSet(
    inputCollection = cms.string("electrons"),
    cutString = cms.string("pt > 40"),
    numberRequired = cms.string(">= 1"),
    )
cutElecEta = cms.PSet(
    inputCollection= cms.string("electrons"),
    cutString = cms.string("fabs(eta) < 2.5"),
    numberRequired = cms.string(">= 1"),
    )
cutElecD0 = cms.PSet(
    inputCollection= cms.string("electrons"),
    cutString = cms.string("fabs(correctedD0Vertex) < 0.02"),
    numberRequired = cms.string(">= 1"),
    )
cutElecDZ = cms.PSet(
    inputCollection= cms.string("electrons"),
    cutString = cms.string("fabs(correctedDZ) < 0.1"),
    numberRequired = cms.string(">= 1"),
    )
cutElecNHits = cms.PSet(
    inputCollection= cms.string("electrons"),
    cutString = cms.string("tkNumValidHits > 4"),
    numberRequired = cms.string(">= 1"),
    )

cutElecMetMTInverse = cms.PSet(
    inputCollection = cms.string("electrons"),
    cutString = cms.string("metMT > 40"),
    numberRequired = cms.string(">= 1"),
    )

cutElecMva = cms.PSet(  # See https://twiki.cern.ch/twiki/bin/view/CMS/MultivariateElectronIdentification#Triggering_MVA
    inputCollection= cms.string("electrons"),
    cutString = cms.string("mvaTrig_HtoWWto2l2nu == 1"),
    numberRequired = cms.string(">= 1"),
    )
cutElecPFIso = cms.PSet(  # See https://twiki.cern.ch/twiki/bin/view/CMS/MultivariateElectronIdentification#Triggering_MVA  
    inputCollection= cms.string("electrons"),
    cutString = cms.string("relPFrhoIso < 0.15"),
    numberRequired = cms.string(">= 1"),
    )
cutElecPassConvVeto = cms.PSet(  # See https://twiki.cern.ch/twiki/bin/view/CMS/MultivariateElectronIdentification#Triggering_MVA  
    inputCollection= cms.string("electrons"),
    cutString = cms.string("passConvVeto == 1"),
    numberRequired = cms.string(">= 1"),
    )
cutElecLostHits = cms.PSet(  # See https://twiki.cern.ch/twiki/bin/view/CMS/MultivariateElectronIdentification#Triggering_MVA  
    inputCollection= cms.string("electrons"),
    cutString = cms.string("numberOfLostHits == 0"),
    numberRequired = cms.string(">= 1"),
    )
cutElecTightID = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("tightID > 0"),
    numberRequired = cms.string(">= 1"),
    )
cutElecLooseIDVeto = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("deltaRMinElecLooseMvaId > 0.15"),
    numberRequired = cms.string(">= 1"),
    )
## cutElecLooseIDVeto = cms.PSet (
##     inputCollection = cms.string("electron-track pairs"),
##     cutString = cms.string("deltaRLooseMvaId < 0.15"),
##     numberRequired = cms.string("= 0"),
##     isVeto = cms.bool(True),  
##     )
cutElecLooseIDOnlyOne = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("mvaNonTrigV0 > 0"),
    numberRequired = cms.string("= 1"),
    )
cutElecLooseIDVetoInv = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("deltaRMinElecLooseMvaId < 0.15"),
    numberRequired = cms.string(">= 1"),
    )
## cutElecLooseIDVetoInv = cms.PSet (
##     inputCollection = cms.string("electrons"),
##     cutString = cms.string("mvaNonTrigV0 > 0"),
##     numberRequired = cms.string(">= 1"),
##     )
cutElecVetoOneMax =   cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("<= 1"),  
    )
cutElecVeto = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("= 0"),
    )
cutElecVetoPt10 = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("mvaNonTrigV0 > 0"),
    # pT > 10 cut is applied in making BEANs  
    numberRequired = cms.string("= 0"),
    )
cutElecPlusMet220 = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("ptPlusMet > 220"),
    numberRequired = cms.string(">= 1"),
    )
cutElecPlusMet110 = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("ptPlusMet > 110"),
    numberRequired = cms.string(">= 1"),
    )

#######################################
#-- Cuts on Electron-Electron Pairs --#
#######################################
cut2ElecPt = cms.PSet(
    inputCollection = cms.string("electrons"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 2"),
    )
cut2ElecEta = cms.PSet(
    inputCollection= cms.string("electrons"),
    cutString = cms.string("fabs(eta) < 2.1"),
    numberRequired = cms.string(">= 2"),
    )
cut2ElecMva = cms.PSet(  # See https://twiki.cern.ch/twiki/bin/view/CMS/MultivariateElectronIdentification#Triggering_MVA
    inputCollection= cms.string("electrons"),
    cutString = cms.string("mvaTrig_HtoWWto2l2nu == 1"),
    numberRequired = cms.string(">= 2"),
    )
cut2ElecD0 = cms.PSet(
    inputCollection= cms.string("electrons"),
    cutString = cms.string("fabs(correctedD0Vertex) < 0.02"),
    numberRequired = cms.string(">= 2"),
    )
cut2ElecDZ = cms.PSet(
    inputCollection= cms.string("electrons"),
    cutString = cms.string("fabs(correctedDZ) < 0.1"),
    numberRequired = cms.string(">= 2"),
    )
cut2ElecPFIso = cms.PSet(  # See https://twiki.cern.ch/twiki/bin/view/CMS/MultivariateElectronIdentification#Triggering_MVA  
    inputCollection= cms.string("electrons"),
    cutString = cms.string("relPFrhoIso < 0.15"),
    numberRequired = cms.string(">= 2"),
    )
cut2ElecPassConvVeto = cms.PSet(  # See https://twiki.cern.ch/twiki/bin/view/CMS/MultivariateElectronIdentification#Triggering_MVA  
    inputCollection= cms.string("electrons"),
    cutString = cms.string("passConvVeto == 1"),
    numberRequired = cms.string(">= 2"),
    )
cut2ElecLostHits = cms.PSet(  # See https://twiki.cern.ch/twiki/bin/view/CMS/MultivariateElectronIdentification#Triggering_MVA  
    inputCollection= cms.string("electrons"),
    cutString = cms.string("numberOfLostHits == 0"),
    numberRequired = cms.string(">= 2"),
    )
cut2ElecNHits = cms.PSet(
    inputCollection= cms.string("electrons"),
    cutString = cms.string("tkNumValidHits > 4"),
    numberRequired = cms.string(">= 2"),
    )
cutElecElecMass = cms.PSet (
    inputCollection = cms.string("electron-electron pairs"),
    cutString = cms.string("invMass > 80 & invMass < 100"),
    numberRequired = cms.string(">= 1"),
    )
cutElecElecChargeProduct = cms.PSet (
    inputCollection = cms.string("electron-electron pairs"),
    cutString = cms.string("chargeProduct == -1"),
    numberRequired = cms.string(">= 1"),
    )
####################################
#-- Cuts on Electron-Track Pairs --#
####################################
cutElecTrkDRSame = cms.PSet (
    inputCollection = cms.string("electron-track pairs"),
    cutString = cms.string("deltaR < 0.15"),
    numberRequired = cms.string(">= 1"),
    )
cutElecTrkDR = cms.PSet (
    inputCollection = cms.string("electron-track pairs"),
    cutString = cms.string("deltaR > 0.15"),
    numberRequired = cms.string(">= 1"),
    )
cutElecTrkDRp5 = cms.PSet (
    inputCollection = cms.string("electron-track pairs"),
    cutString = cms.string("deltaR > 0.5"),
    numberRequired = cms.string(">= 1"),
    )
cutElecTrkInvMass = cms.PSet(
    inputCollection = cms.string("electron-track pairs"),
    cutString = cms.string("invMass > 40 & invMass < 160"),
    numberRequired = cms.string(">= 1"),
    )

cutElecTrkInvMass80To100 = cms.PSet(
    inputCollection = cms.string("electron-track pairs"),
    cutString = cms.string("invMass > 80 & invMass < 100"),
    numberRequired = cms.string(">= 1"),
    )
cutElecTrkDRSameNone = cms.PSet (
    inputCollection = cms.string("electron-track pairs"),
    cutString = cms.string("deltaR < 0.15"),
    numberRequired = cms.string("= 0"),
    )
cutElecTrkChgOpp = cms.PSet (
    inputCollection = cms.string("electron-track pairs"),
    cutString = cms.string("chargeProduct == -1"),
    numberRequired = cms.string(">= 1"),
    )

####################
#-- Cuts on Taus --#
####################
cutTauPt = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 1"),
    )
cutTauPtLeadingTrack = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("leadingTrackPt > 15"),
    numberRequired = cms.string(">= 1"),
    )
cutTauEta = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string(" fabs(eta) < 2.1"),
    numberRequired = cms.string(">= 1"),
    )
cutTauOneProng = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("numProngs == 1"),
    numberRequired = cms.string(">= 1"),
    )
cutTauThreeProng = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("numProngs == 3"),
    numberRequired = cms.string(">= 1"),
    )
cutTauNumSigGamma = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("numSignalGammas == 0"),
    numberRequired = cms.string(">= 1"),
    )
cutTauNumSigNeutral = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("numSignalNeutrals == 0"),
    numberRequired = cms.string(">= 1"),
    )
cutTauNumSigPi0 = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("numSignalPiZeros == 0"),
    numberRequired = cms.string(">= 1"),
    )
cutTauAgainstElectron = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("HPSagainstElectronTight == 1"),
    numberRequired = cms.string(">= 1"),
    )
cutTauAgainstElectronMedium = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("HPSagainstElectronMedium == 1"),
    numberRequired = cms.string(">= 1"),
    )
cutTauForElectron = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("HPSagainstElectronTight == 0"),
    numberRequired = cms.string(">= 1"),
    )
cutTauAgainstMuonTight = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("HPSagainstMuonTight == 1"),
    numberRequired = cms.string(">= 1"),
    )
cutTauAgainstMuonMed = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("HPSagainstMuonMedium == 1"),
    numberRequired = cms.string(">= 1"),
    )
cutTauValidHits = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("leadingTrackValidHits > 4"),
    numberRequired = cms.string(">= 1"),
    )
cutTauLooseIso = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("HPSbyVLooseCombinedIsolationDeltaBetaCorr == 1"),
    numberRequired = cms.string(">= 1"),
    )
cutTauDecayModeFinding = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("HPSdecayModeFinding == 1"),
    numberRequired = cms.string(">= 1"),
    )
cutTauVeto = cms.PSet (
    inputCollection = cms.string("taus"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("= 0"),
    )
cutTauLooseHadronicVeto = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("deltaRMinTauLooseHadronicId > 0.15"),
    numberRequired = cms.string(">= 1"),
    )
## cutTauLooseHadronicVeto = cms.PSet (
##     inputCollection = cms.string("tau-track pairs"),
##     cutString = cms.string("deltaRLooseHadronicID < 0.15"),
##     numberRequired = cms.string("= 0"),
##     isVeto = cms.bool(True),  
##     )
## cutTauLooseHadronicVeto = cms.PSet (
##     inputCollection = cms.string("taus"),
##     cutString = cms.string("looseHadronicID > 0"),
##     numberRequired = cms.string("= 0"),
##     isVeto = cms.bool(True),  
##     )
cutTauLooseHadronicVetoInv = cms.PSet (
    inputCollection = cms.string("taus"),
    cutString = cms.string("looseHadronicID > 0"),
    numberRequired = cms.string(">= 1"),
    )
#############################
#-- Cuts on Tau-Tau Pairs --#
#############################
cutTauPairPt = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 2"),
    )
cutTauPairEta = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("fabs(eta) < 2.1"),
    numberRequired = cms.string(">= 2"),
    )
cutTauPairValidHits = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("leadingTrackValidHits > 4"),
    numberRequired = cms.string(">= 2"),
    )
cutTauPairNumProng = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("numProngs == 1"),
    numberRequired = cms.string(">= 2"),
    )
cutTauPairNumSigGamma = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("numSignalGammas == 0"),
    numberRequired = cms.string(">= 2"),
    )
cutTauPairNumSigNeutral = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("numSignalNeutrals == 0"),
    numberRequired = cms.string(">= 2"),
    )
cutTauPairNumPi0 = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("numSignalPiZeros == 0"),
    numberRequired = cms.string(">= 2"),
    )
cutTauPairInvMass = cms.PSet(
    inputCollection = cms.string("tau-cutTau pairs"),
    cutString = cms.string("invMass > 40 & invMass < 160"),
    numberRequired = cms.string(">= 1"),
    )
##############################
#-- Cuts on Tau-Track Pairs--#
##############################
cutTauTrkDeltaR = cms.PSet(
    inputCollection = cms.string("tau-track pairs"),
    cutString = cms.string("deltaR < 0.15"),
    numberRequired = cms.string(">= 1"),
    )

##############################
#-- Cuts on mcparticles    --#
##############################

cutMCPartPdgZFilter = cms.PSet (
    inputCollection = cms.string("mcparticles"),
    cutString = cms.string("id == 23"),
    numberRequired = cms.string(">= 0"),  # Require 0 so that no events are rejected, but only Z's will be plotted in mcparticles histograms  
    )
cutMCPartPdgZ = cms.PSet (
    inputCollection = cms.string("mcparticles"),
    cutString = cms.string("id == 23"),
    numberRequired = cms.string(">= 1"),  
    )
cutMCPartPdgW = cms.PSet (
    inputCollection = cms.string("mcparticles"),
    cutString = cms.string("fabs(id) == 24"),
    numberRequired = cms.string(">= 1"),  
    )
cutMCPartPdgNuE = cms.PSet (
    inputCollection = cms.string("mcparticles"),
    cutString = cms.string("fabs(id) == 12"),
    numberRequired = cms.string(">= 1"),
    )
cutMCPartPdgE = cms.PSet (
    inputCollection = cms.string("mcparticles"),
    cutString = cms.string("fabs(id) == 11"),
    numberRequired = cms.string(">= 1"),  
    )
cutMCPartPdgMu = cms.PSet (
    inputCollection = cms.string("mcparticles"),
    cutString = cms.string("fabs(id) == 13"),
    numberRequired = cms.string(">= 1"),  
    )
cutMCPartStatus3 = cms.PSet (
    inputCollection = cms.string("mcparticles"),
    cutString = cms.string("status == 3"),
    numberRequired = cms.string(">= 1"),  
    )
cutMCPartStatus3Filter = cms.PSet (
    inputCollection = cms.string("mcparticles"),
    cutString = cms.string("status == 3"),
    numberRequired = cms.string(">= 0"),  
    )
cutMCPartSusy = cms.PSet (
    inputCollection = cms.string("mcparticles"),
    cutString = cms.string("fabs(id) > 1000001 && fabs(id) < 3160113"),
    numberRequired = cms.string(">= 1"),  
    )

cutMCPartChi = cms.PSet (
    inputCollection = cms.string("mcparticles"),
    cutString = cms.string("fabs(id) == 1000024"),
    numberRequired = cms.string(">= 1"),
    )

cutMCPartSusyFilter = cms.PSet (
    inputCollection = cms.string("mcparticles"),
    cutString = cms.string("fabs(id) > 1000001 && fabs(id) < 3160113"),
    numberRequired = cms.string(">= 0"),  
    )
cutMCPartMotherPdgW = cms.PSet (
    inputCollection = cms.string("mcparticles"),
    cutString = cms.string("fabs(mother0Id) == 24"),
    numberRequired = cms.string(">= 1"),  
    )
cutMCPartMotherStatus3 = cms.PSet (
    inputCollection = cms.string("mcparticles"),
    cutString = cms.string("mother0Status == 3"),
    numberRequired = cms.string(">= 1"),  
    )
cutMCPartJetDeltaPhi2p7 = cms.PSet (
    inputCollection = cms.string("mcparticles"),
    cutString = cms.string("deltaPhiMaxSubLeadJet < 2.7"),
    numberRequired = cms.string(">= 1"),  
    )
cutMCPartPt30 = cms.PSet (
    inputCollection = cms.string("mcparticles"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 1"),  
    )
cutMCPartPt50 = cms.PSet (
    inputCollection = cms.string("mcparticles"),
    cutString = cms.string("pt > 50"),
    numberRequired = cms.string(">= 1"),  
    )

##############################
#-- Cuts on BNStop         --#
##############################

cutStopPt50 = cms.PSet (
    inputCollection = cms.string("stops"),
    cutString = cms.string("pt > 50"),
    numberRequired = cms.string(">= 1"),  
    )
cutStopEta2p5 = cms.PSet (
    inputCollection = cms.string("stops"),
    cutString = cms.string("fabs(eta) < 2.5"),
    numberRequired = cms.string(">= 1"),  
    )
cutStopDauIdNotPion = cms.PSet (
    inputCollection = cms.string("stops"),
    cutString = cms.string("fabs(daughter0Id) != 211"),
    numberRequired = cms.string(">= 1"),  
    )
cutStopCtauZero = cms.PSet (
    inputCollection = cms.string("stops"),
    cutString = cms.string("ctau == 0"),
    numberRequired = cms.string(">= 1"),  
    )
cutStopCtauNegative = cms.PSet (
    inputCollection = cms.string("stops"),
    cutString = cms.string("ctau < 0"),
    numberRequired = cms.string(">= 1"),  
    )
cutStopCtauNonZero = cms.PSet (
    inputCollection = cms.string("stops"),
    cutString = cms.string("ctau > 0"),
    numberRequired = cms.string(">= 1"),  
    )
cutStopDecayLengthNonZeroN2 = cms.PSet (
    inputCollection = cms.string("stops"),
    cutString = cms.string("decayLength > 0"),
    numberRequired = cms.string(">= 2"),  
    )
cutStopDecayLengthTrackerN2 = cms.PSet (
    inputCollection = cms.string("stops"),
    cutString = cms.string("fabs(decayVxy) < 110 && fabs(decayVz) < 280"),
    numberRequired = cms.string(">= 2"),  
    )
cutStopDecayLengthZeroVeto = cms.PSet (
    inputCollection = cms.string("stops"),
    cutString = cms.string("decayLength == 0"),
    numberRequired = cms.string("= 0"),
    isVeto = cms.bool(True), 
    )
cutStopDecayLengthOutsideTrackerVeto = cms.PSet (
    inputCollection = cms.string("stops"),
    cutString = cms.string("fabs(decayVxy) > 110 || fabs(decayVz) > 280"),
    numberRequired = cms.string("= 0"),  
    isVeto = cms.bool(True), 
    )


##############################
#-- Standard Event Cleaning ##
##############################
cutEvtFilter = cms.PSet (
    inputCollection = cms.string("events"),
    cutString = cms.string("FilterOutScraping > 0"),
    numberRequired = cms.string(">= 1")
    )

cutVtxGood = cms.PSet (
    inputCollection = cms.string("primaryvertexs"),
    cutString = cms.string("isGood > 0"),
    numberRequired = cms.string(">= 1")
    )


######################################
#-- Cuts on track-mcparticle pairs --#
######################################
cutTrkMCPartPair = cms.PSet (
    inputCollection = cms.string("track-mcparticle pairs"),
    cutString = cms.string("deltaR > -1"),
    numberRequired = cms.string(">= 0"),
    )
