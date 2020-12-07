import sys
from PyQt5 import QtWidgets
import matplotlib
import matplotlib.figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

#from materials.py import *

import pandas as pd
import numpy as np


class Spectrum(QtWidgets.QWidget):
    def __init__(self):
        super(Spectrum, self).__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(100, 100, 800, 600)
        self.center()
        self.setWindowTitle('NeutronPy Spectra Visualization of ' + str(element_name))

        grid = QtWidgets.QGridLayout()
        self.setLayout(grid)


        btn1 = QtWidgets.QPushButton('Plot 1: Cross Section (MeV vs Barns) ', self)
        btn1.resize(btn1.sizeHint())
        btn1.clicked.connect(self.crossSectionalData)
        grid.addWidget(btn1, 5, 0)

        btn2 = QtWidgets.QPushButton('Plot 2: Spectra (Transmission vs Energy)', self)
        btn2.resize(btn2.sizeHint())
        btn2.clicked.connect(self.AntonCode)
        grid.addWidget(btn2, 5, 1)

        #btn3 = QtWidgets.QPushButton('Parameters', self)
        #btn3.resize(btn3.sizeHint())
        #btn3.clicked.connect(self.show_parameter_window)
        #grid.addWidget(btn3, 5, 2)

        self.figure = matplotlib.figure.Figure()
        self.canvas = FigureCanvas(self.figure)
        #self.toolbar = NavigationToolbar(self.canvas, self)
        grid.addWidget(self.canvas, 3, 0, 1, 2)

        self.show()

    def crossSectionalData(self):
        self.figure.clf()
        ax3 = self.figure.add_subplot(111)
        #Pass Diether's cross sectional data

        x = [i for i in range(100)]
        y = [i**0.5 for i in x]

        ax3.plot(x, y, 'r.-')
        ax3.set_title('Cross Section (MeV vs Barns)')
        self.canvas.draw_idle()

    def AntonCode(self):

        self.figure.clf()
        ax1 = self.figure.add_subplot(211)

        x1 = [i for i in range(200)]
        y1 = [x[0]*x[1]*x[2]*x[3]*x[6]*x[7]*x[8]*x[9] for i in x1]

        ax1.plot(x1, y1, 'b.-')
        ax1.set_title("Experimental Spectrum") #obtained from Diether's experimental data
        ax1.set_xlabel("Energy / Time") #Energy, Time, or Wavelength - depending on how the user picks it
        ax1.set_ylabel("Transmission")
        ax2 = self.figure.add_subplot(212)


        x2 = [i for i in range(100)] #pass the x1, y1 values to here for Anton's method

        #pass anton's method using the global variable fullParameters
        y2 = [fullParameters[1] for i in x2]

        ax2.plot(x2, y2, 'b.-')
        self.canvas.draw_idle()
        ax2.set_title('Fitting')
        ax2.set_xlabel("Energy / Time")
        ax2.set_ylabel("Transmission")


    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


def getParameter(self):
    global fullParameters


    #TINO - don't mind the float(self.____) part this was for something else
    flightPath = float(self.flightPath.text()) #1 Flight Path: L (meters)
    delayOnTrigger = float(self.delayOnTrigger.text()) #2 Delay on trigger: dT (miliseconds)
    minimumEnergyRange = float(self.minimumEnergyRange.text()) #3 Minimum and Maximum Energy Range (eV)
    maximumEnergyRange = float(self.maximumEnergyRange.text())

    #PAULINA - don't mind the float(self.____) part this was for something else
    elementName = ""
    isotopicAbundance = float(self.isotopicAbundance.text()) #value between 0 and 1 (for Ag it is 0.52 and 0.48 for Ag-107 and Ag-109 isotopes)
    atomicFraction = float(self.atomicFraction.text()) #number of 0-1. (e.g. Gd2O3 it is 0.4 for Gd and 0.6 for O)
    density = float(self.density.text()) #Rho (g/cm^3)
    thickness = float(self.density.text()) #d (um)
    component = int(self.component.text())# integer number starting from 1 (in case there are several different samples in the beam behind each other)


    #number of assert statements to make sure user input is as desired
    assert flightPath >= 0
    assert delayOnTrigger >= 0
    assert minimumEnergyRange >= 0
    assert maximumEnergyRange > minimumEnergyRange
    assert 0 <= isotopicAbundance and isotopicAbundance <= 1
    assert 0 <= atomicFraction and atomicFraction <= 1
    assert density > 0
    assert thickness > 0
    assert component >= 1



    energyRange = np.array([minimumEnergyRange, maximumEnergyRange]) #size: 2

    #IsotopeName	Abundance	AtomicFraction	Density	AtomicMass	"Thickness,um"	GrupN - will be provided by PAULINA
    materialParameters = np.array([elementName, isotopicAbundance, atomicFraction, density, thickness, component]) #size: 6


    cross_sectional_data = np.array([]) #size: 2 - DIETHER

    #fullParameters = [flightPath, delayOnTrigger, [minE, maxE], [materialParameters (size 6)] 7 by however many elements / isotopes , [cross_sectional_data (size 2)]]
    fullParameters = np.array([flightPath, delayOnTrigger, energyRange, materialParameters, cross_sectional_data]) #size: 5


#TODO - import DIETHER's cross_sectional_data -  Theoretically have diether's array be passed for the cross_sectional_data

#use pandas frame

directory, elementTXT = "cross_sectional_data/file_name.txt".split("/", 1) #unnecessary for integration - DIETHER already has a program/ function for this
element, file_extension = elementTXT.split(".", 1)

element_name = element
#app = QtWidgets.QApplication(sys.argv)
#app.aboutToQuit.connect(app.deleteLater)
#GUI = Spectrum()
#sys.exit(app.exec_())
