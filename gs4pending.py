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
driver.get("file:///C:/pyselenium/form.mhtml")


# Clicking a button
button = driver.find_element(By.ID, "registerBtn")

button.click()

# Clicking a link
link = driver.find_element("link text", "Click Here")
link.click()

# Close the browser
driver.quit()