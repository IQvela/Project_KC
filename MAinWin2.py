# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KCdata_MainWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import time
import sys
import random
import pickle

from PyQt5 import QtCore, QtGui, QtWidgets
import Classes_Backend as KCbckend

import GUIs.GUI_NewProject as gui_newproject
import GUIs.GUI_OpenProject as gui_openproject
# import GUIs.Backup_Projects as backup_projects
import GUIs.GUI_MessageBoxKC as msgbox
import GUIs.GUI_ViewData as gui_viewdata



class Ui_MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        #self.MainWindow=QtWidgets.QMainWindow()
        super(Ui_MainWindow,self).__init__()
        self.finish_window=False
        self.Table_Project_headers=["Index","Project Name","Timeframe","Description","Responsible"]
        self.load_allprojects()

    def closeEvent(self, event):
        with open("{}\{}.pkl".format(KCbckend.Project.filepath,KCbckend.Project.filename),"wb") as f:
            pickle.dump(self.Pr_list,f) 
        print("Projects Saved (Main)")        
        # backup_projects.save_pr(self.Pr_list,KCbckend.Project.filepath,KCbckend.Project.filename)
        self.finish_window=True
        self.close()
        
    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(627, 389)
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
        self.setPalette(palette)
        
        #window general widget
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(250, 10, 271, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        
        #define label: title of the window
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        #define button: Open project
        self.Button_OpenProject = QtWidgets.QPushButton(self.centralwidget)
        self.Button_OpenProject.setGeometry(QtCore.QRect(490, 290, 100, 40))
        self.Button_OpenProject.setObjectName("Button_OpenProject")
        self.Button_OpenProject.clicked.connect(self.open_project)
        #define button: add project
        self.Button_NewProject = QtWidgets.QPushButton(self.centralwidget)
        self.Button_NewProject.setGeometry(QtCore.QRect(360, 290, 100, 40))
        self.Button_NewProject.setShortcut("")
        self.Button_NewProject.setCheckable(False)
        self.Button_NewProject.clicked.connect(self.new_project)
        
        #define button: Delete project
        self.Button_DeleteProject = QtWidgets.QPushButton(self.centralwidget)
        self.Button_DeleteProject.setGeometry(QtCore.QRect(100, 290, 110, 40))
        self.Button_DeleteProject.clicked.connect(self.delete_project)

        #define button: check data
        self.Button_ViewData = QtWidgets.QPushButton(self.centralwidget)
        self.Button_ViewData.setGeometry(QtCore.QRect(230, 290, 100, 40))
        self.Button_ViewData.setObjectName("Button_ViewData")
        self.Button_ViewData.clicked.connect(self.view_data)
        
        #define table: project list
        self.Table_Project_list = QtWidgets.QTableWidget(self.centralwidget)
        self.Table_Project_list.setGeometry(QtCore.QRect(20, 60, 571, 201))
        self.Table_Project_list.setObjectName("Table_Project_list")
        self.Table_Project_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows) #the selection behaviour is by rows 
        self.Table_Project_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers) #disable text editing
        #self.Table_Project_list.setUpdatesEnabled(False)
        
        self.Table_Project_list.setColumnCount(len(self.Table_Project_headers)) #number of columns
        self.Table_Project_list.setRowCount(len(self.Pr_list)) #number of rows --- need to change by list length
        

        #other table defs
        self.Table_Project_list.horizontalHeader().setMinimumSectionSize(36)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 627, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)


    #this function defines all the names that appear in window
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Projects KC"))
        #names of tile and buttons open project, add project and check data
        self.Title.setText(_translate("MainWindow", "KC - data"))
        self.Button_OpenProject.setText(_translate("MainWindow", "OPEN PROJECT"))
        self.Button_NewProject.setText(_translate("MainWindow", "ADD PROJECT"))
        self.Button_ViewData.setText(_translate("MainWindow", "CHECK DATA"))
        self.Button_DeleteProject.setText(_translate("MainWindow", "DELETE PROJECT"))
        #table info definition
        #vertical header names
        if self.Table_Project_list.rowCount()>0:
            for p in list(self.Pr_list):
                temp=p.get_dates_total()
            self.populate_projecttable()

    def populate_projecttable(self):
        #horizontal header names
        self.Table_Project_list.clear()
        self.Table_Project_list.setRowCount(len(self.Pr_list))

        for i in range(self.Table_Project_list.columnCount()):
            item = QtWidgets.QTableWidgetItem()
            self.Table_Project_list.setHorizontalHeaderItem(i, item)
            
        for i,n in list(enumerate(self.Table_Project_headers)):
            item = self.Table_Project_list.horizontalHeaderItem(i)
            item.setText(n)
        
        if len(self.Pr_list)>0:
            
            for i in range(len(self.Pr_list)):
                item = QtWidgets.QTableWidgetItem()
                self.Table_Project_list.setVerticalHeaderItem(i, item)                         
                item = self.Table_Project_list.verticalHeaderItem(i)
                item.setText("")#f"{i}")
                item=self.Table_Project_list.item(i,0)

            for p in list(self.Pr_list):
                temp=p.get_dates_total()
            
            attr={}
            for i,p in list(enumerate(self.Pr_list)):
                attr[0]=str(i)
                attr[1]=p.project_name
                attr[2]=p.date_ini + "-" + p.date_end
                attr[3]=p.project_description
                attr[4]=p.project_responsible
                # print(attr)
                for j,v in attr.items():
                    item = QtWidgets.QTableWidgetItem()
                    self.Table_Project_list.setItem(i, j, item)
                    item=self.Table_Project_list.item(i,j)
                    item.setText(v)

        # self.Table_Project_list.setSortingEnabled(__sortingEnabled)

    def delete_project (self):
        #ind_pr_selected=int(self.Table_Project_list.selectedItems()[0].text())
        try:
            ind_pr_selected=int(self.Table_Project_list.selectedItems()[0].text())
        except:
            msgbox.Message_popup("Error","Error","Please select an Project")
        else:
            if ind_pr_selected >-1:
                # print(f"this is the selected: {ind_pr_selected}")
                yesorno=msgbox.Message_popup("YesorNo","Delete Project", "Are you sure you want to delete the selected Project? Note: All data uploaded to this entry will be deleted (not the files)")
                if yesorno.response=="Yes":
                    del self.Pr_list[ind_pr_selected]
                    self.populate_projecttable()
            
        

    def new_project(self):

        ui_newproject=gui_newproject.Ui_MainWindow()
        ui_newproject.setupUi()
        ui_newproject.show()
        
        while ui_newproject.finish_window==False:
            QtCore.QCoreApplication.processEvents()
            time.sleep(0.05)        
        
        # print("data collected of the new project")
        project_attributes=ui_newproject.project_attributes
        # print(project_attributes)
        if len(project_attributes)>0:
            self.Pr_list.append(KCbckend.Project(project_attributes[0],project_attributes[1],project_attributes[2]))
            self.populate_projecttable()

        
    def open_project(self):
        
        try:
            self.ind_pr_selected=int(self.Table_Project_list.selectedItems()[0].text())
            #print(f"this is the selected: {p_selected}")
        except:
            msgbox.Message_popup("Error","No project","Please select a Project")
        else:
            ui_openproject=gui_openproject.Ui_MainWindow(self.Pr_list,self.ind_pr_selected)
            ui_openproject.setupUi() #introduces the selected project into the ui_open project to open the respective project
            ui_openproject.show()
    
            while ui_openproject.finish_window==False:# and ui_openproject.isVisible()==True:
                QtCore.QCoreApplication.processEvents()
                time.sleep(0.05)    

            if ui_openproject.finish_window==True:
                print("window OpenProject is closed")
                
            self.populate_projecttable()
            




    def load_allprojects(self):
        # print("{}  {}".format(KCbckend.Project.filepath,KCbckend.Project.filename))
        
        try:
            self.Pr_list=[]
            # self.Pr_list=backup_projects.load_pr(KCbckend.Project.filepath,KCbckend.Project.filename)
            with open("{}\{}.pkl".format(KCbckend.Project.filepath,KCbckend.Project.filename),"rb") as f:
                self.Pr_list=pickle.load(f)            
        except:
            msgbox.Message_popup("Error","Load File error","Something Ocurred when loading the file")
            yesorno=msgbox.Message_popup("YesorNo","Load Test Projects","Do you want to create a test project list?")
            if yesorno.response=="Yes":
                self.Pr_list=create_test()
                msgbox.Message_popup("Info","Load Test List","Test List Succesfully Created")
            else:
                self.Pr_list=[]
            
        else:
            msgbox.Message_popup("Info","Load Project","Projects succesfully loaded")
            
    def view_data(self):
        try:
            self.ind_pr_selected=int(self.Table_Project_list.selectedItems()[0].text())
        except:
            msgbox.Message_popup("Warning","No project Selected","Please select one Project")
        else:
            project_selected=self.Pr_list[self.ind_pr_selected]
            if project_selected.date_ini!="ND":
                time_db=project_selected.get_time_db_global("overview",project_selected.date_ini,project_selected.date_end)
                
                ui_viewdata=gui_viewdata.Ui_MainWindow(time_db,project_selected.get_dbnames())
                ui_viewdata.setupUi()
                ui_viewdata.show()
        
                while ui_viewdata.finish_window==False:
                    QtCore.QCoreApplication.processEvents()
                    time.sleep(0.05)          
            else:
                msgbox.Message_popup("Warning","Project has no date","The Project has no uploaded data to get the timespan")
        
    def cancel_window(self):
        with open("{}\{}.pkl".format(KCbckend.Project.filepath,KCbckend.Project.filename),"wb") as f:
            pickle.dump(self.Pr_list,f) 
        print("Projects Saved (Main)")
        # backup_projects.save_pr(self.Pr_list,KCbckend.Project.filepath,KCbckend.Project.filename)
        self.finish_window=True
        self.close()


