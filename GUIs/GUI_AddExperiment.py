


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

   def __init__(self):
        self.MainWindow=QtWidgets.QMainWindow()
        self.finish_window=False 

        self.experiments_attributes=0

    def setupUi(self):
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(759, 655)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_season = QtWidgets.QLabel(self.centralwidget)
        self.label_season.setGeometry(QtCore.QRect(80, 140, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_season.setFont(font)
        self.label_season.setObjectName("label_season")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(190, 130, 131, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.label_DateStart = QtWidgets.QLabel(self.centralwidget)
        self.label_DateStart.setGeometry(QtCore.QRect(80, 310, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_DateStart.setFont(font)
        self.label_DateStart.setObjectName("label_DateStart")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(230, 30, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.Title.setFont(font)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.Button_AddSeason = QtWidgets.QPushButton(self.centralwidget)
        self.Button_AddSeason.setGeometry(QtCore.QRect(370, 130, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Button_AddSeason.setFont(font)
        self.Button_AddSeason.setObjectName("Button_AddSeason")
        self.label_comments = QtWidgets.QLabel(self.centralwidget)
        self.label_comments.setGeometry(QtCore.QRect(80, 500, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_comments.setFont(font)
        self.label_comments.setObjectName("label_comments")
        self.text_fuel = QtWidgets.QTextEdit(self.centralwidget)
        self.text_fuel.setGeometry(QtCore.QRect(190, 440, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_fuel.setFont(font)
        self.text_fuel.setObjectName("text_fuel")
        self.tex_comments = QtWidgets.QTextEdit(self.centralwidget)
        self.tex_comments.setGeometry(QtCore.QRect(190, 480, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tex_comments.setFont(font)
        self.tex_comments.setObjectName("tex_comments")
        self.label_DateEnd = QtWidgets.QLabel(self.centralwidget)
        self.label_DateEnd.setGeometry(QtCore.QRect(80, 350, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_DateEnd.setFont(font)
        self.label_DateEnd.setObjectName("label_DateEnd")
        self.label_fuel = QtWidgets.QLabel(self.centralwidget)
        self.label_fuel.setGeometry(QtCore.QRect(80, 450, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_fuel.setFont(font)
        self.label_fuel.setObjectName("label_fuel")
        self.Button_AddExperiment = QtWidgets.QPushButton(self.centralwidget)
        self.Button_AddExperiment.setGeometry(QtCore.QRect(590, 450, 100, 40))
        self.Button_AddExperiment.setObjectName("Button_AddExperiment")
        self.label_date = QtWidgets.QLabel(self.centralwidget)
        self.label_date.setGeometry(QtCore.QRect(190, 270, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_date.setFont(font)
        self.label_date.setObjectName("label_date")
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(380, 270, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_time.setFont(font)
        self.label_time.setObjectName("label_time")
        self.text_DateStart = QtWidgets.QTextEdit(self.centralwidget)
        self.text_DateStart.setGeometry(QtCore.QRect(190, 300, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_DateStart.setFont(font)
        self.text_DateStart.setObjectName("text_DateStart")
        self.text_DateEnd = QtWidgets.QTextEdit(self.centralwidget)
        self.text_DateEnd.setGeometry(QtCore.QRect(190, 350, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_DateEnd.setFont(font)
        self.text_DateEnd.setObjectName("text_DateEnd")
        self.text_TimeStart = QtWidgets.QTextEdit(self.centralwidget)
        self.text_TimeStart.setGeometry(QtCore.QRect(380, 300, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_TimeStart.setFont(font)
        self.text_TimeStart.setObjectName("text_TimeStart")
        self.text_TimeEnd = QtWidgets.QTextEdit(self.centralwidget)
        self.text_TimeEnd.setGeometry(QtCore.QRect(380, 350, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_TimeEnd.setFont(font)
        self.text_TimeEnd.setObjectName("text_TimeEnd")
        self.Button_Cancel = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Cancel.setGeometry(QtCore.QRect(590, 510, 100, 40))
        self.Button_Cancel.setObjectName("Button_Cancel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 759, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_season.setText(_translate("MainWindow", "Season"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "2024/2025"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "2023/2024"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "2022/2023"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "2021/2022"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "2020/2021"))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "2019/2020"))
        item = self.listWidget.item(6)
        item.setText(_translate("MainWindow", "2018/2019"))
        item = self.listWidget.item(7)
        item.setText(_translate("MainWindow", "2017/2018"))
        item = self.listWidget.item(8)
        item.setText(_translate("MainWindow", "2016/2017"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_DateStart.setText(_translate("MainWindow", "Date start"))
        self.Title.setText(_translate("MainWindow", "Add a new experiment"))
        self.Button_AddSeason.setText(_translate("MainWindow", "Add Season"))
        self.label_comments.setText(_translate("MainWindow", "Comments"))
        self.text_fuel.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt;\">Write fuel here</span></p></body></html>"))
        self.tex_comments.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt;\">write commment here</span></p></body></html>"))
        self.label_DateEnd.setText(_translate("MainWindow", "Date end"))
        self.label_fuel.setText(_translate("MainWindow", "Fuel"))
        self.Button_AddExperiment.setText(_translate("MainWindow", "OK"))
        self.label_date.setText(_translate("MainWindow", "Date (YYYY-MM-DD)"))
        self.label_time.setText(_translate("MainWindow", "TIME (HH:MM)"))
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
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">23:59</span></p></body></html>"))
        self.Button_Cancel.setText(_translate("MainWindow", "Cancel"))

def cancel_window(self):
        self.finish_window=True
        self.MainWindow.close()

#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec_())


ui=Ui_MainWindow()
 ui.setupUi()

ui.MainWindow.show()