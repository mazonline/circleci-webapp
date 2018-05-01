import unittest
from selenium import webdriver

class SearchText(unittest.TestCase):

	def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox()
        # navigate to the application home page
        self.driver.get("http://mazonline.github.io.index.html /")
	
	def test_search_by_text(self):
	element = driver.find_element_by_name("answer").click()
        print ('Button is clicked and contains text!')
        sel.wait_for_page_to_load("30000")

   	def tearDown(self):
        # close the browser window
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()
