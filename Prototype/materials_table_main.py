# This Python file uses the following encoding: utf-8
import sys
import os
import pandas as pd

from PyQt5 import QtWidgets
from MaterialsTable4 import Ui_materials_table

class materials_table(QtWidgets.QMainWindow):
    def __init__(self):
        super(materials_table, self).__init__()
        self.ui = Ui_materials_table()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.get_vars)
        self.ui.pushButton.clicked.connect(self.get_data)

        #self.ui.tableWidget.cellChanged.connect(self.get_vars)
        #self.ui.tableWidget.cellChanged.connect(self.get_data)

    def get_vars(self):
        # Yuki - Since we have multiple materials, I put the input values into lists
        # so they can be indexed if we need to plot multiple
        # in your code, just use them as "elementNames[1]"

        #assigns all inputs to lists to be passed on
        #couldn't find how to index the entire row with tableWidget.item (':' doesn't work) so this'll have to do for now...
        #
        #elementNames are in 0th row
        elementNames = [self.ui.tableWidget.item(0,0).text(),self.ui.tableWidget.item(1,0).text(),
        self.ui.tableWidget.item(2,0).text(), self.ui.tableWidget.item(3,0).text()]
        #
        #isotopicAbundances are in 1st row
        isotopicAbundances = [self.ui.tableWidget.item(0,1).text(),self.ui.tableWidget.item(1,1).text(),
        self.ui.tableWidget.item(2,1).text(), self.ui.tableWidget.item(3,1).text()]
        #
        #atomicFractions are in 2nd row
        atomicFraction = [self.ui.tableWidget.item(0,2).text(),self.ui.tableWidget.item(1,2).text(),
        self.ui.tableWidget.item(2,2).text(), self.ui.tableWidget.item(3,2).text()]
        #
        #densities are in 3nd row
        densities = [self.ui.tableWidget.item(0,3).text(),self.ui.tableWidget.item(1,3).text(),
        self.ui.tableWidget.item(2,3).text(), self.ui.tableWidget.item(3,3).text()]
        #
        #thicknesses are in 4th row
        thicknesses = [self.ui.tableWidget.item(0,4).text(),self.ui.tableWidget.item(1,4).text(),
        self.ui.tableWidget.item(2,4).text(), self.ui.tableWidget.item(3,4).text()]
        #
        #components are in 5th row
        components = [self.ui.tableWidget.item(0,5).text(),self.ui.tableWidget.item(1,5).text(),
        self.ui.tableWidget.item(2,5).text(), self.ui.tableWidget.item(3,5).text()]

    def get_data(self):
        data_1 = data_2 = data_3 = data_4 = data_5 = 0
        #the following should just go in a loop or I should fix the code below this

        fname1 = self.ui.tableWidget.item(0,0).text() + ".txt"
        data_1 = self.file_reader(fname1)

        fname2 = self.ui.tableWidget.item(1,0).text() + ".txt"
        data_2 = self.file_reader(fname2)

        fname3 = self.ui.tableWidget.item(2,0).text() + ".txt"
        data_3 = self.file_reader(fname1)

        fname4 = self.ui.tableWidget.item(3,0).text() + ".txt"
        data_4 = self.file_reader(fname1)

        fname5 = self.ui.tableWidget.item(4,0).text() + ".txt"
        data_5 = self.file_reader(fname1)

        #try data_2 = file_reader(self,fname)
        #try data_3 = file_reader(self,fname)
        #try data_4 = file_reader(self,fname)
        #try data_5 = file_reader(self,fname)

        #for cells 1:5
         #   if cell value = "0000"
          #      data_variable = 0
           # else
            #    fname = #cell value + .txt
             #   data variable = ()
              #  #find the data
               # #put it into a variable

    def file_reader(self,fname):
        #cleans file from random junk
        #returns clean array
        width = [14, 14]
        names = ["x","y"]
        #types = [str, str]

        def splitdatarow(row, width):
            output = []
            ptr = 0
            for w in width:
                output.append(row[ptr:ptr+w].strip())
                ptr += w
            return output

        with open(fname, "r") as f:
            data = f.read().splitlines()
        output = []

        for row in data:
            linedata = splitdatarow(row, width)
            output.append(linedata)
        df = pd.DataFrame(output, columns=names)

        #for c, t in zip(names, types):
            #df[c] = df[c].astype(t)

        #need to skip first 11 rows since those do not have data
        #need to remove last 2 rows since those do not have data
        row_number = len(df.index)
        #row_number - 3 since I need to remove last two rows
        #since Python indexes start at zero, I have to do -3 (instead of -2)
        df = df.loc[11:row_number-3,:]
        return df

    def set_isotopicAbundances(self):
        #sets default isotopicAbundances by reading from
        print("in progress")

    def set_atomicFractions(self):
        #sets default atomicFractions by reading from text file
        print("in progress")

    def set_densities(self):
        #sets default densities by reading from text file
        print("in progress")

    def set_thicknesses(self):
        #sets default thicknesses
        print("in progress")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = materials_table()
    application.show()
    sys.exit(app.exec_())
