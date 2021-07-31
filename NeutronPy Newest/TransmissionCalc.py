#---------------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy as np
#import BeamProfile1 as bm
from tqdm import tqdm_notebook


#---------------------------------------------------------------------------------
# Reads cross section from a given directory for a file name such as Ta-181.txt
# Cuts it to [Emin, Emax] interval, measured in eV.
# IsotopeName - name for the file such as Ta-181, C-nat, etc
# Returns interpolated function, which can be used to calculate Cross section at any value E (in eV)
#---------------------------------------------------------------------------------
def LoadSingleCrossSection(IsotopeName, Emin, Emax):

    S1 = pd.read_table('CrossSections_BeamProfiles\\'+IsotopeName+'.txt')
    #print(S1.head())

    # find the index of first row, where E exceeds Emin
    ind1 = next(x for x, val in enumerate(S1[S1.columns[0]]) if val > Emin*1e-6)
    #print('Ind1 =',ind1)
    # find the index of first row, where E exceeds Emax
    ind2 = next(x for x, val in enumerate(S1[S1.columns[0]]) if val > Emax*1e-6)
    #print('Ind2 =',ind2)
    # select only needed part of table
    S1 = S1.iloc[ind1-1:ind2+1]

    #that is non-inclusive version of selection, do not use it
    # select only values which are in the range of Energy used in calculations
    #S1 = S1.loc[(S1[S1.columns[0]] >= Emin*1e-6) & (S1[S1.columns[0]] <= Emax*1e-6) ]  #original file data is in MeV

    # drop duplicate rows if such exist
    S1 = S1.drop_duplicates(subset=S1.columns[0])

    # create numpy arrays
    Earr = S1[S1.columns[0]].to_numpy()*1e6
    Sarr = S1[S1.columns[1]].to_numpy()

    #interpolate the cross section to allow for any E value
    #CrossSection =  interp1d(Earr, Sarr, kind='cubic',fill_value='extrapolate')
    #CrossSection =  interp1d(Earr, Sarr, kind='linear',fill_value='extrapolate')
    CrossSection =  interp1d(Earr, Sarr, kind='linear')

    Sarr2 = CrossSection(Earr)

    plt.figure(figsize=(6, 2.5))
    plt.plot(Earr, Sarr, label=IsotopeName, color='b', marker='.')
    plt.plot(Earr, Sarr2, label='Interpolated', color='r')
    plt.grid(True)
    plt.xlabel("Neutron energy (eV)")
    plt.ylabel("Cross section (barns)")
    plt.xscale('log')
    plt.yscale('log')
    #plt.xlim([4, 4.5])
    #plt.ylim([-5, 10])
    plt.legend()
    plt.show()

    return {IsotopeName: CrossSection}


# ----------------------------------------------------------------------------------
# This function loads cross section data and does its linear interpolation
# Returns a dictionary of cross sections (key=IsotopeName as in data file name). Cross sect. is interpolated function!
# ----------------------------------------------------------------------------------
def LoadCrossSectionsData(Par):
    # TODO calculate the padding on the left side needed for convolution
    # for now just use factor of 0.7 on Emin
    # changed Emin, Emax to provide for padding needed for convolution with beam profile

    S = {}  # Dictionary of interpolated cross sections (functions) for all the materials, key is Isotope Name
    for i in range(0, Par['Elmnts'].shape[0]):
        rowSeries = Par['Elmnts'].iloc[i]  # this is one line from the param file with elemental data
        S.update(LoadSingleCrossSection(rowSeries[0], Par['Minimum E'], Par['Maximum E']))

    return S

#---------------------------------------------------------------------------------------------------
# converts TOF into energy in eV, TOF in us, L in meters
#---------------------------------------------------------------------------------------------------
def Get_E_FromTOF(TOF, L) :

    #Lamda = (TOF * 3.956 / L / 1000)
    Lamda = TOF * 3.956e-3 / L 
    #E = (6.626**2) / 2 / 1.675 / (Lamda**2) /1.6 / 100
    E = 0.0819102164 / (Lamda**2) 
    
    return E

