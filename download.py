# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 15:04:11 2024

@author: ASUS
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
#find_element(By.ID, "id")
#find_element(By.NAME, "name")
#find_element(By.XPATH, "xpath")
#find_element(By.LINK_TEXT, "link text")
#find_element(By.PARTIAL_LINK_TEXT, "partial link text")
#find_element(By.TAG_NAME, "tag name")
#find_element(By.CLASS_NAME, "class name")
#find_element(By.CSS_SELECTOR, "css selector")

import time

try:


    options = webdriver.ChromeOptions()
    
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--ignore-certificate-errors')
    prefs={"download.default_directory" : "C:\pyselenium"};

    options.add_experimental_option("prefs",prefs);
    driver = webdriver.Chrome(
        options=options,
    )

    driver.get('https://www.browserstack.com/test-on-the-right-mobile-devices');

    gotit= driver.find_element(By.ID,'accept-cookie-notification');

    gotit.click();

    downloadcsv= driver.find_element(By.CSS_SELECTOR,'.icon-csv');

    downloadcsv.click();

    time.sleep(2)    

    driver.close()

except Exception as e:

     print("Invalid URL",e)
