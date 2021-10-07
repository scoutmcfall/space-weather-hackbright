"""Server for space weather app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud
import os
import requests
from jinja2 import StrictUndefined
from datetime import date, timedelta, datetime


app = Flask(__name__)

app.secret_key = "dev" 
app.jinja_env.undefined = StrictUndefined

API_KEY = os.environ["API_KEY"]

@app.route('/')
def homepage():
    """View homepage containing EPIC photo and DONKI forecast"""
#get epic photo
    file_url = 'https://epic.gsfc.nasa.gov/api/enhanced/date/'
    #get the filename first
    res = requests.get(file_url)
    search_result = res.json()
    filename = search_result[0]['image']
    filedate = search_result[0]['date'].split()
    epicdate = filedate[0].replace('-','/')
   
    img_url = 'https://epic.gsfc.nasa.gov/archive/enhanced/'+epicdate+'/png/'+filename +'.png'

#get DONKI forecast
    from datetime import date, timedelta, datetime
    today = date.today()
    #time_now = datetime.now()
    startDate = str(today - timedelta(days=30))
    endDate = str(today)
    #res = requests.get('https://api.nasa.gov/DONKI/WSAEnlilSimulations?startDate=2021-9-28&endDate=2021-9-28&api_key=DEMO_KEY')
    donki_url = 'https://api.nasa.gov/DONKI/WSAEnlilSimulations?startDate=' + startDate + 'endDate='+ endDate + '&api_key='+ API_KEY
    res = requests.get('https://api.nasa.gov/DONKI/WSAEnlilSimulations?startDate=' + startDate + 'endDate='+ endDate + '&api_key='+ API_KEY)
    search_results = res.json()
    #pass the object in the render template so i'll have access in the html, and can pass it in the form
    report = search_results[-1]['impactList'] #what to do if this is a null object?
    print(report)
    if report != None:
        report = search_results[-1]['impactList'][0]
        impact = report['isGlancingBlow']
        if impact == True:
                impact = "will"
        else:
                impact = "will not"
        datetime = report['arrivalTime'].split('T')
        date = datetime[0]
        arrival = report['arrivalTime'].split("T")[1]
        cme_speed = search_results[-1]['cmeInputs'][0]['speed']
    else:
        impact = "will not"
        date = search_results[-1]['modelCompletionTime'].split("T")[0]
        arrival = 'Sorry nope'
        cme_speed = search_results[-1]['cmeInputs'][0]['speed']
 
    return render_template('homepage.html', img_url=img_url, epicdate = epicdate, 
                        impact = impact, date = date, arrival = arrival, cme_speed = cme_speed, donki_url = donki_url, epic_url = img_url)

@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    print("********************")
    print(user)
    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        crud.create_user(email, password)
        flash("Account created! Please log in.")

    return redirect("/")

@app.route("/handle-login", methods = ["POST"])
def handle_login():
    """Log in the user."""
    
    email = request.form.get("login_email")
    password = request.form.get("login_password")
    # - use customers.get_by_email() to retrieve corresponding User
    #   object (if any)
    user = crud.get_user_by_email(email) #query to db
    # - if a Customer with that email was found, check the provided password
    #   against the stored one
    
    if user:
        if user.password == password:
            session["user_email"] = user.email #all routes have access to session
            session["user_id"] = user.user_id
            flash ("Success! Verified! Time to rate this photo of the earth.")
            return redirect ("/")
        else:
            flash ("FAILURE")
            return redirect("/handle-login")
    else:
        flash ("DOES NOT EXIST. PLEASE TRY AGAIN")
        return redirect("/")


@app.route("/rate", methods = ["POST"])
def handle_rating():
    """Log the rating."""
    from datetime import date
    rating = int(request.form.get("num_stars"))
    donki_url = request.form.get("donki_url")
    epic_url = request.form.get("epic_url")
    #date = requests.form.get(date)
    rating_date = date.today()
    comment = request.form.get("comment")
    #create donki object 
    donki_object = crud.create_donki(date, donki_url)

    #create epic object
    epic_object = crud.create_epic(date, epic_url)
    #create rating
    crud.create_rating(rating, session["user_id"], rating_date,
                        donki_object.donki_id, epic_object.epic_id, comment)


    #use crud function to change the rating to be an integer
    #use crud fxn to create a rating with that use and the time they're trying to rate
    #and the number of stars they're rating
    #they thing they're trying to rate might already be in th database so i have to check to see if 
    #other users have rated that same thing and show them together
    #something I can search by (primary key? generated url?)
    #have 1 crud fxn that does all of this together and makes it one database commit
    return redirect("/")

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)

    app.run(debug=True)
 #app.run(host="0.0.0.0", debug=True)