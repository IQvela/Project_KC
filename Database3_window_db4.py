###
#Importing data from excel
###

import numpy as np
import pandas as pd 
import tkinter as tk
import random
from datetime import datetime,timedelta
import time

from PyQt5 import QtCore

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
        
        
    def get_data_fromfile(self,data_type,filename, dates=None): #it should be added a list "dates" for the cases where there are several measurement sets (e.g. GC)
        
        if data_type=="SCADA":
            ExcelTable=pd.read_excel(filename,sheet_name="_DATA")
            name_timecolumn="TIME"
            ExcelTable[name_timecolumn]=pd.to_datetime(ExcelTable[name_timecolumn])
            d_t0=ExcelTable[name_timecolumn]>=self.date_ini ## d_t0=ExcelTable["Acquisition Date & Time"].dt.strftime("%H:%M")>t0 (when t0 is in HH:MM format)
            d_t1=ExcelTable[name_timecolumn]<=self.date_end
            Table_timeinterval=ExcelTable[d_t0 & d_t1]
        
        elif data_type=="GC1" or data_type=="INFERNO":#this must to be checkd because it could exist several measurements sets within the experiment time  
            ExcelTable=pd.read_excel(filename)
            name_timecolumn="Acquisition Date & Time"
            ExcelTable[name_timecolumn]=pd.to_datetime(ExcelTable[name_timecolumn])
            d_t0=ExcelTable[name_timecolumn]>=dates[0]
            d_t1=ExcelTable[name_timecolumn]<=dates[1]     
            Table_timeinterval=ExcelTable[d_t0 & d_t1]

        elif data_type=="SPA":#this must to be checked because it could exist several measurements sets within the experiment time  
            spa_win=guiSPA.Ui_MainWindow()
            spa_win.get_sheets(filename)
            spa_win.MainWindow.show() #displays a window where the different sheets are assigned to the different times when the sample was collected   
            while spa_win.finish_window==False:
                QtCore.QCoreApplication.processEvents()
                time.sleep(0.01)
            try:
                sheets_dates=spa_win.sh_dates
            except:
                guiSPA.Message_popup("Error","Error reading SPA table","The sheets were not read from SPA file")
                #sheets_dates is a dictionary where the key is the time => dict["YYY-MM-DD HH:MM:SS"]. the kays must be sorted by the time
                #the value is a list. list[0]=GPX, list[1]=FR/CR, list[2]=sheet_name of R. (R is the repetition of the GC, X is the spa sample number, P is the point) 
            else:
                for tm,v in sheets_dates.items():
                    Table_timeinterval={tm:[v[0],v[1],pd.read_excel(filename,sheet_name=v[2])]}
            
        return Table_timeinterval 
        

