# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_SelectDataType.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(444, 366)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        #labels-----------------------------------------------------------
        self.Title_DataType = QtWidgets.QLabel(self.centralwidget)
        self.Title_DataType.setGeometry(QtCore.QRect(60, 10, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Title_DataType.setFont(font)
        self.Title_DataType.setAlignment(QtCore.Qt.AlignCenter)
        
        self.label_DataType = QtWidgets.QLabel(self.centralwidget)
        self.label_DataType.setGeometry(QtCore.QRect(30, 80, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_DataType.setFont(font)
        self.label_DataType.setObjectName("label_DataType")

        #list data types----------------------------------------------------------
        self.list_DataType = QtWidgets.QListWidget(self.centralwidget)
        self.list_DataType.setGeometry(QtCore.QRect(120, 80, 261, 141))
        
        item = QtWidgets.QListWidgetItem()
        self.list_DataType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_DataType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_DataType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_DataType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_DataType.addItem(item)

        #Buttons--------------------------------------------------------
        self.Button_Add = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Add.setGeometry(QtCore.QRect(280, 250, 100, 40))
        
        self.Button_Cancel = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Cancel.setGeometry(QtCore.QRect(150, 250, 100, 40))
        

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 444, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Select Data Type"))

        #labels-------------------------------------------------------------------
        self.Title_DataType.setText(_translate("MainWindow", "Select Data type"))
        self.label_DataType.setText(_translate("MainWindow", "Data type"))

        #list----------------------------------------------------------------------
        __sortingEnabled = self.list_DataType.isSortingEnabled()
        self.list_DataType.setSortingEnabled(False)
        item = self.list_DataType.item(0)
        item.setText(_translate("MainWindow", "GC (gas data)"))
        item = self.list_DataType.item(1)
        item.setText(_translate("MainWindow", "SCADA"))
        item = self.list_DataType.item(2)
        item.setText(_translate("MainWindow", "SPA (GC-430)"))
        item = self.list_DataType.item(3)
        item.setText(_translate("MainWindow", "Other files"))
        self.list_DataType.setSortingEnabled(__sortingEnabled)

        #buttons--------------------------------------------------------
        self.Button_Add.setText(_translate("MainWindow", "Add"))
        self.Button_Cancel.setText(_translate("MainWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
