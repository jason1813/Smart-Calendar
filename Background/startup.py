import os, sys

option = str(sys.argv[1:2])

if(option == ‘[\’--start\’]’):
	print ‘start’

	if(not os.path.isfile(‘var/www/Smart-Calendar/HTML/message/message.txt’)):
		file = open(‘var/www/Smart-Calendar/HTML/message/message.txt’, ‘w’)
		file.close()
	os.system(“python ./pins.py &”)
	#download ads/announcements?

elif(option == ‘[\’--stop\’]’):
	print ‘stop’
	os.system(“kill $(ps -eF | grep pins.py | grep -v grep | awk ‘{print $2}’)”)

elif(option == ‘[\’--monitor-on\’]’):
	#i forgot what the command was

elif(option == ‘[\’--monitor-off\’]’):
	#i also forgot this command too
