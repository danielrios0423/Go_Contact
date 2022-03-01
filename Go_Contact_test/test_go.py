import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from .Go_page.go_page_login import Go_page_login
from .Go_page.go_page_data_base import Go_page_data_base
from .Go_page.go_page_up_data import Go_page_up_data
from .Go_page.go_page_template import Go_page_template

from .templates_db import Templates_db
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install()

class GoContactTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        template = Templates_db()
        cls.values = template.read_template()
        cls.driver = webdriver.Chrome()
        cls.driver.minimize_window()
    
    def test_login(self):
        go = Go_page_login(self.driver)
        go.open()
        go.login("rpa@atento-tigo.go-contact.co", "Atento2022*")
        self.assertEqual(("rpa@atento-tigo.go-contact.co", "Atento2022*"), go.keyword_login)
        time.sleep(20)
        
    def test_login_data(self):
        go = Go_page_data_base(self.driver)
        go.data()
        time.sleep(10)
    
    def test_login_up_data(self):
        go = Go_page_up_data(self.driver)
        go.up_data(self.values)
        time.sleep(5)
        
    def test_template(self):
        go = Go_page_template(self.driver)
        go.template_save(self.values)
        
    @classmethod
    def tearDownClass(cls):
        #cls.driver.close()
        pass
              
        
if __name__ == "__main__":
    unittest.main(verbosity= 2, testRunner= HTMLTestRunner(output= "report", report_name= "report_Go"))
    