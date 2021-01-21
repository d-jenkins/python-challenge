#modules

import os
import csv
from datetime import datetime
import ast

csvfile = os.path.join('Resources', 'budget_data.csv') 

def gettotal(csvfile):
    with open(csvfile) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row[1])



with open(csvfile) as csvfile:

        csvfile = csv.reader(csvfile, delimiter=',')
        
        #print(py_reader)
        #Store header 
        csv_header = next(csvfile)

        # index total months
        total_months = len(list(csvfile))
        #total = sum(list(py_reader)

        #Read each row after the header and print
        for row in csvfile:
            print (row[1])


gettotal(csvfile)
