#modules

import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv') 

#Print Total Votes set with separator

print('Election Results')
print("----------------------------")

#open csv
with open(csvpath) as csv_file:
        #call csv reader
        csv_reader = csv.reader(csv_file,delimiter=',') 

        csv_header = next(csv_reader)

        total_votes = len(list(csv_reader))

        print("Total Votes: ",  
            total_votes)
