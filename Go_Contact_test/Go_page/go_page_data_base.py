from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

class Go_page_data_base(object):
    def __init__(self, driver):
        self._driver = driver
        
    @property
    def is_loaded(self):
        WebDriverWait(self._driver, 30).until(EC.visibility_of_element_located((By.ID, "menu_4")))
        WebDriverWait(self._driver, 30).until(EC.visibility_of_element_located((By.ID, "new_db_button")))
        return True
    
    def click_data(self):
        login_button = self._driver.find_element_by_id("menu_4")
        login_button.click()
        
    def click_new(self):
        new_button = self._driver.find_element_by_id("new_db_button")
        new_button.click()    
        
    def data(self):
        self.click_data()
        time.sleep(5)
        self.click_new()