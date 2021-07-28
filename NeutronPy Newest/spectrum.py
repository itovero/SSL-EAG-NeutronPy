import sys, traceback
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import *
import pandas as pd
from beamline import Beamline
from image_viewer import ImageViewerWindow
from materials import Materials
import numpy as np
from error_page import Error

#Graphing modules
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.qt_compat import QtCore, QtWidgets
if QtCore.qVersion() >= "5.":
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)



class plotLoader(QRunnable):
    #Separate Thread to handle mutliprocesses 
    #This one, in particular, deals with assisting the plotting that happens on Button 1 (left)
    def __init__(self, fn, *args, **kwargs):
        super(plotLoader, self).__init__()
        # Store constructor arguments (re-used for processing)
        #args and kwargs could be the parameters for different functionalities
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except: 
            #Handles exception if there's an issue with loading data
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]




class Spectrum(QtWidgets.QWidget):
    def __init__(self, beamline = None, materials = None, imageviewer = None):
        '''
        The Spectrum takes in the instances of beamline, materials, and 
        imageviewer created in main.py. This is to track the variables of inputs
        to be reflected to the spectrum
        '''
        self.beamline = beamline
        self.materials = materials
        self.imageviewer = imageviewer

        '''
        For multi-threading data loadout
        '''
        self.threadpool = QThreadPool()


        super(Spectrum, self).__init__()
        self.initUI()

    def initUI(self):
        '''
        The UI initialization
        '''
        self.setGeometry(100, 100, 960, 600)
        self.center()

        grid = QtWidgets.QGridLayout()
        self.setLayout(grid)

        '''
        Creating buttons to generate the plots.
        We connect the pressing of the buttons to crossSectionalData 
        and AntonCode function for plotting
        '''
        btn1 = QtWidgets.QPushButton('Cross Section (MeV vs Barns) ', self)
        btn1.clicked.connect(self.crossSectionalData)
        grid.addWidget(btn1, 5, 0)

        btn2 = QtWidgets.QPushButton('Spectra (Transmission vs Energy)', self)
        btn2.clicked.connect(self.AntonCode)
        grid.addWidget(btn2, 5, 1)

        btn3 = QtWidgets.QPushButton('Converging Fit', self)
        btn3.clicked.connect(self.ConvergeFit)
        grid.addWidget(btn3, 5, 2)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        grid.addWidget(self.canvas, 3, 0, 1, 3)
        
        self.toolbar = QtWidgets.QToolBar()
        self.toolbar.addWidget(NavigationToolbar(self.canvas, self))
        grid.setMenuBar(self.toolbar)
        #self.show() #- UNCOMMENT THIS LINE FOR SELF DEBUGGING

    def crossSectionalData(self):
        def crossSectionPlot(canvas, sumdata):
            #Plotting initialization
            self.figure.clear()
            ax3 = canvas.figure.subplots()
            #The plotting function itself
            x = [i for i in range(self.z_start, self.z_end)]
            y = [sumdata[i - self.z_start] for i in x]
            ax3.plot(x, y, 'r.-')
            ax3.grid()
            ax3.set_title('Cross Section (MeV vs Barns)')
            canvas.draw_idle()

        try:
            '''
            Obtaining the updated parameter inputs from beamline, materials, 
            and imageviewer
            '''
            self.getUpdatedParameters()

            '''
            Multi-threading functionality
            '''
            crossThread = plotLoader(crossSectionPlot, self.canvas, self.sum_image_data)
            self.threadpool.start(crossThread)
        except:
            self.error = Error("Sample Data Not Yet Selected for Plotting")
            self.error.show()


    def AntonCode(self):
        def AntonPlot(canvas):
            '''
            Plotting initialization
            '''
            self.figure.clear()
            ax1 = canvas.figure.subplots()

            '''
            The plotting function(s) itself (QuickFit)
            As we are plotting multiple functions in one graph
            '''    
            #TODO: Implemenet Anton's codebase onto the graph using sum_image_data
            x1 = [i for i in range(200)]
            y1 = [2 for i in x1]
            x1_1 = [i for i in range(200)]
            y1_1 = np.sin(x1_1)
            ax1.plot(x1, y1, 'b.-')
            ax1.plot(x1_1, y1_1)
            ax1.set_title("Experimental Spectrum")
            ax1.set_xlabel("Energy / Time") #Energy, Time, or Wavelength - depending on how the user picks it
            ax1.set_ylabel("Transmission")
            canvas.draw_idle()
        try:
            '''
            Obtaining the updated parameter inputs from beamline, materials, 
            and imageviewer
            '''
            self.getUpdatedParameters()
            '''
            Multi-threading functionality
            '''
            antonThread = plotLoader(AntonPlot, self.canvas)
            self.threadpool.start(antonThread)
        except:
            antonThread = plotLoader(AntonPlot, self.canvas)
            self.threadpool.start(antonThread)

            self.error = Error("Sample Data Not Yet Selected for Plotting")
            self.error.show()

    def ConvergeFit(self):
        def ConvergePlot(canvas):
            '''
            Plotting initialization - there will be 2 graphs on the window
            '''
            self.figure.clear()
            ax1 = canvas.figure.subplots()

            '''
            The plotting function(s) itself (QuickFit)
            As we are plotting multiple functions in one graph
            '''    
            #TODO: Implemenet Anton's codebase onto the graph using sum_image_data
            x1 = [i for i in range(200)]
            y1 = [2 for i in x1]
            x1_1 = [i for i in range(200)]
            y1_1 = np.cos(x1_1)
            ax1.plot(x1, y1, 'b.-')
            ax1.plot(x1_1, y1_1)
            ax1.set_title("Experimental Spectrum")
            ax1.set_xlabel("Energy / Time") #Energy, Time, or Wavelength - depending on how the user picks it
            ax1.set_ylabel("Transmission")
            canvas.draw_idle()
        try:
            '''
            Obtaining the updated parameter inputs from beamline, materials, 
            and imageviewer
            '''
            self.getUpdatedParameters()
            '''
            Multi-threading functionality
            '''
            convergeThread = plotLoader(ConvergePlot, self.canvas)
            self.threadpool.start(convergeThread)
        except:
            convergeThread = plotLoader(ConvergePlot, self.canvas)
            self.threadpool.start(convergeThread)
            
            self.error = Error("Sample Data Not Yet Selected for Plotting")
            self.error.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def getUpdatedParameters(self):
        '''
        Function that obtains the updated inputs from beamline, materials,
        and image viewer. We call the saveInput functions for all these instances
        and that is converted into an array called fullParameters above
        '''

        '''IMAGEVIEWER INPUT'''
        self.imageviewerInput = self.imageviewer.saveInput() #imageviwerInput = [[xmin, xmax], [ymin, ymax], [z_start, z_end], z, backcoef, self.sumImageCube]

        self.xmin = self.imageviewerInput[0][0]
        self.xmax = self.imageviewerInput[0][1]
        self.ymin = self.imageviewerInput[1][0]
        self.ymax = self.imageviewerInput[1][1]
        self.z_start = self.imageviewerInput[2][0]
        self.z_end = self.imageviewerInput[2][1]
        self.z = self.imageviewerInput[3]
        self.backcoef = self.imageviewerInput[4]
        self.sum_image_data = self.imageviewerInput[5]



        '''BEAMLINE INPUT'''
        self.beamlineInput = self.beamline.saveInput() #beamlineInput = [flightPath, delayOnTrigger, [minimumEnergyRange, maximumEnergyRange]]

        self.flightPath =  self.beamlineInput[0] #1 Flight Path: L (meters)
        self.delayOnTrigger = self.beamlineInput[1] #2 Delay on trigger: dT (miliseconds)
        self.energyRange = self.beamlineInput[2] #3 Minimum and Maximum Energy Range (eV)
        


        '''MATERIALS INPUT'''
        self.materialsInput = self.materials.saveInput() #materialsInput is a pandas frame with the structure shown below:
        '''
                    Element Name | Abundance | Atomic Mass | Atomic Fraction | Density | Thickness | Component 
        Material 1
        Material 2
        Material 3
        Material 4
        Material 5
        '''
        #where you can access the inputs by selecting the coordinates (e.g. materialsInput[0, 1] would return Materials 1's abundance)
        #Note that not all 5 materials are used, for this instance the frame element is entered 'NaN'
        

        #number of assert statements to make sure user input is as desired
        #TODO: Create assertion tests to catch edge cases for completeness
        """
        assert flightPath >= 0
        assert delayOnTrigger >= 0
        assert minimumEnergyRange >= 0
        assert maximumEnergyRange > minimumEnergyRange
        assert 0 <= isotopicAbundance and isotopicAbundance <= 1
        assert 0 <= atomicFraction and atomicFraction <= 1
        assert density > 0
        assert thickness > 0
        assert component >= 1
    
        """

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Spectrum()
    sys.exit(app.exec_())
