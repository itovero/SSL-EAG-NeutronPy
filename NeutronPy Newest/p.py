import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressBar, QWidget, QDialog
from PyQt5.QtCore import Qt

class Example(QWidget):
    
    def __init__(self):
        super().__init__()

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
        self.pbar.setValue(0)
        
        self.setWindowTitle("Loading Files ...")
        self.setGeometry(32,32,320,100)
        #self.setModal(True)
        self.setWindowModality(Qt.ApplicationModal)
        self.show()

        self.timer = QTimer()
        self.timer.timeout.connect(self.handleTimer)
        self.timer.start(100)

    def handleTimer(self):
        value = self.pbar.value()
        if value < 100:
            value = value + 1
            self.pbar.setValue(value)
        else:
            self.timer.stop()
            self.pbar.setFormat('Loading Complete')
            #self.hide()
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())