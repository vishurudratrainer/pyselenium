# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 13:14:39 2024

@author: ASUS
"""

from selenium import webdriver

from selenium.webdriver.common.by import By

# Setup chrome driver
driver = webdriver.Chrome()

# Navigate to the url
driver.get('https://pythonexamples.org/tmp/selenium/index-14.html')

# Find an element by its ID
element = driver.find_element(By.ID, 'child3')

# Check if the element is hidden
if not element.is_displayed():
    print("The element is hidden.")
else:
    print("The element is not hidden.")

# Close the driver
driver.quit()