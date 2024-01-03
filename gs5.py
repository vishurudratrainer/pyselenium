# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 13:20:47 2024

@author: ASUS
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("file:///C:/pyselenium/checkbox.html")


# Clicking a button
checkbox = driver.find_element(By.ID, "myCheck")

checkbox.click()
if checkbox.is_selected():
    print("Checkbox is clicked")

# Close the browser
driver.quit()