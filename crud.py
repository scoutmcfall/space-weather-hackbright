"""CRUD operations for space weather app. """

from model import db, User, Donki, Epic, Rating, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

def create_rating(rating, user_id = None, rating_date = None, donki_id = None, epic_id = None, comment = None):
    """Create and return a new rating."""
    rating = Rating(rating=rating,
                    rating_date = rating_date,
                    donki_id = donki_id,
                    epic_id = epic_id,
                    comment = comment
                    )
  
    db.session.add(rating)
    db.session.commit()

    return rating

def search_ratings(user_id, epic_id):
   """return a rating object based on user_id and epic_id"""
    
    return Rating.query.filter(User.email == email and Epic.epic_id == epic_id).first()


def create_donki(date, donki_url = None):
    """Create and return a new item."""
    donki = Donki(donki_url = donki_url,
                )
    db.session.add(donki)
    db.session.commit()

    return donki

def create_epic(date, epic_url = None):
    """Create and return a new item."""
    epic = Epic(epic_url = epic_url
                )
    db.session.add(epic)
    db.session.commit()

    return epic


if __name__ == '__main__':
    from server import app
    connect_to_db(app)