# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_AddGC.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.resize(558, 551)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        
        #labels-------------------------------------------------------------------
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(60, 40, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.Title.setFont(font)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)

        self.label_date = QtWidgets.QLabel(self.centralwidget)
        self.label_date.setGeometry(QtCore.QRect(180, 120, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_date.setFont(font)
        
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(370, 120, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_time.setFont(font)

        self.label_DateStart = QtWidgets.QLabel(self.centralwidget)
        self.label_DateStart.setGeometry(QtCore.QRect(70, 160, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_DateStart.setFont(font)
        
        self.label_DateEnd = QtWidgets.QLabel(self.centralwidget)
        self.label_DateEnd.setGeometry(QtCore.QRect(70, 200, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_DateEnd.setFont(font)

        self.label_TimeDelay = QtWidgets.QLabel(self.centralwidget)
        self.label_TimeDelay.setGeometry(QtCore.QRect(70, 270, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_TimeDelay.setFont(font)
        
        self.label_file = QtWidgets.QLabel(self.centralwidget)
        self.label_file.setGeometry(QtCore.QRect(70, 341, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_file.setFont(font)

        self.label_comments = QtWidgets.QLabel(self.centralwidget)
        self.label_comments.setGeometry(QtCore.QRect(70, 401, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_comments.setFont(font)
        
        #text boxes----------------------------------------------------
   
        self.text_DateStart = QtWidgets.QTextEdit(self.centralwidget)
        self.text_DateStart.setGeometry(QtCore.QRect(180, 150, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_DateStart.setFont(font)

        self.text_DateEnd = QtWidgets.QTextEdit(self.centralwidget)
        self.text_DateEnd.setGeometry(QtCore.QRect(180, 200, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_DateEnd.setFont(font)
        
        self.text_TimeStart = QtWidgets.QTextEdit(self.centralwidget)
        self.text_TimeStart.setGeometry(QtCore.QRect(370, 150, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_TimeStart.setFont(font)
     
        self.text_TimeEnd = QtWidgets.QTextEdit(self.centralwidget)
        self.text_TimeEnd.setGeometry(QtCore.QRect(370, 200, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_TimeEnd.setFont(font)

        self.text_TimeDelay = QtWidgets.QTextEdit(self.centralwidget)
        self.text_TimeDelay.setGeometry(QtCore.QRect(370, 260, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_TimeDelay.setFont(font)
        
        self.text_FileDir = QtWidgets.QTextEdit(self.centralwidget)
        self.text_FileDir.setGeometry(QtCore.QRect(110, 331, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_FileDir.setFont(font)

        self.tex_comments = QtWidgets.QTextEdit(self.centralwidget)
        self.tex_comments.setGeometry(QtCore.QRect(170, 391, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tex_comments.setFont(font)
        
       
        #Buttons----------------------------------------------------------------------
        self.Button_SearchFile = QtWidgets.QPushButton(self.centralwidget)
        self.Button_SearchFile.setGeometry(QtCore.QRect(390, 330, 100, 31))

        self.Button_AddData = QtWidgets.QPushButton(self.centralwidget)
        self.Button_AddData.setGeometry(QtCore.QRect(390, 461, 100, 40))

        self.Button_Cancel = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Cancel.setGeometry(QtCore.QRect(270, 461, 100, 40))
               

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 558, 26))
       
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
      
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add data GC"))

        #labels--------------------------------------------------------------------
        self.Title.setText(_translate("MainWindow", "Add Data (GC gas)"))
        self.label_date.setText(_translate("MainWindow", "Date (YYYY-MM-DD)"))
        self.label_time.setText(_translate("MainWindow", "TIME (HH:MM)"))
        self.label_DateStart.setText(_translate("MainWindow", "Date start"))
        self.label_DateEnd.setText(_translate("MainWindow", "Date end"))
        self.label_TimeDelay.setText(_translate("MainWindow", "Time Delay (+/- min from SCADA)"))
        self.label_file.setText(_translate("MainWindow", "File"))
        self.label_comments.setText(_translate("MainWindow", "Comments"))
        
        #text boxes
        self.text_DateStart.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))
        self.text_DateEnd.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))
        self.text_TimeStart.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">6:00</span></p></body></html>"))
        self.text_TimeEnd.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">18:00</span></p></body></html>"))
        
        self.text_TimeDelay.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">+3</span></p></body></html>"))
        
        self.text_FileDir.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
       
        self.tex_comments.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
       
        #buttons-----------------------------------------------------------------
        self.Button_AddData.setText(_translate("MainWindow", "ADD DATA"))
        self.Button_Cancel.setText(_translate("MainWindow", "CANCEL"))
        self.Button_SearchFile.setText(_translate("MainWindow", "Search"))

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())