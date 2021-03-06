# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewProject.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Message_popup:
    def __init__(self,m_type,m_title="",m_text=""):
        self.msg=QMessageBox()
        self.msg.setWindowTitle(m_title)
        self.msg.setText(m_text)
        self.response="No"
        if m_type=="Error":
            self.msgError()            
        elif m_type=="Warning":
            self.msgWarning()
        elif m_type=="Info":
            self.msgInfo()         
        elif m_type=="YesorNo":
            self.msgYesNo()
        
    def msgError(self):
        self.msg.setIcon(QMessageBox.Critical)
        return self.msg.exec_()
    def msgWarning(self):
        self.msg.setIcon(QMessageBox.Warning)
        return self.msg.exec_()
    def msgInfo(self): 
        self.msg.setIcon(QMessageBox.Information)
        return self.msg.exec_()       
    def msgYesNo(self): 
        self.msg.setIcon(QMessageBox.Question)
        self.msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.msg.buttonClicked.connect(self.button_selected)
        #self.msg.standardButton()
        return self.msg.exec_()    
    
    def button_selected(self,i):
        if i.text()=="&Yes":
            self.response="Yes"
        else:
            self.response="No"