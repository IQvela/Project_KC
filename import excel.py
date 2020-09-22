###
#Importing data from excel
###

import pandas as pd 

ExcelRead = pd.read_excel('190201_mGC.xlsx')
type (ExcelRead)
print(ExcelRead)
