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

location = "https://demoqa.com/browser-windows"
driver.get(location)
#Click on the "employeeLogin" button to generate the Prompt Alert
button = driver.find_element(By.ID,'windowButton')
button.click()
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
time.sleep(20)
driver.close()