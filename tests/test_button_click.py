import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_button_click_in_site(self):
        driver = self.driver
        driver.get("http://mazonline.github.io/index.html")
        elem = driver.find_element_by_name("answer")
        clicked_button = elem.click()
        print ('Button has been clicked and there is text')
     
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
