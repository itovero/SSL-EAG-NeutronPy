#---------------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy as np
#%matplotlib inline
import BeamProfile1 as bm
import TransmissionCalc as tr
from scipy.optimize import minimize

#----------------------------------------------------------------------
# parameters of the numerical methods used in the model 
#----------------------------------------------------------------------
BEAM_ARR_DIM       = 16   # size of the array for the pulse shape of the beam, use 128 as a default
NsubCells          = 3    # number of points in each time bin of exp. data used for Theoretical calc (averaging over the time bin)

#----------------------------------------------------------------------
# load parameters
Par = tr.LoadParameters()

#----------------------------------------------------------------------
# Load cross sections
S_E = tr.LoadCrossSectionsData(Par)
#----------------------------------------------------------------------
#print(len(Par['Elmnts']))
Par['Elmnts']

#----------------------------------------------------------------------------------
# This section calculates Theoretical transmission TrIdeal_E on a propoerly spaced EarrIdeal mesh
#----------------------------------------------------------------------------------
# create new E array with step size given in parameters, equally spaced
EarrIdeal = tr.Get_E_Array_Properly_Spaced(Par['Minimum E'], Par['Maximum E'])
print('EarrIdeal length=',len(EarrIdeal), 'Min=',min(EarrIdeal),'eV Max=',max(EarrIdeal), 'eV')

TrIdeal_E = tr.CalcIdealTransmission(S_E, Par, EarrIdeal, True)

#----------------------------------------------------------------------------------
# Convolve ideal Theoretical transmission with beam pulse profile
# this depends on L and dT parameters, needs to be within minimizer
#----------------------------------------------------------------------------------
TrConv_T, Tmax = tr.ConvolveTrWithPulseProfile(Par, EarrIdeal, TrIdeal_E, BEAM_ARR_DIM, True, True)
