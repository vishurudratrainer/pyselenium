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

#find_element(By.ID, "id")
#find_element(By.NAME, "name")
#find_element(By.XPATH, "xpath")
#find_element(By.LINK_TEXT, "link text")
#find_element(By.PARTIAL_LINK_TEXT, "partial link text")
#find_element(By.TAG_NAME, "tag name")
#find_element(By.CLASS_NAME, "class name")
#find_element(By.CSS_SELECTOR, "css selector")

element = driver.find_element(By.ID, "passwd-id")
element = driver.find_element(By.NAME, "passwd")
element = driver.find_element(By.XPATH, "//input[@id='passwd-id']")
element = driver.find_element(By.CSS_SELECTOR, "input#passwd-id")
print(element)
driver.quit()