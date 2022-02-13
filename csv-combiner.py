#import all needed packages

import pandas as pd
import glob
import os
import numpy

#Find csv files in the path chosen, please insert your own path to youe csv files
find_files = os.path.join(r'C:\Users\antho\OneDrive - The University of Texas at Dallas\Documents\GitHub\PMG-Coding_Challenge', '*.csv')

#List of all found csv files
list_files = glob.glob(find_files)

#Concat the listed files
df = pd.concat(map(pd.read_csv, list_files), ignore_index=False, keys=['accessories.csv', 'clothing.csv'], names=['filename'])
print(df)

