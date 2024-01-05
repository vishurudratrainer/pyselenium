# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 11:56:24 2024

@author: ASUS
"""

from seleniumpagefactory.Pagefactory import PageFactory

class SignInPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
    'user_name': ('CSS', "#username input"),
    'password': ('CSS', '#password input'),
    'login_btn': ('ID', 'login-btn')
    }

    def select_username(self):
        self.user_name.set_text('demouser\n')
    
    def select_password(self):
        self.password.set_text('testingisfun99\n')
    
    def click_login(self):
        self.login_btn.click()
        


class Homepage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
    "sign_in": ("ID", "signin"),
    "user_name": ("CSS", ".username")
    }

    def click_sign_in(self):
        self.sign_in.click()

    def get_username(self):
        retrieved_username = self.user_name.get_text()
        assert retrieved_username == "demouser"
        
from selenium import webdriver     
def test_browserstack():
    driver = webdriver.Chrome()
    driver.get("https://bstackdemo.com/")

    homepage = Homepage(driver)
    sign_in_page = SignInPage(driver)

    homepage.click_sign_in()

    sign_in_page.select_username()
    sign_in_page.select_password()
    sign_in_page.click_login()
    homepage.get_username()
    print("Success")
    driver.quit()
    
test_browserstack()