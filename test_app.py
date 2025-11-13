import unittest
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))

from app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        """Test that the home page loads correctly"""
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_api_home(self):
        """Test that the API home endpoint returns JSON"""
        result = self.app.get('/api/')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.content_type, 'application/json')

    def test_health_page(self):
        """Test that the health page loads correctly"""
        result = self.app.get('/health')
        self.assertEqual(result.status_code, 200)

    def test_users_page(self):
        """Test that the users page loads correctly"""
        result = self.app.get('/users')
        self.assertEqual(result.status_code, 200)

    def test_api_users_get(self):
        """Test that the API users endpoint returns JSON"""
        result = self.app.get('/api/users')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.content_type, 'application/json')

if __name__ == '__main__':
    unittest.main()