# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 13:31:18 2024

@author: ASUS
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

# Setup chrome driver
driver = webdriver.Chrome()
# Navigate to the url
driver.get('https://pythonexamples.org/tmp/selenium/index-54.html')

# Find elements by name attribute
my_elements = driver.find_elements(By.NAME, 'xyz')
for element in my_elements:
    print(element.get_attribute("outerHTML"))

# Close the driver
driver.quit()