class Point:

    time_db_fields=["DATE","POINT_ROUTE","SCADA","GC1","INFERNO","SPA"] #fileds (or columns) of the database time_db
    def __init__(self,point_comments):
        #self.date_ini=date_ini
        #self.date_end=date_end
        self.point_comments=point_comments
        self.data_added={}

    def add_data(self,point_route,data_type,time_type,date_ini,date_end,delay,db_experiment,name_timecolumn):
        #data_type (str) = type of data to be introduced SCADA,GC1,Inferno,SPA
        #time_type (str)= SCADA or GC
        #date_ini (str) = initial date of the point
        #date_end (str) = end date of the point
        #delay (str) = delay in minutes respect the SCADA time (SCADA -> delay=0 minutes)
        #db_experiment = dictionary with all the data added to the experiment        
        
        #this method defines the attributes of the point created and add the data to the time_db
        
        date_ini=datetime.strptime(date_ini,"%Y-%m-%d %H:%M:%S")
        date_end=datetime.strptime(date_end,"%Y-%m-%d %H:%M:%S")
        delay=float(delay)
        
        self.delay=delay
        self.date_ini=date_ini
        self.date_end=date_end
        self.point_route=point_route#it is a string with Project:project_name/Season:season_name/experiment_#/point_# 
        
        delay_db={k:0 for k in ["SCADA","GC1","INFERNO","SPA"]}
        if time_type=="GC":#if the time is the time of the GC file then the SCADA must to be read at time-delay from file           
            delay_db["SCADA"]=-delay
            date_i=self.date_ini-delay
            date_e=self.date_end-delay
        elif time_type=="SCADA":#if the time is the one of the SCADA file then the GC and inferno must to be read at time+delay             
            delay_db["GC1"]=delay_db["INFERNO"]=delay_db["SPA"]=delay
            date_i=self.date_ini
            date_e=self.date_end
        #minutes0=date_ini.minute
        time_db_pnt={fd:[] for fd in Point.time_db_fields} #generating the drectory time_db for the evaluated point (this later will be added to the global time_db directory)
        
        #key="DATE" => creates a list of rounded time (floor minute) from date_ini to date_end
        #date_i=self.date_ini
        while date_i<=date_e:
            t_rounded=datetime(date_i.day,date_i.month,datetime.day,date_i.hour,date_i.minute,00)#time floor-rounded to the minute
            time_db_pnt["DATE"].append(t_rounded)
            time_db_pnt["POINT_ROUTE"].append(self.point_route)
            date_i+=datetime.timedelta(minutes=1)
        
        
        if data_type=="AUTOMATIC": #the time taken by the point is the SCADA time      
            #collect data from all databases
            Nentries=0
            for k in db_experiment.keys():
                #if k in self.data_point.keys(): #the data from the database k has already added to the point
                #    tk.messagebox.showwarning("Database already added", f"the database {k} has been already added to this point")
                #    continue
                if len(db_experiment[k])==0:
                    #pop up a message saying that the database k is missing
                    tk.messagebox.showwarning("Missed Database", f"the database {k} is missing, please add it to the experiment")
                    continue
                if k in ["SCADA","GC1","INFERNO"]: #this must to be taken from a function (to generalize for the case when data_type!=automatic) 
                    d_t0,d_t1=None,None
                    #search which of the list elements added to the db_experiment[k] has the time interval it is being looking for
                    for db in db_experiment[k]: #db_experiment[k] is a dictionary with a list per each key (when more that one SCADA or GC has been added to the experiment)
                        d_t0=db[name_timecolumn[k]]>=self.date_ini+timedelta(minutes=delay_db[k]) 
                        d_t1=db[name_timecolumn[k]]<=self.date_end+timedelta(minutes=delay_db[k])
                        if all(d_t0)==False or all(d_t1)==False: #means that the timeslot defined is not on the evaluated data entry of the experiment (an experiment can have several GC´s or SCADA´s)
                            d_t0,d_t1=None,None
                            continue                                                    
                        #data_point=db[d_t0 & d_t1] #search in the list where the timslto is
                        #extracts the row dataframes from the different databases to create time_db_pnt[database] 
                        for t_i in time_db_pnt["DATE"]:
                            t0=db[name_timecolumn[k]]>=t_i+timedelta(minutes=delay_db[k])
                            t1=db[name_timecolumn[k]]<=t_i+timedelta(minutes=delay_db[k])+timedelta(seconds=59.999)
                            time_db_pnt[k].append(db[t0 & t1])
                            Nentries+=1
                                                
                    if d_t0==None or d_t1==None:
                        tk.messagebox.showwarning("time error", 
                                                  f"the times defined are not within the database {k}, please add the data within the timeframe or check the time intervals defined")    
                        continue                                                
                elif k=="SPA":
                    Nentries=0 #number of entries of the database k
                    for t_i in time_db_pnt["DATE"]: #goes for all the dates that are stored in time_db_pnt
                        t0=t_i+timedelta(minutes=delay_db[k])
                        t1=t_i+timedelta(minutes=delay_db[k])+timedelta(seconds=59.999)
                        #self.data_point[k]={}
                        fv=0 #number of entries found
                        G_PX0="G_None"
                        #temp=time_db_pnt[k]
                        FC_samples=[]
                        for t_spa,v in db_experiment[k].items():
                            time_SPA=datetime.strptime(t_spa,"%Y-%m-%d %H:%M:%S") #gets the time from the keys of the SPA data (check method get_data_fromfile)
                            if t0<=time_SPA<=t1:
                                if fv==0:
                                    G_PX0=v[0]
                                G_PX1=v[0]
                                if G_PX1 == G_PX0:                                
                                    FC_samples.append([t_spa,v[0],v[1],v[2]]) #collect the different F/C matrices for the evaluated time 
                                    fv+=1
                                    Nentries+=1
                                else:
                                    tk.messagebox.showwarning("Time error",f"The evaluated point is {G_PX0} but at the time {t_spa} corresponds with {G_PX1}. Please check the dates or the G_labels and try to add again the SPA data for {G_PX0}")
                                    FC_samples=[]
                                    #close the window
                                    break
                                
                            else:
                                #as the times t_spa are sorted within the db_experiment["SPA"] it must to be found the time t_spa within the interval [t0,t1] 
                                tk.messagebox.showwarning("time error",f"the time {t_spa} is not within the interval {str(t0)} and {str(t1)}, please check the SPA dates")
                                FC_samples=[]
                                continue
                        
                        if fv>0:
                            tk.message.showinfo("SPA Added",f"It has been added {fv} samples at time t_i={t_i} of the SPA taken at t_spa={t_spa}")
                            time_db_pnt[k].append(FC_samples)
                        #else:
                        #    tk.message.showinfo("No SPA Added","No data of SPA was added at time t_i=. Please check the SPA dates")
                
                #Add the log of the database added to show it in the table of the databases added in the Add_point window
                #data_added[k]=[database date_ini,database date_end,delay,Nentries]
                self.data_added[k]=[self.date_ini+timedelta(minutes=delay_db[k]),
                                    self.date_end+timedelta(minutes=delay_db[k]),
                                    delay_db[k]+delay*(delay_db["SCADA"]!=0),Nentries] 

    ############################################################################
    #add the data acquired of the point to the global time_db database
    ############################################################################

    #def point_attributes(self,times...):
        #takes the maximum and minimum (SCADA) time to define the point that will be shown in the list presented in the experiment window 
        #the kind of db added to the point will be given by the data_point keys  
    
    #def delete_db() #deletes data from the point
    