#---------------------------------------------------------------------------------------------------
# converts energy into TOF; E in eV, TOF in us, L in meters
#---------------------------------------------------------------------------------------------------
def Get_TOF_FromE(E, L) :
    
    TOF = 72.3457051 * L / np.sqrt(E)
    
    return TOF

#---------------------------------------------------------------------------------------------------
# creates array of E values with proper steps
#---------------------------------------------------------------------------------------------------
def Get_E_Array_Properly_Spaced(Emin, Emax) :

    Erange = np.array( [0.0001, 0.001, 0.01, 0.1,  1,    10,   100,  1e3, 1e4, 1e5, 1e6] )
    Esteps = np.array( [5e-5,   5e-4,  5e-3, 5e-3, 1e-2, 1e-2, 1e-2, 0.1, 1,   10,  100] )

    if Emin < Erange[0]:
        raise Exception("Emin is too small!!!!\n Input value was {0} lower than Emin = {1}\n Exit here".format(Emin, Erange[0]))

    if Emax > 20e6:  # 20 MeV is max value in most cross section data
        raise Exception("Emax is too large!!!!\n Input value was {0} larger than Emax = {1}\n Exit here".format(Emax, Erange[-1]))

    MaxInd = len(Erange) - 1
    ind = MaxInd
    for i in range(0, MaxInd) :
        if Emin >= Erange[i] and Emin < Erange[i+1] :
            ind = i

    if ind == MaxInd:
        steps = int((Emax-Emin)/Esteps[ind])
        Earr = np.linspace(Emin, Emax, num=steps)
        #Earr = np.arange(start=Emin, stop=Emax, step=Esteps[ind])
    else :
        right = min(Emax,Erange[ind+1])
        left = Emin
        steps = int((right-left)/Esteps[ind])
        Earr = np.linspace(left, right, num=steps)
        #Earr = np.arange(start=Emin, stop=min(Emax,Erange[ind+1]), step=Esteps[ind])
        for i in range(ind+1, MaxInd) :
            right = min(Emax, Erange[i + 1])
            left = Erange[i]
            if right > left :
                steps = int((right - left) / Esteps[i])
                E1 = np.linspace(left, right, num=steps)
                #E1 = np.arange(start=Erange[i], stop=min(Emax,Erange[i+1]), step=Esteps[i])
                Earr = np.append(Earr, E1)
        if Emax > Erange[MaxInd] :
            right = Emax
            left = Erange[MaxInd]
            steps = int((right - left) / Esteps[MaxInd])
            E1 = np.linspace(left, right, num=steps)
            #E1 = np.arange(start=Erange[MaxInd], stop=Emax, step=Esteps[MaxInd])
            Earr = np.append(Earr, E1)

    Earr = np.unique(Earr)  #remve duplicates, if they exist

    #plt.plot(Earr[1:], np.diff(Earr), color='g',marker='.')
    #plt.grid(True)
    #plt.xscale('log')
    #plt.yscale('log')
    ##plt.xlim([0.08, 2])
    #plt.show()
    
    return Earr

#---------------------------------------------------------------------------------------------------
# creates array of T values with proper steps for the rane in between Emin and Emax (eV)
#---------------------------------------------------------------------------------------------------
# def Get_T_Array_Properly_Spaced(Emin, Emax, L) :

#     Tmin = Get_TOF_FromE(Emax, L)
#     Tmax = Get_TOF_FromE(Emin, L)
    
#     Erange = np.array( [0.0001, 0.001, 0.01, 0.1,  1,    10,   100,  1e3, 1e4, 1e5, 1e6] )
#     # delme section----------------
#     #Esteps = np.array( [5e-5,   5e-4,  5e-3, 5e-3, 1e-2, 1e-2, 1e-2, 0.1, 1,   10,  100] )
#     #Trange = Get_TOF_FromE(Erange[::-1], L)
#     #Tsteps = Trange - Get_TOF_FromE(Erange[::-1]+Esteps[::-1], L) 
#     #print('Tsteps', Tsteps)
#     #print('Trange', Trange)
#     # end delme section----------------

