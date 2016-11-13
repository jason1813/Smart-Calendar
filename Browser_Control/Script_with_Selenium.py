import time

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary)

driver.get('http://seleniumhq.org/')
time.sleep(3) # delays for 5 seconds
driver.get('http://www.espn.com/')