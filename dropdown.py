# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 13:20:47 2024

@author: ASUS
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("file:///C:/pyselenium/dropdown.html")



select = Select(driver.find_element(By.ID,'fruits01'))

# select by visible text
select.select_by_visible_text('Banana')

# select by value 
select.select_by_value('1')
# Close the browser
driver.quit()