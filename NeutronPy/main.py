from PyQt5 import QtCore, QtGui, QtWidgets
from spectrum import Spectrum
from beamline import Beamline, saveInput
from materials import Materials
from image_viewer import ImageViewerWindow
import os
import ctypes

class Ui_integrated(object):
    def setupUi(self, integrated):
        global fullParameters

        integrated.setObjectName("NeutronPy")

        #Setting up the tabs
        self.tabWidget = QtWidgets.QTabWidget(integrated)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1301, 651))
        self.tabWidget.setObjectName("tabWidget")

        #Image Viewer
        self.tab = ImageViewerWindow()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")

        #Beam Line Characteristics
        self.tab_2 = Beamline()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, " ")

        #Materials Characteristics
        self.tab_3 = Materials()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")

        #Data Visualization

        #fullParameters = [flightPath, delayOnTrigger, [minE, maxE], [materialParameters (size 6)] 7 by however many elements / isotopes , [cross_sectional_data (size 2)]]
        fullParameters = [saveInput()]
        print(fullParameters)
        self.tab_4 = Spectrum(fullParameters)
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")

        self.retranslateUi(integrated)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(integrated)

    #Displays text
    def retranslateUi(self, integrated):
        _translate = QtCore.QCoreApplication.translate
        integrated.setWindowTitle(_translate("NeutronPy", "NeutronPy"))

        #text for tab 1
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("integrated", "File Selection"))

        #text for tab 2
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("integrated", "Beam Line"))

        #text for tab 3
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("integrated", "Material Characteristics"))

        #text for tab 4
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("integrated", "Spectra Visualization"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    #adding the logo of the application
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    app.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'logo.png'))
    app_icon = QtGui.QIcon()
    app_icon.addFile('logo.png', QtCore.QSize(48,48))

    integrated = QtWidgets.QWidget()
    ui = Ui_integrated()
    ui.setupUi(integrated)

    integrated.show()
    sys.exit(app.exec_())
