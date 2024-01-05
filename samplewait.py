# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 12:04:33 2024

@author: ASUS
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup chrome driver
driver = webdriver.Chrome()

# Navigate to the url
driver.get('https://pythonexamples.org/tmp/selenium/index-18.html')

# Set the maximum waiting time in seconds
wait = WebDriverWait(driver, 10)  # Adjust the waiting time (e.g., 10 seconds)

# Find the element you want to wait for (using any appropriate locator)
element_locator = (By.ID, 'firstname')  # Replace 'element_id' with the actual ID of the element

# Wait until the element is visible
element = wait.until(EC.visibility_of_element_located(element_locator))

# Perform actions on the element after it becomes visible
element.send_keys('Apple Banana')
screenshot = element.screenshot_as_png

# Save the screenshot to a file
with open('element_screenshot.png', 'wb') as file:
    file.write(screenshot)

# Close the WebDriver
driver.quit()