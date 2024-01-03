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

location = "file:///C:/pyselenium/confirm.html"
driver.get(location)

#Click on the "Alert" button to generate the Confirmation Alert
button = driver.find_element(By.NAME,'alert')
button.click()

#Switch the control to the Alert window
obj = driver.switch_to.alert

#Retrieve the message on the Alert window
message=obj.text
print ("Alert shows following message: "+ message )

time.sleep(2)

#Section 1
#use the accept() method to accept the alert
obj.accept()

#get the text returned when OK Button is clicked.
txt = driver.find_element(By.ID,'msg')
print(txt.text)

time.sleep(2)

#refresh the webpage
driver.refresh()

# Section 2
# Re-generate the Confirmation Alert
button = driver.find_element(By.NAME,'alert')
button.click()

time.sleep(2)

#Switch the control to the Alert window
obj = driver.switch_to.alert

# Dismiss the Alert using
obj.dismiss()

#get the text returned when Cancel Button is clicked.
txt = driver.find_element(By.ID,'msg')
print(txt.text)

driver.close()