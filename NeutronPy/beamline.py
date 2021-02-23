import sys
from PyQt5 import QtCore, QtGui, QtWidgets

import pandas as pd
import numpy as np


class Beamline(QtWidgets.QWidget):
    def __init__(self):
        super(Beamline, self).__init__()
        self.initUI()

    def initUI(self):

        self.groupBox_3 = QtWidgets.QGroupBox(self)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 20, 280, 241))
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

        self.retranslateUi(QtWidgets.QWidget())

        #self.show() - UNCOMMENT THIS LINE FOR SELF DEBUGGING

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

#beam line input backend logic for saving to variables
def saveInput():
    ui = Beamline()
    def returnInput():
        return [flightPath, delayOnTrigger, [minimumEnergyRange, maximumEnergyRange]]
    try:
        flightPath = float(ui.length.text())
        delayOnTrigger = float(ui.delay.text())
        minimumEnergyRange = float(ui.minE.text())
        maximumEnergyRange = float(ui.maxE.text())
        returnInput()
    except ValueError:
        print('One of your inputs is not a number')
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Beamline()

    #triggers for beam line input
    ui.length.textChanged['QString'].connect(saveInput)
    ui.delay.textChanged['QString'].connect(saveInput)
    ui.minE.textChanged['QString'].connect(saveInput)
    ui.maxE.textChanged['QString'].connect(saveInput)
    sys.exit(app.exec_())
