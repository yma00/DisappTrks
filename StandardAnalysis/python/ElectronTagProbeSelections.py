import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.StandardAnalysis.EventSelections import *  # Get the composite cut definitions

##################################################
## Electron tag skim
##################################################
ElectronTagSkim = cms.PSet(
    name = cms.string("ElectronTagSkim"),
    triggers = triggersSingleEle,
    cuts = cms.VPSet (),
)
tagElectronCuts = [
    cutElectronPt25,
    cutElectronEta21,
    cutElectronTightID,
    cutElectronTightPFIso,
]
addCuts(ElectronTagSkim.cuts, tagElectronCuts)


##################################################
## Higher pt to be closer to candidate track selection
##################################################
ElectronTagPt35 = copy.deepcopy(ElectronTagSkim)
ElectronTagPt35.name = cms.string("ElectronTagPt35")
addSingleCut(ElectronTagPt35.cuts,  cutElectronPt35, cutElectronPt25)
removeCuts  (ElectronTagPt35.cuts, [cutElectronPt25])
jetCuts = [
    cutJetPt,
    cutJetEta,
    cutJetTightLepVeto,
    cutDijetDeltaPhiMax,
    # Exclude cutJetMetPhi  
]  
addCuts     (ElectronTagPt35.cuts,  jetCuts) 
addCuts     (ElectronTagPt35.cuts, [cutTrkPt35])
addCuts     (ElectronTagPt35.cuts,  candTrkCuts)
removeCuts  (ElectronTagPt35.cuts, [cutTrkPt55]) 
removeCuts  (ElectronTagPt35.cuts, [cutTrkElecVeto])  
addCuts     (ElectronTagPt35.cuts, [cutTrkMatchRecoElec])

ElectronTagPt35NoTrig = copy.deepcopy(ElectronTagPt35)
ElectronTagPt35NoTrig.name = cms.string("ElectronTagPt35NoTrig")
ElectronTagPt35NoTrig.triggers = cms.vstring() 

ElectronTagPt35MetTrig = copy.deepcopy(ElectronTagPt35)
ElectronTagPt35MetTrig.name = cms.string("ElectronTagPt35MetTrig")
ElectronTagPt35MetTrig.triggers = triggersMet 

ElectronTagPt35MetCut = copy.deepcopy(ElectronTagPt35)
ElectronTagPt35MetCut.name = cms.string("ElectronTagPt35MetCut")
cutsToAdd = [ 
    cutElectronMetMinusOne, 
]
addCuts(ElectronTagPt35MetCut.cuts, cutsToAdd)  

jetCuts = [
    cutJetPt,
    cutJetEta,
    cutJetTightLepVeto,
    cutDijetDeltaPhiMax,
]

ElectronTagPt55 = copy.deepcopy(ElectronTagPt35)
ElectronTagPt55.name = cms.string("ElectronTagPt55")
addSingleCut(ElectronTagPt55.cuts,  cutElectronPt50, cutElectronPt35)
removeCuts  (ElectronTagPt55.cuts, [cutElectronPt35])  
addSingleCut(ElectronTagPt55.cuts,  cutTrkPt55, cutTrkPt35)
removeCuts  (ElectronTagPt55.cuts, [cutTrkPt35])  

ElectronTagPt55MetTrig = copy.deepcopy(ElectronTagPt55)
ElectronTagPt55MetTrig.name = cms.string("ElectronTagPt55MetTrig")
ElectronTagPt55MetTrig.triggers = triggersMet 

ElectronTagPt55NMissOut = copy.deepcopy(ElectronTagPt55)
ElectronTagPt55NMissOut.name = cms.string("ElectronTagPt55NMissOut")
addSingleCut(ElectronTagPt55NMissOut.cuts,  cutTrkNMissOut, cutTrkTauHadVeto) 

