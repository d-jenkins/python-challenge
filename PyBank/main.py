#modules

import os
import csv
from datetime import datetime

py_path = os.path.join('Resources', 'budget_data.csv') 

#Read in CSV and store header row
profits_losses = []


#Print title of result set with separator
print('Finacial Analysis')
print("----------------------------")

#open csv
with open(py_path) as py_csv:
    #call csv reader
    py_reader = csv.reader(py_csv, delimiter=',')
    
    #Store header 
    csv_header = next(py_reader)

    # index total months
    total_months = len(list(py_reader))
    #total = sum(list(py_reader)

   #Print totals
   
    print("Total Months:", total_months)
  


  

 