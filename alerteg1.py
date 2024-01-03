# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 14:36:55 2024

@author: ASUS
"""

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
#driver.get("file:///C:/pyselenium/radio.html")

location = "file:///C:/pyselenium/alert.html"
driver.get(location)

#Click on the "Alert" button to generate the Simple Alert
button  = driver.find_element(By.NAME, "alert")

button.click()

#Switch the control to the Alert window
obj = driver.switch_to.alert

#Retrieve the message on the Alert window
msg=obj.text
print ("Alert shows following message: "+ msg )

time.sleep(2)

#use the accept() method to accept the alert
obj.accept()

print(" Clicked on the OK Button in the Alert Window")

driver.close()