ElectronTagPt55NMissOutMetTrig = copy.deepcopy(ElectronTagPt55NMissOut)
ElectronTagPt55NMissOutMetTrig.name = cms.string("ElectronTagPt55NMissOutMetTrig")
ElectronTagPt55NMissOutMetTrig.triggrs = triggersMet  



################################################################################
## Electron tag and probe sample
################################################################################
ZtoEleIsoTrk = copy.deepcopy(ElectronTagSkim)
ZtoEleIsoTrk.name = cms.string("ZtoEleIsoTrk")

eleTrkCuts = [
    cutEleTrkInvMass10,
]
addCuts(ZtoEleIsoTrk.cuts, [cutElectronArbitration])
addCuts(ZtoEleIsoTrk.cuts, [cutTrkPt30]) 
addCuts(ZtoEleIsoTrk.cuts, isoTrkCuts)
addCuts(ZtoEleIsoTrk.cuts, eleTrkCuts)
cutsToRemove = [
    cutTrkPt55,
]
removeCuts(ZtoEleIsoTrk.cuts, cutsToRemove)

ZtoEleProbeTrk = copy.deepcopy(ZtoEleIsoTrk)
ZtoEleProbeTrk.name = cms.string("ZtoEleProbeTrk")
# Add cuts in reverse order
addSingleCut(ZtoEleProbeTrk.cuts, cutTrkTauHadVeto, cutTrkJetDeltaPhi) 
addSingleCut(ZtoEleProbeTrk.cuts, cutTrkMuonVeto,   cutTrkJetDeltaPhi) 


ZtoEleProbeTrkWithZCuts = copy.deepcopy(ZtoEleProbeTrk)
ZtoEleProbeTrkWithZCuts.name = cms.string("ZtoEleProbeTrkWithZCuts")
cutsToAdd = [
    cutEleTrkInvMass80To100,
    cutEleTrkOS,
]
addCuts(ZtoEleProbeTrkWithZCuts.cuts, cutsToAdd)

ZtoEleCandTrk = copy.deepcopy(ZtoEleProbeTrkWithZCuts)
ZtoEleCandTrk.name = cms.string("ZtoEleCandTrk")
addSingleCut(ZtoEleCandTrk.cuts, cutTrkElecVeto, cutTrkTauHadVeto)

ZtoEleDisTrk = copy.deepcopy(ZtoEleCandTrk)
ZtoEleDisTrk.name = cms.string("ZtoEleDisTrk")
addSingleCut(ZtoEleDisTrk.cuts, cutTrkNMissOut, cutTrkElecVeto)
addSingleCut(ZtoEleDisTrk.cuts, cutTrkEcalo,    cutTrkElecVeto) 

ZtoEleDisTrkNoNMissOut = copy.deepcopy(ZtoEleDisTrk) 
ZtoEleDisTrkNoNMissOut.name = cms.string("ZtoEleDisTrkNoNMissOut") 
removeCuts(ZtoEleDisTrkNoNMissOut.cuts, [cutTrkNMissOut])  

ZtoEleCandTrkSdbandEcalo = copy.deepcopy(ZtoEleCandTrk) 
ZtoEleCandTrkSdbandEcalo.name = cms.string("ZtoEleCandTrkSdbandEcalo")
addSingleCut(ZtoEleCandTrkSdbandEcalo.cuts, cutTrkEcaloInv, cutTrkElecVeto)
addSingleCut(ZtoEleCandTrkSdbandEcalo.cuts, cutTrkNMissOut, cutTrkElecVeto)

ZtoEleCandTrkSdbandNMissOut = copy.deepcopy(ZtoEleCandTrk) 
ZtoEleCandTrkSdbandNMissOut.name = cms.string("ZtoEleCandTrkSdbandNMissOut")
addSingleCut(ZtoEleCandTrkSdbandNMissOut.cuts, cutTrkNMissOutInv, cutTrkElecVeto) 
addSingleCut(ZtoEleCandTrkSdbandNMissOut.cuts, cutTrkEcalo,       cutTrkElecVeto) 



