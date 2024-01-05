# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 13:22:08 2024

@author: ASUS
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

# Setup chrome driver
driver = webdriver.Chrome()

# Navigate to the url
driver.get('file:///C:/pyselenium/hover.html')

# Find the element
element_to_hover = driver.find_element(By.ID, 'msg')

# Create an instance of ActionChains
actions = ActionChains(driver)

# Optional
time.sleep(3)

# Move the mouse to the element to hover on
actions.move_to_element(element_to_hover).perform()

# Optional
time.sleep(3)

# Close the browser
driver.quit()