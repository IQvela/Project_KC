# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_ViewInfoSeason.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import time
from PyQt5 import QtCore, QtGui, QtWidgets

#import Project/season data

class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self,project_selected,ind_season_selected):
        super(Ui_MainWindow,self).__init__()
        #info need
        self.project_selected=project_selected
        #self.ind_season_selected=ind_season_selected  
        print(self.project_selected)
        self.season_selected=self.project_selected.seasons[ind_season_selected]


        self.finish_window=False

    def closeEvent(self, event):
        self.finish_window=True
        self.close()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(576, 541)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.Title_ViewInfoSeason = QtWidgets.QLabel(self.centralwidget)
        self.Title_ViewInfoSeason.setGeometry(QtCore.QRect(30, 40, 521, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)

        #Labels---------------------------------------------------------
        self.Title_ViewInfoSeason.setFont(font)
        self.Title_ViewInfoSeason.setAlignment(QtCore.Qt.AlignCenter)
        
        self.label_DateStartFrom = QtWidgets.QLabel(self.centralwidget)
        self.label_DateStartFrom.setGeometry(QtCore.QRect(40, 120, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_DateStartFrom.setFont(font)
        
        self.label_DateEndTo = QtWidgets.QLabel(self.centralwidget)
        self.label_DateEndTo.setGeometry(QtCore.QRect(320, 120, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_DateEndTo.setFont(font)

        self.label_description = QtWidgets.QLabel(self.centralwidget)
        self.label_description.setGeometry(QtCore.QRect(40, 180, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_description.setFont(font)
        

        #Text Boxes------------------------------------------------------------
        self.text_DateStart = QtWidgets.QTextEdit(self.centralwidget)
        self.text_DateStart.setGeometry(QtCore.QRect(120, 110, 150, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_DateStart.setFont(font)
        
        self.text_DateEnd = QtWidgets.QTextEdit(self.centralwidget)
        self.text_DateEnd.setGeometry(QtCore.QRect(400, 110, 150, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_DateEnd.setFont(font)

        self.label_ExperimentList = QtWidgets.QLabel(self.centralwidget)
        self.label_ExperimentList.setGeometry(QtCore.QRect(40, 290, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_ExperimentList.setFont(font)
                
        self.text_description = QtWidgets.QTextEdit(self.centralwidget)
        self.text_description.setGeometry(QtCore.QRect(40, 200, 501, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_description.setFont(font)
       

        #List---------------------------------------------------------------------
        self.list_experiments = QtWidgets.QListWidget(self.centralwidget)
        self.list_experiments.setGeometry(QtCore.QRect(40, 320, 501, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.list_experiments.setFont(font)
        self.list_experiments.setObjectName("list_experiments")
        item = QtWidgets.QListWidgetItem()
        self.list_experiments.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_experiments.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_experiments.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_experiments.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_experiments.addItem(item)

        

        #Button ------------------------------------------------------
        self.Button_OK = QtWidgets.QPushButton(self.centralwidget)
        self.Button_OK.setGeometry(QtCore.QRect(440, 450, 100, 40))
        self.Button_OK.clicked.connect(self.ok)

        self.Button_Cancel = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Cancel.setGeometry(QtCore.QRect(300, 450, 100, 40))
        self.Button_Cancel.clicked.connect(self.ok)

        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 576, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Information Season"+" "+self.season_selected.season_name))

        #labels-------------------------------------------------------------------
        self.Title_ViewInfoSeason.setText(self.season_selected.season_name)
        self.label_DateStartFrom.setText(_translate("MainWindow", "From"))
        self.label_DateEndTo.setText(_translate("MainWindow", "To"))
        self.label_ExperimentList.setText(_translate("MainWindow", "Experiments list"))
        self.label_description.setText(_translate("MainWindow", "Description"))

        #tex boxes---------------------------------------------------------------------
        self.text_DateStart.setText(self.season_selected.date_ini)
        self.text_DateEnd.setText(self.season_selected.date_end)
        self.text_description.setText(self.season_selected.season_name)
        #list-------------------------------------------------------------
        __sortingEnabled = self.list_experiments.isSortingEnabled()
        self.list_experiments.setSortingEnabled(False)
        for e_i,e in enumerate(self.season_selected.experiments):
            item = self.list_experiments.item(e_i)
            item.setText(_translate("MainWindow", e.exp_name))
        #item = self.list_experiments.item(1)
        #item.setText(_translate("MainWindow", "Exp B: Low temperature"))
        #item = self.list_experiments.item(2)
        #item.setText(_translate("MainWindow", "Exp C: Circulation"))
        #item = self.list_experiments.item(3)
        #item.setText(_translate("MainWindow", "Exp D: asadfad"))
        #item = self.list_experiments.item(4)
        #item.setText(_translate("MainWindow", "Exp X: test"))
        self.list_experiments.setSortingEnabled(__sortingEnabled)
        
        #buttons-------------------------------------------------------------------
        self.Button_OK.setText(_translate("MainWindow", "OK"))
        self.Button_Cancel.setText(_translate("MainWindow", "Cancel"))

#closes the window
    def back_button(self):
        self.finish_window=True
        self.close()
    
    def ok(self):
        self.finish_window=True
        self.close()

#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec_())
