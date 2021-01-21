#modules

import os
import csv
from datetime import datetime
import ast

csvfile = os.path.join('Resources', 'budget_data.csv') 




def gettotal(csvfile):
    """
    Read the first row and store values in a tuple
    """
    with open(csvfile) as csvfile:
        total = sum()
    return total


def writeCursor(csvFile, fieldnames):
    """
    Convert csv rows into an array of dictionaries
    All data types are automatically checked and converted
    """
    cursor = []  # Placeholder for the dictionaries/documents
    with open(csvFile) as csvFile:
        for row in islice(csvFile, 1, None):
            values = list(row.strip('\n').split("\t"))
            for i, value in enumerate(values):
                nValue = ast.literal_eval(value)
                values[i] = nValue
            cursor.append(dict(zip(fieldnames, values)))
    return cursor

#gettotal(csvfile)
writeCursor(csvfile)