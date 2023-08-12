import pandas as pd
import os    
import glob
import csv

# load all files
files = glob.glob('./data/ziraatbank/*.csv')

for file in files:
    # remove rows with zeroes
    df = pd.read_csv(file, encoding= 'unicode_escape')
    df = df[(df.iloc[:, 1:] != 0).all(1)]
    df.to_csv(file, index=False)

    # if all zero rows are removed and we are left with the header row -> remove file
    with open(file,"r") as f:
        reader = csv.reader(f,delimiter = ",")
        data = list(reader)
        row_count = len(data)

    if row_count == 1:
        os.remove(file)
