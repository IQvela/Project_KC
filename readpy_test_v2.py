# -*- coding: utf-8 -*-
"""
Created on Wed Dec 1 2020

@author: canete
"""
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import time

#from GUIs import GUI_SPA
import GUIs.MAinWin2 #the empty file __init__.py was added to the GUIs folder to indicate to python that this is a package

#alternative way
#sys.path.insert(1,"C:\\Users\\refor\\OneDrive - Chalmers University of Technology\\PhD Research\\Python Course\\Python Project\\KC_project_Python\\Windows")
#import GUI_SPA

app=QtWidgets.QApplication(sys.argv)
ui= GUIs.MAinWin2.Ui_MainWindow()
ui.setupUi()

filename="430_190201_G_190123.xls" #SPA xls test file
ui.get_sheets(filename)

ui.MainWindow.show()

while ui.finish_window==False:
    QtCore.QCoreApplication.processEvents()
    time.sleep(0.01)
    #    pass

try:
    b=ui.sh_dates
except:
    GUIs.GUI_SPA.Message_popup("Error","Error reading SPA table","The sheets were not read from SPA file")

    
print("Done")

#     #sys.exit(app.exec_())

