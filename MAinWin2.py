# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KCdata_MainWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import time


from PyQt5 import QtCore, QtGui, QtWidgets
import Classes_Backend as KCbckend

import GUIs.GUI_NewProject as gui_newproject
import GUIs.GUI_OpenProject as gui_openproject


Pr={} #dictionary containing all the projects (this must to be initialized from a previous file where all the projects were saved)

class Ui_MainWindow(object):
    Table_Project_headers=["Project name","Timeframe","Description","Responsible"]
    def __init__(self):
        self.MainWindow=QtWidgets.QMainWindow()
        self.finish_window=False
    
    def setupUi(self):
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(627, 389)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 197, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 226, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 98, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 131, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 197, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 226, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 197, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 226, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 98, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 131, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 197, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 226, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 98, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 197, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 226, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 98, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 131, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 98, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 98, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 197, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 197, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(157, 197, 234))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.MainWindow.setPalette(palette)
        #window general widget
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(250, 10, 271, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        #define label: title of the window
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        #define button: Open project
        self.Button_OpenProject = QtWidgets.QPushButton(self.centralwidget)
        self.Button_OpenProject.setGeometry(QtCore.QRect(490, 290, 100, 40))
        self.Button_OpenProject.setObjectName("Button_OpenProject")
        self.Button_OpenProject.clicked.connect(self.open_project)
        #define button: add project
        self.Button_NewProject = QtWidgets.QPushButton(self.centralwidget)
        self.Button_NewProject.setGeometry(QtCore.QRect(360, 290, 100, 40))
        self.Button_NewProject.setShortcut("")
        self.Button_NewProject.setCheckable(False)
        self.Button_NewProject.clicked.connect(self.new_project)
        
        #define button: check data
        self.Button_CheckData = QtWidgets.QPushButton(self.centralwidget)
        self.Button_CheckData.setGeometry(QtCore.QRect(230, 290, 100, 40))
        self.Button_CheckData.setObjectName("Button_CheckData")
        #define table: project list
        self.Table_Project_list = QtWidgets.QTableWidget(self.centralwidget)
        self.Table_Project_list.setGeometry(QtCore.QRect(20, 60, 571, 201))
        self.Table_Project_list.setObjectName("Table_Project_list")
        col= self.Table_Project_list.setColumnCount(len(Ui_MainWindow.Table_Project_headers)) #number of columns
        raw = self.Table_Project_list.setRowCount(5) #number of rows --- need to change by list length
        #vertical header
        item = QtWidgets.QTableWidgetItem()
        self.Table_Project_list.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Project_list.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Project_list.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Project_list.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Project_list.setVerticalHeaderItem(4, item)
        #horizontal header
        item = QtWidgets.QTableWidgetItem()
        self.Table_Project_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Project_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Project_list.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Table_Project_list.setHorizontalHeaderItem(3, item)
        #items inside table --- more need to be defined to add thing inside table
        i=0
        j=0
        for i in [0,1,2,3,4]:
            for j in [0,1,2,3]:
                item = QtWidgets.QTableWidgetItem()
                self.Table_Project_list.setItem(i, j, item)
        #item = QtWidgets.QTableWidgetItem()
        #self.Table_Project_list.setItem(0, 1, item)
        #item = QtWidgets.QTableWidgetItem()
        #self.Table_Project_list.setItem(1, 0, item)
        #other table defs
        self.Table_Project_list.horizontalHeader().setMinimumSectionSize(36)
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 627, 21))
        self.menubar.setObjectName("menubar")
        self.MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)


    #this function defines all the names that appear in window
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "Projects KC"))
        #names of tile and buttons open project, add project and check data
        self.Title.setText(_translate("MainWindow", "KC - data"))
        self.Button_OpenProject.setText(_translate("MainWindow", "OPEN PROJECT"))
        self.Button_NewProject.setText(_translate("MainWindow", "ADD PROJECT"))
        self.Button_CheckData.setText(_translate("MainWindow", "CHECK DATA"))
        #table info definition
        #vertical header names
        item = self.Table_Project_list.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.Table_Project_list.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.Table_Project_list.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.Table_Project_list.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.Table_Project_list.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        #horizontal header names
        item = self.Table_Project_list.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Project name"))
        item = self.Table_Project_list.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Timeframe"))
        item = self.Table_Project_list.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Description"))
        item = self.Table_Project_list.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "??"))
        #things inside table --- need to be changed with function calling class/list, more items need to be added here and above
        __sortingEnabled = self.Table_Project_list.isSortingEnabled()
        self.Table_Project_list.setSortingEnabled(False)
        i=0
        j=0
        for i in [0,1,2,3,4]:
            for j in [0,1,2,3]:
                item = self.Table_Project_list.item(i, j)
                item.setText(_translate("MainWindow", "a"))
        
        #item = self.Table_Project_list.item(0, 0)
        #item.setText(_translate("MainWindow", "a"))
        #item = self.Table_Project_list.item(0, 1)
        #item.setText(_translate("MainWindow", "21 namez"))
        #item = self.Table_Project_list.item(1, 0)
        #item.setText(_translate("MainWindow", "12 namey"))
        self.Table_Project_list.setSortingEnabled(__sortingEnabled)

    
    def new_project(self):
        ui_newproject=gui_newproject.Ui_MainWindow()
        ui_newproject.setupUi()
        ui_newproject.MainWindow.show()
        
        while ui_newproject.finish_window==False:
            QtCore.QCoreApplication.processEvents()
            time.sleep(0.01)        
        
        project_attributes=ui_newproject.project_attributes
        
        Pr[len(Pr.keys())]=KCbckend.Project(project_attributes)        
        
    def open_project(self):
        ui_openproject=gui_openproject.Ui_MainWindow()
        ui_openproject.setupUi()
        ui_openproject.MainWindow.show()
        
        while ui_openproject.finish_window==False:
            QtCore.QCoreApplication.processEvents()
            time.sleep(0.01)    
            
        
    def cancel_window(self):
        self.finish_window=True
        self.MainWindow.close()
        
        
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

ui_Mother=Ui_MainWindow()
ui_Mother.setupUi()
ui_Mother.MainWindow.show()