import unittest

from application import app

class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_service(self):
        response = self.app.get('/helloworld/')
        self.assertEquals("Hello World!", response.data)
        self.assertEquals(200, response.status_code)
