###
#Importing data from excel
###
import sys
import numpy as np
import pandas as pd 
import tkinter as tk
import random
from datetime import datetime,timedelta
import time

from PyQt5 import QtCore,QtGui,QtWidgets

import GUIs.GUI_SPA as guiSPA

# #Function which defines the filename #this should come from a explorer window to select the file
#later the file must to be saved in the backup folder
def define_file(dataname):

     if dataname=="SCADA":
         filename="190201 trend.XLS"

     elif dataname=="GC1":
         filename="190201_mGC.xlsx"#"C:/Users/rforero/Documents/GitHub/Project_KC/190201_mGC.xlsx"
     
     elif dataname=="SPA":
         filename="430_190201_G_190123.xls"#"C:/Users/rforero/Documents/GitHub/Project_KC/190201_mGC.xlsx"
         
     return filename
 
    
# In[1]:
# #we need to create the collect_data function

# dsource="GC"
# ExcelTable = pd.read_excel(define_file(dsource))

# t0,t1=0,0
# if dsource=="GC":
#     columns_list=["Acquisition Date & Time","Quantity/He","Quantity/H2","Quantity/O2"]#,"Quantity/N2","Quantity/CH4"]
#     t0="12:00"
#     t1="13:00"

# ExcelTable["Acquisition Date & Time"]=pd.to_datetime(ExcelTable["Acquisition Date & Time"])

# d_t0=ExcelTable["Acquisition Date & Time"].dt.strftime("%H:%M")>t0
# d_t1=ExcelTable["Acquisition Date & Time"].dt.strftime("%H:%M")<t1
# Table_timeslot=ExcelTable[d_t0 & d_t1]

# Table_timeslot=Table_timeslot[columns_list]

# print(Table_timeslot)


class timeinterval: #this is the most elemental and general class
    
    #dataKC={}
    def __init__(self,date_ini,date_end):
        self.date_ini=date_ini #the format should be YYYY-MM-DD HH:MM:SS
        self.date_end=date_end

  
#    def get_experiment(self): #this method must to be overrriden with another that be defined in the Experiment class
#        return "no associated experiment"
        
        

        

