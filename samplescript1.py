# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 12:59:00 2024

@author: ASUS
"""

from selenium import webdriver

driver=webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://pythonbasics.org")
js = 'alert("Hello World")'
driver.execute_script(js)
driver.quit()


from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://stackoverflow.com/questions/7794087/running-javascript-in-selenium-using-python") 
driver.execute_script("document.getElementsByClassName('comment-user')[0].click()")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.quit()
