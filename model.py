""" Models for space weather app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""
    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement = True,
                        primary_key = True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __repr__(self):
        return f'<User user_id={self.user_id} email = {self.email}>'
    

class Donki(db.Model):
    """A donki forecast."""
    __tablename__ = 'donki'
    donki_id = db.Column(db.Integer,
                        autoincrement = True,
                        primary_key = True)
    donki_url = db.Column(db.String, unique = True)
    date = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Donki donki_id = {self.donki_id}>'


class Epic(db.Model):
    """An epic photo."""
    __tablename__ = 'epic'
    epic_id = db.Column(db.Integer,
                        autoincrement = True,
                        primary_key = True)
    epic_url = db.Column(db.String, unique = True)
    date = db.Column(db.DateTime)
    #put unique contraint on epic url, 
    def __repr__(self):
        return f'<Epic epic_id = {self.epic_id}>'

class Rating(db.Model):
    """A rating."""

    __tablename__ = 'ratings'

    rating_id = db.Column(db.Integer,
                    autoincrement=True,
                    primary_key=True)
    rating = db.Column(db.Integer)
    donki_id = db.Column(db.Integer,
            db.ForeignKey("donki.donki_id"))
    epic_id = db.Column(db.Integer,
            db.ForeignKey("epic.epic_id"))     
    user_id = db.Column(db.Integer,
                        db.ForeignKey("users.user_id"))
    rating_date = db.Column(db.DateTime)
    comment = db.Column(db.Text)#should this be string or text?
    
    donki = db.relationship("Donki", backref="ratings")
    epic = db.relationship("Epic", backref = "ratings")
    user = db.relationship("User", backref="ratings") 

    def __repr__(self):
        return f'<Rating rating_id={self.rating_id} \nrating={self.rating}>'


def connect_to_db(flask_app, db_uri="postgresql:///space_weather", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

  # Potentially make fxn for tests.py sample data
    # def example_data():
    #     """Create some sample data."""
    
if __name__ == "__main__":
        from server import app

        # Call connect_to_db(app, echo=False) if your program output gets
        # too annoying; this will tell SQLAlchemy not to print out every
        # query it executes.

        connect_to_db(app)
        db.create_all()