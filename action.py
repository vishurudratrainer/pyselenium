# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 14:48:21 2024

@author: ASUS
"""

from selenium import webdriver


from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Edge()

driver.get("https://www.browserstack.com/")
element=driver.find_element("link text", "Sign in")


action = ActionChains(driver)

action.click(on_element = element)

action.perform()