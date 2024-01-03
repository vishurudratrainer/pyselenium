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
driver.get("file:///C:/pyselenium/radio.html")


# Clicking a button
yes = driver.find_element(By.ID, "yes")
no = driver.find_element(By.ID, "no")

yes.click()
if yes.is_selected() and no.is_selected()== False:
    print("Yes button is clicked")

# Close the browser
driver.quit()