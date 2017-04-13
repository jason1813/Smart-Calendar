import os, sys, time

os.system("python /var/www/Smart-Calendar/Background/startup.py --monitor-off") #dont let anyone see desktop
os.system("python /var/www/Smart-Calendar/Background/startup.py --start") #startup services

time.sleep(60) #wait in seconds

os.system("python /var/www/Smart-Calendar/Background/startup.py --monitor-on") #browser should have loaded by now
