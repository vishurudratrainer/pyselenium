# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 14:30:48 2024

@author: ASUS
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from time import sleep
# Set options for not prompting DevTools information
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

print("testing started")
driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com/")
sleep(3)


# Find element using element's id attribute
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
sleep(5)

text = driver.find_element(By.CLASS_NAME, "title").text

# Check if login was successful 
assert "products" in text.lower()

print("TEST PASSED : LOGIN SUCCESSFUL")

# Close the driver
driver.quit()