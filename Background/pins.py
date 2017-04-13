import os, time, pwd, time

do_monitor = 1;

def timestamp(first, llast, rlast, door_on, cal_on):
	stamp = 'Detected activity from '
	
	if(first == 0): #entry point
		stamp = stamp + 'left to '
	elif(first == 1):
		stamp = stamp + 'right to '
	else:
		stamp = stamp + 'IDK to '
	
	if(llast == 1 and rlast == 0): #exit point
		stamp = stamp + 'left at '
	elif(llast == 0 and rlast == 1):
		stamp = stamp + 'right at '
	else:
		stamp = stamp + 'IDK at '
	
	stamp = stamp + time.asctime() + '.' #time
	
	if(door_on == 1 and cal_on == 1): #extra info
		stamp = stamp + ' They stopped at the door and calendar.'
	elif(door_on == 1):
		stamp = stamp + ' They stopped at the door.'
	elif(cal_on == 1):
		stamp = stamp + ' They stopped at the calendar.'

	stamp = stamp + '\n'
	file = open('/var/www/Smart-Calendar/HTML/temporary/stamp.txt', 'a')
	file.write(stamp)
	file.close()

state = 0 #0 = idle state, 1 = active state
timeout = 0 #counts seconds of inactivity
caltimer = 0 #counts seconds of activity for left sensor above calendar
doortimer = 0 #counts seconds of activity for right sensor above door
first = 0 #-1 = Invalid, 0 = Left, 1 = Right, 
llast = 0 #boolean, true = left sensor was active last check
rlast = 0 #boolean, true = right sensor was active last check
calstop = 0 #boolean, true = user stopped at calendar
doorstop = 0 #boolean, true = user stopped at door
cal_is_on = 1 #boolean, true = monitor is on
cal_is_active = 1 #boolean, false = idly displaying ads, true = active

while(1):
	file = open("/sys/class/gpio/gpio17/value", "r") #read pins
	L = int(file.read())
	file.close()
	file = open("/sys/class/gpio/gpio27/value", "r")
	R = int(file.read())
	file.close()
	
	if state == 0: #idle
		#print 'idle'
		if(L == 1 and R == 1): #left and right activity
			state = 1
			first = -1 #did not expect both sensors to turn on at same time
			llast = 1
			rlast = 1
			caltimer = 1
			doortimer = 1
			timeout = 0
		elif(L == 1): #left activity
			state = 1
			first = 0
			llast = 1
			rlast = 0
			caltimer = 1
			doortimer = 0
			timeout = 0
		elif(R == 1): #right activity
			state = 1
			first = 1
			llast = 0
			rlast = 1
			caltimer = 0
			doortimer = 1
			timeout = 0
		else: #no activity
			timeout = timeout + 1
	elif state == 1: #activity
		#print 'activity'
		L_visited = 1
		if(L == 0 and R == 0): #no activity
			state = 0
			timestamp(first, llast, rlast, doorstop, calstop)
			calstop = 0
			doorstop = 0
		
		if L == 1: #left activity
			caltimer = caltimer + 1
			llast = 1
		else:
			caltimer = 0
			llast = 0

		if caltimer >= 4:
			caltimer = 4
			calstop = 1
		
		if R == 1: #right activity
			doortimer = doortimer + 1
			rlast = 1
		else:
			doortimer = 0
			rlast = 0

		if doortimer >= 6:
			doortimer = 6
			doorstop = 1
	
	if(do_monitor == 1):
		if(timeout < 900 and cal_is_on == 0):
			os.system("python startup.py --monitor-on &")
			#print 'turn on'		
			cal_is_on = 1
		elif(timeout >= 900):
			timeout = 900
			if(cal_is_on == 1):
				os.system("python startup.py --monitor-off &")
				#print 'turn off'
				cal_is_on = 0
	
	if(timeout < 90 and cal_is_active == 0): #calendar becomes active
		file = open('var/www/Smart-Calendar/HTML/temporary/message.txt', 'w')
		file.write('b')
		file.close()
		cal_is_active = 1
	elif(timeout >= 90 and cal_is_active == 1): #calendar becomes idle
		file = open('var/www/Smart-Calendar/HTML/temporary/message.txt', 'w')
		file.write('i')
		file.close()
		cal_is_active = 0
	
	time.sleep(1)
