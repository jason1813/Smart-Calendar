import os

os.system("chromium-browser --kiosk file:///home/jason/Documents/Smart_Calendar/Smart_HTML/Calendar.html &") #unix command to open chromium in a new process in kiosk mode, opens html file on my desktop


fifoname = 'pipe'

if (not os.path.exists(fifoname)): #look for file called fifoname
	os.mkfifo(fifoname) #make a named fifo pipe named fifoname if file does not exist

talktopipe = os.open(fifoname, os.O_RDWR) #open the pipe for read/write
os.write(talktopipe, '0') #write 0 to pipe

message = os.read(talktopipe,1) #read from pipe; if pipe is empty, the program will not continue
print message

filename = 'UsefulCode.py'
file_read = open(filename, 'r') #open a file to read
message = file_read.readline() #read a line in the file
print message
