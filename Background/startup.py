import os, sys, serial

option = str(sys.argv[1:2])

if(option == '[\'--start\']'):
	print 'start'

	if(not os.path.isfile('/var/www/Smart-Calendar/temporary/message.txt')):
		file = open('/var/www/Smart-Calendar/temporary/message.txt', 'w+')
		file.close()
	if(not os.path.isfile('/var/www/Smart-Calendar/temporary/stamp.txt')):
		file = open('/var/www/Smart-Calendar/temporary/stamp.txt', 'w+')
		file.close()
	os.system("echo 17 > /sys/class/gpio/export")
	os.system("echo in > /sys/class/gpio/gpio17/direction")
	os.system("echo 27 > /sys/class/gpio/export")
	os.system("echo in > /sys/class/gpio/gpio27/direction")
	os.system("python /var/www/Smart-Calendar/Background/pins.py &")
	#download ads/announcements?

elif(option == '[\'--stop\']'):
	print 'stop'
	os.system("kill $(ps -eF | grep pins.py | grep -v grep | awk '{print $2}')")
	os.system("echo 17 > /sys/class/gpio/unexport")
	os.system("echo 27 > /sys/class/gpio/unexport")

elif(option == '[\'--monitor-on\']'):
	os.system("tvservice -p; chvt 6; chvt 7")
	ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
	code = 'A00101A2'
	ser.write(code.decode('HEX'))

elif(option == '[\'--monitor-off\']'):
	os.system("tvservice -p; tvservice -o")
	ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
	code = 'A00100A1'
	ser.write(code.decode('HEX'))
