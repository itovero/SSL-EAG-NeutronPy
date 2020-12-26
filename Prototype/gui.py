
import spectrum
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NeutronPy(object):
    def setupUi(self, NeutronPy):
        NeutronPy.setObjectName("NeutronPy")
        NeutronPy.resize(1186, 600)
        self.groupBox = QtWidgets.QGroupBox(NeutronPy)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 581, 431))
        self.groupBox.setObjectName("groupBox")
        self.graphicsView = QtWidgets.QGraphicsView(self.groupBox)
        self.graphicsView.setGeometry(QtCore.QRect(10, 20, 381, 371))
        self.graphicsView.setObjectName("graphicsView")
        self.comboBox_5 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_5.setGeometry(QtCore.QRect(10, 400, 331, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.groupBox)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(30, 360, 331, 16))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.groupBox)
        self.verticalScrollBar.setGeometry(QtCore.QRect(360, 50, 16, 301))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox)
        self.horizontalSlider.setGeometry(QtCore.QRect(410, 240, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser_5.setGeometry(QtCore.QRect(410, 20, 71, 31))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser_6.setGeometry(QtCore.QRect(410, 60, 71, 31))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser_7.setGeometry(QtCore.QRect(410, 100, 71, 31))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser_8.setGeometry(QtCore.QRect(410, 140, 71, 31))
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser_9.setGeometry(QtCore.QRect(410, 180, 71, 31))
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(460, 220, 61, 16))
        self.label.setObjectName("label")
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(500, 20, 62, 31))
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_4.setGeometry(QtCore.QRect(500, 60, 62, 31))
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_5.setGeometry(QtCore.QRect(500, 100, 62, 31))
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_6.setGeometry(QtCore.QRect(500, 140, 62, 31))
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.doubleSpinBox_7 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_7.setGeometry(QtCore.QRect(500, 180, 62, 31))
        self.doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.groupBox_4 = QtWidgets.QGroupBox(NeutronPy)
        self.groupBox_4.setGeometry(QtCore.QRect(630, 10, 531, 441))
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 20, 511, 201))
        self.groupBox_2.setObjectName("groupBox_2")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.groupBox_2)
        self.graphicsView_2.setGeometry(QtCore.QRect(10, 30, 261, 161))
        self.graphicsView_2.setObjectName("graphicsView_2")

        #self.graphicsView_2 = spectrum.start()



        self.verticalScrollBar_2 = QtWidgets.QScrollBar(self.groupBox_2)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(250, 40, 16, 141))
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.horizontalScrollBar_2 = QtWidgets.QScrollBar(self.groupBox_2)
        self.horizontalScrollBar_2.setGeometry(QtCore.QRect(20, 170, 221, 16))
        self.horizontalScrollBar_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_2.setObjectName("horizontalScrollBar_2")
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_10.setGeometry(QtCore.QRect(300, 30, 101, 31))
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.comboBox_6 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_6.setGeometry(QtCore.QRect(420, 30, 61, 31))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_11.setGeometry(QtCore.QRect(300, 70, 101, 31))
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.doubleSpinBox_8 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_8.setGeometry(QtCore.QRect(420, 70, 62, 31))
        self.doubleSpinBox_8.setObjectName("doubleSpinBox_8")
        self.textBrowser_12 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_12.setGeometry(QtCore.QRect(300, 110, 101, 31))
        self.textBrowser_12.setObjectName("textBrowser_12")
        self.doubleSpinBox_9 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_9.setGeometry(QtCore.QRect(420, 110, 62, 31))
        self.doubleSpinBox_9.setObjectName("doubleSpinBox_9")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 230, 511, 201))
        self.groupBox_6.setObjectName("groupBox_6")
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.groupBox_6)
        self.graphicsView_4.setGeometry(QtCore.QRect(10, 30, 261, 161))
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.verticalScrollBar_4 = QtWidgets.QScrollBar(self.groupBox_6)
        self.verticalScrollBar_4.setGeometry(QtCore.QRect(250, 40, 16, 141))
        self.verticalScrollBar_4.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_4.setObjectName("verticalScrollBar_4")
        self.horizontalScrollBar_4 = QtWidgets.QScrollBar(self.groupBox_6)
        self.horizontalScrollBar_4.setGeometry(QtCore.QRect(20, 170, 221, 16))
        self.horizontalScrollBar_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_4.setObjectName("horizontalScrollBar_4")
        self.textBrowser_17 = QtWidgets.QTextBrowser(self.groupBox_6)
        self.textBrowser_17.setGeometry(QtCore.QRect(300, 30, 101, 31))
        self.textBrowser_17.setObjectName("textBrowser_17")
        self.comboBox_9 = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox_9.setGeometry(QtCore.QRect(420, 30, 61, 31))
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.textBrowser_18 = QtWidgets.QTextBrowser(self.groupBox_6)
        self.textBrowser_18.setGeometry(QtCore.QRect(300, 70, 101, 31))
        self.textBrowser_18.setObjectName("textBrowser_18")
        self.doubleSpinBox_13 = QtWidgets.QDoubleSpinBox(self.groupBox_6)
        self.doubleSpinBox_13.setGeometry(QtCore.QRect(420, 70, 62, 31))
        self.doubleSpinBox_13.setObjectName("doubleSpinBox_13")
        self.textBrowser_19 = QtWidgets.QTextBrowser(self.groupBox_6)
        self.textBrowser_19.setGeometry(QtCore.QRect(300, 110, 101, 31))
        self.textBrowser_19.setObjectName("textBrowser_19")
        self.doubleSpinBox_14 = QtWidgets.QDoubleSpinBox(self.groupBox_6)
        self.doubleSpinBox_14.setGeometry(QtCore.QRect(420, 110, 62, 31))
        self.doubleSpinBox_14.setObjectName("doubleSpinBox_14")
        self.groupBox_3 = QtWidgets.QGroupBox(NeutronPy)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 460, 391, 121))
        self.groupBox_3.setObjectName("groupBox_3")
        self.doubleSpinBox_12 = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_12.setGeometry(QtCore.QRect(240, 30, 62, 31))
        self.doubleSpinBox_12.setObjectName("doubleSpinBox_12")
        self.comboBox_8 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_8.setGeometry(QtCore.QRect(320, 30, 51, 31))
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.textBrowser_16 = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser_16.setGeometry(QtCore.QRect(10, 30, 201, 31))
        self.textBrowser_16.setObjectName("textBrowser_16")
        self.groupBox_5 = QtWidgets.QGroupBox(NeutronPy)
        self.groupBox_5.setGeometry(QtCore.QRect(440, 460, 731, 121))
        self.groupBox_5.setObjectName("groupBox_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_5)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 201, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox_5)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 60, 201, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.groupBox_5)
        self.textBrowser_3.setGeometry(QtCore.QRect(390, 60, 201, 31))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.groupBox_5)
        self.textBrowser_4.setGeometry(QtCore.QRect(390, 20, 201, 31))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        self.doubleSpinBox.setGeometry(QtCore.QRect(600, 60, 62, 31))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(600, 20, 62, 31))
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox.setGeometry(QtCore.QRect(220, 20, 131, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_2.setGeometry(QtCore.QRect(220, 60, 131, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_3.setGeometry(QtCore.QRect(670, 20, 51, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_4.setGeometry(QtCore.QRect(670, 60, 51, 31))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")

        self.retranslateUi(NeutronPy)
        QtCore.QMetaObject.connectSlotsByName(NeutronPy)

    def retranslateUi(self, NeutronPy):
        _translate = QtCore.QCoreApplication.translate
        NeutronPy.setWindowTitle(_translate("NeutronPy", "NeutronPy"))
        self.groupBox.setTitle(_translate("NeutronPy", "Viewer"))
        self.comboBox_5.setItemText(0, _translate("NeutronPy", "File 1"))
        self.comboBox_5.setItemText(1, _translate("NeutronPy", "File 2"))
        self.comboBox_5.setItemText(2, _translate("NeutronPy", "File 3"))
        self.textBrowser_5.setHtml(_translate("NeutronPy", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">X-Min</p></body></html>"))
        self.textBrowser_6.setHtml(_translate("NeutronPy", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">X-Max</p></body></html>"))
        self.textBrowser_7.setHtml(_translate("NeutronPy", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Y-Min</p></body></html>"))
        self.textBrowser_8.setHtml(_translate("NeutronPy", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Y-Max</p></body></html>"))
        self.textBrowser_9.setHtml(_translate("NeutronPy", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Z</p></body></html>"))
        self.label.setText(_translate("NeutronPy", "Brightness"))
        self.groupBox_4.setTitle(_translate("NeutronPy", "Plots"))
        self.groupBox_2.setTitle(_translate("NeutronPy", "Spectrum"))
        self.textBrowser_10.setHtml(_translate("NeutronPy", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Units of Index</p></body></html>"))
        self.comboBox_6.setItemText(0, _translate("NeutronPy", "Unit"))
        self.textBrowser_11.setHtml(_translate("NeutronPy", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">TOF</p></body></html>"))
        self.textBrowser_12.setHtml(_translate("NeutronPy", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Energy</p></body></html>"))
        self.groupBox_6.setTitle(_translate("NeutronPy", "Quick Fit"))
        self.textBrowser_17.setHtml(_translate("NeutronPy", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Units of Index</p></body></html>"))
        self.comboBox_9.setItemText(0, _translate("NeutronPy", "Unit"))
        self.textBrowser_18.setHtml(_translate("NeutronPy", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">TOF</p></body></html>"))
        self.textBrowser_19.setHtml(_translate("NeutronPy", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Energy</p></body></html>"))
        self.groupBox_3.setTitle(_translate("NeutronPy", "Beam Line Characteristics"))
        self.comboBox_8.setItemText(0, _translate("NeutronPy", "cm"))
        self.comboBox_8.setItemText(1, _translate("NeutronPy", "mm"))
        self.comboBox_8.setItemText(2, _translate("NeutronPy", "um"))
        self.comboBox_8.setItemText(3, _translate("NeutronPy", "nm"))
        self.textBrowser_16.setHtml(_translate("NeutronPy", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Thickness of A</p></body></html>"))
        self.groupBox_5.setTitle(_translate("NeutronPy", "Material Characteristics"))
        self.textBrowser.setHtml(_translate("NeutronPy", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Material A</p></body></html>"))
        self.textBrowser_2.setHtml(_translate("NeutronPy", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Material B</p></body></html>"))
        self.textBrowser_3.setHtml(_translate("NeutronPy", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Thickness of B</p></body></html>"))
        self.textBrowser_4.setHtml(_translate("NeutronPy", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Thickness of A</p></body></html>"))
        self.comboBox.setItemText(0, _translate("NeutronPy", "Carbon Fiber"))
        self.comboBox.setItemText(1, _translate("NeutronPy", "Paper"))
        self.comboBox.setItemText(2, _translate("NeutronPy", "Plastic"))
        self.comboBox_2.setItemText(0, _translate("NeutronPy", "Diamond"))
        self.comboBox_2.setItemText(1, _translate("NeutronPy", "Stainless Steel"))
        self.comboBox_2.setItemText(2, _translate("NeutronPy", "Paper"))
        self.comboBox_2.setItemText(3, _translate("NeutronPy", "Plastic"))
        self.comboBox_3.setItemText(0, _translate("NeutronPy", "cm"))
        self.comboBox_3.setItemText(1, _translate("NeutronPy", "mm"))
        self.comboBox_3.setItemText(2, _translate("NeutronPy", "um"))
        self.comboBox_3.setItemText(3, _translate("NeutronPy", "nm"))
        self.comboBox_4.setItemText(0, _translate("NeutronPy", "cm"))
        self.comboBox_4.setItemText(1, _translate("NeutronPy", "mm"))
        self.comboBox_4.setItemText(2, _translate("NeutronPy", "um"))
        self.comboBox_4.setItemText(3, _translate("NeutronPy", "nm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NeutronPy = QtWidgets.QMainWindow()
    ui = Ui_NeutronPy()
    ui.setupUi(NeutronPy)
    NeutronPy.show()
    sys.exit(app.exec_())
