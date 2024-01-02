# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 15:31:55 2024

@author: ASUS
"""


from selenium import webdriver
from selenium.webdriver.common.by import By


from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()

driver.get("file:///C:/pyselenium/password.html")


element = driver.find_element(By.ID, "passwd-id")
element = driver.find_element(By.NAME, "passwd")
element = driver.find_element(By.XPATH, "//input[@id='passwd-id']")
element = driver.find_element(By.CSS_SELECTOR, "input#passwd-id")
print(element)
driver.quit()