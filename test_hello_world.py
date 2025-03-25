import unittest
from hello_world import app

class HelloWorldTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_homepage_404(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 404)

    def test_greeting_page(self):
        response = self.app.get('/greeting')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, World!', response.data)

if __name__ == '__main__':
    unittest.main()
