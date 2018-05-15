import unittest
import os
import json
import app

class TestGetAll(unittest.TestCase):
    '''
    Below function will set up the New test Client as global variable
    This will help us to initialize new Client in Every Method
    '''
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app.app.test_client()
        self.listSample={'name': 'This is Sample Post Data'}


    def test_api_can_get_all(self):
        """Test API can get a Produce Inventory (GET request)."""
        res = self.app.post('/produceInventory/',data=self.listSample)
        self.assertEqual(res.status_code, 404)
        res = self.app.get('/produceInventory')
        self.assertEqual(res.status_code, 200)
        #self.assertIn('{{"produceInventory": [{"produce_name": "Lettuce", "produce_code": "A12T-4GH7-QPL9-3N4M", "produce_unitprice": 3.46}, {"produce_name": "Peach", "produce_code": "E5T6-9UI3-TH15-QR88", "produce_unitprice": 2.99}, {"produce_name": "Green Pepper", "produce_code": "YRT6-72AS-K736-L4AR", "produce_unitprice": 0.79}, {"produce_name": "Gala Apple", "produce_code": "TQ4C-VV6T-75ZX-1RMR", "produce_unitprice": 3.59}]}}', str(res.data))

    def test_api_cat_get__by_id(self):
        """Test API can get a single product_code by using it's id."""
        res = self.app.post('/produceInventory/', data=self.listSample)
        self.assertEqual(res.status_code, 404)
        res = self.app.get('/produceInventory/A12T-4GH7-QPL9-3N4M')
        self.assertEqual(res.status_code, 200)
        self.assertIn('{"Inventory has":[{"produce_code":"A12T-4GH7-QPL9-3N4M","produce_name":"Lettuce","produce_unitprice":3.46}]}', str(res.data))

    def test_produceSchema_cant_be_edited(self):
        """Test API can edit an existing Products. (PUT request)"""
        rv = self.app.post(
            '/produceInventory/',
            data={'name': 'Indian Mangoes'})
        self.assertEqual(rv.status_code, 404)
        rv = self.app.put(
            '/produceInventory/1',
            data={
                "name": "broccoli from North Dakota)"
            })
        self.assertEqual(rv.status_code, 405)
        results = self.app.get('/produceInventory/1')
        self.assertIn('{"error":"Invalid Operation or Input"}', str(results.data))

    def test_Product_deletion(self):
        """Test API can delete an existing Products or Not. (DELETE request)."""
        rv = self.app.post(
            '/produceInventory/',
            data={'name': 'Strawberry'})
        self.assertEqual(rv.status_code, 404)
        res = self.app.delete('/produceInventory/1')
        self.assertEqual(res.status_code, 405)
        # Test to see if it exists, should return a 404
        result = self.app.get('/produceInventory/1')
        self.assertEqual(result.status_code,200)
        results = self.app.get('/produceInventory/1')
        self.assertIn('{"error":"Invalid Operation or Input"}', str(results.data))

    def test_when_product_code_isWrong_formatted(self):
        """Test API will check if Wrong and Random Product_code can modify API result or not?."""

        """
        By using I am Checking my API by Security aspect as well
        Sometime bit modified and invalid input to the API can also damage our API {E.g. SQL Injection Attack}
        
        Our API should maintain strong White-list{List of  Allowable inputs}
        
        Parameterized Query always prevents the malicious attack to the API via Inputs
        
        """

        rv = self.app.post(
            '/produceInventory/',
            data={'name': 'A12T-4GH7-QPL9'}) #My input is 12 digits only and Code must have 16 digit alphanumerics
        self.assertEqual(rv.status_code, 404)
        res = self.app.get('/produceInventory/A12T-QPL9')
        self.assertEqual(res.status_code, 200)
        results = self.app.get('/produceInventory/A12T-QPL9')
        self.assertIn('{"error":"Invalid Operation or Input"}', str(results.data))
        # Test to see if it exists, should return a 404
        result = self.app.get('/produceInventory/A12T-4GH7-QPL9-**')
        self.assertEqual(result.status_code, 200)
        results = self.app.get('/produceInventory/A12T-4GH7-QPL9-**')
        self.assertIn('{"error":"Invalid Operation or Input"}', str(results.data))


if __name__ == "__main__":
    unittest.main()