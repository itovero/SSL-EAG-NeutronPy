from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from spectrum import Spectrum
from beamline import Beamline
from materials import Materials
from image_viewer import ImageViewerWindow
import os
import ctypes

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("NeutronPy")

        layout = QGridLayout()
        #layout.setColumnStretch(2,3)
        #layout.setColumnStretch(1,5)

        beamline = Beamline()
        materials = Materials()
        imageviewer = ImageViewerWindow()
        spectrum = Spectrum(beamline, materials, imageviewer)

        layout.addWidget(beamline, 0, 4, 1, 1)
        layout.addWidget(materials, 2, 2, 1, 3)
        layout.addWidget(spectrum, 0, 2, 2, 2)
        layout.addWidget(imageviewer, 0, 0, 3, 2)

        height = 800
        width = 1550
        self.setMinimumSize(width, height)


        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        #print(Beamline().maxE.text())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    #adding the logo of the application
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    app.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'logo.png'))
    app_icon = QtGui.QIcon()
    app_icon.addFile('logo.png', QtCore.QSize(48,48))

    window = MainWindow()

    window.show()
    sys.exit(app.exec_())
