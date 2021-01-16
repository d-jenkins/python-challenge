#Import module for reading CSV

import os
import csv
csvpath = os.path.join('../..', 'Resources', 'budget_data.csv')

#Read in CSV and store header row

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    print(csvreader)



#Print title of result set with separator
print('Finacial Analysis')
print("----------------------")

