import sys
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import *

#Class for the loading window!
class Progress(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Loading Data ... ')
        self.resize(500, 100)

        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(25, 25, 300, 40)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)

        self.setWindowModality(Qt.ApplicationModal)
        self.show()

    @pyqtSlot(int, int, float)
    def setValue(self, n, runtime = 1, timer = 0): #Updates the percentage loaded to be shown
        if runtime == 1:
            self.progressBar.setValue(n)
            if (n == 100):
                self.setWindowTitle('Complete!')
                #self.setWindowTitle(f'Complete! Finishing loading data in {toc - tic:0.4f} seconds')
        elif runtime == 2:
            self.finishFits2Array(timer)
        elif runtime == 4:
            self.closePopup()

    #Couple of helper functions to update states
    def finishFits2Array(self, timer): 
        self.setWindowTitle(f'Finished loading all .fits file in {timer:0.4f} seconds!')
        self.progressBar.setFormat(f"Finished loading all .fits file in {timer:0.4f} seconds!")
        self.progressBar.setAlignment(Qt.AlignCenter)

    def startLoadImageCube(self):
        self.setWindowTitle('Loading Image Cube now... (may take a while)')
        self.progressBar.setFormat("Loading Image Cube now... (may take a while)")
        self.progressBar.setAlignment(Qt.AlignCenter)

    def finishLoadImageCube(self, timer):
        self.setWindowTitle(f'Finished loading Image Cube in {timer:0.4f} seconds!')
        self.progressBar.setFormat(f"Finished loading Image Cube in {timer:0.4f} seconds!")
        self.progressBar.setAlignment(Qt.AlignCenter)

    def closePopup(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    loading = Progress()
    loading.show()
    #sys.exit(app.exec_())       