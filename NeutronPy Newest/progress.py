import sys
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar
from PyQt5.QtCore import QTimer

class Progress(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Loading Data ...')
        self.resize(500, 100)

        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(25, 25, 300, 40)
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)

    def setValue(self, n):
        self.progressBar.setValue(n)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    loading = Progress()
    loading.show()
    #sys.exit(app.exec_())       