class Point:

    #the time_db directory (that later will become in a pandas dataframe) corresponds with the main database that compiles all the data
    #it is practically the concept table. The first column is the time, then the route, the scada data, gc, etc..
    #each row corresponds with a minute
    
    time_db_fields=["DATE","POINT_ROUTE","SCADA","GC1","INFERNO","SPA"] #fields (or columns) of the database time_db
    time_db_global=pd.DataFrame(columns=time_db_fields)
    
    def __init__(self,point_name,point_comments,point_route):
        #self.date_ini=date_ini
        #self.date_end=date_end
        self.point_name=point_name
        self.point_comments=point_comments
        self.data_added={}
        self.point_route=point_route #String which contains the indexes of the Project/Season/Experiment/Point
    
    def get_point_route(self):
        pn=enumerate()
    
    def set_point_data(self,data_type,time_type,date_ini,date_end,delay,db_experiment):#,name_timecolumn): #delete data_type
        #data_type (str) = type of data to be introduced SCADA,GC1,Inferno,SPA
        #time_type (str)= SCADA or GC
        #date_ini (str) = initial date of the point
        #date_end (str) = end date of the point
        #delay (str) = delay in minutes respect the SCADA time (SCADA -> delay=0 minutes)
        #db_experiment = dictionary with all the data added to the experiment given by the attribute data_experiment of the Experiment class      
        
        #this method defines the attributes of the point created and add the data to the time_db
        
        date_ini=datetime.strptime(date_ini,"%Y-%m-%d %H:%M:%S")
        date_end=datetime.strptime(date_end,"%Y-%m-%d %H:%M:%S")
        delay=float(delay)
        
        self.delay=delay
        self.date_ini=date_ini
        self.date_end=date_end
        #self.point_route=point_route#it is a string with the indexes of Project/Season/experiment/point 
        
        delay_db={k:0 for k in ["SCADA","GC1","INFERNO","SPA"]}
        if time_type=="GC":#if the time is the time of the GC file then the SCADA must to be read at time-delay from scada file. (however the point date will be always the scada time)           
            delay_db["SCADA"]=-delay #it is negative because the SCADA is the real time
            date_i=self.date_ini-delay #the point date will be always the scada time
            date_e=self.date_end-delay #the point date will be always the scada time
        elif time_type=="SCADA":#if the time is the one of the SCADA file then the GC and inferno must to be read at time+delay             
            delay_db["GC1"]=delay_db["INFERNO"]=delay_db["SPA"]=delay
            date_i=self.date_ini
            date_e=self.date_end
        #minutes0=date_ini.minute
        self.time_db_pnt={fd:[] for fd in Point.time_db_fields} #initializing the directory time_db for the evaluated point (this later will be added to the global time_db directory)
        #time_dp_pnt will be transformed into a pandas dataframe 
        
        #key="DATE" => creates a list of rounded time (floor minute) from date_ini to date_end
        #date_i=self.date_ini
        while date_i<=date_e:
            t_rounded=datetime(date_i.year,date_i.month,date_i.day,date_i.hour,date_i.minute,00)#time floor-rounded to the minute (this is in order to create the point time slot list)
            self.time_db_pnt["DATE"].append(t_rounded)
            self.time_db_pnt["POINT_ROUTE"].append(self.point_route)
            date_i+=timedelta(minutes=1)
        
        
        if data_type=="AUTOMATIC": #the time taken by the point is the SCADA time      
            #collect data from all databases
            Nentries={k:0 for k in Experiment.db_names}
            for k in db_experiment.keys():
                #if k in self.data_point.keys(): #the data from the database k has already added to the point
                #    tk.messagebox.showwarning("Database already added", f"the database {k} has been already added to this point")
                #    continue
                if len(db_experiment[k])==0:
                    #pop up a message saying that the database k is missing
                    guiSPA.Message_popup("Error","Missed Database", f"the database {k} is missing, please add it to the experiment")
                    continue
                if k in ["SCADA","GC1","INFERNO"]: #this must to be taken from a function (to generalize for the case when data_type!=automatic) 
                    d_t0,d_t1=None,None
                    Nentries[k]=0
                    #search which of the list elements added to the db_experiment[k] has the time interval it is being looking for
                    for db in db_experiment[k]: #db_experiment[k] is a dictionary with a list per each key (when more that one SCADA or GC has been added to the experiment)
                        d_t0=db[Experiment.name_timecolumn[k]]>=self.date_ini+timedelta(minutes=delay_db[k]) 
                        d_t1=db[Experiment.name_timecolumn[k]]<=self.date_end+timedelta(minutes=delay_db[k])
                        if all(d_t0==False) and all(d_t1==False): #means that the timeslot defined is not on the evaluated data entry of the experiment (an experiment can have several GC´s or SCADA´s)
                            guiSPA.Message_popup("Warning","time error", 
                                                  f"the times defined are not within the database {k}, please add the data within the timeframe or check the time intervals defined")                                
                            continue                                                    

                        #extracts the row dataframes from the different databases to create self.time_db_pnt[database] 
                        for t_i in self.time_db_pnt["DATE"]:
                            t0=db[Experiment.name_timecolumn[k]]>=t_i+timedelta(minutes=delay_db[k])
                            t1=db[Experiment.name_timecolumn[k]]<=t_i+timedelta(minutes=delay_db[k])+timedelta(seconds=59.999)
                            self.time_db_pnt[k].append(db[t0 & t1]) #in this way each entry in the list will correspond with a time in the row of the pnadas dataframe
                            if len(self.time_db_pnt[k][-1])>0:
                                Nentries[k]+=1
                                               
                elif k=="SPA": 
                    Nentries[k]=0 #number of entries of the database k
                    for t_i in self.time_db_pnt["DATE"]: #goes for all the dates that are stored in time_db_pnt (each date will be at each row of the pandas dataframe)
                        t0=t_i+timedelta(minutes=delay_db[k])
                        t1=t_i+timedelta(minutes=delay_db[k])+timedelta(seconds=59.999)
                        #self.data_point[k]={}
                        fv=0 #number of entries found
                        G_PX0="G_None"
                        #temp=time_db_pnt[k]
                        SPA_samples=[]                        
                        for db in db_experiment[k]: #considering that several SPA files were added in that experiment
                            
                            #When two SPA's are in series both share the same time, therefore two dataframes must to be in the db_experiment["SPA"] dictionary for a specific key (since the key is the time)
                            for t_spa,v_list in db.items():
                                time_SPA=datetime.strptime(t_spa,"%Y-%m-%d %H:%M:%S") #gets the time from the keys of the SPA data (check method get_data_fromfile)
                                if t0<=time_SPA<=t1:                               
                                    SPA_samples.append([[t_spa,v[0],v[1],v[2]] for v in v_list]) #collect the different F/C matrices for the evaluated time 
                                    #each SPA file has its data grouped into certain times, then once the time is found it must to jump to the other SPA file added
                                    
                                    break # maybe not <- the loop must continue because it must allow the case when 2 SPA syringes are used (both are marked at the same hour)                        
                        
                        #at the end, all the list fields should be joined together into just one list (not a list of lists as it is right know (one list for each SPA file))  
                        #guiSPA.Message_popup("Info","SPA Added",f"It has been added {len(SPA_samples)} samples at time t_i={t_i} of the SPA taken at t_spa={t_spa}")
                        self.time_db_pnt[k].append(SPA_samples)                            
                            
                        if len(SPA_samples)>0:
                            Nentries[k]+=1
                        #else:
                            #as the times t_spa are sorted within the db_experiment["SPA"] it must to be found the time t_spa within the interval [t0,t1]
                            #print(f"there is no data within the interval {str(t0)} and {str(t1)}\n in any of the {len(db_experiment[k])} databases added in the experiment.\n Please check the SPA dates")
                            # guiSPA.Message_popup("Error","time error",
                            #                      f"there is no data within the interval {str(t0)} and {str(t1)}\n in any of the {len(db_experiment[k])} databases added in the experiment.\n Please check the SPA dates")

                            #continue                            
                        #else:
                        #    tk.message.showinfo("No SPA Added","No data of SPA was added at time t_i=. Please check the SPA dates")
                
                #Add the log of the database added to show it in the table of the databases added in the Add_point window
                #data_added[k]=[database date_ini,database date_end,delay,Nentries]
                
                self.data_added[k]=[self.date_ini+timedelta(minutes=delay_db[k]),
                                    self.date_end+timedelta(minutes=delay_db[k]),
                                    delay_db[k]+delay*(delay_db["SCADA"]!=0),Nentries[k]] 
        
        for k,v in self.time_db_pnt.items():
            if len(v)==0:
                self.time_db_pnt[k]=["No Data" for i in self.time_db_pnt["DATE"]]
                
        self.update_db_global()
    ############################################################################
    #add the data acquired of the point to the global time_db database
    ############################################################################
    @classmethod
    def update_db_global(cls,self):
        
        cls.time_db_global=cls.time_db_global.append(self.time_db_pnt,ignore_index=True,sort=False) #the time_db_pnt must to be appended to the global data
    
    #def point_attributes(self,times...):
        #takes the maximum and minimum (SCADA) time to define the point that will be shown in the list presented in the experiment window 
        #the kind of db added to the point will be given by the data_point keys  
    
    #def delete_db() #deletes data from the point
    
