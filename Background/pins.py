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
#timeout = 0
caltimer = 0
doortimer = 0
doorm = 0
calm = 0
L_visited = 0
R_visited = 0
first = 0

while(1):
		time.sleep(1)
		file = open("/sys/class/gpio/gpio17/value", "r")
		L = int(file.read())
		file.close()
		file = open("/sys/class/gpio/gpio27/value", "r")
		R = int(file.read())
		file.close()
		
		if R == 1 && doortimer < 5:
			doortimer = doortimer+1
		elif R == 1:
			print 'doorstop'
		else
			doortimer = 0
		
		if L == 1 && caltimer < 5:
			caltimer = caltimer+1
		elif R == 1:
			print 'calstop'
		else
			caltimer = 0
		
		if state == 0: #idle
			print 'idle'
			if L == 1 && R == 1:
				state = 5 #error!
			elif L == 1:
				state = 1
				first = 0
			elif R == 1:
				state = 2
				first = 1
		
		elif state == 1: #LHold
			print 'L Hold'
			L_visited = 1
			if L == 0 && R == 0:
				state = 0
				if first == 0:
					print 'Came L left L'
				else
					print 'Came R left L'
			elif L == 0 && R == 1:
				state = 2
			
		elif state == 2: #RHold
			print 'R Hold'
			R_visited = 1
			if L == 0 && R == 0:
				state = 0
				if first == 0:
					print 'Came L left R'
				else
					print 'Came R left R'
			elif L == 1 && R == 0:
				state = 1
			
		elif state == 5: #wait
			print 'Wait'
			if L == 0 && R == 0:
				state = 0
		
		
		
