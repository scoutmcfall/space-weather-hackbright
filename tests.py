import unittest

from server import app
from model import db, connect_to_db


class Tests(unittest.TestCase):
    """Tests for my space weather site."""

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        result = self.client.get("/")
        self.assertIn(b"hit earth", result.data)

    def test_profile(self):
        result = self.client.post("/profile")
        self.assertIn(b"On average", result.data)

    # def test_rsvp(self):
    #maybe this could test the login part?
    #     result = self.client.post("/rsvp",
    #                               data={"name": "Jane",
    #                                     "email": "jane@jane.com"},
    #                               follow_redirects=True)
    #     self.assertIn(b"Yay!", result.data)
    #     self.assertIn(b"Details", result.data)


class TestsDatabase(unittest.TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

        #Connect to test database (uncomment when testing database)
        connect_to_db(app, "postgresql:///testdb")

        #Create tables and add sample data (uncomment when testing database)
        db.create_all()
        # example_data() what do i do if i don't have example data

    def tearDown(self):
        """Do at end of every test."""

        #(uncomment when testing database)
        db.session.close()
        db.drop_all()

    # def test_games(self):
        # FIXME: test that the games page displays the game from example_data()
        # result = self.client.get("/games")
        # self.assertIn(b"test_name", result.data)


if __name__ == "__main__":
    unittest.main()
