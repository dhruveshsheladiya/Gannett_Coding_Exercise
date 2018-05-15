import unittest #Build in Library for Unit-testing in Python
import app
#import main
import requests

class TestFlaskHomePageUsingClientRequest(unittest.TestCase): #UnitTest.TestCase denotes TestCase

    '''
    Unit Testing: Testing of all Individual components of Software.
    Unit Tests validates each unit of Software Before we Move ahead to Integration
    Python provide same functionality as Java provides for Unit Testing {JUNIT}

    Below Function will check Client's expected input and response given by Server

    By Asserting Equals We are Expecting that both Should be Equal

    If It passes then We are correct if It fails then We assume something wrong or our there is something broken in our code.
    '''
    def TestFlaskHomePagefromClient(self):
        response = requests.get('http://localhost:8000')
        self.assertEqual(response.json(), {'Welcome to Product Inventory API': 'You can view productInventory Table, product_code and product_Name'})


class TestFlaskApi(unittest.TestCase):
    '''
    Below Function will Setup the test_client for the Api
    '''
    def setUp(self):
        self.app = app.app.test_client()

    '''
    Below function is rendering to the current page {Home Page} and getting response
    '''
    def test_HomePage(self):
        response = self.app.get('/')

#Initialization of Main()
if __name__ == "__main__":
    unittest.main()