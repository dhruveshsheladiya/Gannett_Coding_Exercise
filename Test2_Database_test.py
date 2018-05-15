import unittest
import app
import requests
import os
import tempfile


class FlaskrTestCase(unittest.TestCase):

    '''
    Below Method Will initialize a new Client and Database Connection
    This function is called before each individual test function is run.

    The mkstemp() function does two things for us: it returns a low-level file handle and a random file name, the latter we use as database name.
    '''
    def setUp(self):
        self.db_fd, app.app.config['PRODUCE'] = tempfile.mkstemp()
        flaskr.app.testing = True
        self.app = app.app.test_client()
        with app.app.app_context():
            app.init_db()

    '''
    Below Function will Delete the Database instance after ;
    It will close the file and remove it from the FileSystem
    
    This will help us to keep our Database Clean and Neat;
    Often a time we Add, modify, Delete just for Testing our Database; I consider it as a wrong practise
    '''
    def deleteDB(self):
        os.close(self.db_fd)
        os.unlink(app.app.config['PRODUCE'])


    '''
    Below Test will Fail because there is Data in Database
    '''
    def test_db_Empty_or_not(self):
        rv = self.app.get('/')
        assert b'No entries here so far' in rv.data


#initialization of main()
if __name__ == '__main__':
    unittest.main()