#this creates the class experiment which is the most basic class (apart from the timeinterval)
#since this class is inheriting from timeinterval then there is no need to declare the getter methods of data_ini and data_end
class Experiment(timeinterval):
    
    db_names=["SCADA","GC1","INFERNO","SPA"]#,"Logging"] #here it is possible to add new methods
    
    name_timecolumn={"SCADA":"Acquisition Date & Time",
                     "GC1":"TIME",
                     "INFERNO":"TIME"} #the name of the time column for each databese
    
    def __init__(self,date_ini,date_end,fuel_type,bed_type,exp_comments):
        #Experiment_name,Temp_particle_distrib_,... (many attributes to be included maybe this can be done through a pandas or directory read from an excel sheet (check ideas_CLasses.docx))
        #instead it can be a list that be read from the pandas column titles
        super().__init__(date_ini,date_end)
        self.fuel_type=fuel_type
        self.exp_comments=exp_comments
        self.bed_type=bed_type
        self.data_experiment={k:[] for k in Experiment.db_names} #results collected from the different databases
        
        
    def modify_Exp_attributes(self,date_ini,date_end,fuel_type,exp_comments):
        super().__init__(date_ini,date_end)
        self.fuel_type=fuel_type
        self.exp_comments=exp_comments        
    
    #this method will be used to generate the table we create with the different database
    #this method is triggered by a button that directs to other window where the kind of database is chosen
    def add_data(self,data_type,filename,dates=None):
        #data_type (str) = type of data to be introduced SCADA,GC1,Inferno,SPA
        #filename (str)= this is the route of the file where the information will be extracted out (user defined through a explorer window)
        #dates (list)=it is a list of the initial and final date of the GC file [file start date, file end date] (maybe this is not needed because the pandas can load all dates)

        #The data can be read from a predefined excel sheet format
        #the different data should be stored in a dictionary (with the data_type string as the key)
        #each experiment can have several time intervals (to check)
        
        if data_type=="SCADA":
            self.data_experiment[data_type].append(self.get_data_fromfile(data_type,filename)) #it must to search all the files which are within the dates given (maybe not)
        if data_type=="GC1" or data_type=="INFERNO": #The time interval of the GC corresponds with the whole time registered in the file 
            self.data_experiment[data_type].append(self.get_data_fromfile(data_type,filename,dates)) #maybe this one 
        if data_type=="SPA":
            self.data_experiment[data_type].append(self.get_data_fromfile(data_type,filename))
        
        #at the end the data_experiment must to be rearranged as a function of time (the key must to be the time and the itmes the different databases at that time)
        #this is in order to build the "concept" table 
    
class Season:
    def __init__(self,season_name,season_description=""):
        self.season_name=season_name
        self.season_description=season_description #this cannot be empty (a message should appear)
        self.experiments=[]
        
 
    def add_Experiment(self,date_ini,date_end,fuel_type,exp_comments=""):
        #shows a window were the arguments date_ini, date_end, fuel_type and commments will be collected
        #or maybe the window calls this method instead, once the button ok is pressed after all the required values are filled and 
        #win_new_experiment()
        new_experiment=Experiment(date_ini,date_end,fuel_type,exp_comments)#entry)
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
            
            
class Project:
    
    Totalnumberprojects=0 #stores the total number of projects
    
    #allprojects=[] #the initial value of this variable should be loaded from a special python .pkl file which contains the objects (projects) with its resepctive attributes
    
    def __init__(self,project_name,project_description=""):
        
        self.project_name=project_name
        self.project_description=project_description
        self.seasons=[]#this should be a dictionary?? (maybe not because we are saving classes)
        
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
        new_Season=Season(season_name,season_description)
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




