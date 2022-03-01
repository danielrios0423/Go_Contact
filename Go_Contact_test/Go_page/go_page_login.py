from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Go_page_login(object):
    def __init__(self, driver):
        self._driver = driver
        self._url = "https://atento-tigo.go-contact.co"
        
    @property
    def is_loaded(self):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
        return True
    
    @property
    def keyword_login(self):
        email =self._driver.find_element_by_name("email")
        password =self._driver.find_element_by_name("password")
        return (email.get_attribute("value"), password.get_attribute("value"))
    
    def open(self):
        self._driver.get(self._url)
        
    def type_login(self, keyword_email, keyword_password):
        email =self._driver.find_element_by_name("email")
        email.send_keys(keyword_email)
        password =self._driver.find_element_by_name("password")
        password.send_keys(keyword_password)
    
    def click_login(self):
        login_button = self._driver.find_element_by_id("btn-login")
        login_button.click()
        
    def login(self, keyword_email, keyword_password):
        self.type_login(keyword_email, keyword_password)
        self.click_login()
        
    
        