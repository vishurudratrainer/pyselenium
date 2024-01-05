# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 13:02:36 2024

@author: ASUS
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

# Setup chrome driver
driver = webdriver.Chrome()
driver.set_window_size(500, 400)

# Navigate to the url
driver.get('https://pythonexamples.org/tmp/selenium/index-38.html')

# Take a screenshot before JS code execution
driver.save_screenshot("screenshot-1.png")

# Execute custom JavaScript
driver.execute_script("document.body.append('Apple Banana');")

# Take a screenshot after JS code execution
driver.save_screenshot("screenshot-2.png")

# Close the driver
driver.quit()