def randomclasses(a,b):
    global seed
    seed+=1
    random.seed(17*seed)
    return random.randint(a,b)

seed=10

Projects_list=[]
N_P=randomclasses(1,5)
P=list(range(N_P))
for p in range(0,N_P):
    P[p]=Project(f"Proj{p}",f"this is project {p}")
    for s in range(0,randomclasses(1,5)):
        P[p].add_Season(f"Ses_p{p}_s{s}",f"this is season p{p}_s{s}")
#    P1.add_Season("Ses1_2","this is season 1_2") #check that the names are not the same
#    P1.add_Season("Ses1_3","this is season 1_3")
        for e in range(0,randomclasses(1,10)):
            d_0="11:00"#"2020-10-18"
            d_1="13:00"#"2020-10-20"
            descrp=["added some moisture","the bed was with iron"]
            ind=random.randint(0,1)
            P[p].seasons[s].add_Experiment(d_0,d_1,"Polyethylene",descrp[ind])
        #P1.seasons[0].add_Experiment("2020-10-21","2020-10-23","Polyethylene","the bed was with iron")  
    Projects_list.append(P[p])



window=False
#results=""



def win_new_experiment():
    #global window,entries
    window=tk.Tk()
    window.title("Add new experiment")
    window.geometry("370x300")
    
    rc,cc=0,0
    L_title=tk.Label(window,text="Introduce new Experiment info")
    L_title.grid(row=rc,column=cc+1,sticky="e")
    
    L1=tk.Label(window,text="Date Start",anchor="e")
    L1.grid(row=rc+2,column=cc,sticky="e")

    L1=tk.Label(window,text="Date End",anchor="e")
    L1.grid(row=rc+3,column=cc,sticky="e")
    
    L2=tk.Label(window,text="Date (YYYY-MM-DD)")
    L2.grid(row=rc+1,column=cc+1)
    
    L2=tk.Label(window,text="Time (HH:MM:SS)")
    L2.grid(row=rc+1,column=cc+2)
   
    D1=tk.Entry(window,width=15) #Date Start
    D1.grid(row=rc+2,column=cc+1)
    T1=tk.Entry(window,width=10) #Time Start
    T1.grid(row=rc+2,column=cc+2)    

    D2=tk.Entry(window,width=15) #Date End
    D2.grid(row=rc+3,column=cc+1)
    T2=tk.Entry(window,width=10) #Time End
    T2.grid(row=rc+3,column=cc+2)       
    
    L1=tk.Label(window,text="") #blank row
    L1.grid(row=rc+4,column=cc) 
    
    L1=tk.Label(window,text="Fuel Type")
    L1.grid(row=rc+5,column=cc,sticky="e")    
    Fuel=tk.Entry(window,width=20)
    Fuel.grid(row=rc+5,column=cc+1)
    
    L1=tk.Label(window,text="")#blank row
    L1.grid(row=rc+6,column=cc)  
    
    L1=tk.Label(window,text="Comments")
    L1.grid(row=rc+7,column=cc,sticky="e")    
    Comment=tk.Text(window,height=5,width=30)
    Comment.grid(row=rc+7,column=cc+1,columnspan=2)#padx=1,pady=5)
    
    entries=[D1,T1,D2,T2,Fuel,Comment]
    
    add_button=tk.Button(window,text="Add Experiment",command=lambda: getdatafromboxes(window,entries,"new_experiment"))
    add_button.grid(row=rc+9,column=cc+1)
    
    cancel_button=tk.Button(window,text="Cancel",command=window.destroy)
    cancel_button.grid(row=rc+9,column=cc+2)   
    
    window.mainloop()
    

    
def getdatafromboxes(windw,entry0,wtype=""): #action="collect_data"
    global entry#window,entries#results,D1,T1,D2,T2,Fuel,Comment
    entry=entry0
    if wtype=="new_experiment":
        #window=False
        date_ini=entry[0].get()+" "+entry[1].get()#D1.get()+" "+T1.get()
        date_end=entry[2].get()+" "+entry[3].get()
        fuel_type=entry[4].get()#Fuel.get()
        exp_comments=entry[5].get("1.0",tk.END) #retrieves all the text (from row 1 and letter in position 0 until the end)  
        entry=(date_ini,date_end,fuel_type,exp_comments)
    if wtype=="":
        tk.messagebox.showinfo(title="Caution",text="No wtype defined")
    windw.destroy()
    #window.mainloop()


#type (ExcelRead)
#print(ExcelRead)
#win_new_experiment()
#print(entry)

# In[1]:
    
db="SCADA"
P[0].seasons[0].experiments[0].add_results_database(db,define_file(db))


