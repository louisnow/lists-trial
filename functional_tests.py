from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
		
	def tearDown(self):
		self.browser.quit()
	
	def test_to_see_how_tests_run(self):
		self.fail("first test failed")
		
	def test_can_start_a_list_and_retrieve_it_later(self):
		# accessing the homepage
		self.browser.get('http://localhost:8000')

		#page title mentions a To Do list
		self.assertIn('To-Do',self.browser.title)
		self.fail('Finish the test!')


#Can enter an item into the To do list

#An item is entered into the text box

#The page updates and now the list shows the first item on the to do list

#There is still a text box into which an item can be entered

#Another item is added and it shows up as the second item in the to do list

#There is a URL generated to come back to the list and some text that explains
#how to use it

#The to do list is still there after visiting the URL

#The browser can be closed

if __name__ == '__main__':
	unittest.main(warnings='ignore')
