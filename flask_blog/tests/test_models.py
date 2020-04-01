

import unittest
import flask_blog.models
from flask_blog.models import User

class TestModels(unittest.TestCase):

    def setUp(self):
        self.user_1 = User(username='User One', email='user_1@email.com', password='password')

    def tearDown(self):
        pass

    def test_reset_token(self):
        # user_1 = User('User One')
        # user_1 = User('User One', 'user_1@email.com', 'password')
        # result = self.user_1.get_reset_token(self, expires_seconds=1800)
        self.assertEqual(self.user_1.username, 'User One')

print("testing testing")


if __name__ == '__main__':
    unittest.main

# python -m unittest test_models.py to run test
