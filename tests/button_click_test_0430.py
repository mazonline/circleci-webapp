from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest, time, re

class NewTest(unittest.TestCase):
# We create our unittest test case

    def setUp(self):
        self.verificationErrors = []
        # This is an empty array where we will store any verification errors
        # we find in our tests

        self.selenium = selenium("localhost", 4444, "*firefox",
                "https://mazonline.github.io/index.html/")
        self.selenium.start()
        # We instantiate and start the browser

    def test_new(self):
        # This is the test code.  Here you should put the actions you need
        # the browser to do during your test.

        sel = self.selenium
        # We assign the browser to the variable "sel" (just to save us from
        # typing "self.selenium" each time we want to call the browser).

        sel.open("/")
        #sel.type("q", "selenium rc")
        #element = sel.click("btnG")
        button = driver.find_element_by_name('answer')
        button.click()
        print ('Button is clicked and contains text!')
        sel.wait_for_page_to_load("30000")
        self.failUnless(sel.is_text_present("Results * for selenium rc"))
        # These are the real test steps

    def tearDown(self):
        self.selenium.stop()
        # we close the browser (I'd recommend you to comment this line while
        # you are creating and debugging your tests)

        self.assertEqual([], self.verificationErrors)
        # And make the test fail if we found that any verification errors
        # were found
