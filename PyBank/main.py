#Import module for reading CSV

import os
import csv

py_path = os.path.join('Resources', 'budget_data.csv') 

#import date time module
from datetime import datetime

first_date = datetime.strptime('Jan-2010', '%b-%Y')
last_date = datetime.strptime('Feb-2017', '%b-%Y')

#Read in CSV and store header row

with open(py_path) as py_csv:

    py_reader = csv.reader(py_csv, delimiter=',')
    row_count = 0
    
    print(py_reader)
    #Store header 
    csv_header = next(py_reader)
   
    print(f"CSV Header: {csv_header}")

    #Read each row after the header and print
    for row in py_reader:
        #csv_header = csv_header.replace("-", " ")
        print(row)


#Print title of result set with separator
print('Finacial Analysis')
print("----------------------")



# %b Month as locale’s abbreviated name.    
