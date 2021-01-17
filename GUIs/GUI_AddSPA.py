# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Adddatafile.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os
from PyQt5 import QtCore, QtGui, QtWidgets
from . import GUI_MessageBoxKC as msgbox
from . import GUI_SPA as guispa

class Ui_MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self,n_db_loaded):
        # self.MainWindow=QtWidgets.QMainWindow()
        super(Ui_MainWindow,self).__init__()

        self.n_db_loaded=n_db_loaded #number of GC databases loaded
        self.datafile_info=""
        self.default_attributes=""
        
        self.finish_window=False
    
    def closeEvent(self, event):
        self.finish_window=True
        self.close()
        
    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(558, 300)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(50, 15, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)


        #labels-----------------------------------------------------------------------------------------
        self.label_timeformat = QtWidgets.QLabel(self.centralwidget)
        self.label_timeformat.setGeometry(QtCore.QRect(310, 58, 100, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_timeformat.setFont(font)
        
        self.label_TimeDelay = QtWidgets.QLabel(self.centralwidget)
        self.label_TimeDelay.setGeometry(QtCore.QRect(70, 80, 200, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_TimeDelay.setFont(font)
        
        self.label_file = QtWidgets.QLabel(self.centralwidget)
        self.label_file.setGeometry(QtCore.QRect(70, 130, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_file.setFont(font)

        self.label_comments = QtWidgets.QLabel(self.centralwidget)
        self.label_comments.setGeometry(QtCore.QRect(70, 190, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_comments.setFont(font)

        
        #text boxes-------------------------------------------------------

        self.text_comments = QtWidgets.QTextEdit(self.centralwidget)
        self.text_comments.setGeometry(QtCore.QRect(170, 180, 311, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_comments.setFont(font)
            
        self.text_filepath = QtWidgets.QTextEdit(self.centralwidget)
        self.text_filepath.setGeometry(QtCore.QRect(110, 120, 270, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.text_filepath.setFont(font)

        self.line_TimeDelay = QtWidgets.QLineEdit(self.centralwidget)
        self.line_TimeDelay.setGeometry(QtCore.QRect(290, 75, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_TimeDelay.setFont(font)
        self.line_TimeDelay.setAlignment(QtCore.Qt.AlignCenter)
        
        
        #buttons------------------------------------------------------
        self.Button_SearchFile = QtWidgets.QPushButton(self.centralwidget)
        self.Button_SearchFile.setGeometry(QtCore.QRect(390, 120, 100, 31))
        self.Button_SearchFile.clicked.connect(self.search_file)

        self.Button_AddData = QtWidgets.QPushButton(self.centralwidget)
        self.Button_AddData.setGeometry(QtCore.QRect(390, 240, 100, 40))
        self.Button_AddData.clicked.connect(self.add_data)
        
        self.Button_Cancel = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Cancel.setGeometry(QtCore.QRect(270, 240, 100, 40))
        self.Button_Cancel.clicked.connect(self.cancel_button)
       

        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 558, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Add Data (SPA)"))
        self.label_timeformat.setText(_translate("MainWindow", "HH:MM:SS")) 
        self.label_TimeDelay.setText(_translate("MainWindow", "Time Delay (+/- from SCADA)"))   
        
        self.Title.setText(_translate("MainWindow", "Add Data (SPA)"))
        self.label_comments.setText(_translate("MainWindow", "Comments"))
        self.label_file.setText(_translate("MainWindow", "File"))
        self.Button_AddData.setText(_translate("MainWindow", "ADD DATA"))

        self.Button_Cancel.setText(_translate("MainWindow", "CANCEL"))
        self.Button_SearchFile.setText(_translate("MainWindow", "Search"))
        self.Button_AddData.setText(_translate("MainWindow", "ADD DATA"))
        self.Button_Cancel.setText(_translate("MainWindow", "CANCEL"))
        
        self.write_default_attrib()

    def write_default_attrib(self):
        _translate = QtCore.QCoreApplication.translate
        #print("default_attributes =",self.default_attributes)
        if self.default_attributes=="":
            delay="00:03:00"
            comments="This is SPA_{}".format(self.n_db_loaded)
            self.default_attributes=(delay,comments)
        # print("default_attributes ",self.default_attributes)

        self.line_TimeDelay.setPlaceholderText(_translate("MainWindow", self.default_attributes[0]))
        self.text_filepath.setPlaceholderText(_translate("MainWindow", "datafile data file path"))
        self.text_comments.setPlaceholderText(_translate("MainWindow", self.default_attributes[-1]))

    
    def search_file(self):

        default_path=os.getcwd()
        #print(default_path)
        file_name=QtWidgets.QFileDialog.getOpenFileName(self,"Open datafile File",default_path,"Excel files (*.xls *.xlsx)")
        self.text_filepath.setText(file_name[0])

    def add_data(self):
        
        
        
        self.line_TimeDelay.setText(self.default_attributes[0])
        self.text_comments.setText(self.default_attributes[-1])
        if self.text_filepath=="":
            msgbox.Message_popup("Error","No file","No file selected. Please select the respective file")
            self.datafile_info=""
        else:
            self.datafile_info=[self.text_filepath.toPlainText(),self.line_TimeDelay.text(),self.text_comments.toPlainText()]
            print(self.datafile_info)
            self.cancel_button()

    def cancel_button(self):
        self.finish_window=True
        self.close()
        
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     ui = Ui_MainWindow(0)
#     ui.setupUi()
#     ui.show()
#     sys.exit(app.exec_())

# ui = Ui_MainWindow(0)
# ui.setupUi()
# ui.show()