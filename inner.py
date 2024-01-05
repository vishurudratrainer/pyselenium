# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 13:26:23 2024

@author: ASUS
"""

from selenium import webdriver

from selenium.webdriver.common.by import By

# Setup chrome driver
driver = webdriver.Chrome()

# Navigate to the url
driver.get('https://pythonexamples.org/tmp/selenium/index-10.html')

# Get the element
element = driver.find_element(By.ID, "msg")

# Get inner HTML of the element
html = element.get_attribute("innerHTML")
print(html)
html = element.get_attribute("outerHTML")
print(html)
# Close the driver
driver.quit()