# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_OpenPoint.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


# import random
import random
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import Classes_Backend as KCbckend
import GUIs.GUI_MessageBoxKC as msgbox
# from . import GUI_MessageBoxKC as msgbox
import GUIs.GUI_LinkDataPoint as gui_linkdatapoint

class Ui_MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self,Pr_list,exp_route):
        # self.MainWindow=QtWidgets.QMainWindow()
        super(Ui_MainWindow,self).__init__()

        self.Pr_list=Pr_list
        self.ind_pr_selected=exp_route[0] #index of the selected project
        self.ind_season_selected=exp_route[1] #index of the selected season       
        self.ind_exp_selected=exp_route[2] #index of the selected experiment
        self.exp_selected=self.Pr_list[self.ind_pr_selected].seasons[self.ind_season_selected].experiments[self.ind_exp_selected]
        self.point_selected="ND"#self.Pr_list[self.ind_pr_selected].seasons[self.ind_season_selected].experiments[self.ind_exp_selected].points[self.ind_point_selected]
        
        self.table_col_headers=["Index","Type","StartDate","EndDate","Delay","Nentries"]
        self.finish_window=False
    
    def closeEvent(self, event):
        self.finish_window=True
        self.close()

    def setupUi(self):
        self.setObjectName("MainWindows")
        self.resize(1050, 620)

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
        self.setPalette(palette)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        #Point information (labels, text and button)---------------------------------------------------------------------------------
        self.Title_PointName = QtWidgets.QLabel(self.centralwidget)
        self.Title_PointName.setGeometry(QtCore.QRect(20, 20, 1061, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.Title_PointName.setFont(font)
        self.Title_PointName.setAlignment(QtCore.Qt.AlignCenter)

        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(50, 100, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_name.setFont(font)

        self.label_comments = QtWidgets.QLabel(self.centralwidget)
        self.label_comments.setGeometry(QtCore.QRect(50, 140, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_comments.setFont(font)


        
        #Table Data Avaible/already existing---------------------------------------------------------------------------------
        self.table_DataLinked = QtWidgets.QTableWidget(self.centralwidget)
        self.table_DataLinked.setGeometry(QtCore.QRect(50, 260, 531, 221))
        self.table_DataLinked.setColumnCount(len(self.table_col_headers))


        #Label Data available
        self.label_DataLinked = QtWidgets.QLabel(self.centralwidget)
        self.label_DataLinked.setGeometry(QtCore.QRect(50, 230, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.label_DataLinked.setFont(font)


        #Text
        self.text_name = QtWidgets.QTextEdit(self.centralwidget)
        self.text_name.setGeometry(QtCore.QRect(160, 90, 721, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_name.setFont(font)

        self.text_comments = QtWidgets.QTextEdit(self.centralwidget)
        self.text_comments.setGeometry(QtCore.QRect(160, 130, 721, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_comments.setFont(font)
        
        #Buttons under data available---------------------------------------------------------------------------------
        
        #Button Modify info point
        self.Button_CreatePoint = QtWidgets.QPushButton(self.centralwidget)
        self.Button_CreatePoint.setGeometry(QtCore.QRect(910, 80, 100, 30))
        self.setCentralWidget(self.centralwidget)
        self.Button_CreatePoint.clicked.connect(self.create_point)

        self.Button_ModifyInfoPoint = QtWidgets.QPushButton(self.centralwidget)
        self.Button_ModifyInfoPoint.setGeometry(QtCore.QRect(910, 130, 100, 30))
        self.setCentralWidget(self.centralwidget)
        self.Button_ModifyInfoPoint.clicked.connect(self.modify_attrib)

        self.Button_AnalyseData = QtWidgets.QPushButton(self.centralwidget)
        self.Button_AnalyseData.setGeometry(QtCore.QRect(190, 500, 100, 40))
        
        # self.Button_ModifyData = QtWidgets.QPushButton(self.centralwidget)
        # self.Button_ModifyData.setGeometry(QtCore.QRect(190, 505, 100, 40))
        
        self.Button_DeleteData = QtWidgets.QPushButton(self.centralwidget)
        self.Button_DeleteData.setGeometry(QtCore.QRect(340, 500, 100, 40))
        self.Button_DeleteData.clicked.connect(self.delete_data)
        
        self.Button_ViewData = QtWidgets.QPushButton(self.centralwidget)
        self.Button_ViewData.setGeometry(QtCore.QRect(50, 500, 100, 40))
        
        #Button Add new data (after selecting data TYPE)
        self.Button_LinkData = QtWidgets.QPushButton(self.centralwidget)
        self.Button_LinkData.setGeometry(QtCore.QRect(920, 420, 100, 40))
        self.Button_LinkData.clicked.connect(self.link_data)



        self.label_status = QtWidgets.QLabel(self.centralwidget)
        self.label_status.setGeometry(QtCore.QRect(50, 195, 300, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_status.setFont(font)
        
        # Selecting a data type and adding the data to the point-----------------------------------       

        #List of types of data
        self.label_SelectType = QtWidgets.QLabel(self.centralwidget)
        self.label_SelectType.setGeometry(QtCore.QRect(670, 360, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_SelectType.setFont(font)
        
        self.list_types = QtWidgets.QListWidget(self.centralwidget)
        self.list_types.setGeometry(QtCore.QRect(670, 380, 221, 101))
        self.list_types.setObjectName("list_types")
        for i in range(len(self.exp_selected.get_dbnames())+1):
            item = QtWidgets.QListWidgetItem()
            self.list_types.addItem(item)

        
        #line for visual separation
        self.line_separate = QtWidgets.QFrame(self.centralwidget)
        self.line_separate.setGeometry(QtCore.QRect(610, 210, 20, 331))
        self.line_separate.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_separate.setFrameShadow(QtWidgets.QFrame.Sunken)
        
        self.label_linkdatapoint = QtWidgets.QLabel(self.centralwidget)
        self.label_linkdatapoint.setGeometry(QtCore.QRect(670, 330, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.label_linkdatapoint.setFont(font)
        
        
        #Buttons Cancel and OK---------------------------------------------------------------------------------
        self.Button_Ok = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Ok.setGeometry(QtCore.QRect(920, 560, 100, 40))
        self.Button_Ok.clicked.connect(self.cancel_button)
        
        # self.Button_Cancel = QtWidgets.QPushButton(self.centralwidget)
        # self.Button_Cancel.setGeometry(QtCore.QRect(830, 560, 100, 40))
        # self.Button_Cancel.setObjectName("Button_Cancel")


        #DAte elements------------------------------------------------------------------------------------------

        self.label_DateStart = QtWidgets.QLabel(self.centralwidget) 
        self.label_DateStart.setGeometry(QtCore.QRect(670, 220, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_DateStart.setFont(font)
        self.label_DateStart.setObjectName("label_DateStart")
        
        self.label_DateEnd = QtWidgets.QLabel(self.centralwidget)
        self.label_DateEnd.setGeometry(QtCore.QRect(670, 260, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_DateEnd.setFont(font)
        self.label_DateEnd.setObjectName("label_DateEnd")

        self.label_date = QtWidgets.QLabel(self.centralwidget)
        self.label_date.setGeometry(QtCore.QRect(770, 190, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_date.setFont(font)
        self.label_date.setObjectName("label_date")
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(920, 190, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_time.setFont(font)
        self.label_time.setObjectName("label_time")

        self.text_DateStart = QtWidgets.QTextEdit(self.centralwidget)
        self.text_DateStart.setGeometry(QtCore.QRect(770, 210, 120, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.text_DateStart.setFont(font)
        self.text_DateStart.setObjectName("text_DateStart")
        self.text_DateEnd = QtWidgets.QTextEdit(self.centralwidget)
        self.text_DateEnd.setGeometry(QtCore.QRect(770, 260, 120, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.text_DateEnd.setFont(font)
        self.text_DateEnd.setObjectName("text_DateEnd")
        
        self.text_TimeStart = QtWidgets.QTextEdit(self.centralwidget)
        self.text_TimeStart.setGeometry(QtCore.QRect(930, 210, 80, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.text_TimeStart.setFont(font)
        self.text_TimeStart.setObjectName("text_TimeStart")
        
        self.text_TimeEnd = QtWidgets.QTextEdit(self.centralwidget)
        self.text_TimeEnd.setGeometry(QtCore.QRect(930, 260, 80, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.text_TimeEnd.setFont(font)
        self.text_TimeEnd.setObjectName("text_TimeEnd")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindows", "MainWindow"))
        
        self.Title_PointName.setText(_translate("MainWindows", "Season 1/ Experiment 1/Point 1"))
        self.label_date.setText(_translate("MainWindow", "Date (YYYY-MM-DD)"))
        self.label_DateStart.setText(_translate("MainWindow", "Date start"))
        self.label_DateEnd.setText(_translate("MainWindow", "Date end"))
        self.label_time.setText(_translate("MainWindow", "Time (HH:MM:SS)"))

        self.label_linkdatapoint.setText(_translate("MainWindows", "Link data to point"))
        self.label_name.setText(_translate("MainWindows", "Name"))
        self.label_DataLinked.setText(_translate("MainWindows", "Data Linked"))
        
        self.label_status.setText("Status: Creating Point...")


        self.Button_AnalyseData.setText(_translate("MainWindows", "ANALYZE DATA"))
        # self.Button_ModifyData.setText(_translate("MainWindows", "MODIFY DATA"))
        # self.Button_DeleteData.setText(_translate("MainWindows", "CREATE POINT"))
        self.Button_ViewData.setText(_translate("MainWindows", "VIEW DATA"))
        self.label_comments.setText(_translate("MainWindows", "Comments"))
        self.label_SelectType.setText(_translate("MainWindows", "Select type "))
        self.Button_ModifyInfoPoint.setText(_translate("ProjectWin", "MODIFY POINT"))
        self.Button_CreatePoint.setText(_translate("ProjectWin", "CREATE POINT"))

        #buttons existing data--------------------------------------------------------
        self.Button_AnalyseData.setText(_translate("ProjectWin", "ANALYZE DATA"))
        # self.Button_ModifyData.setText(_translate("ProjectWin", "MODIFY DATA"))
        self.Button_DeleteData.setText(_translate("ProjectWin", "DELETE DATA"))
        self.Button_ViewData.setText(_translate("ProjectWin", "VIEW DATA"))

        self.Button_Ok.setText(_translate("MainWindows", "OK"))
        # self.Button_Cancel.setText(_translate("MainWindows", "CANCEL"))

        self.Button_LinkData.setText(_translate("MainWindows", "LINK DATA"))        
        
        
        
        #table existing/available data-------------------------------------------
        self.table_DataLinked.setColumnWidth(0, 50)
        self.table_DataLinked.setColumnWidth(1, 70)
        self.table_DataLinked.setColumnWidth(2, 120)
        self.table_DataLinked.setColumnWidth(3, 120)
        self.table_DataLinked.setColumnWidth(4, 70)
        self.table_DataLinked.setColumnWidth(5, 50)
        
        # self.populate_linkeddatatable()
        for c_i,c in enumerate(self.table_col_headers):
            item=QtWidgets.QTableWidgetItem()
            self.table_DataLinked.setHorizontalHeaderItem(c_i,item)
            item = self.table_DataLinked.horizontalHeaderItem(c_i)
            item.setText(c)
        
        __sortingEnabled = self.table_DataLinked.isSortingEnabled()
        self.table_DataLinked.setSortingEnabled(False)
        self.table_DataLinked.setSortingEnabled(__sortingEnabled)
        
        

        __sortingEnabled = self.list_types.isSortingEnabled()
        self.list_types.setSortingEnabled(False)
        
        list_items=["AUTOMATIC"]+self.exp_selected.get_dbnames()
        
        for lst_i,lst in enumerate(list_items):
            item = self.list_types.item(lst_i)
            item.setText(_translate("MainWindows", lst))

        self.list_types.setSortingEnabled(__sortingEnabled)


        
        self.text_boxes=[self.text_name,self.text_comments,self.text_DateStart,self.text_TimeStart,self.text_DateEnd,self.text_TimeEnd]
        
        self.modifypoint_items=[self.table_DataLinked,self.Button_ModifyInfoPoint,self.list_types,self.Button_LinkData,self.Button_ViewData,self.Button_DeleteData,self.Button_AnalyseData]
        for item in self.modifypoint_items:
            item.setEnabled(False)
        
        self.populate_attributes()
        
        

    #write the info of the point in the text boxes
    def populate_attributes(self):
        
        if self.table_DataLinked.isEnabled()==True:
            self.default_attributes=[self.point_selected.point_name,self.point_selected.point_comments,
                                     self.point_selected.date_ini.split(" ")[0],self.point_selected.date_ini.split(" ")[1],
                                     self.point_selected.date_end.split(" ")[0],self.point_selected.date_end.split(" ")[1]]
            for i,t_box in enumerate(self.text_boxes):
                # print(t_box)
                t_box.setText(str(self.default_attributes[i]))
                t_box.setEnabled(False)            
        else:
            self.default_attributes=["Point {}".format(len(self.exp_selected.points)),"This is Point {}".format(len(self.exp_selected.points)),
                                     self.exp_selected.date_ini.split(" ")[0],self.exp_selected.date_ini.split(" ")[1],
                                     self.exp_selected.date_end.split(" ")[0],self.exp_selected.date_end.split(" ")[1]]                                     
    
            for i,t_box in enumerate(self.text_boxes):
                t_box.setPlaceholderText(str(self.default_attributes[i]))
                #t_box.setEnabled(False)

    
    def create_point(self):

        for i,t_box in enumerate(self.text_boxes):
            if t_box.toPlainText()=="":
                t_box.setText(self.default_attributes[i])
        
        d_ini=self.text_DateStart.toPlainText()+" "+self.text_TimeStart.toPlainText()
        d_end=self.text_DateEnd.toPlainText()+" "+self.text_TimeEnd.toPlainText()   
        print("{},{}".format(d_ini,d_end))
        if len(self.text_TimeStart.toPlainText().split(":"))==2:
            d_ini+=":00"
        if len(self.text_TimeEnd.toPlainText().split(":"))==2:
            d_end+=":00"
        try:
            d_ini=datetime.strptime(d_ini,"%Y-%m-%d %H:%M:%S")
            d_end=datetime.strptime(d_end,"%Y-%m-%d %H:%M:%S")   
            
            if d_ini>d_end or d_ini<datetime.strptime(self.exp_selected.date_ini,"%Y-%m-%d %H:%M:%S") or d_end>datetime.strptime(self.exp_selected.date_ini,"%Y-%m-%d %H:%M:%S")  :
                raise Exception("overtime","overtime")            
        except Exception as exc:
            if exc.args[0]=="overtime":
                if d_ini>d_end:
                    msgbox.Message_popup("Error","Error Date","Start date is later than End Date. Check that!")
                elif d_ini<datetime.strptime(self.exp_selected.date_ini,"%Y-%m-%d %H:%M:%S"):
                    msgbox.Message_popup("Error","Error Date","Start date is earlier than Experiment's Start Date. Check that!")
                elif d_end>datetime.strptime(self.exp_selected.date_end,"%Y-%m-%d %H:%M:%S"):
                    msgbox.Message_popup("Error","Error Date","End date is later than Experiment's End Date. Check that!")
            else:
                msgbox.Message_popup("Error","Error Date","the date or the time or the delay has not the right format. Please check: Date: YYYY-MM-DD, time: HH:MM:SS")
        else:
            d_ini=d_ini.strftime("%Y-%m-%d %H:%M:%S")
            d_end=d_end.strftime("%Y-%m-%d %H:%M:%S")
            
            # for t_box in self.text_boxes:
            #     if t_box.toPlainText()=="":
            #         t_box.setText(self.default_attributes)
                    
            self.exp_selected.add_Point(self.text_name.toPlainText(),d_ini,d_end,self.text_comments.toPlainText()) #creates the point in the selected experiment
            self.point_selected=self.exp_selected.points[-1]
            
            for item in self.modifypoint_items:
                item.setEnabled(True)
            time.sleep(0.1)
            
            self.populate_attributes()
            #self.Button_ModifyInfoPoint.setText("MODIFY INFO")
            self.Button_CreatePoint.setEnabled(False)
            #self.populate_linkeddatatable()
            self.label_status.setText("Status: Point Created!")
            #self.Button_ModifyInfoPoint.clicked.connect(self.modify_attrib)
            
    #write the info in the tablewidget of the data linked to the point selected
    def populate_linkeddatatable(self):
        self.table_DataLinked.setRowCount(sum(len(self.point_selected.data_added[k]) for k in self.point_selected.data_added.keys()))
        
        # self.table_col_headers=["Index","Type","StartDate","EndDate","Delay","Nentries"]

        #from the point class in the backend
        # self.data_added[k]=[self.date_ini+timedelta(minutes=delay_db[k]),
        #                     self.date_end+timedelta(minutes=delay_db[k]),
        #                     delay_db[k]+delay*(delay_db["SCADA"]!=0),Nentries[k]] 
        
        for c_i,c in enumerate(self.table_col_headers):
            item=QtWidgets.QTableWidgetItem()
            self.table_DataLinked.setHorizontalHeaderItem(c_i,item)
            item = self.table_DataLinked.horizontalHeaderItem(c_i)
            item.setText(c)
        
        self.table_info={k:[] for k in self.exp_selected.get_dbnames()}
        if self.table_DataLinked.rowCount()>0:
            r_i=0
            for k,v in self.point_selected.data_added.items():                    
                for db in v:
                    item=QtWidgets.QTableWidgetItem()
                    self.table_DataLinked.setVerticalHeaderItem(r_i,item)
                    item = self.table_DataLinked.verticalHeaderItem(r_i)
                    item.setText("") #no id number in the row header
                    d_ini=db[0].strftime("%Y-%m-%d %H:%M:%S")#self.point_selected.data_added[k][0].strftime("%Y-%m-%d %H:%M:%S")
                    d_end=db[1].strftime("%Y-%m-%d %H:%M:%S")#self.point_selected.data_added[k][1].strftime("%Y-%m-%d %H:%M:%S")
                    delay=str(db[2])
                    print(delay)
                    # delaystr=[str(elem) if len(str(elem))>1 else "0"+str(elem) for elem in delay_db[k]]
                  
                    self.table_info[k].append([r_i,k,d_ini,d_end,delay,db[3]]) #table_info will have information about the index in the table for a particular data linked to the point 
                    #print(self.table_info)
                    for c_i in range(len(self.table_col_headers)):
                        item=QtWidgets.QTableWidgetItem()
                        self.table_DataLinked.setItem(r_i, c_i, item)
                        item=self.table_DataLinked.item(r_i, c_i)
                        item.setText(str(self.table_info[k][-1][c_i]))
                    r_i+=1    
        
      
        
    def link_data(self):
        self.label_status.setText("Status: Linking Data...")
        if len(self.list_types.selectedIndexes())==0 or len(self.list_types.selectedIndexes())>1:
            msgbox.Message_popup("Warning","No selection","Please select one data collection from the list")
        else:
            # self.label_status.setText("Status: Adding New Data...")
            collect_data=self.list_types.selectedIndexes()[0].data() 
            if collect_data=="AUTOMATIC":
                collect_data=self.exp_selected.get_dbnames()
            else:
                collect_data=[collect_data]
            
            ui_linkdatapoint=gui_linkdatapoint.Ui_MainWindow(collect_data,[self.point_selected.date_ini,self.point_selected.date_end])
            ui_linkdatapoint.setupUi()
            ui_linkdatapoint.show()
            
            while ui_linkdatapoint.finish_window==False:
                QtCore.QCoreApplication.processEvents()
                time.sleep(0.05)   
            
            # print(ui_linkdatapoint.linkdata_attrib)
            if len(ui_linkdatapoint.linkdata_attrib)>0:
                c_data=ui_linkdatapoint.linkdata_attrib[0]
                d_ini=ui_linkdatapoint.linkdata_attrib[1]
                d_end=ui_linkdatapoint.linkdata_attrib[2]
                delay=ui_linkdatapoint.linkdata_attrib[3]
                self.point_selected.link_point_data(c_data,"SCADA",d_ini,d_end,delay,self.exp_selected.data_experiment)
                self.populate_linkeddatatable()
                msgbox.Message_popup("Info","Data Linked","Data of the experiment was succesfully linked to this point")
        self.label_status.setText("Status: Ready!")

    def modify_attrib(self):
        self.label_status.setText("Status: Modifying Attributes...")
        d_ini_list=[d_info[0]-d_info[2] for d_type in self.exp_selected.get_dbnames() for d_info in self.point_selected.data_added[d_type]]
        d_end_list=[d_info[1]-d_info[2] for d_type in self.exp_selected.get_dbnames() for d_info in self.point_selected.data_added[d_type] ]

        # print(d_ini_list)
        # print(d_end_list)
        if self.text_name.isEnabled()==True:
            
            d_ini=self.text_DateStart.toPlainText()+" "+self.text_TimeStart.toPlainText()
            d_end=self.text_DateEnd.toPlainText()+" "+self.text_TimeEnd.toPlainText()   
            if len(self.text_TimeStart.toPlainText().split(":"))==2:
                d_ini+=":00"
            if len(self.text_TimeEnd.toPlainText().split(":"))==2:
                d_end+=":00"
            try:
                d_ini=datetime.strptime(d_ini,"%Y-%m-%d %H:%M:%S")
                d_end=datetime.strptime(d_end,"%Y-%m-%d %H:%M:%S")
                if d_ini>d_end:
                    raise Exception("overtime","overtime")                    
            except Exception as exc:
                if exc.args[0]=="overtime":
                    msgbox.Message_popup("Error","Dates Error","The Date Start is later than Date End")
                else:
                    msgbox.Message_popup("Error","Dates Format Error","the date or time has not the right format. Please check: Date: YYYY-MM-DD, time:HH:MM:SS")
            else:
                
                if self.table_DataLinked.rowCount()>0: #if there is any data already loaded to the experiment check that the new dates include within the dates of the data linked
                    d_ini_list=[d_info[0]-d_info[2] for d_type in self.exp_selected.get_dbnames() for d_info in self.point_selected.data_added[d_type]]
                    d_end_list=[d_info[1]-d_info[2] for d_type in self.exp_selected.get_dbnames() for d_info in self.point_selected.data_added[d_type] ]
                    # print("d_ini {},min_d_ini_list {}".format(d_ini,min(d_ini_list)))
                    # print("d_end {},max_d_end_list {}".format(d_end,max(d_end_list)))
                    if d_ini<=min(d_ini_list) and d_end>=max(d_end_list):                                        
                        self.point_selected.date_ini=d_ini.strftime("%Y-%m-%d %H:%M:%S")
                        self.point_selected.date_end=d_end.strftime("%Y-%m-%d %H:%M:%S")
                    else:
                        msgbox.Message_popup("Error","New Dates Error","The span of the new timeframe does not cover the times of the data linked. Please Check, or delete from the table the data that is out of the interval. The times will be reset to their original value")
                        self.text_DateStart.setText(self.point_selected.date_ini.split(" ")[0])
                        self.text_TimeStart.setText(self.point_selected.date_ini.split(" ")[1])
                        self.text_DateEnd.setText(self.point_selected.date_end.split(" ")[0])
                        self.text_TimeEnd.setText(self.point_selected.date_end.split(" ")[1])
                else:
                    self.point_selected.date_ini=d_ini.strftime("%Y-%m-%d %H:%M:%S")
                    self.point_selected.date_end=d_end.strftime("%Y-%m-%d %H:%M:%S")
                    
                self.point_selected.exp_name=self.text_name.toPlainText()
                self.point_selected.exp_comments=self.text_comments.toPlainText()
            
                self.populate_attributes()
                msgbox.Message_popup("Info","Modify Attributes","Valid attributes were succesfully updated")
                self.label_status.setText("Status: Ready!")
        else:
            
            for t_box in self.text_boxes:
                t_box.setEnabled(True)                    
        
    def delete_data(self):
        pass


    def cancel_button(self):
        self.finish_window=True
        self.close()
        
        
def randomclasses(a,b):
    global seed
    seed+=1
    random.seed(17*seed)
    return random.randint(a,b)

seed=25

Pr=[]
N_P=randomclasses(1,5)
#P=list(range(N_P))
for p in range(0,N_P):
    Pr.append(KCbckend.Project(f"Proj{p}",f"this is project {p}",f"resp{p}"))
    for s in range(0,randomclasses(1,5)):
        Pr[p].add_Season(f"Ses_p{p}_s{s}",f"this is season p{p}_s{s}. In this season many techniques were applied, also the temperature was controlled and many parameters were varied")
        for e in range(0,randomclasses(1,5)):
            d_0="2020-10-{} 10:00:00".format(randomclasses(1,10))
            d_1="2020-10-{} 12:00:00".format(randomclasses(15,30))
            descrp=["added some moisture with alakali, the temperature was controlled during all the process and many variables were taken into account",
                    "the bed was with iron, and it was neessary to verify potential leakages"]
            fuel=["Polyethylene","Textiles","PVC"]
            ind=random.randint(0,1)
            ind2=randomclasses(0,len(fuel)-1)
            Pr[p].seasons[s].add_Experiment(f"exp{e}",d_0,d_1,fuel[ind2],"silica sand",descrp[ind])
            for pnt in range(0,randomclasses(0,5)):
                # print(f"p{p},s{s},e{e}")
                d_0="2020-10-11 {}:00:00".format(randomclasses(6,12))
                d_1="2020-10-15 {}:00:00".format(randomclasses(13,18))
                Pr[p].seasons[s].experiments[e].add_Point(f"Point{pnt}",d_0,d_1,f"this is the point {pnt}")     

Pr[0].seasons[0].add_Experiment("Exp 1","2019-02-01 08:00:00","2019-02-01 17:00:00","Polyethylene","Olevine","this is a test experiment") #if the date is in HH:MM add the == for the seconds
Pr[0].seasons[0].experiments[-1].add_data("SCADA","190201 trend.XLS","00:00:00","This is first SCADA")
Pr[0].seasons[0].experiments[-1].add_data("GC1","190201_mGC.xlsx","00:03:00","This is first GC1")
# Pr[0].seasons[0].experiments[-1].add_data("SPA","430_190201_G_190201.xls","00:03:00","This is first SPA")
Pr[0].seasons[0].experiments[-1].add_Point("Point 1A","2019-02-01 11:55:00","2019-02-01 12:27:00","this was the point 1 and we used gas bags")
# # In[1]:
# #set_point_data(self,point_route,data_type,time_type,date_ini,date_end,delay,db_experiment)
# #pnt_route=Pr[0].project_name+"/"+P[0].seasons[0].season_name+"/"+Pr[0].seasons[0].experiments[0].exp_name+"/"+P[0].seasons[0].experiments[0].points[0].point_name
# db_exp=Pr[0].seasons[0].experiments[-1].data_experiment
# Pr[0].seasons[0].experiments[-1].points[-1].link_point_data(["SCADA","GC1","INFERNO","SPA"],"SCADA","2019-02-01 11:55:00","2019-02-01 12:27:00",3,db_exp)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow(Pr,[0,0,-1])
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())


# ui=Ui_MainWindow(Pr,[0,0,-1])#[0,0,-1])
# ui.setupUi()
# ui.show()
            
            
            