#     # set Tseps here. Above code calculates these from Esteps
#     Tsteps = np.array( [5e-3, 0.01, 0.05, 0.002, 0.005, 0.05, 0.5, 10, 100, 500, 1000] )
#     # convert these values relative to L=14.6 m, which was used for calibration
#     Tsteps = Tsteps * L / 14.6

#     MaxInd = len(Trange) - 1
#     ind = MaxInd
#     for i in range(0, MaxInd) :
#         if Tmin >= Trange[i] and Tmin < Trange[i+1] :
#             ind = i

#     if ind == MaxInd:
#         steps = int((Tmax-Tmin)/Tsteps[ind])
#         Tarr = np.linspace(Tmin, Tmax, num=steps)
#         #Tarr = np.arange(start=Tmin, stop=Tmax, step=Tsteps[ind])
#     else :
#         right = min(Tmax,Trange[ind+1])
#         left = Tmin
#         steps = int((right-left)/Tsteps[ind])
#         Tarr = np.linspace(left, right, num=steps)
#         #Tarr = np.arange(start=Tmin, stop=min(Tmax,Trange[ind+1]), step=Tsteps[ind])
#         for i in range(ind+1, MaxInd) :
#             right = min(Tmax, Trange[i + 1])
#             left = Trange[i]
#             if right > left :
#                 steps = int((right - left) / Tsteps[i])
#                 T1 = np.linspace(left, right, num=steps)
#                 #T1 = np.arange(start=Trange[i], stop=min(Tmax,Trange[i+1]), step=Tsteps[i])
#                 Tarr = np.append(Tarr, T1)
#         if Tmax > Trange[MaxInd] :
#             right = Tmax
#             left = Trange[MaxInd]
#             steps = int((right - left) / Tsteps[MaxInd])
#             T1 = np.linspace(left, right, num=steps)
#             #T1 = np.arange(start=Trange[MaxInd], stop=Tmax, step=Tsteps[MaxInd])
#             Tarr = np.append(Tarr, T1)

#     Tarr = np.unique(Tarr)  #remve duplicates, if they exist


    ##plt.plot(Tarr[1:], np.diff(Tarr), color='g', marker='.')
    #plt.plot(Tarr, Tarr, color='g', marker='.')
    #plt.grid(True)
    #plt.xscale('log')
    ##plt.yscale('log')
    ##plt.xlim([70, 70.1])

    print('Created time array with',len(Tarr),'Time cells')
    
    return Tarr


#---------------------------------------------------------------------------------------------------
# Loads parameters from the filename, by default it is "IsotopesToFit.txt"
#---------------------------------------------------------------------------------------------------
def LoadParameters(filename="IsotopesToFit.txt"):
    Parameters = {'Proton pulse gap': 0, 'Flight path': 0, 'Trigger delay': 0, 'Time bin': 0, 'Minimum E': 0,
                  'Maximum E': 0, 'CROSS_SECT_SKIP_POINTS': 10}

    FILE = open(filename)

    for i in range(7):
        s = FILE.readline()
        if s[0:1] != '//' and s[0] != '#' :
            value, name = s.split('-')
            if name.find('Proton pulse gap') != -1:
                Parameters['Proton pulse gap'] = float(value)
            elif name.find('Flight path') != -1:
                Parameters['Flight path'] = float(value)
            elif name.find('Trigger delay') != -1:
                Parameters['Trigger delay'] = float(value)
            elif name.find('Time bin') != -1:
                Parameters['Time bin'] = float(value)
            elif name.find('Minimum E') != -1:
                Parameters['Minimum E'] = float(value)
            elif name.find('Maximum E') != -1:
                Parameters['Maximum E'] = float(value)
            elif name.find('CROSS_SECT_SKIP_POINTS') != -1:
                Parameters['CROSS_SECT_SKIP_POINTS'] = int(value)

    #print(Parameters)

    # --------------------------------
    # material parameters here
    # --------------------------------
    Elements = []
    for line in FILE:
        if line[0:2] != '//' and s[0] != '#':
            ln = line.split()
            if len(ln) == 7 :  #drop out lines which do not have all the parameters in them
                Elements.append(ln)
            else :
                print('Dropped this line out as it is not correct',line)

    # create pandas dataframe for Material parameters
    ElemPar = pd.DataFrame(Elements,
                           columns=['Isotope Name', 'Abundance', 'AtomicFraction', 'Density (g/cm3)', 'AtomicMass',
                                    'Thickness (um)', 'GrupN'])

    # convert strings parameters into numbers
    for i in range(len(ElemPar.columns) - 1):
        ElemPar[ElemPar.columns[i + 1]] = ElemPar[ElemPar.columns[i + 1]].astype(float)
    ElemPar['GrupN'] = ElemPar['GrupN'].astype(int)
    # remove .txt if it exists from isotope file names
    for i in range(len(ElemPar)):
        ElemPar.loc[i, 'Isotope Name'] = ElemPar.loc[i, 'Isotope Name'].replace('.txt', '')

    # sort elements by their group number then by Isotope name
    ElemPar.sort_values(by=['GrupN','Isotope Name'], inplace=True)

    Parameters['Elmnts'] = ElemPar

    ElemPar

    return Parameters


