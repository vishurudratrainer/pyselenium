# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 13:12:15 2024

@author: ASUS
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

# Setup chrome driver
driver = webdriver.Chrome()
driver.set_window_size(500, 400)

# Navigate to the url
driver.get('https://pythonexamples.org/tmp/selenium/index-39.html')

# Find all input text fields
input_text_fields = driver.find_elements(By.XPATH, '//input[@type="text"]')

# Iterate over the input text fields
for input_text in input_text_fields:
    input_text.send_keys("Apple")

# Take a screenshot
driver.save_screenshot("screenshot.png")


input_text_1 = driver.find_element(By.XPATH, "//input[@name='firstname']")

# Get the value in input text field
value = input_text_1.get_attribute('value')

# Check if value is empty
if value == '':
    print("Input text field is empty.")
else:
    print("Input text field is not empty.")

# Close the driver
driver.quit()