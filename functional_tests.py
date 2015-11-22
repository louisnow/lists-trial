from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
		
	def tearDown(self):
		self.browser.quit()
			
	def test_can_start_a_list_and_retrieve_it_later(self):
		# accessing the homepage
		self.browser.get('http://localhost:8000')

		#page title mentions a To Do list
		self.assertIn('To-Do',self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do',header_text)

		#Can enter an item into the to do list
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'),
		'Enter a to-do item'
		)

		#An item is entered into the text box
		inputbox.send_keys('Buy condoms')

		#The page updates and now the list shows 
		#the first item on the to do list
		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_element_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Buy condoms' for row in rows)
			)

#There is still a text box into which an item can be entered
		self.fail('Finish the test!')

#Another item is added and it shows up as the second item in the to do list

#There is a URL generated to come back to the list and some text that explains
#how to use it

#The to do list is still there after visiting the URL

#The browser can be closed

if __name__ == '__main__':
	unittest.main(warnings='ignore')
