import pandas
import crontab 
import os
import sys
import time
import json
import csv

# Assessing the cwd(current working directory)
cwd = os.getcwd()
print(cwd)

### Getting the current system time   
CurrentTime = time.time()
Time_Now = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(CurrentTime))
print('The Time Now Is: ', Time_Now)

### Loading in API Data 
Data = pandas.read_json('https://healthdata.gov/resource/qwij-f3kq.json')
Data

### Export API Data to directory Data folder 
Data.to_csv('Data/Child_Victim_Trend.csv')

### Creating a new file in the current working directory
with open(cwd + '/DataFile_' + Time_Now + '.txt', 'w') as f:f.write(str(Data))

