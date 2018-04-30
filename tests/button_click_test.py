#!/usr/bin/python
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        options.add_argument("--headless")
        self.driver = webdriver.Firefox(firefox_options=options)

    def test_search_in_python_org(self):
        driver.get("https://mazonline.github.com/index.html")
        driver.implicitly_wait(20)
        element = driver.find_element_by_xpath("/html/body/button")
        element.click()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
