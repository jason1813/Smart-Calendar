#open this in a second terminal to talk to browser controller
import os

fifoname = 'pipe'

if (not os.path.exists(fifoname)):
	os.mkfifo(fifoname)
talktopipe = os.open(fifoname, os.O_RDWR)

message = '0'

print '0 = Calendar\n1 = Ads\n2 = Messager\n9 = quit'
while(message != '9'):
	message = raw_input('> ')
	os.write(talktopipe, message)

