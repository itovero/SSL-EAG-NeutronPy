import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from os import listdir, path

class Materials(QtWidgets.QWidget):
    def __init__(self):
        super(Materials, self).__init__()
        self.initUI()

    def initUI(self):
        #Create the table layout
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 767, 180))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 6, item)

        self.retranslateUi(QtWidgets.QWidget())

        self.show()

    def retranslateUi(self, integrated):
        _translate = QtCore.QCoreApplication.translate

        #populate the header labels with text
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("integrated", "Material 1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("integrated", "Material 2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("integrated", "Material 3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("integrated", "Material 4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("integrated", "Material 5"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("integrated", "Element Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("integrated", "Abundance"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("integrated", "Atomic Mass"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("integrated", "Atomic Fraction"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("integrated", "Density"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("integrated", "Thickness"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("integrated", "Component"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        #populate the entry boxes with blank values
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("integrated", " "))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("integrated", " "))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("integrated", " "))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("integrated", " "))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("integrated", " "))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("integrated", " "))
        item = self.tableWidget.item(0, 6)
        item.setText(_translate("integrated", " "))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("integrated", " "))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("integrated", " "))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("integrated", " "))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("integrated", " "))
        item = self.tableWidget.item(1, 4)
        item.setText(_translate("integrated", " "))
        item = self.tableWidget.item(1, 5)
        item.setText(_translate("integrated", " "))
        item = self.tableWidget.item(1, 6)
        item.setText(_translate("integrated", " "))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("integrated", " "))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("integrated", " "))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("integrated", " "))
        item = self.tableWidget.item(2, 3)
        item.setText(_translate("integrated", " "))
        item = self.tableWidget.item(2, 4)
        item.setText(_translate("integrated", " "))
        item = self.tableWidget.item(2, 5)
        item.setText(_translate("integrated", " "))
        item = self.tableWidget.item(2, 6)
        item.setText(_translate("integrated", " "))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("integrated", " "))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("integrated", " "))
        item = self.tableWidget.item(3, 2)
        item.setText(_translate("integrated", " "))
        item = self.tableWidget.item(3, 3)
        item.setText(_translate("integrated", " "))
        item = self.tableWidget.item(3, 4)
        item.setText(_translate("integrated", " "))
        item = self.tableWidget.item(3, 5)
        item.setText(_translate("integrated", " "))
        item = self.tableWidget.item(3, 6)
        item.setText(_translate("integrated", " "))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("integrated", " "))
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("integrated", " "))
        item = self.tableWidget.item(4, 2)
        item.setText(_translate("integrated", " "))
        item = self.tableWidget.item(4, 3)
        item.setText(_translate("integrated", " "))
        item = self.tableWidget.item(4, 4)
        item.setText(_translate("integrated", " "))
        item = self.tableWidget.item(4, 5)
        item.setText(_translate("integrated", " "))
        item = self.tableWidget.item(4, 6)
        item.setText(_translate("integrated", " "))
        self.tableWidget.setSortingEnabled(__sortingEnabled)


    #returns a 2D pandas frame containing al of the table's values
    def saveInput(self):
        rows = self.tableWidget.rowCount()
        columns = self.tableWidget.columnCount()
        new_frame = pd.DataFrame(index=range(rows + 1))
        for i in range(rows):
            for j in range(columns):
                text = self.tableWidget.item(i,j).text()
                try:
                    value = float(text)
                except:
                    if j == 0 :
                        value = text
                    else:
                        value = 'NaN'
                new_frame.loc[i, j] = value
        print(new_frame)
        return new_frame

    def update_table(self, pandasFrame):
        _translate = QtCore.QCoreApplication.translate
        rows = self.tableWidget.rowCount()
        columns = self.tableWidget.columnCount()
        for i in range(rows):
            for j in range(columns):
                item = self.tableWidget.item(i, j)
                if str(pandasFrame.iloc[i, j]) != 'nan':
                    item.setText(_translate("integrated", str(pandasFrame.iloc[i, j])))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(__sortingEnabled)

    def save_file(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self,"Save Parameters","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            file = open(fileName, 'w')
            rows = self.tableWidget.rowCount()
            columns = self.tableWidget.columnCount()
            strList = []
            for i in range(rows):
                for j in range(columns):
                    strList.append(self.tableWidget.item(i,j).text())
            file.write('/'.join(strList))
            file.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Materials()
    
    sys.exit(app.exec_())
