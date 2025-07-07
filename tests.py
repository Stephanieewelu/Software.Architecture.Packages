# tests.py

import unittest
from models import User

class TestUser(unittest.TestCase):
    def test_user_info(self):
        user = User(1, "testuser")
        self.assertEqual(user.get_info(), "User ID: 1, Username: testuser")

    def test_app_status(self):
        from app import Application
        app = Application("TestApp")
        self.assertEqual(app.get_status(), "TestApp is running smoothly.")

if __name__ == '__main__':
    unittest.main()