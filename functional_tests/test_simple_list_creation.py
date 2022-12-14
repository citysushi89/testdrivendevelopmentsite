from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest
from webdriver_manager.firefox import GeckoDriverManager

MAX_WAIT = 10


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_for_one_user(self):
        # Edit has aheard about a cool new online to-do app. 
        # She goes to check out its homepage
        self.browser.get(self.live_server_url)

        # She notices the page title and ehader mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.get_item_input_box()
        self.assertEqual(inputbox.get_attribute('placeholder'),
        'Enter a to-do item')

        # She types "buy peacock feathers" into a text box (Edit's hobby is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # when she hit enter, the page updates, and now the page lists "#1` Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # There is still a text box inviting her to add another item She enters "Use peacock featehrs to make a fly" 
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
       

        # the page updates, and now shoes both items on her list
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        self.assertIn(
            '2: Use peacock feathers to make a fly',
            [row.text for row in rows]
        )

        # Edit wonders whether the site will remember her listThen she sees that the site has gerenrated a quniue URL for her and there is some explanatory text to that effect

        # She visits taht url and her to-do list is still there  
        # Satisfied, she goes back to sleep


    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Edit starts a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # She notices that the list has as unique URL
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        # Now a new user, Francis, comes along to the site

        # We use a new browser session to make sure that no information
        # Of Edith's is coming through from cookies
        self.browser.quit()
        self.browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

        # Francis visits the home page, there is no sign of edith's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis starts a new list by entering a new item. He is less interesting than Edit
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Francis gets his own unqiue URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Again, there is no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # Satisfied, they both go back to sleep
