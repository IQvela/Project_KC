# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 12:38:09 2021

@author: refor
"""
# import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self,time_db,db_names):
        # self.MainWindow=QtWidgets.QMainWindow()
        super(Ui_MainWindow,self).__init__()

        self.time_db=time_db
        self.db_names=db_names
        self.finish_window=False
    
    def closeEvent(self, event):
        self.finish_window=True
        self.close()

    def setupUi(self):
        self.setObjectName("MainWindows")
        self.resize(700, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        
        self.table_timedb=QtWidgets.QTableWidget(self.centralwidget)
        self.table_timedb.setGeometry(QtCore.QRect(10,10,680,530))
        self.table_timedb.setColumnCount(len(self.time_db.columns))
        self.table_timedb.setRowCount(len(self.time_db))
        self.table_timedb.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.Button_ok = QtWidgets.QPushButton(self.centralwidget)
        self.Button_ok.setGeometry(QtCore.QRect(570, 550, 70, 40))
        self.Button_ok.clicked.connect(self.cancel_button)
        
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        d_ini,d_end="No Data","No Data"
        if len(self.time_db)>0:
            d_ini=self.time_db.iloc[0,0]
            d_end=self.time_db.iloc[-1,0]
        self.setWindowTitle(_translate("MainWindows", "View Data: {} - {}".format(d_ini,d_end)))
        
        self.Button_ok.setText("OK")
        self.populate_table_timedb()
        
    def populate_table_timedb(self):

        brush_green=QtGui.QBrush(QtGui.QColor(170,255,0,255))
        brush_green.setStyle(QtCore.Qt.SolidPattern)
        brush_red=QtGui.QBrush(QtGui.QColor(255,0,0,255))
        brush_red.setStyle(QtCore.Qt.SolidPattern) 
        
        c_names=list(self.time_db.columns)
        # print(c_names)
        for c_i,c in enumerate(c_names):
            item=QtWidgets.QTableWidgetItem()
            self.table_timedb.setHorizontalHeaderItem(c_i,item)
            item = self.table_timedb.horizontalHeaderItem(c_i)
            item.setText(c)            
            for r_i in range(self.table_timedb.rowCount()):
                item=QtWidgets.QTableWidgetItem()
                self.table_timedb.setVerticalHeaderItem(r_i,item)                
                item=QtWidgets.QTableWidgetItem()
                self.table_timedb.setItem(r_i, c_i, item)
                item=self.table_timedb.item(r_i, c_i)
                item.setText(str(self.time_db.iloc[r_i,c_i]))
                if c in self.db_names:
                    if item.text()=="0":
                        item.setBackground(brush_red)
                    else:
                        item.setBackground(brush_green)
        
        self.table_timedb.setColumnWidth(0,150)
        
       
        
        # print("Done!")            
                
        
    def cancel_button(self):
        self.finish_window=True
        self.close()


# df3 = pd.DataFrame(
#     {
#         "A": ["A0", "A1", "A2", "A3","A10"],
#         "B": ["B0", "0", "B2", "B3","0"],
#         "C": ["C0", "C1", "0", "C3","C10"],
#         "D": ["D0", "D1", "D2", "D3","D10"],
#     },
#     # index=[0, 1, 2, 3],
# )

# ui=Ui_MainWindow(df3,["B","C","D"])
# ui.setupUi()
# ui.show()        
        
        
        