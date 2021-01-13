# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projectWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import time
from PyQt5 import QtCore, QtGui, QtWidgets
# from . import GUI_AddExperiment as gui_addexperiment
# from . import Classes_Backend
from . import GUI_NewSeason as gui_newseason
from . import GUI_NewExperiment as gui_newexperiment
from . import GUI_OpenExperiment as gui_openexperiment
from . import GUI_MessageBoxKC as msgbox

# import GUIs.GUI_NewSeason as gui_newseason
# import GUIs.GUI_NewExperiment as gui_newexperiment
# import GUIs.GUI_OpenExperiment as gui_openexperiment
# import GUIs.GUI_MessageBoxKC as msgbox
# import Classes_Backend as KCbckend
# import random

class Ui_MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self,Pr_list,ind_pr_selected):
        # self.MainWindow=QtWidgets.QMainWindow()
        super(Ui_MainWindow,self).__init__()
        self.finish_window=False
        self.Pr_list=Pr_list
        self.ind_pr_selected=ind_pr_selected
        self.project_selected=self.Pr_list[ind_pr_selected]
    
    def closeEvent(self, event):
        self.finish_window=True
        self.close()
        # print(self.finish_window)
        # print("closing OpenProject window")
        
    def setupUi(self):
        
        self.setObjectName("MainWindow")
        self.resize(900, 550)
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
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        

        #Labels---------------------------------------------------------------------------------
        self.Label_Title = QtWidgets.QLabel(self.centralwidget)
        self.Label_Title.setGeometry(QtCore.QRect(20, 30, 861, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.Label_Title.setFont(font)
        self.Label_Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Title.setObjectName("Title")
        
        self.Label_Description = QtWidgets.QLabel(self.centralwidget)
        self.Label_Description.setGeometry(QtCore.QRect(80, 60, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Label_Description.setFont(font)
        self.Label_Description.setObjectName("label_5")
        
        #TextBoxes---------------------------------------------------------------------------------       
        self.Textbox_Description = QtWidgets.QTextEdit(self.centralwidget)
        self.Textbox_Description.setGeometry(QtCore.QRect(80, 100, 761, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Textbox_Description.setFont(font)  
        
        
        #GroupBox
        self.groupBox_season=QtWidgets.QGroupBox((self.centralwidget))
        self.groupBox_season.setGeometry(QtCore.QRect(710, 240, 120, 85))        
        
        self.groupBox_exp=QtWidgets.QGroupBox((self.centralwidget))
        self.groupBox_exp.setGeometry(QtCore.QRect(710, 335, 120, 100))
        
                
        #Buttons---------------------------------------------------------------------------------
        fontb=QtGui.QFont()
        #fontb.setPointSize(10)
        fontb.setBold(True)
       
        #New Season
        self.Button_NewSeason = QtWidgets.QPushButton(self.centralwidget)
        self.Button_NewSeason.setGeometry(QtCore.QRect(720, 195, 100, 40))
        self.Button_NewSeason.clicked.connect(self.new_season)
        self.Button_NewSeason.setFont(fontb)
        
        #View Info < GroupBox_season
        self.Button_viewinfoseason = QtWidgets.QPushButton(self.groupBox_season)
        self.Button_viewinfoseason.setGeometry(QtCore.QRect(10, 15, 100, 25))
        self.Button_viewinfoseason.clicked.connect(self.view_infoseason)         
        
        #Add experiment < GroupBox_season
        self.Button_NewExperiment = QtWidgets.QPushButton(self.groupBox_season)
        self.Button_NewExperiment.setGeometry(QtCore.QRect(10, 45, 100, 35))
        self.Button_NewExperiment.clicked.connect(self.new_experiment) 

        
        #view data button < GrouoBox Experiment
        self.Button_ViewData = QtWidgets.QPushButton(self.groupBox_exp)
        self.Button_ViewData.setGeometry(QtCore.QRect(10, 15, 100, 40))
        self.Button_ViewData.setObjectName("Button_ViewData")
        self.Button_ViewData.setFont(fontb)
        self.Button_ViewData.clicked.connect(self.open_experiment)

        #Delete Experiment button < GrouoBox Experiment
        self.Button_DeleteExp = QtWidgets.QPushButton(self.groupBox_exp)
        self.Button_DeleteExp.setGeometry(QtCore.QRect(10, 60, 100, 30))
        self.Button_DeleteExp.setObjectName("Button_ModifyData")
        self.Button_DeleteExp.clicked.connect(self.delete_experiment)        
        
        #Analysis
        self.Button_AnalyseData = QtWidgets.QPushButton(self.centralwidget)
        self.Button_AnalyseData.setGeometry(QtCore.QRect(720, 440, 100, 40))
        self.Button_AnalyseData.setObjectName("Button_AnalyseData")
        self.Button_AnalyseData.clicked.connect(self.data_analysis)
        self.Button_AnalyseData.setFont(fontb)
        
        #back button
        self.Button_back = QtWidgets.QPushButton(self.centralwidget)
        self.Button_back.setGeometry(QtCore.QRect(830, 480, 60, 30))
        self.Button_back.clicked.connect(self.back_button)
        

        
        #Treeview---------------------------------------------------------------------------------
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(80, 190, 600, 291))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.treeWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows) #the selection behaviour is by rows 
        # font1=QtGui.QFont()
        # font1.setBold(True)
        # font1.setPointSize(10)
        # font2=QtGui.QFont()
        # font2.setItalic(True)
        # font2.setPointSize(9)        
        for s in self.project_selected.seasons:
            item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget) #creates high hierarchical entry
            # for c in range(7):
            #     item_0.setFont(c,font1)
            for e in s.experiments:
                item_1 = QtWidgets.QTreeWidgetItem(item_0) #sub entry
                for pnt in e.points:
                    item_2 = QtWidgets.QTreeWidgetItem(item_1) #sub-sub-entry
        
        # item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget) #creates high hierarchical entry
        # item_1 = QtWidgets.QTreeWidgetItem(item_0) #sub entry
        # item_2 = QtWidgets.QTreeWidgetItem(item_1) #sub-sub-entry
        # item_2 = QtWidgets.QTreeWidgetItem(item_1) #sub-sub-entry
        # item_1 = QtWidgets.QTreeWidgetItem(item_0) #sub entry
        # item_2 = QtWidgets.QTreeWidgetItem(item_1) #sub-sub-entry
        # item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        # item_1 = QtWidgets.QTreeWidgetItem(item_0)
        # item_2 = QtWidgets.QTreeWidgetItem(item_1)
        # item_2 = QtWidgets.QTreeWidgetItem(item_1)        
        
        #Menus---------------------------------------------------------------------------------
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 26))
        self.menubar.setObjectName("menubar")
        self.menu1 = QtWidgets.QMenu(self.menubar)
        self.menu1.setObjectName("menu1")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(self)
        self.actionOpen.setObjectName("actionOpen")
        self.menu1.addAction(self.actionOpen)
        self.menu1.addSeparator()
        self.menubar.addAction(self.menu1.menuAction())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        # self.project_selected.add_Season("Season 2020-11","This is the 2020_11 test season") #CHECK!!!!
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "OPEN PROJECT"))
        
        self.Button_NewSeason.setText(_translate("MainWindow", "NEW SEASON"))
        self.Button_viewinfoseason.setText(_translate("MainWindow", "VIEW INFO"))
        self.Button_NewExperiment.setText(_translate("MainWindow", "NEW EXPERIMENT"))
        
        self.Button_ViewData.setText(_translate("MainWindow", "VIEW DATA"))
        self.Button_DeleteExp.setText(_translate("MainWindow", "DELETE EXP"))
        self.Button_AnalyseData.setText(_translate("MainWindow", "ANALYZE DATA"))
        
        self.Button_back.setText(_translate("MainWindow", "BACK"))

        self.Label_Description.setText(_translate("MainWindow", "Description"))
        self.menu1.setTitle(_translate("MainWindow", "Project"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        
        self.Label_Title.setText(_translate("MainWindow", "Project: " + self.project_selected.project_name))

        self.Textbox_Description.setText(self.project_selected.project_description)
               
        self.groupBox_season.setTitle(_translate("MainWindow", u"Season", None))
        self.groupBox_exp.setTitle(_translate("MainWindow", u"Experiment", None))

        font_header=QtGui.QFont()
        font_header.setBold(True)
        font_header.setPointSize(11)
        
        tree_titles=["NAME","Date Ini","Date End","Ent.","Fuel Type","Description/Comments","ID",]
        for c in range(len(tree_titles)):
            item=self.treeWidget.headerItem()
            item.setText(c, _translate("MainWindow", tree_titles[c]))
            item.setFont(c, font_header)

  
        self.treeWidget.setColumnWidth(0, 120)
        self.treeWidget.setColumnWidth(1, 200)
        self.treeWidget.setColumnWidth(2, 200)
        self.treeWidget.setColumnWidth(3, 50)
        self.treeWidget.setColumnWidth(4, 100)
        self.treeWidget.setColumnWidth(5, 500)
        self.treeWidget.setColumnWidth(6, 40)
        
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)

        self.populate_tree()

        self.treeWidget.setSortingEnabled(__sortingEnabled)
        
    def populate_tree(self):
        _translate = QtCore.QCoreApplication.translate
        
        ncols=self.treeWidget.columnCount()
        # print(f"number of columns:{ncols}")
        
        # for s in self.project_selected.seasons:
        #     item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget) #creates high hierarchical entry
        #     for e in s.experiments:
        #         item_1 = QtWidgets.QTreeWidgetItem(item_0) #sub entry
        #         for pnt in e.points:
        #             item_2 = QtWidgets.QTreeWidgetItem(item_1) #sub-sub-entry
        
        
        font1=QtGui.QFont()
        font1.setBold(False)
        font1.setPointSize(10)
        # font11=QtGui.QFont() #for column Exp/pnts
        # font11.setBold(False)
        # font11.setPointSize(9)        
        font2=QtGui.QFont()
        font2.setItalic(True)
        font2.setPointSize(9)
        font3=QtGui.QFont()
        #font3.setItalic(True)
        font3.setPointSize(8)  
        
        #max_desc_length=50 #maximum number of caracteres to show in the description
        for s_i,s in enumerate(self.project_selected.seasons):
            col_content=[s.season_name,s.get_dates_total()[0],s.get_dates_total()[1],str(len(s.experiments)),s.get_fuel_total(),s.season_description,str(s_i)]            
            for c in range(ncols):
                item=self.treeWidget.topLevelItem(s_i)
                item.setText(c, _translate("MainWindow", col_content[c]))
                item.setFont(c,font1)

            for e_i,e in enumerate(s.experiments):
                col_content=[e.exp_name,e.date_ini,e.date_end,str(len(e.points)),e.fuel_type,e.exp_comments,str(s_i)+"/"+str(e_i)]                            
                for c in range(ncols):
                    item=self.treeWidget.topLevelItem(s_i).child(e_i)
                    item.setText(c, _translate("MainWindow", col_content[c]))
                    item.setFont(c,font2)                

                for pnt_i,pnt in enumerate(e.points):
                    col_content=[pnt.point_name,pnt.date_ini,pnt.date_end,"-",e.fuel_type,pnt.point_comments,str(s_i)+"/"+str(e_i)+"/"+str(pnt_i)]                            
                    for c in range(ncols):
                        item=self.treeWidget.topLevelItem(s_i).child(e_i).child(pnt_i)
                        item.setText(c, _translate("MainWindow", col_content[c]))
                        item.setFont(c,font3)

                    
        #self.treeWidget.expandToDepth(0) 
        self.treeWidget.resizeColumnToContents(1) #date_ini
        self.treeWidget.resizeColumnToContents(2) #date_end
        self.treeWidget.resizeColumnToContents(4) #fueltype        
    
    #Opens the window to create a new season and add the new season to project selected
    def new_season(self):
        ui_newseason=gui_newseason.Ui_MainWindow()
        ui_newseason.setupUi()
        ui_newseason.show()

        while ui_newseason.finish_window==False:
            QtCore.QCoreApplication.processEvents()
            time.sleep(0.05) 
        if ui_newseason.season_attributes!="":
            # print("N. seasons of project selected:{}".format(len(self.project_selected.seasons)))
            (season_name,season_description)=ui_newseason.season_attributes
            self.project_selected.add_Season(season_name,season_description)
            # print("new season created. N. seasons of project selected:{}".format(len(self.project_selected.seasons)))
            item=QtWidgets.QTreeWidgetItem(self.treeWidget) #creates the high level item in the tree
            #self.treeWidget.addTopLevelItem(item)
            self.populate_tree()
            # print("tree populated!")            
            
        else:
            msgbox.Message_popup("Error","Season Error","Season cannot be created because neither the season name nor its description was given, please check!")

    #Opens the season information window
    def view_infoseason(self):
        pass
        
    #Opens Add Experiment window------------------------------------------------------------------------------------------
    def new_experiment(self):
        ind_season_selected=self.treeWidget.selectedIndexes()[-1].data().split("/")[0]
        n_seasons0=len(self.project_selected.seasons)#total number fo seasons of the selected project
        print(f"season_selected:{ind_season_selected}")
        default_attributes=""
        ui_newexperiment=gui_newexperiment.Ui_MainWindow(self.project_selected,default_attributes,ind_season_selected)
        ui_newexperiment.setupUi()
        ui_newexperiment.show()
        
        while ui_newexperiment.finish_window==False:
            QtCore.QCoreApplication.processEvents()
            time.sleep(0.05)  
        
        print("add experiment window closed")
        ind_season_selected=ui_newexperiment.index_season_selected#int(ind_season_selected)
        #print(ind_season_selected)
        if type(ind_season_selected)==int:
            n_exp0=len(self.project_selected.seasons[ind_season_selected].experiments)
            # print(f"{n_seasons0}, season:{ind_season_selected}, exp:{n_exp0}")
            if ui_newexperiment.exp_attributes!="":            
                (exp_name,d_ini,d_end,fuel_type,bed_type,exp_comments)=ui_newexperiment.exp_attributes
                # print("creating the experiment object. attributes:",ui_newexperiment.exp_attributes)
                self.project_selected.seasons[ind_season_selected].add_Experiment(exp_name,d_ini,d_end,fuel_type,bed_type,exp_comments)
                if len(self.project_selected.seasons)>n_seasons0:
                    item=QtWidgets.QTreeWidgetItem(self.treeWidget)
                if len(self.project_selected.seasons[ind_season_selected].experiments)>n_exp0:
                    item_child=QtWidgets.QTreeWidgetItem(self.treeWidget.topLevelItem(ind_season_selected))
                self.populate_tree()
                print("tree populated")
            else:
                msgbox.Message_popup("Error","Error","The Experiment attributes were not read. Please check and add again the info")    
        
    #Delete experiment---------------------------------------------------------------------------------------------------- 
    def delete_experiment(self): #must to display a message to make sure the user wants to delete the selected experiment
        pass
    
    #Opens window Experiment---------------------------------------------------------------------------------------------
    def open_experiment(self):        
        #exp_selected1=self.treeWidget.selectedItems()
        exp_selected=self.treeWidget.selectedIndexes()[-1].data()
        
        if len(exp_selected.split("/"))<2 or len(exp_selected.split("/"))>3:
            msgbox.Message_popup("Error","Error","Please select an Experiment row")
        else:
            season_selected=int(exp_selected.split("/")[0])
            exp_selected=int(exp_selected.split("/")[1])
                    
        print("opening the open_experiment window")
        ui_openexperiment=gui_openexperiment.Ui_MainWindow(self.Pr_list,[self.ind_pr_selected,season_selected,exp_selected])
        ui_openexperiment.setupUi()
        ui_openexperiment.show()

        #print("window openned")
        while ui_openexperiment.finish_window==False:
            QtCore.QCoreApplication.processEvents()
            time.sleep(0.05)  
            
    #opens the window to analysis of the data------------------------------------------------------------------------------    
    def data_analysis(self):
        pass
    
    #closes the window
    def back_button(self):
        self.finish_window=True
        self.close()
        
# def randomclasses(a,b):
#     global seed
#     seed+=1
#     random.seed(17*seed)
#     return random.randint(a,b)

# seed=25

# Pr=[]
# N_P=randomclasses(1,5)
# #P=list(range(N_P))
# for p in range(0,N_P):
#     Pr.append(KCbckend.Project(f"Proj{p}",f"this is project {p}",f"resp{p}"))
#     for s in range(0,randomclasses(1,5)):
#         Pr[p].add_Season(f"Ses_p{p}_s{s}",f"this is season p{p}_s{s}. In this season many techniques were applied, also the temperature was controlled and many parameters were varied")
#         for e in range(0,randomclasses(1,5)):
#             d_0="2020-10-{} 10:00:00".format(randomclasses(1,10))
#             d_1="2020-10-{} 12:00:00".format(randomclasses(15,30))
#             descrp=["added some moisture with alakali, the temperature was controlled during all the process and many variables were taken into account",
#                     "the bed was with iron, and it was neessary to verify potential leakages"]
#             fuel=["Polyethylene","Textiles","PVC"]
#             ind=random.randint(0,1)
#             ind2=randomclasses(0,len(fuel)-1)
#             Pr[p].seasons[s].add_Experiment(f"exp{e}",d_0,d_1,fuel[ind2],"silica sand",descrp[ind])
#             for pnt in range(0,randomclasses(0,5)):
#                 # print(f"p{p},s{s},e{e}")
#                 Pr[p].seasons[s].experiments[e].add_Point(f"Point{pnt}",f"this is the point {pnt}")    



        
        
# # if __name__ == "__main__":
# #     import sys
# #     app = QtWidgets.QApplication(sys.argv)
# #     ui = Ui_MainWindow()
# #     ui.setupUi(Pr[1])
# #     ui.show()
# #     sys.exit(app.exec_())


# ui=Ui_MainWindow()
# ui.setupUi(Pr[1])

# ui.show()