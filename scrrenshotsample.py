# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 12:36:03 2024

@author: ASUS
"""

from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('https://www.python.org')
sleep(1)

driver.get_screenshot_as_file("screenshot.png")
driver.quit()
print("end...")