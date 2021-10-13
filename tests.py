import unittest

from server import app
from model import db, connect_to_db
import os
import crud


class TestServer(unittest.TestCase):
    """Tests for my space weather site."""

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True
        os.system('createdb testdb')       
        connect_to_db(app, "postgresql:///testdb")
        db.create_all()
        #create user
        crud.create_user(email = "testperson", password = "password")

        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_email'] = "testperson"

    def test_homepage(self):
        result = self.client.get("/")
        self.assertIn(b"hit Earth", result.data)

    def test_profile(self):
        result = self.client.get("/profile")
        self.assertIn(b"Thank you", result.data)

    def tearDown(self):
        """Do at end of every test."""

        #(uncomment when testing database)
        db.session.close()
        db.drop_all()
        os.system('dropdb testdb')


# class TestsDatabase(unittest.TestCase):
#     """Flask tests that use the database."""

#     def setUp(self):
#         """Stuff to do before every test."""
#         #commit a bunch of objs to the db to test on
#         self.client = app.test_client()
#         app.config['TESTING'] = True

#         #Connect to test database (uncomment when testing database)
#         connect_to_db(app, "postgresql:///testdb")

#         #Create tables and add sample data (uncomment when testing database)
#         db.create_all()
#         # example_data() what do i do if i don't have example data

#     def tearDown(self):
#         """Do at end of every test."""

#         #(uncomment when testing database)
          #os.system('dropdb testdb')
#         db.session.close()
#         db.drop_all()

#     def test_rate(self):
#         """test that rating route works? ugh so many arguments"""
#         rate_1 = Rating()
        
#         result = self.client.get("/rate")
#         self.assertIn(b"what goes here", result.data)
    
#     def test_create_user(self):
#         """test that the login works"""
#         test_user = User("name", "password")
#         #commit to db

#         test_user.password = "password"


if __name__ == "__main__":
    unittest.main()
