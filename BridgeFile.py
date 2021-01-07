# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 12:20:12 2020

@author: refor
"""
import sys
from PyQt5 import QtCore
import time

#from GUIs import GUI_SPA
import GUIs.GUI_SPA #the empty file __init__.py was added to the GUIs folder to indicate to python that this is a package
import KCbackend.Database3_window_db5_3 as KCbckend

#alternative way
#sys.path.insert(1,"C:\\Users\\refor\\OneDrive - Chalmers University of Technology\\PhD Research\\Python Course\\Python Project\\KC_project_Python\\Windows")
#import GUI_SPA

P={}
P[0]=KCbckend.Project("Proj1","This is the test project 1")
P[0].add_Season("Season 2020-11","This is the 2020_11 test season")
# P[0].seasons[0].add_Experiment("Exp 1","2019-02-01 08:00:00","2019-02-01 17:00:00","Polyethylene","Olevine","this was the first experiment") #if the date is in HH:MM add the == for the seconds
# P[0].seasons[0].experiments[0].add_data("SCADA","190201 trend.XLS")
# P[0].seasons[0].experiments[0].add_data("GC1","190201_mGC.xlsx")
# P[0].seasons[0].experiments[0].add_data("SPA","430_190201_G_190123.xls")
# P[0].seasons[0].experiments[0].add_Point("Point 1A","this was the point 1 and we used gas bags")


def add_proj(pr_dict,p_name,p_desc):
    thedict=pr_dict
    thedict[len(pr_dict.keys())]=KCbckend.Project(p_name,p_desc)

def add_seas(pr,s_name,s_desc):
    temp=pr
    temp.add_Season(s_name,s_desc)

add_seas(P[0],"Season 2020-12","This is the 2020_12 test season")
add_seas(P[0],"Season 2021-01","This is the 2021_01 test season")

add_proj(P,"Proj2","This is the test project 2")
add_seas(P[1],"Season 2021-02","This is the 2021_02 test season of project 2")
add_proj(P,"Proj3","This is the test project 3")
# ui= GUIs.GUI_SPA.Ui_MainWindow()
# ui.setupUi()

# filename="430_190201_G_190123.xls"
# ui.read_file(filename)

# ui.MainWindow.show()

# while ui.finish_window==False:
#     QtCore.QCoreApplication.processEvents()
#     time.sleep(0.01)
#     #    pass

# try:
#     b=ui.sh_dates
# except:
#     GUIs.GUI_SPA.Message_popup("Error","Error reading SPA table","The sheets were not read from SPA file")
#     #GUI_SPA.Message_popup("")
    
print("Done")
# MainWindow = QtWidgets.QMainWindow()
# ui = Ui_MainWindow()
# ui.setupUi(MainWindow)
# #MainWindow.show()
#     #sys.exit(app.exec_())

# filename="430_190201_G_190123.xls"
# ui.get_sheets(filename)
# #table_sh=ui.read_table()

# MainWindow.show()