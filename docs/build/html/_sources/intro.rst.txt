Back End
============================================

This explain main construction of backend.

The code is object oriented and contain 5 classes interconnected as shown in the figure,
and have the following fuction:

* Project
* Seasson
* Experiment
* Point
* Time_interval

.. figure::  images/Classes.png
   :align:   center

**Summary of the classes**

The following image shows all the classes and its variables and functions:

.. figure::  images/Classes_details.png
   :align:   center

**Class timeinterval**

The class timeinterval only contains the data when something starts and ends, as sowhn below::

	def __init__(self,date_ini,date_end):
        	self.date_ini=date_ini #the format should be YYYY-MM-DD HH:MM:SS
        	self.date_end=date_end

**Class Point**

The class point consist of::

	def __init__(self,point_name,point_comments,point_route):

including: the point name, comments and the point route (String which contains the indexes of the Project/Season/Experiment/Point)

and ::

	def set_point_data(self,collect_data,time_type,date_ini,date_end,delay,db_experiment):
        	#collect_data (str) = type of data to be introduced SCADA,GC1,Inferno,SPA
        	#time_type (str)= SCADA or GC
        	#date_ini (str) = initial date of the point
        	#date_end (str) = end date of the point
        	#delay (str) = delay in minutes respect the SCADA time (SCADA -> delay=0 minutes)
        	#db_experiment = dictionary with all the data added to the experiment given by the attribute data_experiment of the Experiment class    


Also adding the data acquired of the point to the database is needed::
	
	@classmethod
	def update_db_global(cls,pnt):

**Class Experiment**

The class Experiment(timeinterval) consist of::

	def __init__(self,exp_name,date_ini,date_end,fuel_type,bed_type,exp_comments,exp_route):

including: the experiment name, dates, fuel and sand types, comments and the experiment route (String which contains the indexes of the Project/Season/Experiment)

and ::

	def modify_Exp_attributes(self,date_ini,date_end,fuel_type,exp_comments):
	def add_Point(self,point_name,point_description):
	def add_data(self,data_type,filename,delay,comments=""):
	def get_data_fromfile(self,data_type,filename):	
	def get_dates_db(self,db,index):
	#get the maximum and the minimum dates of the files loaded
	def get_dbnames(self): 
	#get the names of the database  

Also adding nother database to the names list is needed::

	@classmethod
	def add_dbtype(cls,new_db):

**Class Season**

The class Season consist of::

	def __init__(self,season_name,season_description,season_route):

including: the season name, description and the route (String which contains the indexes of the Project/Season/)

and ::

	def add_Experiment(self,exp_name,date_ini,date_end,fuel_type,bed_type,exp_comments=""):
	def modify_Season_attributes(self,season_name,season_description):
	def delete_Experiment(self,exp_index):
	def get_dates_total(self): 
	#get the date of the object given the subclasses that are within it
	def get_fuel_total(self):
	#returns if during the season only use one type of fuel (ex. PE) or different fuel: Mix

**Class Project**

The class Project consist of::

	def __init__(self,project_name,project_description,project_responsible):

including: the project name, description, dates, fuel and sand types, seasons, and  route (project_index)

and ::

	def add_Season(self,season_name,season_description=""):	
	def modify_Project_attributes(self,project_name,project_description):
	def delete_Season(self,season_index):
	def transfer_Season(self,to_project,season_index_list):
	def get_dates_total(self): 
	#get the date of the object given the subclasses that are within it
	def get_fuel_total(self):


Also adding another project to the list if needed::

 	@classmethod
    	def get_numberprojects(cls):
        	return cls.Totalnumberprojects

   	@classmethod
    	def modify_numberprojects(cls,new_number):
        	cls.Totalnumberprojects=new_number


**Data storage**

The data is stored as the folllowing picture depicts. 
The SCADA data is stored every minute of the day, while the others (GC, inferno, SPA) has a limited timeframe.
GC and Inferno data (which is also GC data type) can be store one or more minutes, while SPA correspond to only one minute of time.
Other data will also be able to be stored in the future, but now it is underconstruction.


.. figure::  images/Data_storage.png
   :align:   center