#this creates the class experiment which is the most basic class (apart from the timeinterval)
#since this class is inheriting from timeinterval then there is no need to declare the getter methods of data_ini and data_end
class Experiment(timeinterval,Point):
    
    db_names=["SCADA","GC1","INFERNO","SPA"]#,"Logging"] #here it is possible to add new methods
    
    name_timecolumn={"SCADA":"TIME",
                     "GC1":"Acquisition Date & Time",
                     "INFERNO":"TIME"} #the name of the time column for each databese
    
    def __init__(self,exp_name,date_ini,date_end,fuel_type,bed_type,exp_comments,exp_route):
        #Experiment_name,Temp_particle_distrib_,... (many attributes to be included maybe this can be done through a pandas or directory read from an excel sheet (check ideas_CLasses.docx))
        #instead it can be a list that be read from the pandas column titles
        timeinterval.__init__(date_ini,date_end)
        self.exp_name=exp_name
        self.fuel_type=fuel_type
        self.exp_comments=exp_comments
        self.bed_type=bed_type
        self.data_experiment={k:[] for k in Experiment.db_names} #results collected from the different databases
        self.points=[] #list with all points
        self.exp_route=exp_route
        
        
    def modify_Exp_attributes(self,date_ini,date_end,fuel_type,exp_comments):
        timeinterval.__init__(date_ini,date_end)
        self.fuel_type=fuel_type
        self.exp_comments=exp_comments        
    
    def add_Point(self,point_name,point_description):
        newpoint_route=self.exp_route+"/"+len(self.points)
        self.points.append(Point.__init__(point_name,point_description,newpoint_route))
    
    #this method will be used to generate the table we create with the different database
    #this method is triggered by a button that directs to other window where the kind of database is chosen
    def add_data(self,data_type,filename):
        #data_type (str) = type of data to be introduced SCADA,GC1,Inferno,SPA
        #filename (str)= this is the route of the file where the information will be extracted out (user defined through a explorer window)
        #dates (list)=it is a list of the initial and final date of the GC file [file start date, file end date] (maybe this is not needed because the pandas can load all dates)

        #The data can be read from a predefined excel sheet format
        #the different data should be stored in a dictionary (with the data_type string as the key)
        #each experiment can have several time intervals (to check)
        
        if data_type=="SCADA":
            self.data_experiment[data_type].append(self.get_data_fromfile(data_type,filename)) #it must to search all the files which are within the dates given (maybe not)
        elif data_type=="GC1" or data_type=="INFERNO": #The time interval of the GC corresponds with the whole time registered in the file 
            self.data_experiment[data_type].append(self.get_data_fromfile(data_type,filename)) #maybe this one 
        elif data_type=="SPA":
            self.data_experiment[data_type].append(self.get_data_fromfile(data_type,filename))
        
        #at the end the data_experiment must to be rearranged as a function of time (the key must to be the time and the values the different databases at that time)
        #this is in order to build the "concept" table 
    
    def get_data_fromfile(self,data_type,filename):#, dates=None): #it should be added a list "dates" for the cases where there are several measurement sets (e.g. GC)
        
        if data_type=="SCADA":
            ExcelTable=pd.read_excel(filename,sheet_name="_DATA")
            name_timecolumn="TIME"
            ExcelTable[name_timecolumn]=pd.to_datetime(ExcelTable[name_timecolumn])
            d_t0=ExcelTable[name_timecolumn]>=self.date_ini ## d_t0=ExcelTable["Acquisition Date & Time"].dt.strftime("%H:%M")>t0 (when t0 is in HH:MM format)
            d_t1=ExcelTable[name_timecolumn]<=self.date_end
            Table_timeinterval=ExcelTable[d_t0 & d_t1]
            return Table_timeinterval
        
        elif data_type=="GC1" or data_type=="INFERNO":#this must to be checkd because it could exist several measurements sets within the experiment time  
            ExcelTable=pd.read_excel(filename)
            name_timecolumn="Acquisition Date & Time"
            ExcelTable[name_timecolumn]=pd.to_datetime(ExcelTable[name_timecolumn])
            d_t0=ExcelTable[name_timecolumn]>=self.date_ini #dates[0]  #It must to be read the whole file (this is why it is important tha the experiment dates be wider enough)
            d_t1=ExcelTable[name_timecolumn]<=self.date_end #dates[1]     
            Table_timeinterval=ExcelTable[d_t0 & d_t1]
            return Table_timeinterval

        elif data_type=="SPA":#this must to be checked because it could exist several measurements sets within the experiment time  
            #app=QtWidgets.QApplication(sys.argv)
            spa_win=guiSPA.Ui_MainWindow()
            spa_win.setupUi()
            spa_win.read_file(filename)
            spa_win.MainWindow.show() #displays a window where the different sheets are assigned to the different times when the sample was collected   
            while spa_win.finish_window==False:
                QtCore.QCoreApplication.processEvents()
                time.sleep(0.01)
            try:
                sheets_dates=spa_win.sh_dates
            except:
                guiSPA.Message_popup("Error","Error reading SPA table","The sheets were not read from SPA file")
                #sheets_dates is a dictionary where the key is the time => dict["YYY-MM-DD HH:MM:SS"]. the keys must be sorted by the time
                #the value is a list. list[0]=GPX, list[1]=FR/CR, list[2]=sheet_name of R. (R is the repetition of the GC, X is the spa sample number, P is the point) 
            else: #read the excel tables from the respective files
                print("done with the SPA file!")
                Table_timeinterval={}
                for tm,v_list in sheets_dates.items():                    
                    #print("V[2]={}".format(v1[2]))
                    Table_timeinterval[tm]=[[v[0],v[1],pd.read_excel(filename,sheet_name=v[2])] for v in v_list]
                print("SPA directory created")
                #     #sys.exit(app.exec_())
                return Table_timeinterval 
    
    
