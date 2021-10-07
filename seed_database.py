"""Drop database/createdatabase/create tables/populate database w/data--using data from data/movies.json to create movies
& create 10 rando users; for each user, create 10 ratings on random movies with random scores"""

import os
import json
from random import choice, randint
from datetime import datetime
import crud, model, server

os.system('dropdb space_weather')
os.system('createdb space_weather')

model.connect_to_db(server.app)
model.db.create_all()

# with open('data/movies.json') as f:
#     movie_data = json.loads(f.read())

#can use the python faker library

# Create movies, store them in list so we can use them
# to create fake ratings later

# for item in item_data:# item data will be undefined until i can read in a file
#     url = (
#         item['url'],
#     )
    #release_date = datetime.strptime(movie['release_date'],'%Y-%m-%d')
#db_item = crud.create_item('garbage string')
db_donki1 = crud.create_donki(donki_url = 
    'this would be a link to a donki forecast', date = 2021-10-2)
db_epic1 = crud.create_epic(epic_url = 
    'this would be an link to the epic photo', date = 2021-10-2)
items_in_db = [db_donki1, db_epic1]


for n in range(10):
    email = f'user{n}@test.com'  # make a unique email
    password = 'test'

# create a user 
    user = crud.create_user(email, password)
# create 10 ratings for the user
    for _ in range(5):
        random_item = choice(items_in_db)
        rating = randint(1, 10)
        crud.create_rating(user, rating)