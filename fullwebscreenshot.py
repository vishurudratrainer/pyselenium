# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 12:37:22 2024

@author: ASUS
"""

#coding=utf-8                                                                                                                                                                              
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)

URL = 'https://pythonbasics.org'

driver.get(URL)

S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment                                                                                                                
driver.find_element(By.TAG_NAME,'body').screenshot('web_screenshot.png')
print("Done")
driver.quit()