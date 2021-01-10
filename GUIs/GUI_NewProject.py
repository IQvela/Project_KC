# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewProject.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from . import GUI_MessageBoxKC as msgbox


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()        
        #self.MainWindow=QtWidgets.QMainWindow()
        self.finish_window=False        
        
        self.project_attributes=0
        
    def closeEvent(self, event):
        self.finish_window=True
        self.close()      
        
    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(550, 330)
        
        #Labels
        self.Label_Title = QtWidgets.QLabel(self)
        self.Label_Title.setGeometry(QtCore.QRect(180, 10, 200, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.Label_Title.setFont(font)
        self.Label_Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Title.setObjectName("Label_Title")
        
        self.Label_Name = QtWidgets.QLabel(self)
        self.Label_Name.setGeometry(QtCore.QRect(20, 70, 100, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Label_Name.setFont(font)
        self.Label_Name.setObjectName("Label_Name")
        
        self.Label_Description = QtWidgets.QLabel(self)
        self.Label_Description.setGeometry(QtCore.QRect(20, 120, 70, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Label_Description.setFont(font)
        self.Label_Description.setObjectName("Label_Description")

        self.Label_Responsible = QtWidgets.QLabel(self)
        self.Label_Responsible.setGeometry(QtCore.QRect(20, 230, 70, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Label_Responsible.setFont(font)
        self.Label_Responsible.setObjectName("Label_Responsible")
        
        #TextBoxes
        self.Textbox_Name = QtWidgets.QTextEdit(self)
        self.Textbox_Name.setGeometry(QtCore.QRect(120, 70, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Textbox_Name.setFont(font)
                
        self.Textbox_Description = QtWidgets.QTextEdit(self)
        self.Textbox_Description.setGeometry(QtCore.QRect(120, 120, 400, 90)) 
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Textbox_Description.setFont(font)
        
        self.Textbox_Responsible = QtWidgets.QTextEdit(self)
        self.Textbox_Responsible.setGeometry(QtCore.QRect(120, 230, 300, 31)) 
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Textbox_Responsible.setFont(font)
        
        #Buttons
        self.Button_Create = QtWidgets.QPushButton(self)
        self.Button_Create.setGeometry(QtCore.QRect(120, 280, 100, 40))
        self.Button_Create.clicked.connect(self.create_project)
        
        self.Button_Cancel = QtWidgets.QPushButton(self)
        self.Button_Cancel.setGeometry(QtCore.QRect(320, 280, 100, 40))
        self.Button_Cancel.clicked.connect(self.cancel_window)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "New Project"))

        self.Label_Title.setText(_translate("MainWindow", "New project"))
        self.Label_Name.setText(_translate("MainWindow", "Project Name"))
        self.Label_Description.setText(_translate("MainWindow", "Description"))
        self.Label_Responsible.setText(_translate("MainWindow", "Responsible"))
        
        self.Button_Create.setText(_translate("MainWindow", "Create"))
        self.Button_Cancel.setText(_translate("MainWindow", "Cancel"))


    def create_project(self):
        print("creating the project")
        if self.Textbox_Name.toPlainText()=="" or self.Textbox_Description.toPlainText()=="" or self.Textbox_Responsible.toPlainText()=="":
            # print("No text was written")
            msgbox.Message_popup("Error","No Text","No text was written")
        else:

            self.project_attributes=(self.Textbox_Name.toPlainText(),self.Textbox_Description.toPlainText(),self.Textbox_Responsible.toPlainText())
            print("the text was read")
            self.cancel_window()
        
    def cancel_window(self):
        self.finish_window=True
        self.close()


# class Message_popup:
#     def __init__(self,m_type,m_title="",m_text=""):
#         self.msg=QMessageBox()
#         self.msg.setWindowTitle(m_title)
#         self.msg.setText(m_text)
#         if m_type=="Error":
#             self.msgError()            
#         elif m_type=="Warning":
#             self.msgWarning()
#         elif m_type=="Info":
#             self.msgInfo()         
#         elif m_type=="YesorNo":
#             self.msgYesNo()
        
#     def msgError(self):
#         self.msg.setIcon(QMessageBox.Critical)
#         return self.msg.exec_()
#     def msgWarning(self):
#         self.msg.setIcon(QMessageBox.Warning)
#         return self.msg.exec_()
#     def msgInfo(self): 
#         self.msg.setIcon(QMessageBox.Information)
#         return self.msg.exec_()       
#     def msgYesNo(self): 
#         self.msg.setIcon(QMessageBox.Question)
#         self.msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
#         #self.msg.standardButton()
#         return self.msg.exec_()    

        
# if __Name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
#     #sys.exit(app.exec_())

# ui=Ui_MainWindow()
# ui.setupUi()

# ui.show()