class Season(Experiment):
    def __init__(self,season_name,season_description,season_route):
        self.season_name=season_name
        self.season_description=season_description #this cannot be empty (a message should appear)
        self.experiments=[]
        self.season_route=season_route
        
 
    def add_Experiment(self,exp_name,date_ini,date_end,fuel_type,bed_type,exp_comments=""):
        #shows a window were the arguments date_ini, date_end, fuel_type and commments will be collected
        #or maybe the window calls this method instead, once the button ok is pressed after all the required values are filled and 
        #win_new_experiment()
        
        newexp_route=self.season_route+"/"+len(self.experiments)
        new_experiment=super().__init__(exp_name,date_ini,date_end,fuel_type,bed_type,exp_comments,newexp_route)#entry)
        self.experiments.append(new_experiment)
    
    #this method is called after ok is pressed in a window that allows to change the attributes of the season
    #the arguments are read from boxes that after ok is pressed will send the value to the arguments
    def modify_Season_attributes(self,season_name,season_description):
        self.season_name=season_name
        self.season_description=season_description
        
    def delete_Experiment(self,exp_index): #experiment_number is the index of the list of experiments
        #a windows must pop up asking for confimration
        Msgbox=tk.messagebox.askquestion("Delete Experiment",
                                         "Are you sure you want to delete the Experiment(s): {} from season: {}".format(exp_index,self.season_name),
                                         icon="warning")
        if Msgbox=="yes":
            del self.experiments[exp_index]
        else:
            tk.messagebox.showinfo("Delete Experiment", "None experiment will be deleted")

        
    #transfers seasons to other project (to_project is the object to which the seasons will be transferred)
    #season_index_list is the list of seasons that wants to eliminate (taken from a box where the season indexes are separated by comma)
    def transfer_Experiment(self,to_season,Exp_index_list):
        #a windows must pop up asking for confimration
        Exp_index_list.sort()
        Msgbox=tk.messagebox.askquestion("Transfer Experiment",
                                         "Are you sure you want to transfer the Experiment(s):{} from season:{} to season:{}".format(Exp_index_list,self.season_name,to_season.season_name),
                                         icon="warning")
        #seasons_selected=[self.seasons[i] for i in season_index_list]
        
        if Msgbox=="yes": 
            j=0
            for i in Exp_index_list:            
                to_season.experiments.append(self.experiments[i]) #insert the experiment(s) into the other project 
            for i in Exp_index_list:
                del self.experiments[i-j] #deletes the experiment(s) from the actual project
                j+=1
        else:
            tk.messagebox.showinfo("Delete Experiment", "None experiment will be deleted")
            
            
