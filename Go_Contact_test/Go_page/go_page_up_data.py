from re import template
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

import time
class Go_page_up_data(object):
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
        data_name =self._driver.find_element_by_id("new_db_name")
        campaign =self._driver.find_element_by_id("new_db_campaign_select")
        document_csv =self._driver.find_element_by_id("file_name")
        values = (data_name.get_attribute("value"), campaign.get_attribute("value"), document_csv.get_attribute("value"))
        return (values)
            
    def type_data(self, values):
        data_name =self._driver.find_element_by_id("new_db_name").send_keys(values['data_name'])
        campaign =self._driver.find_element_by_id("new_db_campaign_select").send_keys(values['campaign'])
        document_csv =self._driver.find_element_by_id("db_upload_file").send_keys(values['db_upload_file'])
    
    def click_upload(self):
        login_button = self._driver.find_element_by_id("upload_new_db").click()
        
    def up_data(self, values):
        self.type_data(values)
        self.click_upload()
        