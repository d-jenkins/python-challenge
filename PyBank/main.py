#modules

import os
import csv
from datetime import datetime

py_path = os.path.join('Resources', 'budget_data.csv') 




# List of variables to store values
first_date = datetime.strptime('Jan-2010', '%b-%Y')
last_date = datetime.strptime('Feb-2017', '%b-%Y')
total_months = []
total = []
average_change = []
greatest_increase = []
greatest_decrease = []


#Read in CSV and store header row

#Print title of result set with separator
print('Finacial Analysis')
print("----------------------")


with open(py_path) as py_csv:

    py_reader = csv.reader(py_csv, delimiter=',')
    
    #print(py_reader)
    #Store header 
    csv_header = next(py_reader)
   
    #print(f"CSV Header: {csv_header}")

    # index total months
    total_months = len(list(py_reader))
    print("Total Months:",total_months)

    print("Total:", total)
    print("Average Change:", average_change)
    print("Greatest Increase in Profits:", greatest_increase)
    print("Greatest Decrease in Profits:", greatest_decrease)

    #Read each row after the header and print
    #for row in py_reader:
        #print (row[0])
        #month_set = set(total_months)
        # total_months = len(month_set)
        #print("Total Months:",total_months)

# %b Month as locale’s abbreviated name.    