def randomclasses(a,b):
    global seed
    seed+=1
    random.seed(17*seed)
    return random.randint(a,b)

seed=25

def create_test():

    
    Pr_t=[]
    N_P=randomclasses(1,5)
    #P=list(range(N_P))
    for p in range(0,N_P):
        Pr_t.append(KCbckend.Project(f"Proj{p}",f"this is project {p}",f"resp{p}"))
        for s in range(0,randomclasses(1,5)):
            Pr_t[p].add_Season(f"Ses_p{p}_s{s}",f"this is season p{p}_s{s}. In this season many techniques were applied, also the temperature was controlled and many parameters were varied")
            for e in range(0,randomclasses(1,5)):
                d_0="2020-10-{} 10:00:00".format(randomclasses(1,10))
                d_1="2020-10-{} 12:00:00".format(randomclasses(15,30))
                descrp=["added some moisture with alakali, the temperature was controlled during all the process and many variables were taken into account",
                        "the bed was with iron, and it was neessary to verify potential leakages"]
                fuel=["Polyethylene","Textiles","PVC"]
                ind=random.randint(0,1)
                ind2=randomclasses(0,len(fuel)-1)
                Pr_t[p].seasons[s].add_Experiment(f"exp{e}",d_0,d_1,fuel[ind2],"silica sand",descrp[ind])
                for pnt in range(0,randomclasses(0,5)):
                    # print(f"p{p},s{s},e{e}")
                    d_0="2020-10-11 {}:00:00".format(randomclasses(6,12))
                    d_1="2020-10-15 {}:00:00".format(randomclasses(13,18))
                    Pr_t[p].seasons[s].experiments[e].add_Point(f"Point{pnt}",d_0,d_1,f"this is the point {pnt}")     
    
    Pr_t[0].seasons[0].add_Experiment("Exp 1","2019-02-01 08:00:00","2019-02-01 17:00:00","Polyethylene","Olevine","this is a test experiment") #if the date is in HH:MM add the == for the seconds
    # Pr_t[0].seasons[0].experiments[-1].add_data("SCADA","190201 trend.XLS","00:00:00","This is first SCADA")
    # Pr_t[0].seasons[0].experiments[-1].add_data("GC1","190201_mGC.xlsx","00:03:00","This is first GC1")
    # Pr_t[0].seasons[0].experiments[-1].add_data("SPA","430_190201_G_190201.xls","00:03:00","This is first SPA")
    # Pr_t[0].seasons[0].experiments[-1].add_Point("Point 1A","2019-02-01 11:55:00","2019-02-01 12:27:00","this was the point 1 and we used gas bags")
    # # In[1]:
    # #set_point_data(self,point_route,data_type,time_type,date_ini,date_end,delay,db_experiment)
    # #pnt_route=Pr_t[0].project_name+"/"+P[0].seasons[0].season_name+"/"+Pr[0].seasons[0].experiments[0].exp_name+"/"+P[0].seasons[0].experiments[0].points[0].point_name
    # db_exp=Pr_t[0].seasons[0].experiments[-1].data_experiment
    # Pr_t[0].seasons[0].experiments[-1].points[-1].link_point_data(["SCADA","GC1","INFERNO","SPA"],"SCADA","2019-02-01 11:55:00","2019-02-01 12:27:00",3,db_exp)
    return Pr_t
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui_Mother = Ui_MainWindow()
    ui_Mother.setupUi()
    ui_Mother.show()
    sys.exit(app.exec_())

#ui_Mother=Ui_MainWindow()
#ui_Mother.setupUi()
#ui_Mother.show()