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

def create_rating(rating, user_id= None, rating_date = None, donki_id = None, epic_id = None, comment = None):
    """Create and return a new rating."""
    rating = Rating(rating=rating,
                    user_id = user_id,
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
    
    result_obj = Rating.query.filter(Rating.user_id == user_id and Rating.epic_id == epic_id).first()
    
    if result_obj != None:
        return True
    else:
        return False

def get_avg_photo_rating(epic_id):
    """return average rating for epic photo."""
    #not sure if this is the right way to do it
    
    variable = Rating.query.filter(Rating.epic_id == epic_id).all()
    total = 0
    for i in variable:
        total  += i.rating
    return total/(len(variable))

def get_avg_user_rating(user_id):
    """return average of all ratings by user."""
    #not sure about this one either
    # user_obj = User.query.filter(User.user_id == user_id).first()
    variable =  Rating.query.filter(Rating.user_id == user_id).all()
    total = 0
    for i in variable:
        total += i.rating
    if len(variable) != 0:
        return total/(len(variable))
    else:
        return 0

def get_total_user_rating(user_id):
    """return number of all ratings by user."""
    #select rating from ratings where rating.user_id == user_id
    #so i need to get the user_id
    # user_obj = User.query.filter(User.user_id == user_id).first()
    rating_obj_list =  Rating.query.filter(Rating.user_id == user_id).all()
    # total = 0
    # for i in len(rating_obj_list):
    #     total += rating_obj
    return len(rating_obj_list)

def create_donki(date, donki_url = None):
    """Create and return a new donki unless the donki already exists."""
    donki_search = Donki.query.filter(Donki.donki_url == donki_url).first()
    if donki_search != None:
        return donki_search
    else:
        donki = Donki(donki_url = donki_url,
                    )
        db.session.add(donki)
        db.session.commit()
        return donki

def create_epic(date, epic_url = None):
    """Create and return a new item."""
    epic_search = Epic.query.filter(Epic.epic_url == epic_url).first()
    if epic_search != None:
        return epic_search
    else:
        epic = Epic(epic_url = epic_url
                    )
        db.session.add(epic)
        db.session.commit()
        #try to make a epic object, and if you get an error, then instead of making new one use existing one
        return epic


if __name__ == '__main__':
    from server import app
    connect_to_db(app)