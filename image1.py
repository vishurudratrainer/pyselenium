# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 13:04:51 2024

@author: ASUS
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

# Setup chrome driver
driver = webdriver.Chrome()

# Navigate to the url
driver.get('https://pythonexamples.org/tmp/selenium/index-30.html')

# Find all images
images = driver.find_elements(By.TAG_NAME, 'img')

# Print number of images
print(f'There are {len(images)} images.')

# Close the driver
driver.quit()