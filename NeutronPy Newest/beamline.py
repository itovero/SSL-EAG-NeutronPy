import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from materials import Materials
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pandas as pd
import numpy as np
from os import listdir, path



class Beamline(QtWidgets.QWidget):
    def __init__(self):
        super(Beamline, self).__init__()
        self.initUI()

    #establish the layout of the beamline UI
    def initUI(self):
        self.groupBox_3 = QtWidgets.QGroupBox(self)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 0, 280, 300)) #set window size
        self.groupBox_3.setObjectName("groupBox_3")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(10, 40, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 140, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 190, 101, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(180, 40, 41, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(180, 90, 71, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(180, 140, 71, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(180, 190, 71, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(140, 240, 120, 16))
        self.label_9.setObjectName("label_9")

        #establish text input boxes
        self.length = QtWidgets.QLineEdit(self.groupBox_3)
        self.length.setGeometry(QtCore.QRect(120, 40, 51, 22))
        self.length.setText("0")
        self.length.setObjectName("length")
        self.delay = QtWidgets.QLineEdit(self.groupBox_3)
        self.delay.setGeometry(QtCore.QRect(120, 90, 51, 22))
        self.delay.setText("0")
        self.delay.setObjectName("delay")
        self.minE = QtWidgets.QLineEdit(self.groupBox_3)
        self.minE.setGeometry(QtCore.QRect(120, 140, 51, 22))
        self.minE.setText("0")
        self.minE.setObjectName("minE")
        self.maxE = QtWidgets.QLineEdit(self.groupBox_3)
        self.maxE.setGeometry(QtCore.QRect(120, 190, 51, 22))
        self.maxE.setText("0")
        self.maxE.setObjectName("maxE")

        #Load beamline characteristics from file
        self.loadbeam_button = QToolButton(self)
        self.loadbeam_button.setText('Load Characteristics')
        self.loadbeam_button.clicked.connect(self.loadbeam_file)
        self.loadbeam_button.move(5, 240)

        #Save characteristics
        self.savebeam_button = QToolButton(self)
        self.savebeam_button.setText('Save Characteristics')
        self.savebeam_button.clicked.connect(self.savebeam_file)
        self.savebeam_button.move(5, 270)


        self.retranslateUi(QtWidgets.QWidget())
        self.show()

    #return input box values as an array of floats
    def saveInput(self):
        try:
            flightPath = float(self.length.text())
            delayOnTrigger = float(self.delay.text())
            minimumEnergyRange = float(self.minE.text())
            maximumEnergyRange = float(self.maxE.text())
            print([flightPath, delayOnTrigger, [minimumEnergyRange, maximumEnergyRange]])
            return [flightPath, delayOnTrigger, [minimumEnergyRange, maximumEnergyRange]]
        except ValueError:
            print('One of your inputs is not a number')

    #load saved characteristics
    def loadbeam_file(self):
        self.selectedFile = QFileDialog.getOpenFileName(self, "Load Characteristics")
        if path.isfile(self.selectedFile[0]): 
            pathArr = self.selectedFile[0].split('/')
            self.label_9.setText(pathArr[-1])
            file = open(self.selectedFile[0], 'r')
            fileString = file.read()
            textArr = fileString.split(' ')
            self.length.setText(textArr[0])
            self.delay.setText(textArr[1])
            self.minE.setText(textArr[2])
            self.maxE.setText(textArr[3])

    def savebeam_file(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self,"Save Characteristics","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            file = open(fileName, 'w')

            flightPath = self.length.text()
            delayOnTrigger = self.delay.text()
            minimumEnergyRange = self.minE.text()
            maximumEnergyRange = self.maxE.text()
            text = flightPath + ' ' + delayOnTrigger + ' ' + minimumEnergyRange + ' ' + maximumEnergyRange

            file.write(text)
            file.close()


    #populate the labels created previously with text
    def retranslateUi(self, integrated):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox_3.setTitle(_translate("deliverable", "Beam Line Characteristics"))
        self.label.setText(_translate("deliverable", "Flight Path Length"))
        self.label_2.setText(_translate("deliverable", "Delay on Trigger"))
        self.label_3.setText(_translate("deliverable", "Minimum Energy"))
        self.label_4.setText(_translate("deliverable", "Maximum Energy"))
        self.label_5.setText(_translate("deliverable", "meters"))
        self.label_6.setText(_translate("deliverable", "milliseconds"))
        self.label_7.setText(_translate("deliverable", "electronvolt"))
        self.label_8.setText(_translate("deliverable", "electronvolt"))
        self.label_9.setText(_translate("deliverable", "None Selected"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Beamline()
    sys.exit(app.exec_())
