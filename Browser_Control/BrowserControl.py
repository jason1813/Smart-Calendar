import time, os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

o = Options()
#o.add_argument("--kiosk") #uncomment to show kiosk mode works
driver = webdriver.Chrome('/usr/local/selenium/webdriver/chromedriver',0,o) #executable, port, options

file_dir = 'File://' + os.getcwd()[:-15] + 'Smart_HTML/' #equivalent to pwd/../Smart_HTML/Ads.html

driver.get(file_dir + 'Ads.html') #open Ads.html

fifoname = 'pipe'
message = '0'

if (not os.path.exists(fifoname)): #look for file called fifoname
	os.mkfifo(fifoname) #make a named fifo pipe named fifoname if file does not exist
talktopipe = os.open(fifoname, os.O_RDWR) #open the pipe for read/write

while (message != '9'):
	message = os.read(talktopipe,1) #read from pipe; if pipe is empty, the program will not continue
	if(message == '0'):
		driver.get(file_dir + 'Calendar.html')
	elif(message == '1'):
		driver.get(file_dir + 'Ads.html')
	elif(message == '2'):
		driver.get(file_dir + 'Mali_Messager.html')
	else:
		print 'bad input detected!'

driver.quit()
