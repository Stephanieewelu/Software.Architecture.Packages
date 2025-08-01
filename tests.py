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

    def test_install_package(self):
        from app import Application
        app = Application("TestApp")
        # We can't directly test print statements, but we can ensure the method runs without error
        try:
            app.install_package("TestPackage")
            self.assertTrue(True) # If no exception, test passes
        except Exception as e:
            self.fail(f"install_package raised an exception: {e}")

def test_user_validation(self):
        user = User(2, "validuser")
        self.assertTrue(len(user.username) > 0)

if __name__ == '__main__':
    unittest.main()