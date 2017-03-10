import os, time, atexit, pwd

#pinreaderUID = pwd.getpwnam('pinreader')[2]
#os.setuid(pinreaderUID)

def closepin():
		os.system("echo 17 > /sys/class/gpio/unexport")
		os.system("echo 27 > /sys/class/gpio/unexport")
		os.system("echo 22 > /sys/class/gpio/unexport")

atexit.register(closepin)

os.system("echo 17 > /sys/class/gpio/export")
os.system("echo in > /sys/class/gpio/gpio17/direction")

os.system("echo 27 > /sys/class/gpio/export")
os.system("echo in > /sys/class/gpio/gpio27/direction")

os.system("echo 22 > /sys/class/gpio/export")
os.system("echo in > /sys/class/gpio/gpio22/direction")


while(1):
		time.sleep(2)
		file = open("/sys/class/gpio/gpio17/value", "r")
		print 'left', file.read()
		file.close()
		
		file = open("/sys/class/gpio/gpio27/value", "r")
		print 'middle', file.read()
		file.close()
		
		file = open("/sys/class/gpio/gpio22/value", "r")
		print 'right', file.read()
		file.close()