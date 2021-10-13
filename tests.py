import unittest

from server import app
from model import db, connect_to_db
import os
import crud


# class TestServer(unittest.TestCase):
#     """Tests for my space weather site."""

#     def setUp(self):
#         self.client = app.test_client()
#         app.config['TESTING'] = True
#         os.system('createdb testdb')       
#         connect_to_db(app, "postgresql:///testdb")
#         db.create_all()
#         #create user to test profile page
#         crud.create_user(email = "testperson", password = "password")

#         with self.client as c:
#             with c.session_transaction() as sess:
#                 sess['user_email'] = "testperson"

#     def test_homepage(self):
#         result = self.client.get("/")
#         self.assertIn(b"hit Earth", result.data)

#     def test_profile(self):
#         result = self.client.get("/profile")
#         self.assertIn(b"Thank you", result.data)

#     def tearDown(self):
#         """Do at end of every test."""
#         db.session.close()
#         db.drop_all()
#         os.system('dropdb testdb')


class TestsDatabase(unittest.TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        """Stuff to do before every test."""
        #commit a bunch of objs to the db to test on
        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'key'

        os.system('createdb testdb')       
   
        #Connect to test database (uncomment when testing database)
        connect_to_db(app, "postgresql:///testdb")

        #Create tables and add sample data (uncomment when testing database)
        db.create_all()
        #add test user
        user = crud.create_user(email = "testperson", password = "password")
          
        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_email'] = "testperson"


    def tearDown(self):
        """Do at end of every test."""
        db.session.close()
        db.drop_all()
        os.system('dropdb testdb')

    def test_rate(self):
        """test that rating route works? ugh so many arguments"""

        test_rating = crud.create_rating(rating = 1, user_id = user.user_id, rating_date = 2021-10-12,
                                donki_id = 1, epic_id = 1, comment = "comment")
        result = self.client.get("/rate")
        self.assertIn(b"You have rated this earth photo", result.data)
        #test would be that Rating.query.filter(user_id, epic_id) is true?

    
    def test_create_user(self):
        """test that the crud user fxn works"""
    
        result = self.client.post("/users",
                                    data={"email": "testperson", "password": "password"},
                                    follow_redirects=True)
        self.assertIn(b"Account created!", result.data)
        #test would be if User.query.filter("testperson") is true?
    
    def test_login(self):
        """Test handle-login route."""

        result = self.client.post("/handle-login",
                                    data={"email": "testperson", "password": "password"},
                                    follow_redirects=True)
        self.assertIn(b"Success!", result.data)
        #wouldn't the test be that the user info was now in session? 
    
    def test_logout(self):
        """Test handle-logout route."""

        result = self.client.post("/handle-logout",
                                    data={"email": "testperson", "password": "password"},
                                    follow_redirects=True)
        self.assertIn(b"logged out!", result.data)
        #the test would be if session was empty- how do i do that?

if __name__ == "__main__":
    unittest.main()
