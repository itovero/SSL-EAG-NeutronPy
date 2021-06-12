import sys
#from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar
#from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import *

class Progress(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Loading Data ... ')
        self.resize(500, 100)

        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(25, 25, 300, 40)
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)

        self.setWindowModality(Qt.ApplicationModal)
        self.show()


    def setValue(self, n, runtime = 1):
        self.progressBar.setValue(n)
        if (n == 100):
            self.setWindowTitle('Complete!')
            #self.setWindowTitle(f'Complete! Finishing loading data in {toc - tic:0.4f} seconds')

    def finishFits2Array(self, timer):
        self.setWindowTitle(f'Finished loading all .fits file in {timer:0.4f} seconds!')
        self.progressBar.setFormat(f"Finished loading all .fits file in {timer:0.4f} seconds!")
        self.progressBar.setAlignment(Qt.AlignCenter)

    def startLoadImageCube(self):
        self.setWindowTitle('Loading Image Cube now...')
        self.progressBar.setFormat("Loading Image Cube now...")
        self.progressBar.setAlignment(Qt.AlignCenter)

    def finishLoadImageCube(self, timer):
        self.setWindowTitle(f'Finished loading Image Cube in {timer:0.4f} seconds!')
        self.progressBar.setFormat(f"Finished loading Image Cube in {timer:0.4f} seconds!")
        self.progressBar.setAlignment(Qt.AlignCenter)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    loading = Progress()
    loading.show()
    #sys.exit(app.exec_())       