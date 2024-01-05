# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 12:42:40 2024

@author: ASUS
"""

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup chrome driver
driver = webdriver.Chrome()

# Navigate to the url
driver.get('https://jqueryui.com/droppable/')

# Set the maximum waiting time in seconds
driver.switch_to.frame(0)


# identifying the source and target elements
source= driver.find_element(By.ID,"draggable");
target= driver.find_element(By.ID,"draggable");
# action chain object creation
action = ActionChains(driver)
# drag and drop operation and the perform
action.drag_and_drop(source, target).perform()
print("Success")
driver.close()