class Project(Season):
    
    Totalnumberprojects=0 #stores the total number of projects
    
    #allprojects=[] #the initial value of this variable should be loaded from a special python .pkl file which contains the objects (projects) with its resepctive attributes
    
    def __init__(self,project_name,project_description,project_responsible):
        
        self.project_name=project_name
        self.project_description=project_description
        self.project_responsible=project_responsible
        self.seasons=[]#this should be a dictionary?? (maybe not because we are saving classes)
        self.project_route=Project.Totalnumberprojects #this corresponds with the project_index
        
        # ui=gui_project
        #self.date_ini=date_ini 
        #self.date_end=date_end
        #self.fuel_type=fuel_type #can this change for the same project and season?
        #self.season=season #can this change for the same project? if it does, this should be worked through a method called addseason}
        #is the fuel_type a sub set of the season? (or the other way around?). If it is then it should be displayed within the window of add_season a button that allows to add_fuel and add_timeinterval
        #actually The fuel_type and timeinterval should be at the same level and within a specific season
        #the season could be a different class with attributes (description, fuel type and time interval (the list of timeintervals must to be on this class instead))
        
        #list of the different timeintervals were the project was running in (should it be a dictionary instead and with the season as the keys?)
        #also the fuel_type can change for the same project and even for the same season
        #self.timeintervals=[]      
        #self.seasons=[] #check how it is done for the employees - managers example
        
        Project.Totalnumberprojects+=1 #updates the total number of projects by on (this can be used to compare with the length of "projects" list)

    
        
    #this method will come after a window is displayed (where all the seasons are shown) and the button "add season" be pressed
    #after that a window should display where the fields: season_name,season_description="", date_ini and date_end must be there to introduce the information 
    #once give click in ok then it should appear in the season list the new season created (rigth now the season is empty)
    #after this there should be a button "add experiment" where the dates (ini,end) and the fuel type is introduced
    #another button, "show experiments", opens a list with the different experiments done on each season
    def add_Season(self,season_name,season_description=""):
        newseason_route=self.project_route+"/"+len(self.seasons)
        new_Season=super()._init(season_name,season_description,newseason_route)
        self.seasons.append(new_Season)
        
    #this method is called after ok is pressed in a window that allows to change the attributes of the Project
    #the arguments are read from boxes that after ok is pressed will send the value to the arguments        
    def modify_Project_attributes(self,project_name,project_description):
        self.project_name=project_name
        self.project_description=project_description        
    

    def delete_Season(self,season_index): #experiment_number is the index of the list of seasons
        #A windows must pop up asking for confirmation
        Msgbox=tk.messagebox.askquestion("Delete Season",
                                         "Are you sure you want to delete the season(s): {} from project: {}".format(season_index,self.project_name),
                                         icon="warning")
        if Msgbox=="yes":                   
            del self.seasons[season_index]
        else:
            tk.messagebox.showinfo("Delete Season", "None season will be deleted")
            

    #transfers seasons to other project (to_project is the object to which the seasons will be transferred)
    #season_index_list is the list of seasons that wants to eliminate (taken from a box where the season indexes are separated by comma)
    def transfer_Season(self,to_project,season_index_list):
        #a windows must pop up asking for confimration
        season_index_list.sort()
        Msgbox=tk.messagebox.askquestion("Transfer Season",
                                         "Are you sure you want to transer the season(s):{} from project:{} to project:{} ".format(season_index_list,self.project_name,to_project.project_name),
                                         icon="warning")
        if Msgbox=="yes":
            #seasons_selected=[self.seasons[i] for i in season_index_list]
            j=0
            for i in season_index_list:            
                to_project.seasons.append(self.seasons[i]) #insert the seasons in the other project 
            for i in season_index_list:
                del self.seasons[i-j] #deletes the seasons from the actual project
                j+=1
        else:
            tk.messagebox.showinfo("Delete Season", "None season will be transfered")


    @classmethod
    def get_numberprojects(cls):
        return cls.Totalnumberprojects

    @classmethod
    def modify_numberprojects(cls,new_number):
        cls.Totalnumberprojects=new_number