# ----------------------------------------------------------------------------------
# This function calculates Theoretical transmission on a propoerly spaced Earr mesh
# S - dictionary of cross sections (key=IsotopeName as in data file name). Cross sect. is interpolated function!
# Par - parameters read from the Parameter file (including path length, etc. and the elemental composition table)
# Earr - existing array of E values on which Tr will be calculated
# Returns the calculated transmission for the entire set of elements
# ----------------------------------------------------------------------------------
def CalcIdealTransmission(S, Par, Earr, Plot=False):
    # ExpTerm = Rho * d * w * A * S2 / (w * m * A) / 1.6605389e4
    # calculate exponential term for transmission, group by group
    Elem = Par['Elmnts']
    ExpTerm = np.zeros(len(Earr))  # create array with 0 values for Exponential Term

    for GrpN in range(0, max(Elem['GrupN']) + 1):  # iterate over group numbers here
        GrpSubset = Elem.loc[Elem['GrupN'] == GrpN]  # select subset of rows with GrpN
        if len(GrpSubset) > 0:
            A = np.zeros(len(Earr))  # empty array for that group
            Mass = 0
            for i in range(len(GrpSubset)):  # iterate within single group here
                row = GrpSubset.iloc[i]
                A += row['Abundance'] * row['AtomicFraction'] * S[row['Isotope Name']](Earr) * row['Thickness (um)'] * row['Density (g/cm3)'] / 1.6605389e4
                Mass += row['AtomicFraction'] * row['AtomicMass']
                print(row['Isotope Name'])
            print('Mass=',Mass)
            ExpTerm += A / Mass
            print('-----------------')

    Tr1 = np.exp(-ExpTerm)

    if Plot :
        plt.figure(figsize=(6,5))
        plt.subplot(211)
        plt.plot(Earr, Tr1, label='Ideal theory', color='b')
        plt.xlabel("Energy (eV)")
        plt.xscale('log')
        plt.ylabel("Theor. transm.")
        plt.grid(True)
        #-------------
        plt.subplot(212)
        plt.plot(Get_TOF_FromE(Earr, Par['Flight path']), Tr1, label='Ideal theory', color='g')
        plt.xlabel("TOF (us)")
        plt.xscale('log')
        plt.ylabel("Theor. transm.")
        plt.grid(True)
        # plt.yscale('log')
        # plt.xlim([500,1200])
        plt.subplots_adjust(top=1, bottom=0.0, left=0.0, right=1, hspace=0.3, wspace=0.1)

        plt.show()

    return Tr1


