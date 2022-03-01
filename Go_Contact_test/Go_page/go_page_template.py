from re import template
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

import time
class Go_page_template(object):
    def __init__(self, driver):
        self._driver = driver
        #self._driver = webdriver.Chrome()

    @property
    def is_loaded(self):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, "new_db_name")))
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.ID, "upload_new_db")))
        return True
    
    @property
    def keyword_login(self):
        template =self._driver.find_element_by_id("template_select")
        return (template.get_attribute("value"))
                    
    def templates_data(self, values):
        templates = Select(self._driver.find_element_by_id("template_select"))
        templates.select_by_visible_text(values['template']) 
        time.sleep(4)
        
    def button_templates(self):
        login_button = self._driver.find_element_by_id("apply_matching_button").click()
        time.sleep(4)
        
    def button_load(self):
        login_button = self._driver.find_element_by_id("load_db_button").click()
        
    def template_save(self, values):
        self.templates_data(values)
        self.button_templates()
        self.button_load()
        
    
        