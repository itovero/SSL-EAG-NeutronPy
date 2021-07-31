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
        self.groupBox_3.setGeometry(QtCore.QRect(0, 0, 280, 380)) #set window size
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
        #self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        #self.label_9.setGeometry(QtCore.QRect(140, 240, 120, 16))
        #self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(10, 240, 101, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(10, 290, 101, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(10, 340, 101, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(180, 240, 101, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(180, 290, 101, 16))
        self.label_14.setObjectName("label_14")

        #establish text input boxes
        self.length = QtWidgets.QLineEdit(self.groupBox_3)
        self.length.setGeometry(QtCore.QRect(120, 40, 51, 22))
        self.length.setText("16.4")
        self.length.setObjectName("length")
        self.delay = QtWidgets.QLineEdit(self.groupBox_3)
        self.delay.setGeometry(QtCore.QRect(120, 90, 51, 22))
        self.delay.setText("3.6")
        self.delay.setObjectName("delay")
        self.minE = QtWidgets.QLineEdit(self.groupBox_3)
        self.minE.setGeometry(QtCore.QRect(120, 140, 51, 22))
        self.minE.setText("0")
        self.minE.setObjectName("minE")
        self.maxE = QtWidgets.QLineEdit(self.groupBox_3)
        self.maxE.setGeometry(QtCore.QRect(120, 190, 51, 22))
        self.maxE.setText("0")
        self.maxE.setObjectName("maxE")
        self.proton = QtWidgets.QLineEdit(self.groupBox_3)
        self.proton.setGeometry(QtCore.QRect(120, 240, 51, 22))
        self.proton.setText("0")
        self.proton.setObjectName("proton")
        self.timeBin = QtWidgets.QLineEdit(self.groupBox_3)
        self.timeBin.setGeometry(QtCore.QRect(120, 290, 51, 22))
        self.timeBin.setText("0")
        self.timeBin.setObjectName("timeBin")
        self.skipPoints = QtWidgets.QLineEdit(self.groupBox_3)
        self.skipPoints.setGeometry(QtCore.QRect(120, 340, 51, 22))
        self.skipPoints.setText("0")
        self.skipPoints.setObjectName("skipPoints")

        #Load beamline characteristics from file
        #self.loadbeam_button = QToolButton(self)
        #self.loadbeam_button.setText('Load Characteristics')
        #self.loadbeam_button.clicked.connect(self.loadbeam_file)
        #self.loadbeam_button.move(5, 240)

        #Save characteristics
        #TODO: Merge save method with materials.py and save with pandas
        #self.savebeam_button = QToolButton(self)
        #self.savebeam_button.setText('Save Characteristics')
        #self.savebeam_button.clicked.connect(self.savebeam_file)
        #self.savebeam_button.move(5, 270)


        self.retranslateUi(QtWidgets.QWidget())
        self.show()

    #return input box values as an array of floats
    def saveInput(self):
        try:
            flightPath = float(self.length.text())
            delayOnTrigger = float(self.delay.text())
            minimumEnergyRange = float(self.minE.text())
            maximumEnergyRange = float(self.maxE.text())
            protonPulseGap = float(self.proton.text())
            timeBin = float(self.timeBin.text())
            skipPoints = float(self.skipPoints.text())
            #print([flightPath, delayOnTrigger, [minimumEnergyRange, maximumEnergyRange], protonPulseGap, timeBin, skipPoints])
            return [flightPath, delayOnTrigger, [minimumEnergyRange, maximumEnergyRange], protonPulseGap, timeBin, skipPoints]
        except ValueError:
            print('One of your inputs is not a number')

    def saveArray(self):
        try:
            flightPath = float(self.length.text())
            delayOnTrigger = float(self.delay.text())
            minimumEnergyRange = float(self.minE.text())
            maximumEnergyRange = float(self.maxE.text())
            protonPulseGap = float(self.proton.text())
            timeBin = float(self.timeBin.text())
            skipPoints = float(self.skipPoints.text())
            return [flightPath, delayOnTrigger, minimumEnergyRange, maximumEnergyRange, protonPulseGap, timeBin, skipPoints]
        except ValueError:
            print('One of your inputs is not a number')

    def update_inputs(self, pandasFrame):
        self.length.setText(str(pandasFrame.iloc[5, 0]))
        self.delay.setText(str(pandasFrame.iloc[5, 1]))
        self.minE.setText(str(pandasFrame.iloc[5, 2]))
        self.maxE.setText(str(pandasFrame.iloc[5, 3]))
        self.proton.setText(str(pandasFrame.iloc[5, 4]))
        self.timeBin.setText(str(pandasFrame.iloc[5, 5]))
        self.skipPoints.setText(str(pandasFrame.iloc[5, 6]))


    #populate the labels created previously with text
    def retranslateUi(self, integrated):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox_3.setTitle(_translate("deliverable", "Beam Line Characteristics"))
        self.label.setText(_translate("deliverable", "Flight Path Length"))
        self.label_2.setText(_translate("deliverable", "Delay on Trigger"))
        self.label_3.setText(_translate("deliverable", "Minimum Energy"))
        self.label_4.setText(_translate("deliverable", "Maximum Energy"))
        self.label_5.setText(_translate("deliverable", "meters"))
        self.label_6.setText(_translate("deliverable", "microseconds"))
        self.label_7.setText(_translate("deliverable", "electronvolt"))
        self.label_8.setText(_translate("deliverable", "electronvolt"))
        #self.label_9.setText(_translate("deliverable", "None Selected"))
        self.label_10.setText(_translate("deliverable", "Proton Pulse Gap"))
        self.label_11.setText(_translate("deliverable", "Time Bin"))
        self.label_12.setText(_translate("deliverable", "Skip Points"))
        self.label_13.setText(_translate("deliverable", "microseconds"))
        self.label_14.setText(_translate("deliverable", "microseconds"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Beamline()
    sys.exit(app.exec_())
