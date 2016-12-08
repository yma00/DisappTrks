#!/usr/bin/env python

# Calculates the systematic uncertainty associated with Ecalo, by reweighting data and MC distributions by the signal distribution, then taking the difference in yields.
#
# Example usage:
# Usage:  makeSystEcaloTextFile.py -l systematicConfig_EcaloVary.py

import sys
import os
import re
from math import *
from array import *
from decimal import *
from optparse import OptionParser
import copy
from operator import itemgetter

from ROOT import TFile, gROOT, gStyle, gDirectory, TStyle, THStack, TH1F, TCanvas, TString, TLegend, TArrow, THStack, TIter, TKey, TGraphErrors, Double

from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *
from OSUT3Analysis.Configuration.formattingUtilities import *


parser = OptionParser()
parser = set_commandline_arguments(parser)
(arguments, args) = parser.parse_args()

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + arguments.localConfig.split(".")[0] + " import *")


def getIntegral(sample, hist, xlo, xhi):
    inputFile = TFile("condor/"+condor_dir+"/"+sample+".root")
    #print "Reading file:  " + inputFile.GetName()

    HistogramObj = inputFile.Get("OSUAnalysis/"+channel+"/"+hist)
    if not HistogramObj:
        print "WARNING: Could not find histogram " + "OSUAnalysis/"+channel+"/"+hist + " in file " + sample +".root" + ". Will skip it and continue."
        return
    histogram = HistogramObj.Clone()
    histogram.SetDirectory(0)
    inputFile.Close()

    xloBin = histogram.GetXaxis().FindBin(float(xlo))
    xhiBin = histogram.GetXaxis().FindBin(float(xhi))
    xlo = histogram.GetXaxis().GetBinLowEdge(xloBin)   # lo edge is the left edge of the first bin
    xhi = histogram.GetXaxis().GetBinLowEdge(xhiBin+1) # hi edge is the left edge of the bin to the right of the last bin
    intError = Double (0.0)
    integral = histogram.IntegralAndError(xloBin, xhiBin, intError)

    line = "Integral of " + hist + " in " + inputFile.GetName() + " from " + str(xlo) + " to " + str(xhi) + ": " + str (integral) + " +- " + str (intError)
    print line
    return integral


outputFile = os.environ['CMSSW_BASE']+"/src/DisappTrks/StandardAnalysis/data/systematic_values__" + systematic_name + ".txt"
if not makeRewtdPlot:
    fout = open (outputFile, "w")

for sample in datasets:
    # FIXME:  Do not need to re-run mergeOutput.py, if you instead just do rewtHist.py for the data and the sum of all background.
    # Those datasets should be specified as an argument rather than passing in localOptionsCtrlDblMuon.py.
    #    command = "rewtHist.py -f condor/condor_2014_03_07_NoCutsFilterMC/" + sample + ".root -i OSUAnalysis/FullSelectionFilterMC/trackCaloTot_RhoCorr -c " + condor_dir + " -n OSUAnalysis/" + channel + "/trackCaloTot_RhoCorr"
    command = "rewtHist.py -f condor/fullSelectionAllSigWithEcalGapVeto/" + sample + ".root -i OSUAnalysis/FullSelection/trackCaloTot_RhoCorr -c " + condor_dir + " -n OSUAnalysis/" + channel + "/trackCaloTot_RhoCorr"
    os.system(command + " -d SingleMu")
    os.system(command + " -d Background")
    print "Finished running: " + command
    yieldDataTot = getIntegral('SingleMu',   'numEvents', 0, 10)
    yieldBkgdTot = getIntegral('Background', 'numEvents', 0, 10)
    yieldDataPt  = getIntegral('SingleMu',   'trackCaloTot_RhoCorr_Reweighted', 0, 100)
    yieldBkgdPt  = getIntegral('Background', 'trackCaloTot_RhoCorr_Reweighted', 0, 100)
    normFactor   = yieldDataTot / yieldBkgdTot
    plus_factor  = yieldDataPt / (yieldBkgdPt * normFactor)
    minus_factor = plus_factor
    print "Found systematic error: " + str(plus_factor)
    if makeRewtdPlot:
        os.system(command + " -l localOptionsCtrlMuon.py")
        plotCmd = "makePlots.py -q trackCaloTot_RhoCorr_Reweighted -f -N " + str(normFactor) + " -l localOptionsCtrlMuon.py -c " + condor_dir + " -o stacked_histogramsRewt_" + sample + ".root"
        print "Running:  " + plotCmd
        os.system(plotCmd)
    line = '{0: <24}'.format(str(sample)) + " " + '{0: <8}'.format(minus_factor) + " " + '{0: <8}'.format(plus_factor) + "\n" # format the sample name to use a fixed number of characters
    print line
    if not makeRewtdPlot:
        fout.write (line)
if not makeRewtdPlot:
    fout.close()
    print "Finished writing systematics file: " + outputFile






