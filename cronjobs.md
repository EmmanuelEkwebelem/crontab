# Schedule of Cron Jobs

Once A Day at 12:00AM

0 0 * * * \emman\Desktop\HHA 507\crontab\crontab.py



Every Sunday night at 10:00PM

0 22 * * SUN \emman\Desktop\HHA 507\crontab\crontab.py



Every 3 Months at 8:00AM

0 08 1 */3 * \emman\Desktop\HHA 507\crontab\crontab.py > log.txt 2>&1 &
