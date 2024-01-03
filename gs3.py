# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 13:20:47 2024

@author: ASUS
"""

from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("file:///C:/pyselenium/form.mhtml")

# Validate the title
expected_title = "QA Practice | Learn with RV"
actual_title = driver.title

if expected_title == actual_title:
    print("Title validation successful!")
else:
    print("Title validation failed. Expected:", expected_title, "Actual:", actual_title)

# Close the browser
driver.quit()