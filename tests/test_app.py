import unittest
from app import app

class SiteTests(unittest.TestCase):
    def setUp(self):
        app.config.update(TESTING=True)
        self.client = app.test_client()

    def test_routes_and_demo_forms(self):
        for path in ("/", "/rooms", "/booking", "/contact"):
            self.assertEqual(self.client.get(path).status_code, 200, path)
        for path in ("/booking", "/contact"):
            response = self.client.post(path, data={"name":"Guest", "email":"g@example.com"}, follow_redirects=True)
            self.assertIn(b"sent or saved", response.data)
