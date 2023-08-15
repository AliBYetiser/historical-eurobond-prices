import pandas as pd
import glob
import csv
from itertools import groupby


files = glob.glob('./data/ziraatbank/*.csv')
df = pd.DataFrame()
for file in files:
    data = pd.read_csv(file)
    df = pd.concat([df, data], axis=0)


df.sort_values([df.columns[0], df.columns[2]], inplace = True, ascending=False)

df.to_csv('merged.csv', index=False)

header_row = ["ISIN", "Maturity", "Days Until", "Currency", "Buy", "Buy Rate", "Sell", "Sell Rate"]
for key, rows in groupby(csv.reader(open("merged.csv")),
                         lambda row: row[0]):
    with open("./data/by_ISIN/%s.csv" % key, "w") as output:
        output.write(",".join(header_row)+"\n")
        for row in rows:
            output.write(",".join(row) + "\n")
            print(row)