# -------------------------------------------------------------------------------
# Convolve idealtransmission with the neutron pulse time profile
# EarrIdeal - array of energy values for which Tr needs to be convolved
# TrIdeal   - function interpolated for the ideal theoretical transmission
# Returns the function interpolated for convlolved transmission on interval [Emin,Emax]
# -------------------------------------------------------------------------------
def ConvolveTrWithPulseProfile(Par, EarrIdeal, TrIdeal, BEAM_ARR_DIM, Plot=False, FileOutput=False):
    # create the time array corresponding to energy array of theoretical cross ection
    Tarr1 = Get_TOF_FromE(EarrIdeal, Par['Flight path'])

    # interpolate transmission over new Tarr
    # Tr = interp1d(Tarr1, TrIdeal, kind='linear', fill_value='extrapolate')
    Tr1 = interp1d(Tarr1, TrIdeal, kind='linear')

    # create working arrays to be used in convolution, only needed here
    BeamProfile_T = np.zeros(BEAM_ARR_DIM)  # just make an empty array to be filled up
    BeamProfile_Amp = np.zeros(BEAM_ARR_DIM)  # just make an empty array to be filled up
    TrTemp = np.zeros(BEAM_ARR_DIM)  # just make an empty array to be filled up

    # select only fraction of Earr between Emin and Emax, otherwise interpolation does not work for BeamProfile width added on the right side
    #Earr2 = EarrIdeal[np.where((EarrIdeal >= Par['Minimum E']) & (EarrIdeal <= Par['Maximum E']))]
    # leave only those elements which have enough data for convolution  - cut the left side of the array
    # subtract the time length equal to beam profile width at min Energy
    Tmax = Get_TOF_FromE(min(EarrIdeal), Par['Flight path']) - bm.BeamProfileWidth(min(EarrIdeal))*1.05  # 1.05 is the safety margin
    Emin = Get_E_FromTOF(Tmax, Par['Flight path'])
    Earr2 = EarrIdeal[np.where((EarrIdeal >= Emin))]
    Earr2 = Earr2[0::Par['CROSS_SECT_SKIP_POINTS']]  # take each N-th element in the Energy properly spaced array to speed up calculation
    #include last point Emax in Earr2
    if Earr2[-1] < EarrIdeal[-1]: Earr2 = np.append(Earr2, max(EarrIdeal))

    Tr2 = np.zeros(len(Earr2))  # just make an empty array to be filled up
    Tarr2 = Get_TOF_FromE(Earr2, Par['Flight path']) # pay attention here that Tarr2 is in reverse order, descending

    print('Will calculate', len(Earr2), 'points in time between', Earr2[0], 'eV and', Earr2[-1], 'eV')

    for i in tqdm_notebook(range(len(Earr2)), total=len(Earr2), desc="Convolving with beam profile", bar_format="{l_bar}{bar} [ time left: {remaining} ]") :
#        for i in range(len(Earr2)):
        E = Earr2[i]
        bm.BeamProfileArrayCalculated(Par['Proton pulse gap'], E, BeamProfile_T, BeamProfile_Amp, BEAM_ARR_DIM)
        TrTemp = Tr1(BeamProfile_T + Tarr2[i])  # these are arrays, not scalars, times as BmProfile shifted by Tarr4[i]
        Tr2[i] = np.sum(np.multiply(BeamProfile_Amp, TrTemp))
        len(Earr2)

    # interpolate convolved transmission
    # TrConvolved = interp1d(Tarr2, Tr2, kind='linear', fill_value='extrapolate')
    TrConvolved = interp1d(Tarr2, Tr2, kind='linear')

    #print('DONE with calucluations!\n-----------')

    if Plot :
        plt.figure(figsize=(6,5))
        plt.subplot(211)
        plt.plot(Get_E_FromTOF(Tarr2, Par['Flight path']), Tr2, label='Exper. predicted', color='b')
        plt.xlabel("Energy (eV)")
        plt.xscale('log')
        plt.ylabel("Theor. transm.")
        plt.grid(True)
        #-------------
        plt.subplot(212)
        plt.plot(Tarr2, Tr2, label='Exper. predicted', color='g')
        plt.xlabel("TOF (us)")
        plt.xscale('log')
        plt.ylabel("Theor. transm.")
        plt.grid(True)
        # plt.yscale('log')
        # plt.xlim([500,1200])
        plt.subplots_adjust(top=1, bottom=0.0, left=0.0, right=1, hspace=0.3, wspace=0.1)

        plt.show()

    if FileOutput :
        FileArr = np.array([EarrIdeal, TrIdeal])
        FileArr = FileArr.T
        np.savetxt('TrIdeal.csv', FileArr, fmt='%f', delimiter=',', header='E (eV),Tr Ideal')
        FileArr = np.array([Get_E_FromTOF(Tarr2, Par['Flight path']), Tr2])
        FileArr = FileArr.T
        np.savetxt('TrBeamline.csv', FileArr, fmt='%f', delimiter=',', header='E (eV),Tr beamline')

    return TrConvolved, Tarr2[0]

