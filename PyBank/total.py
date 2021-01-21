#modules

import os
import csv
from datetime import datetime

py_path = os.path.join('Resources', 'budget_data.csv') 



#Read in CSV and store header row

#Print title of result set with separator
print('Finacial Analysis')
print("----------------------------")

profits_losses = []


def total_months(py_csv):
    with open(py_path) as py_csv:

        py_reader = csv.reader(py_csv, delimiter=',')
        
        #Store header 
        csv_header = next(py_reader)

        # index total months
        total_months = len(list(py_reader))

            
        print("Total Months:", total_months)


  
def p_l(py_reader):
    for row in  py_reader:
        profits_losses.append(row[1])
        for column in row:
            print(column)
 
p_l(py_reader)