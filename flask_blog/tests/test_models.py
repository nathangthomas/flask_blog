from flask import Flask
from flask_testing import TestCase

import unittest
import flask_blog.models
from flask_blog.models import User, Post

# class TestModels(unittest.TestCase):
class TestModels(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def setUp(self):
        self.user_1 = User(id=1, username='User One', email='user_1@email.com', password='password')
        self.user_2 = User(id=2, username='User Two', email='user_2@email.com', password='password')

        self.post_1 = Post(title="User_1's first post", content='This is some content for my first post.', user_id=self.user_1.id)
        self.post_2 = Post(title="User_1's second post", content='This is some content for my second post.', user_id=self.user_1.id)
        self.post_3 = Post(title="User_2's first post", content='Blah, blah, blah', user_id=self.user_2.id)

    def tearDown(self):
        pass

    def test_user_attributes(self):
        self.assertEqual(self.user_1.username, 'User One')
        self.assertEqual(self.user_1.email, 'user_1@email.com')
        self.assertEqual(self.user_1.password, 'password')
        
        # Need to complete testing for functions in User Class

        # user_1 = self.user_1
        # self.assertEqual(user_1.get_reset_token(user_1), 'password')

    def test_post_attributes(self):
        self.assertEqual(self.post_1.title, "User_1's first post")
        self.assertEqual(self.post_1.content, "This is some content for my first post.")
        self.assertEqual(self.post_1.user_id, 1)
        self.assertEqual(self.post_2.title, "User_1's second post")
        self.assertEqual(self.post_2.content, "This is some content for my second post.")
        self.assertEqual(self.post_2.user_id, 1)
        self.assertEqual(self.post_3.title, "User_2's first post")
        self.assertEqual(self.post_3.content, 'Blah, blah, blah')
        self.assertEqual(self.post_3.user_id, 2)




if __name__ == '__main__':
    unittest.main

# python -m unittest test_models.py to run test
# or nose2-v
