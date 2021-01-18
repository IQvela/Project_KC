


from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
#from . import GUI_MessageBoxKC as msgbox
#from . import GUI_NewSeason as gui_newseason
import random
import time
import GUIs.GUI_NewSeason as gui_newseason
import GUIs.GUI_MessageBoxKC as msgbox
import Classes_Backend as KCbckend

class Ui_MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self,project_selected,default_attributes="",index_season_selected="ND"):
        super(Ui_MainWindow,self).__init__()
        self.finish_window=False
        self.project_selected=self.project_selected
        self.index_season_selected=index_season_selected
        
        self.default_attributes=default_attributes #attributes to be written in the different text box by default (when the windows shows up)
        self.exp_attributes=0


    def closeEvent(self, event):
        self.finish_window=True
        self.close()
        
    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(600, 550)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(170, 20, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.Title.setFont(font)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")           
        
        self.label_season = QtWidgets.QLabel(self.centralwidget)
        self.label_season.setGeometry(QtCore.QRect(30, 100, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_season.setFont(font)
        self.label_season.setObjectName("label_season")
        
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(30, 145, 111, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_season")     

        self.label_DateStart = QtWidgets.QLabel(self.centralwidget)
        self.label_DateStart.setGeometry(QtCore.QRect(30, 240, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_DateStart.setFont(font)
        self.label_DateStart.setObjectName("label_DateStart")
        
        self.label_DateEnd = QtWidgets.QLabel(self.centralwidget)
        self.label_DateEnd.setGeometry(QtCore.QRect(30, 280, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_DateEnd.setFont(font)
        self.label_DateEnd.setObjectName("label_DateEnd")
        
        self.label_fuel = QtWidgets.QLabel(self.centralwidget)
        self.label_fuel.setGeometry(QtCore.QRect(30, 380, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_fuel.setFont(font)
        self.label_fuel.setObjectName("label_fuel")
        
        self.label_bed = QtWidgets.QLabel(self.centralwidget)
        self.label_bed.setGeometry(QtCore.QRect(30, 335, 70, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_bed.setFont(font)
        self.label_bed.setObjectName("label_fuel")        

        self.label_date = QtWidgets.QLabel(self.centralwidget)
        self.label_date.setGeometry(QtCore.QRect(130, 200, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_date.setFont(font)
        self.label_date.setObjectName("label_date")
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(320, 200, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_time.setFont(font)
        self.label_time.setObjectName("label_time")

        self.label_comments = QtWidgets.QLabel(self.centralwidget)
        self.label_comments.setGeometry(QtCore.QRect(30, 430, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_comments.setFont(font)
        self.label_comments.setObjectName("label_comments")

        
        #Buttons-------------------------------------------------------------------------------------------
        self.Button_NewSeason = QtWidgets.QPushButton(self.centralwidget)
        self.Button_NewSeason.setGeometry(QtCore.QRect(310, 90, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Button_NewSeason.setFont(font)
        self.Button_NewSeason.clicked.connect(self.new_season)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.Button_AddExperiment = QtWidgets.QPushButton(self.centralwidget)
        self.Button_AddExperiment.setGeometry(QtCore.QRect(460, 380, 100, 40))
        self.Button_AddExperiment.setFont(font)
        self.Button_AddExperiment.clicked.connect(self.create_experiment)

        self.Button_Cancel = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Cancel.setGeometry(QtCore.QRect(460, 440, 100, 40))
        self.Button_Cancel.setFont(font)
        self.Button_Cancel.clicked.connect(self.cancel_window)

        #Text Boxes-----------------------------------------------------------------------------------------
        self.text_name = QtWidgets.QTextEdit(self.centralwidget)
        self.text_name.setGeometry(QtCore.QRect(130, 140, 290, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_name.setFont(font)

        
        self.text_fuel = QtWidgets.QTextEdit(self.centralwidget)
        self.text_fuel.setGeometry(QtCore.QRect(130, 370, 290, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_fuel.setFont(font)
        self.text_fuel.setObjectName("text_fuel")
        
        self.text_bed = QtWidgets.QTextEdit(self.centralwidget)
        self.text_bed.setGeometry(QtCore.QRect(130, 330, 290, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_bed.setFont(font)
        self.text_bed.setObjectName("text_fuel")        
        
        self.text_comments = QtWidgets.QTextEdit(self.centralwidget)
        self.text_comments.setGeometry(QtCore.QRect(130, 410, 290, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_comments.setFont(font)
        self.text_comments.setObjectName("text_comments")


        self.text_DateStart = QtWidgets.QTextEdit(self.centralwidget)
        self.text_DateStart.setGeometry(QtCore.QRect(130, 230, 150, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.text_DateStart.setFont(font)
        self.text_DateStart.setObjectName("text_DateStart")
        self.text_DateEnd = QtWidgets.QTextEdit(self.centralwidget)
        self.text_DateEnd.setGeometry(QtCore.QRect(130, 280, 150, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.text_DateEnd.setFont(font)
        self.text_DateEnd.setObjectName("text_DateEnd")
        
        self.text_TimeStart = QtWidgets.QTextEdit(self.centralwidget)
        self.text_TimeStart.setGeometry(QtCore.QRect(320, 230, 100, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.text_TimeStart.setFont(font)
        self.text_TimeStart.setObjectName("text_TimeStart")
        self.text_TimeEnd = QtWidgets.QTextEdit(self.centralwidget)
        self.text_TimeEnd.setGeometry(QtCore.QRect(320, 280, 100, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.text_TimeEnd.setFont(font)
        self.text_TimeEnd.setObjectName("text_TimeEnd")

        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 759, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        #Dropdownlist---------------------------------------------------------------------------------------
        self.comboBox_seasons=QtWidgets.QComboBox(self.centralwidget)
        if len(self.project_selected.seasons)>0:
            for i in range(len(self.project_selected.seasons)):
                self.comboBox_seasons.addItem("")
        self.comboBox_seasons.setGeometry(QtCore.QRect(130, 90, 170, 30))
        self.comboBox_seasons.setFont(font)
        self.comboBox_seasons.currentIndexChanged.connect(self.get_info) #connects with the get_index function when an item in the list is selected


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "ADD NEW EXPERIMENT"))
        self.label_season.setText(_translate("MainWindow", "Season"))

        self.Title.setText(_translate("MainWindow", "ADD NEW EXPERIMENT"))
        
        self.label_comments.setText(_translate("MainWindow", "Comments"))
        self.label_name.setText(_translate("MainWindow", "Exp. Name"))
        self.label_DateStart.setText(_translate("MainWindow", "Date start"))        
        self.label_DateEnd.setText(_translate("MainWindow", "Date end"))
        self.label_fuel.setText(_translate("MainWindow", "Fuel"))
        self.label_bed.setText(_translate("MainWindow", "Bed Type"))
        self.label_date.setText(_translate("MainWindow", "Date (YYYY-MM-DD)"))
        self.label_time.setText(_translate("MainWindow", "TIME (HH:MM)"))

        self.Button_NewSeason.setText(_translate("MainWindow", "New Season"))
        self.Button_AddExperiment.setText(_translate("MainWindow", "CREATE"))        
        self.Button_Cancel.setText(_translate("MainWindow", "CANCEL"))

        
        if len(self.project_selected.seasons)>0:
            for s_i,s in enumerate(self.project_selected.seasons):
                self.comboBox_seasons.setItemText(s_i, _translate("MainWindow", s.season_name))
                
        if self.index_season_selected!="ND":
            self.index_season_selected=int(self.index_season_selected)
            self.comboBox_seasons.setCurrentIndex(int(self.index_season_selected))        
            self.write_default_attrib(self.index_season_selected)
        else:
            self.index_season_selected=int(self.comboBox_seasons.currentIndex())
    
    #writes the default attributes into the text boxes
    def write_default_attrib(self,ind_season):
        _translate = QtCore.QCoreApplication.translate
        print("default_attributes =",self.default_attributes)
        if self.default_attributes=="":
            name="Experiment {}".format(len(self.project_selected.seasons[ind_season].experiments)+1)
            d_ini="2021-01-22 10:00:00"
            d_end="2021-01-22 12:00:00"
            fuel="Polyethylene"
            bed="Silica Sand"
            comments="This is {}".format(name)
            self.default_attributes=(name,d_ini,d_end,fuel,bed,comments)
        # print("default_attributes ",self.default_attributes)
        self.text_name.setPlaceholderText(_translate("MainWindow", self.default_attributes[0]))
        # print("the text is:{}".format(self.text_name.toPlainText()))
        self.text_DateStart.setPlaceholderText(_translate("MainWindow", self.default_attributes[1].split(" ")[0]))
        self.text_TimeStart.setPlaceholderText(_translate("MainWindow", self.default_attributes[1].split(" ")[1]))
        self.text_DateEnd.setPlaceholderText(_translate("MainWindow", self.default_attributes[2].split(" ")[0]))
        self.text_TimeEnd.setPlaceholderText(_translate("MainWindow", self.default_attributes[2].split(" ")[1]))
        self.text_fuel.setPlaceholderText(_translate("MainWindow", self.default_attributes[3]))
        self.text_bed.setPlaceholderText(_translate("MainWindow", self.default_attributes[4]))
        self.text_comments.setPlaceholderText(_translate("MainWindow", self.default_attributes[5]))

    #creates a new season
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
            self.comboBox_seasons.addItem("")
            self.comboBox_seasons.setItemText(len(self.project_selected.seasons)-1, self.project_selected.seasons[-1].season_name)
            self.comboBox_seasons.setCurrentIndex(len(self.project_selected.seasons)-1)
            self.write_default_attrib(len(self.project_selected.seasons)-1)
        else:
            msgbox.Message_popup("Error","Season Error","Season cannot be created because neither the season name nor its description was given, please check!")
        

    #creates new experiment
    def create_experiment(self):
        print("creating experiment")
        text_boxes=[self.text_name,self.text_DateStart,self.text_TimeStart,self.text_DateEnd,self.text_TimeEnd,self.text_fuel,self.text_bed,self.text_comments]
        for tx in text_boxes:
            if tx.toPlainText()=="":
                tx.setText(tx.placeholderText())
        #time.sleep(5)
        if self.text_TimeStart.toPlainText()=="" or self.text_TimeEnd.toPlainText()=="":
            #print("No text was written")
            msgbox.Message_popup("Error","No Text","No time was given in one of the respective boxes")
        elif self.text_DateStart.toPlainText()=="" or self.text_DateEnd.toPlainText()=="":
            msgbox.Message_popup("Error","No Text","No date was given in one of the respective boxes")
        elif self.text_name.toPlainText()=="" or self.text_bed.toPlainText()=="" or self.text_fuel.toPlainText()=="" or self.text_comments.toPlainText()=="":
            msgbox.Message_popup("Error","No Text","One text box is empty, please make sure all the boxes have their respective info")
        else:
            d_ini=self.text_DateStart.toPlainText()+" "+self.text_TimeStart.toPlainText()
            d_end=self.text_DateEnd.toPlainText()+" "+self.text_TimeEnd.toPlainText()   
            if len(self.text_TimeStart.toPlainText().split(":"))==2:
                d_ini+=":00"
            elif len(self.text_TimeEnd.toPlainText().split(":"))==2:
                d_ini+=":00"
            try:
                d_ini=datetime.strptime(d_ini,"%Y-%m-%d %H:%M:%S")
                d_end=datetime.strptime(d_end,"%Y-%m-%d %H:%M:%S")                
            except:
                msgbox.Message_popup("Error","No Text","the date or time has not the right format. Please check: Date: YYYY-MM-DD, time:HH:MM:SS")
            else:
                d_ini=d_ini.strftime("%Y-%m-%d %H:%M:%S")
                d_end=d_end.strftime("%Y-%m-%d %H:%M:%S")
                self.index_season_selected=self.comboBox_seasons.currentIndex()
                self.exp_attributes=(self.text_name.toPlainText(),d_ini,d_end, 
                                         self.text_fuel.toPlainText(),self.text_bed.toPlainText(),self.text_comments.toPlainText()) #add more and order desired
            print("the text was read")
            self.cancel_window()
        # return print(self.exp_attributes)
      
    def get_info(self):
        #print(type(self.comboBox_seasons.currentIndex()))
        # print("combo box changed",self.comboBox_seasons.currentIndex())
        if self.default_attributes!="":
            text_boxes=[self.text_name,self.text_DateStart,self.text_TimeStart,self.text_DateEnd,self.text_TimeEnd,self.text_fuel,self.text_bed,self.text_comments]
            a=0
            for tx in text_boxes:
                if tx.toPlainText()=="":
                    a+=1
            if a==len(text_boxes):
                self.default_attributes=""
        self.write_default_attrib(self.comboBox_seasons.currentIndex())
        
    
    def cancel_window(self):
        self.finish_window=True
        self.close()

def randomclasses(a,b):
    global seed
    seed+=1
    random.seed(17*seed)
    return random.randint(a,b)

seed=25

Pr=[]
N_P=randomclasses(1,5)
#P=list(range(N_P))
for p in range(0,N_P):
    Pr.append(KCbckend.Project(f"Proj{p}",f"this is project {p}",f"resp{p}"))
    for s in range(0,randomclasses(1,5)):
        Pr[p].add_Season(f"Ses_p{p}_s{s}",f"this is season p{p}_s{s}. In this season many techniques were applied, also the temperature was controlled and many parameters were varied")
        for e in range(0,randomclasses(1,5)):
            d_0="2020-10-{} 10:00:00".format(randomclasses(1,10))
            d_1="2020-10-{} 12:00:00".format(randomclasses(15,30))
            descrp=["added some moisture with alakali, the temperature was controlled during all the process and many variables were taken into account",
                    "the bed was with iron, and it was neessary to verify potential leakages"]
            fuel=["Polyethylene","Textiles","PVC"]
            ind=random.randint(0,1)
            ind2=randomclasses(0,len(fuel)-1)
            Pr[p].seasons[s].add_Experiment(f"exp{e}",d_0,d_1,fuel[ind2],"silica sand",descrp[ind])
            for pnt in range(0,randomclasses(0,5)):
                # print(f"p{p},s{s},e{e}")
                Pr[p].seasons[s].experiments[e].add_Point(f"Point{pnt}",f"this is the point {pnt}")   


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    ui = Ui_MainWindow()
#    ui.setupUi()
#    ui.MainWindow.show()
#    sys.exit(app.exec_())

ui = Ui_MainWindow(Pr[1],"",1)
ui.setupUi()
ui.show()