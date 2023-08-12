import os

files = os.listdir()

for i in range(1, len(files)):
    day = files[i][20:22]
    year = files[i][26:30]
    os.rename(files[i], files[i][:20]+year+"-"+files[i][23:25]+"-"+day+".csv")

   
    

