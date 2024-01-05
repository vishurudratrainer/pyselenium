# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 13:27:54 2024

@author: ASUS
"""


from selenium import webdriver

from selenium.webdriver.common.by import By
import time

# Setup chrome driver
driver = webdriver.Chrome()

# Navigate to the url
driver.get('https://pythonexamples.org/tmp/selenium/index-29.html')

# Get the element
the_element = driver.find_element(By.ID, "para3")

time.sleep(2)

# Scroll to the element using JavaScript
driver.execute_script("arguments[0].scrollIntoView();", the_element)

time.sleep(3)

# Close the driver
driver.quit()