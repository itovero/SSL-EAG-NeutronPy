import sys
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import *

#Class for generating for any errors
class Error(QWidget):
    def __init__(self, error):
        super().__init__()

        self.setWindowTitle('Error!')
        vbox = QVBoxLayout()
        self.label = QLabel(error)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Times", 11, QtGui.QFont.Bold))
        vbox.addWidget(self.label)
        self.setLayout(vbox)
        self.resize(500, 100)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    error = Error("hi")
    error.show()
    sys.exit(app.exec_())       