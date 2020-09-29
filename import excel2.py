###
#Importing data from excel
###

import numpy as np
import pandas as pd 

#Function which defines the filename
def define_file(dataname="GC"):
    if dataname=="GC":
        filename="190201_mGC.xlsx"#"C:/Users/rforero/Documents/GitHub/Project_KC/190201_mGC.xlsx"

    #we need to define the other filenames
    #SCADA
    #GC Inferno
    #SPA
    #GCs
    #logging
    return filename

#we need to create the collect_data function

dsource="GC"
ExcelTable = pd.read_excel(define_file(dsource))

t0,t1=0,0
if dsource=="GC":
    columns_list=["Acquisition Date & Time","Quantity/He","Quantity/H2","Quantity/O2"]#,"Quantity/N2","Quantity/CH4"]
    t0="12:00"
    t1="13:00"

ExcelTable["Acquisition Date & Time"]=pd.to_datetime(ExcelTable["Acquisition Date & Time"])

d_t0=ExcelTable["Acquisition Date & Time"].dt.strftime("%H:%M")>t0
d_t1=ExcelTable["Acquisition Date & Time"].dt.strftime("%H:%M")<t1
Table_timeslot=ExcelTable[d_t0 & d_t1]

Table_timeslot=Table_timeslot[columns_list]

print(Table_timeslot)

#type (ExcelRead)
#print(ExcelRead)

