import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.StandardAnalysis.EventSelections import *
from DisappTrks.StandardAnalysis.MuonTagProbeSelections import *

################################################################################
## ISR signal systematic
################################################################################

ZtoMuMuISRStudy = copy.deepcopy(ZtoMuMu)
ZtoMuMuISRStudy.name = cms.string("ZtoMuMuISRStudy")
cutsToAdd = [
    cutJetPt,
    cutJetEta,
    cutJetTightLepVeto,
    cutDijetDeltaPhiMax,
]
addCuts(ZtoMuMuISRStudy.cuts, cutsToAdd)

ZtoMuMuISRStudy2016 = copy.deepcopy(ZtoMuMuISRStudy)
ZtoMuMuISRStudy2016.name = cms.string("ZtoMuMuISRStudy2016")
ZtoMuMuISRStudy2016.triggers = triggersSingleMu2016

# Drop MET requirement, jet pt requirement of only 30
ZtoMuMuISRStudyJet30 = copy.deepcopy(ZtoMuMu)
ZtoMuMuISRStudyJet30.name = cms.string("ZtoMuMuISRStudyJet30")
cutsToAdd = [
    cutJetPt30,
    cutJetEta,
    cutJetTightLepVeto,
    cutDijetDeltaPhiMax,
]
addCuts(ZtoMuMuISRStudyJet30.cuts, cutsToAdd)

ZtoMuMuISRStudy2016Jet30 = copy.deepcopy(ZtoMuMuISRStudyJet30)
ZtoMuMuISRStudy2016Jet30.name = cms.string("ZtoMuMuISRStudy2016Jet30")
ZtoMuMuISRStudy2016Jet30.triggers = triggersSingleMu2016

################################################################################
## JEC signal systematic
################################################################################

disTrkSelectionJECUp = copy.deepcopy(disTrkSelection)
disTrkSelectionJECUp.name = cms.string("disTrkSelectionJECUp")
removeCuts(disTrkSelectionJECUp.cuts, [cutJetPt])
addCuts(disTrkSelectionJECUp.cuts, [cutJetPtJECUp])

disTrkSelectionJECDown = copy.deepcopy(disTrkSelection)
disTrkSelectionJECDown.name = cms.string("disTrkSelectionJECDown")
removeCuts(disTrkSelectionJECDown.cuts, [cutJetPt])
addCuts(disTrkSelectionJECDown.cuts, [cutJetPtJECDown])

################################################################################
## JER signal systematic
################################################################################

disTrkSelectionSmearedJets = copy.deepcopy(disTrkSelection)
disTrkSelectionSmearedJets.name = cms.string("disTrkSelectionSmearedJets")
removeCuts(disTrkSelectionSmearedJets.cuts, [cutJetPt])
addCuts(disTrkSelectionSmearedJets.cuts, [cutJetJERSmearedPt])

disTrkSelectionSmearedJetsUp = copy.deepcopy(disTrkSelection)
disTrkSelectionSmearedJetsUp.name = cms.string("disTrkSelectionSmearedJetsUp")
removeCuts(disTrkSelectionSmearedJetsUp.cuts, [cutJetPt])
addCuts(disTrkSelectionSmearedJetsUp.cuts, [cutJetJERSmearedPtUp])

disTrkSelectionSmearedJetsDown = copy.deepcopy(disTrkSelection)
disTrkSelectionSmearedJetsDown.name = cms.string("disTrkSelectionSmearedJetsDown")
removeCuts(disTrkSelectionSmearedJetsDown.cuts, [cutJetPt])
addCuts(disTrkSelectionSmearedJetsDown.cuts, [cutJetJERSmearedPtDown])

disTrkSelectionSmearedJetsJECUp = copy.deepcopy(disTrkSelection)
disTrkSelectionSmearedJetsJECUp.name = cms.string("disTrkSelectionSmearedJetsJECUp")
removeCuts(disTrkSelectionSmearedJetsJECUp.cuts, [cutJetPt])
addCuts(disTrkSelectionSmearedJetsJECUp.cuts, [cutJetJERSmearedPtJECUp])

disTrkSelectionSmearedJetsJECDown = copy.deepcopy(disTrkSelection)
disTrkSelectionSmearedJetsJECDown.name = cms.string("disTrkSelectionSmearedJetsJECDown")
removeCuts(disTrkSelectionSmearedJetsJECDown.cuts, [cutJetPt])
addCuts(disTrkSelectionSmearedJetsJECDown.cuts, [cutJetJERSmearedPtJECDown])
