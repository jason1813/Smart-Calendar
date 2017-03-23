import os, time, atexit, pwd, datetime

def closepin():
		os.system("echo 17 > /sys/class/gpio/unexport")
		os.system("echo 27 > /sys/class/gpio/unexport")

atexit.register(closepin)

def timestamp(first, llast, rlast, door_on, cal_on):
	stamp = 'Detected activity from '
	if(first == 0):
		stamp = stamp, 'left to '
	elif(first == 1)
		stamp = stamp, 'right to '
	else
		stamp = stamp, 'IDK to '
	
	if(llast == 1 && rlast == 0):
		stamp = stamp, 'left at '
	elif(llast == 0 && rlast == 1):
		stamp = stamp, 'right at '
	else:
		stamp = stamp, 'IDK at '
	
	stamp = stamp, datetime.datetime.now(), '.'
	
	if(door_on == 1 && cal_on == 1):
		stamp = stamp, ' They stopped at the door and calendar.'
	elif(door_on == 1)
		stamp = stamp, ' They stopped at the door.'
	elif(cal_on == 1)
		stamp = stamp, ' They stopped at the calendar.'
	
	print stamp
	
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
calstop = 0
doorstop = 0
cal_is_on = 0

while(1):
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
			caltimer = 1
			doortimer = 1
		elif L == 1:
			state = 1
			first = 0
			llast = 1
			rlast = 0
			caltimer = 1
			timeout = 0
		elif R == 1:
			state = 1
			first = 1
			llast = 0
			rlast = 1
			doortimer = 1
			timeout = 0
		else:
			timeout = timeout + 1
	
	elif state == 1: #activity
		print 'activity'
		L_visited = 1
		if L == 0 && R == 0:
			state = 0
			timestamp(first, llast, rlast, doorstop, calstop)
			calstop = 0
			doorstop = 0
		
		if L == 1:
			caltimer = caltimer + 1
			llast = 1
		else:
			caltimer = 0
			llast = 0

		if caltimer >= 4:
			caltimer = 4
			calstop = 1
		
		if R == 1:
			doortimer = doortimer + 1
			rlast = 1
		else:
			doortimer = 0
			rlast = 0

		if doortimer >= 6:
			doortimer = 6
			doorstop = 1
	
	
	if(timeout < 900 && cal_is_on == 0):
		os.system("python startup.py --monitor-on")
		cal_is_on = 1
	elif(timeout >= 900):
		timeout = 900
		if(cal_is_on == 1):
			os.system("python startup.py --monitor-off")
			cal_is_on = 0
	
	time.sleep(1)