# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 13:04:51 2024

@author: ASUS
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException

# Setup chrome driver
driver = webdriver.Chrome()

# Navigate to the url
driver.get('https://pythonexamples.org/tmp/selenium/index-30.html')

# Find the image
image_1 = driver.find_element(By.ID, 'image1')

# Check if image is visible
if image_1.is_displayed():
    print("The image is visible.")
else:
    print("The image is not visible.")

# Click on image
image_1.click()
print('Clicked on image.')


# Get image alt text
alt_text = image_1.get_attribute('alt')
print(alt_text)

# Get image size
try:
    size = image_1.size
    print(size)
    # Print width and height separately
    width  = size['width']
    height = size['height']
    print(f'Width : {width}')
    print(f'Height : {height}')
except ElementNotInteractableException:
    print('image could be hidden')
# Close the driver
driver.quit()