# -------------------------------------------------------------------------------
# Read measured transmission data from a TXT or CSV file into pandas frame
# then convert it to numpy arrays
# Returns Time and Tr arrays for the experimental data
# -------------------------------------------------------------------------------
def ReadExpTransmission(FileName) :
    # read experimental data
    Measured = pd.read_table(FileName)
    # create numpy arrays
    T = Measured[Measured.columns[0]].to_numpy()*1e6  # convert to us
    Tr = Measured[Measured.columns[1]].to_numpy()
    return T, Tr


# -------------------------------------------------------------------------------
# Calculate theoretical transmission for Experimental TOF values
# -----INPUT
# Par - paremeters of the model
# Texp - time array of experimental data
# TrExp - measured transmission values
# TrConvld - Theoretical transmission convolved with beam profile
# NsubCells - how many subcells to use in averagin of theoretical transm for TOF bin in experiment
# Plot - optional, whether to plot the graph or not
# -----RETURNS
# square of differences between Exp and Theoretical values
# -------------------------------------------------------------------------------
def CalcTransmForExpPoints(Par, Texp, TrExp, TrConvld,  Tmax, NsubCells, Plot=False):
    #Tbin = Par['Time bin']
    Tbin = CalcTbinArray(Texp)
    dT = Par['Trigger delay']

    # select only exp. points which are above the Emin(Tmax) value and below Emax
    # T max was reduced by convolution from corresponding Emin value!!!
    Tmin   = Get_TOF_FromE(Par['Maximum E'], Par['Flight path'])
    #Tmax   = Get_TOF_FromE(Par['Minimum E'], Par['Flight path'])
    Tmin1 = max(Tmin,(Tmin - dT))
    Tmax1 = min(Tmax,(Tmax - Tbin[-1] - dT)) # use last Tbin here, the longest TOF to be used in that estimate
    #print('Emin',Get_E_FromTOF(Tmax1, Par['Flight path']), 'Emax=', Get_E_FromTOF(Tmin1, Par['Flight path']))
    Texp1  = Texp  [np.where(((Texp > Tmin1) & (Texp < Tmax1)))]
    TrExp1 = TrExp [np.where(((Texp > Tmin1) & (Texp < Tmax1)))]

    # calculate the values of Theoretical transmission averaged over the time bin used in experiment
    TrTheor = np.zeros(len(Texp1))
    # set TtempArr to first Tbin value, then will be chekcing if it needs to be recalculated
    TbinCurrent = Tbin[0]
    TtempArr = np.arange(NsubCells) * Tbin[0]/ NsubCells
    for i in range(len(Texp1)):
        #check if Tbin has changed, need to recalculate TtempArr
        if TbinCurrent != Tbin[i] :
            TbinCurrent = Tbin[i]
            TtempArr = np.arange(NsubCells) * Tbin[i] / NsubCells
        #Calculate transmission in all points in TtempArr shifted by dT and Texp[i]
        TrTempArr = TrConvld(TtempArr + Texp1[i] + dT)
        TrTheor[i] = np.average(TrTempArr)

    ChiSq = np.sum((TrTheor - TrExp1) ** 2)
    #ChiSq = -np.sum( (TrTheor * TrExp1) )
    print('Chi square=', ChiSq,'\n**********************************\n')

    if Plot:
        plt.figure(figsize=(14,3.5))
        plt.subplot(121)
        plt.scatter(Texp1, TrExp1, label='Measured', color='g', marker='.')
        plt.plot(Texp1, TrTheor, label='Fitted', color='m')
        plt.legend()
        plt.grid(True)
        plt.xlabel("Time (us)")
        plt.xscale('log')
        plt.ylabel("Transmission")
        # plt.xlim([50,200])
        #--------------------------------
        plt.subplot(122)
        Earr = Get_E_FromTOF(Texp1+dT, Par['Flight path'])
        plt.scatter(Earr, TrExp1, label='Measured', color='g', marker='.')
        plt.plot(Earr, TrTheor, label='Fitted', color='m')
        plt.legend()
        plt.grid(True)
        plt.xlabel("Energy (eV)")
        plt.xscale('log')
        plt.ylabel("Transmission")

    return ChiSq


