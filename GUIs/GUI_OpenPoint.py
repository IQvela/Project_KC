# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_OpenPoint.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProjectWin(object):

    def setupUi(self, ProjectWin):
        ProjectWin.setObjectName("ProjectWin")
        ProjectWin.resize(1116, 681)

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
        ProjectWin.setPalette(palette)

        self.centralwidget = QtWidgets.QWidget(ProjectWin)
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
        
        #Text
        self.text_PointName = QtWidgets.QTextEdit(self.centralwidget)
        self.text_PointName.setGeometry(QtCore.QRect(160, 90, 721, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_PointName.setFont(font)

        self.text_comments = QtWidgets.QTextEdit(self.centralwidget)
        self.text_comments.setGeometry(QtCore.QRect(160, 130, 721, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_comments.setFont(font)
        
        #Button Modify info point
        self.Button_ModifyInfoPoint = QtWidgets.QPushButton(self.centralwidget)
        self.Button_ModifyInfoPoint.setGeometry(QtCore.QRect(910, 110, 100, 40))
        ProjectWin.setCentralWidget(self.centralwidget)

        #Table Data Avaible/already existing---------------------------------------------------------------------------------
        self.table_DataAvailable = QtWidgets.QTableWidget(self.centralwidget)
        self.table_DataAvailable.setGeometry(QtCore.QRect(50, 240, 531, 221))
        self.table_DataAvailable.setColumnCount(5)
        self.table_DataAvailable.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.table_DataAvailable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_DataAvailable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_DataAvailable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_DataAvailable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_DataAvailable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_DataAvailable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_DataAvailable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_DataAvailable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_DataAvailable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_DataAvailable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_DataAvailable.setItem(3, 1, item)

        #Label Data available
        self.label_DataAvailable = QtWidgets.QLabel(self.centralwidget)
        self.label_DataAvailable.setGeometry(QtCore.QRect(50, 200, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.label_DataAvailable.setFont(font)
        
        #Buttons under data available---------------------------------------------------------------------------------

        self.Button_AnalyseData = QtWidgets.QPushButton(self.centralwidget)
        self.Button_AnalyseData.setGeometry(QtCore.QRect(340, 480, 100, 40))
        
        self.Button_ModifyData = QtWidgets.QPushButton(self.centralwidget)
        self.Button_ModifyData.setGeometry(QtCore.QRect(190, 480, 100, 40))
        
        self.Button_ReadData = QtWidgets.QPushButton(self.centralwidget)
        self.Button_ReadData.setGeometry(QtCore.QRect(480, 480, 100, 40))
        
        self.Button_ViewData = QtWidgets.QPushButton(self.centralwidget)
        self.Button_ViewData.setGeometry(QtCore.QRect(50, 480, 100, 40))
        
        # Selecting a data type and adding the data to the point-----------------------------------       

        #List of types of data
        self.label_SelectType = QtWidgets.QLabel(self.centralwidget)
        self.label_SelectType.setGeometry(QtCore.QRect(670, 250, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_SelectType.setFont(font)
        self.list_types = QtWidgets.QListWidget(self.centralwidget)
        self.list_types.setGeometry(QtCore.QRect(670, 280, 221, 101))
        self.list_types.setObjectName("list_types")
        item = QtWidgets.QListWidgetItem()
        self.list_types.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_types.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_types.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_types.addItem(item)

        #Button Add new data (after selecting data TYPE)
        self.Button_AddNewData = QtWidgets.QPushButton(self.centralwidget)
        self.Button_AddNewData.setGeometry(QtCore.QRect(920, 310, 100, 40))
        
        #line for visual separation
        self.line_separate = QtWidgets.QFrame(self.centralwidget)
        self.line_separate.setGeometry(QtCore.QRect(610, 210, 20, 331))
        self.line_separate.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_separate.setFrameShadow(QtWidgets.QFrame.Sunken)
        
        self.label_AddNewData = QtWidgets.QLabel(self.centralwidget)
        self.label_AddNewData.setGeometry(QtCore.QRect(670, 210, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.label_AddNewData.setFont(font)
        
        
        #Buttons Cancel and OK---------------------------------------------------------------------------------
        self.Button_Ok = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Ok.setGeometry(QtCore.QRect(950, 560, 100, 40))
        
        self.Button_Cancel = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Cancel.setGeometry(QtCore.QRect(830, 560, 100, 40))
        self.Button_Cancel.setObjectName("Button_Cancel")

        self.retranslateUi(ProjectWin)
        QtCore.QMetaObject.connectSlotsByName(ProjectWin)

    def retranslateUi(self, ProjectWin):
        _translate = QtCore.QCoreApplication.translate
        ProjectWin.setWindowTitle(_translate("ProjectWin", "PointWindow"))

        #point info-----------------------------------------------------------------------
        self.Title_PointName.setText(_translate("ProjectWin", "Season 1/ Experiment 1/Point 1"))
        self.label_comments.setText(_translate("ProjectWin", "Comments"))
        self.text_comments.setHtml(_translate("ProjectWin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Button_ModifyInfoPoint.setText(_translate("ProjectWin", "MODIFY INFO"))

        #buttons existing data--------------------------------------------------------
        self.Button_AnalyseData.setText(_translate("ProjectWin", "ANALYZE DATA"))
        self.Button_ModifyData.setText(_translate("ProjectWin", "MODIFY DATA"))
        self.Button_ReadData.setText(_translate("ProjectWin", "READ DATA"))
        self.Button_ViewData.setText(_translate("ProjectWin", "VIEW DATA"))

        #table existing/available data-------------------------------------------
        item = self.table_DataAvailable.horizontalHeaderItem(0)
        item.setText(_translate("ProjectWin", "Index"))
        item = self.table_DataAvailable.horizontalHeaderItem(1)
        item.setText(_translate("ProjectWin", "StartDate"))
        item = self.table_DataAvailable.horizontalHeaderItem(2)
        item.setText(_translate("ProjectWin", "EndDate"))
        item = self.table_DataAvailable.horizontalHeaderItem(3)
        item.setText(_translate("ProjectWin", "Type"))
        item = self.table_DataAvailable.horizontalHeaderItem(4)
        item.setText(_translate("ProjectWin", "Comment"))
        __sortingEnabled = self.table_DataAvailable.isSortingEnabled()
        self.table_DataAvailable.setSortingEnabled(False)
        self.table_DataAvailable.setSortingEnabled(__sortingEnabled)
        self.label_DataAvailable.setText(_translate("ProjectWin", "Data available"))

        #add data to point a nd select data ------------------------------------------
        self.label_SelectType.setText(_translate("ProjectWin", "Select type "))
        #list    
        __sortingEnabled = self.list_types.isSortingEnabled()
        self.list_types.setSortingEnabled(False)
        item = self.list_types.item(0)
        item.setText(_translate("ProjectWin", "SCADA"))
        item = self.list_types.item(1)
        item.setText(_translate("ProjectWin", "GC"))
        item = self.list_types.item(2)
        item.setText(_translate("ProjectWin", "SPA"))
        item = self.list_types.item(3)
        item.setText(_translate("ProjectWin", "Others"))
        self.list_types.setSortingEnabled(__sortingEnabled)
        #button
        self.Button_AddNewData.setText(_translate("ProjectWin", "ADD DATA"))
        #labels and text
        self.label_AddNewData.setText(_translate("ProjectWin", "Add data to point"))
        self.label_name.setText(_translate("ProjectWin", "Name"))
        self.text_PointName.setHtml(_translate("ProjectWin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        
        #basic buttons------------------------------------------------------------------
        self.Button_Ok.setText(_translate("ProjectWin", "OK"))
        self.Button_Cancel.setText(_translate("ProjectWin", "CANCEL"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProjectWin = QtWidgets.QMainWindow()
    ui = Ui_ProjectWin()
    ui.setupUi(ProjectWin)
    ProjectWin.show()
    sys.exit(app.exec_())
