# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 14:58:25 2024

@author: ASUS
"""

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
#driver.get("file:///C:/pyselenium/radio.html")

location = "file:///C:/pyselenium/prompt.html"
driver.get(location)
#Click on the "employeeLogin" button to generate the Prompt Alert
button = driver.find_element(By.NAME,'employeeLogin')
button.click()

#Switch the control to the Alert window
obj = driver.switch_to.alert

time.sleep(2)

#Enter text into the Alert using send_keys()
obj.send_keys('Meenakshi')

time.sleep(2)

#use the accept() method to accept the alert
obj.accept()

#Retrieve the message on the Alert window
message=obj.text
print ("Alert shows following message: "+ message )

time.sleep(2)

obj.accept()

#get the text returned when OK Button is clicked.
txt = driver.find_element(By.ID,'msg')
print(txt.text)
driver.close()