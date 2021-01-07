# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 11:10:15 2021

@author: refor
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Message_popup:
    def __init__(self,m_type,m_title="",m_text=""):
        self.msg=QMessageBox()
        self.msg.setWindowTitle(m_title)
        self.msg.setText(m_text)
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
        #self.msg.standardButton()
        return self.msg.exec_()    