# def randomclasses(a,b):
#     global seed
#     seed+=1
#     random.seed(17*seed)
#     return random.randint(a,b)

# seed=10

# Projects_list=[]
# N_P=randomclasses(1,5)
# P=list(range(N_P))
# for p in range(0,N_P):
#     P[p]=Project(f"Proj{p}",f"this is project {p}")
#     for s in range(0,randomclasses(1,5)):
#         P[p].add_Season(f"Ses_p{p}_s{s}",f"this is season p{p}_s{s}")
# #    P1.add_Season("Ses1_2","this is season 1_2") #check that the names are not the same
# #    P1.add_Season("Ses1_3","this is season 1_3")
#         for e in range(0,randomclasses(1,10)):
#             d_0="11:00"#"2020-10-18"
#             d_1="13:00"#"2020-10-20"
#             descrp=["added some moisture","the bed was with iron"]
#             ind=random.randint(0,1)
#             P[p].seasons[s].add_Experiment(d_0,d_1,"Polyethylene",descrp[ind])
#         #P1.seasons[0].add_Experiment("2020-10-21","2020-10-23","Polyethylene","the bed was with iron")  
#     Projects_list.append(P[p])



# In[1]:



# P={}
# P[0]=Project("Proj1","This is the test project 1")
# P[0].add_Season("Season 2020-11","This is the 2020_11 test season")
# P[0].seasons[0].add_Experiment("Exp 1","2019-02-01 08:00:00","2019-02-01 17:00:00","Polyethylene","Olevine","this was the first experiment") #if the date is in HH:MM add the == for the seconds
# P[0].seasons[0].experiments[0].add_data("SCADA","190201 trend.XLS")
# P[0].seasons[0].experiments[0].add_data("GC1","190201_mGC.xlsx")
# P[0].seasons[0].experiments[0].add_data("SPA","430_190201_G_190201.xls")
# P[0].seasons[0].experiments[0].add_Point("Point 1A","this was the point 1 and we used gas bags")
# # In[1]:
# #set_point_data(self,point_route,data_type,time_type,date_ini,date_end,delay,db_experiment)
# pnt_route=P[0].project_name+"/"+P[0].seasons[0].season_name+"/"+P[0].seasons[0].experiments[0].exp_name+"/"+P[0].seasons[0].experiments[0].points[0].point_name
# db_exp=P[0].seasons[0].experiments[0].data_experiment
# P[0].seasons[0].experiments[0].points[0].set_point_data(pnt_route,"AUTOMATIC","SCADA","2019-02-01 11:55:00","2019-02-01 12:27:00",3,db_exp)

#type (ExcelRead)
#print(ExcelRead)
#win_new_experiment()
#print(entry)


    
#db="SCADA"
#P[0].seasons[0].experiments[0].add_results_database(db,define_file(db))

# In[1]:
# k="SCADA"
# date_i=datetime.strptime("2019-02-01 16:55:00","%Y-%m-%d %H:%M:%S")#P[0].seasons[0].experiments[0].points[0].date_ini
# date_e=datetime.strptime("2019-02-01 17:00:00","%Y-%m-%d %H:%M:%S")#P[0].seasons[0].experiments[0].points[0].date_end
# delay_db={i:0 for i in ["SCADA","GC1","INFERNO","SPA"]}
# delay_db["GC1"]=delay_db["INFERNO"]=delay_db["SPA"]=P[0].seasons[0].experiments[0].points[0].delay
# db=db_exp[k][0]
# d_t0=db[Experiment.name_timecolumn[k]]>=date_i+timedelta(minutes=delay_db[k]) 
# d_t1=db[Experiment.name_timecolumn[k]]<=date_e+timedelta(minutes=delay_db[k])
# a=db[d_t0 & d_t1]


