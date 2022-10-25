# HHA 507 - Assignment # 5

This repository represents the completion of HHA 504 Assignment # 5

Instructions:

Create a new GitHub repo called 'crontab'

Create 1 python file that pulls down data from an API and then create 3 cron jobs for that python API based on the following parameters: 
One should pull down data from an API once a day (don’t care about what time) 
One should pull down data every Sunday night at 10:00pm 
And another one should pull down data at the end of every quarter  

Report the appropriate cron job command (like in page 12 of this presentation) within the GitHub repo within the markdown file

So repo should contain two files: 
- markdown file (.md) with instructions for how the python files were automated using crontab 
- a python file (.py) that contains the python code for pulling down the data /// the retrieved data should then be saved locally on that machine where the cron job is running - e.g., should be part of the python code (e.g., df.to_csv(‘path/to/file/saved/data_10-10-10.csv)

Once A Day at 12:00AM
0 0 * * * \emman\Desktop\HHA 507\crontab\crontab.py

Every Sunday night at 10:00PM
0 22 * * SUN \emman\Desktop\HHA 507\crontab\crontab.py

Every 3 Months at 8:00AM
0 08 1 */3 * /usr/bin/python3 /home/daniel/crontab/main.py