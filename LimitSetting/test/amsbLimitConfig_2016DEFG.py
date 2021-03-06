#!/usr/bin/env python

# Local options file to be used with makeDataCards.py
# Usage:
# > makeDatacards.py -l amsbLimitConfig.py -c test
#
# Copied from https://raw.github.com/DisplacedSUSY/DisplacedSUSY/master/LimitsCalculation/test/sampleLimitConfig.py

from DisappTrks.SignalMC.signalCrossSecs import *
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
from amsbLimitConfigBkgds_2016DEFG import *    # Produced with ../scripts/makeANTables.py

dirs = getUser ()

##################################
### Event Selection Parameters ###
##################################

#name of histogram to integrate to get yields
integrateHistogramName = "metPt"

#########################
### Signal Parameters ###
#########################

# a separate datacard will be produced with each value of MASS,TAU
# named "datacard_AMSB_mGravMASSK_TAUns.txt"

samplesByGravitinoMass = False

#NOTE: These are the chargino masses in GeV
masses = ['100', '200', '300', '400', '500', '600', '700']

#chargino tau values in cm
lifetimes = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
             '20', '30', '40', '50', '60', '70', '80', '90', '100',
             '200', '300', '400', '500', '600', '700', '800', '900', '1000',
             '2000', '3000', '4000', '5000', '6000', '7000', '8000', '9000', '10000']

signalScaleFactor = lumi["MET_2016DEFG"] / lumi["MET_2016DEFGH"]
lumi = lumi["MET_2016DEFG"]

#condor directory in which to find signal root files
signal_condor_dir = dirs["Andrew"] + '/2016/disappearingTracks_signal_DEFGH_v2/'

signal_suffix = '80X'
signal_suffix_in_datacard = '80X_DEFGH'

#name of event selection from which to take signal yields
signal_channel = 'DisTrkSelectionPlotter/Met Plots'

#######################
### Data Parameters ###
#######################

#this just sets the observed number of events equal to the total background expectation
run_blind_limits = True

data_dataset = "MET_2016DEFGH"

#condor directory in which to find data root file
data_condor_dir = dirs["Andrew"] + '/2016_ICHEP/disappearingTracks/'

#name of event selection from which to take observed events
data_channel = 'DisTrkSelectionPlotter/Met Plots'

#############################
### Systematic Uncertainties ###
#############################

external_systematic_uncertainties = [
    # Use order of AN
    "isr_2016",
    "jec_2016",
    "jer_2016",
    "metVaryElectronEn_2016",
    "metVaryJetEn_2016",
    "metVaryJetRes_2016",
    "metVaryPhotonEn_2016",
    "metVaryTauEn_2016",
    "metVaryUnclusteredEn_2016",
    "pileup_2016D",
    "trigger_metLegWeightData_2016DEFG",
    "trigger_metLegWeightMC_2016DEFG",
    "trigger_trackLegWeightData_2016DEFG",
    "trigger_trackLegWeightMC_2016DEFG",
]

#uncertainties on signal only (we can alter this if we need to)
# For now, use the largest value of the uncertainty range from Run 1
signal_systematic_uncertainties = {
    'lumi' :  {
        'value' : '1.026',
    },
    'trkReco' :  {
        'value' : '1.017',
    },
    'Ecalo' : {
        'value' : str (1.0 + 1.01724553994 / 100.0),
    },
    'Nmissin' :  {
        'value' : str (1.0 + 2.93113227546 / 100.0),
    },
    'Nmissmid' :  {
        'value' : str (1.0 + 1.23438446885 / 100.0),
    },
    'NMissOut' : {
        'value' : str (1.0 + 9.0172855903 / 100.0),
    },
}
