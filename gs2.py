# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 14:45:25 2024

@author: ASUS
"""

from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time
options = Options()
options.add_argument("headless")

driver = webdriver.Edge(options = options)

driver.get('https://bing.com')

element = driver.find_element(By.ID, 'sb_form_q')
element.send_keys('WebDriver')
element.submit()

time.sleep(2)
driver.quit()