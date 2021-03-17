from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from spectrum import Spectrum
from beamline import Beamline, saveInput
from materials import Materials
from image_viewer import ImageViewerWindow
import os
import ctypes

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("NeutronPy")

        layout = QGridLayout()
        #layout.setColumnStretch(1,3)
        #layout.setColumnStretch(2,3)


        layout.addWidget(Beamline(), 2, 3, 1, 1)
        layout.addWidget(Beamline(), 2, 2, 1, 1)
        layout.addWidget(Spectrum(1), 0, 2, 2, 2)
        layout.addWidget(ImageViewerWindow(), 0, 0, 3, 2)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

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
