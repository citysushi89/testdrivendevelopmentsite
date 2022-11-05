from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
# import os
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a    _list_and_retrieve_it_later(self):
        # Edit has aheard about a cool new online to-do app. 
        # She goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and ehader mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away

        # She types "buy peacock feathers" into a text box (Edit's hobby is tying fly-fishing lures)

        # when she hit enter, the page updates, and now the page lists "#1` Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting her to add another item She enters "Use peacock featehrs to make a fly" 

        # the page updates, and now shoes both items on her list

        # Edit wonders whether the site will remember her listThen she sees that the site has gerenrated a quniue URL for her and there is some explanatory text to that effect

        # She visits taht url and her to-do list is still there  

        # Satisfied, she goes back to sleep


# geckodriver = os.environ['geckodriver'] 
# browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))



# She notices the page title and header mention to-do lists
# assert 'To-Do' in browser.title, 'Browser title was' + browser.title

if __name__ == '__main__':
    unittest.main()