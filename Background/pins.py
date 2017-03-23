import os, time, atexit, pwd

def closepin():
		os.system("echo 17 > /sys/class/gpio/unexport")
		os.system("echo 27 > /sys/class/gpio/unexport")

atexit.register(closepin)

os.system("echo 17 > /sys/class/gpio/export")
os.system("echo in > /sys/class/gpio/gpio17/direction")

os.system("echo 27 > /sys/class/gpio/export")
os.system("echo in > /sys/class/gpio/gpio27/direction")

state = 0
timeout = 0
caltimer = 0
doortimer = 0
first = 0
llast = 0
rlast = 0
cal_on = 0
door_on = 0

while(1):
		time.sleep(1)
		file = open("/sys/class/gpio/gpio17/value", "r")
		L = int(file.read())
		file.close()
		file = open("/sys/class/gpio/gpio27/value", "r")
		R = int(file.read())
		file.close()
		
		if state == 0: #idle
			print 'idle'
			if L == 1 && R == 1:
				state = 1
				first = -1 #did not expect both sensors to turn on at same time
			elif L == 1:
				state = 1
				first = 0
				llast = 1
				rlast = 0
			elif R == 1:
				state = 1
				first = 1
				llast = 0
				rlast = 1
			else:
				timeout = timeout + 1
		
		elif state == 1: #activity
			print 'L Hold'
			L_visited = 1
			if L == 0 && R == 0:
				state = 0
				#create timestamp
			if L == 1:
				caltimer = caltimer + 1
				llast = 1
			else:
				caltimer = 0
				llast = 0

			if caltimer >= 4:
				caltimer = 4
				cal_on = 1
			
			if R == 1:
				doortimer = doortimer + 1
				rlast = 1
			else:
				doortimer = 0
				rlast = 0

			if doortimer >= 6:
				doortimer = 6
				door_on = 1
		
		
		
