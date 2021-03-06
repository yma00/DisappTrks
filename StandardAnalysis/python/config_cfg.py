from DisappTrks.StandardAnalysis.protoConfig_cfg import *

################################################################################
# MET channels
################################################################################
# Channel requiring only MET
#  add_channels  (process,  [metMinimalSkim],  histSetsMetJet,  weights,  [],  collectionMap,  variableProducers,  True)

# Channels needed for background estimates and systematics
#  add_channels  (process,  [basicSelection],         histSetsMetJet,  weights,  [],  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [disTrkSelectionNHits3],  histSets,        weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionNHits4],  histSets,        weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionNHits5],  histSets,        weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionNHits6],  histSets,        weights,  [],  collectionMap,  variableProducers,  False)

# Channels requiring MET+jet+track
#  add_channels  (process,  [isoTrkSelection],    histSets,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [candTrkSelection],   histSets,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [elecCtrlSelection],  histSets,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [muonCtrlSelection],  histSets,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [tauCtrlSelection],   histSets,  weights,  [],  collectionMap,  variableProducers,  False)

# Variations of the disappearing tracks search region
#  add_channels  (process,  [disTrkIdElec],      histSets,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkIdMuon],      histSets,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkIdTau],       histSets,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkIdFake],      histSets,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkNoNMissOut],  histSets,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkNoEcalo],     histSets,  weights,  [],  collectionMap,  variableProducers,  False)

# THE disappearing tracks search region
#  add_channels  (process,  [disTrkSelection],  histSets,  weights,  [],  collectionMap,  variableProducers,  False)
################################################################################

################################################################################
## Testing channels
################################################################################

#  add_channels  (process,  [basicSelectionOneJet14to18PV],         histSetsMetJet,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionOneJet14to18PVNHits3],  histSets,        weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionOneJet14to18PVNHits4],  histSets,        weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionOneJet14to18PVNHits5],  histSets,        weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [disTrkSelectionOneJet14to18PVNHits6],  histSets,        weights,  [],  collectionMap,  variableProducers,  False)

#  add_channels  (process,  [justAVertex],         histSets,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [justADisTrk],         histSets,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [justADisTrkNHits3],   histSets,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [justADisTrkNHits4],   histSets,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [justADisTrkNHits5],   histSets,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [justADisTrkNHits6],   histSets,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [justAFakeTrk],        histSets,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [justAFakeTrkNHits3],  histSets,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [justAFakeTrkNHits4],  histSets,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [justAFakeTrkNHits5],  histSets,  weights,  [],  collectionMap,  variableProducers,  False)
#  add_channels  (process,  [justAFakeTrkNHits6],  histSets,  weights,  [],  collectionMap,  variableProducers,  False)