# -------------------------------------------------------------------------------
# Fitting function for L and dT
# FitPar - list of two parameters L and dT in FitPar[0] and FitPar[1]
# Texp, TrExp_T - experimental data cross section
# EarrIdeal, TrIdeal_E - energy array and ideal theoretical cross section function
# Par - parameters of the model
# -------------------------------------------------------------------------------
def FuncToMinimize_PathCalibration(FitPar, Texp, TrExp_T, EarrIdeal, TrIdeal_E, Par):
    Par['Flight path'] = FitPar[0]
    Par['Trigger delay'] = FitPar[1]
    print('L=', FitPar[0], 'dT=', FitPar[1])
    # ----------------------------------------------------------------------------------
    # Convolve ideal Theoretical transmission with beam pulse profile
    # this depends on L and dT parameters, needs to be within minimizer
    TrConv_T, Tmax = tr.ConvolveTrWithPulseProfile(Par, EarrIdeal, TrIdeal_E, BEAM_ARR_DIM)
    # Calculate the difference from experimental points
    ChiSq = tr.CalcTransmForExpPoints(Par, Texp, TrExp_T, TrConv_T, Tmax, NsubCells)

    return ChiSq


# -------------------------------------------------------------------------------
# Calculate array of Tbn values from the experimental TOF array.
# The left boundary is saved in Pixelman code, Tbin starts from TOF value to the right (adding time)
# Input: Texp - TOF array from experimental data file
# Returns: Tbin Array
# -------------------------------------------------------------------------------
def CalcTbinArray(Texp):
    # Calculate Tbin array automatically
    # need to take care of the readout gaps
    TexpDif1 = np.diff(Texp)
    TexpDif2 = np.diff(TexpDif1)

    # check that there are not too many jumps in Tbin values (due to gaps), otherwise something is not right here
    if len(np.where(TexpDif2>TexpDif1[1:]*0.05)) > 100 : # compared to *0.05 - Spectra.txt file has limited number of digits and often Tbins vary slightly, e.g. 10.24 us binning at 10 ms has 10000.2, then 10001.3, etc
        raise Exception("Cannot calculate Tbn array, something is wrong with TOF array!!!!\n Too many large jumps in TOF array\n Exit here")
    print('Found gaps in TOF array at indices',np.where(TexpDif2>TexpDif1[1:]*0.05))

    Tbin = np.zeros(len(Texp))
    # first cell is set to second Diff cell
    Tbin[0] = TexpDif1[0]
    # rest of Tbins are the differences from the cell to the previos one
    Tbin[1:] = TexpDif1
    # now correct those large jumps in TexpDiff1 (e.g. gaps for readout) - set them to proper values
    for i in np.where(TexpDif2>TexpDif1[1:]*0.05):
        Tbin[i+2] = TexpDif1[i+2]

    #plt.plot(Texp, Tbin, label='Fitted', color='m')
    #plt.xlim([0,100])
    #plt.ylim([0,0.1])

    return Tbin
