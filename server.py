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
#get most recent epic photo
    file_url = 'https://epic.gsfc.nasa.gov/api/enhanced/'
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
    report = search_results[-1]["impactList"] 
  
    if report != None:
        report = search_results[-1]['impactList'][0]
        impact = report['isGlancingBlow']
        if impact == True:
            impact = "will"
            blow = "Just a glancing blow, whatever that means."
            arrival = report["arrivalTime"].split("T")[1]
            arrival_statement = "Time of impact:" + arrival
            cme_speed = search_results[-1]["cmeInputs"][0]["speed"]
            cme_time = search_results[-1]["cmeInputs"][0]["cmeStartTime"].split("T")[1]
            format_cme_time = cme_time[:-1]
            date = search_results[-1]["cmeInputs"][0]["cmeStartTime"]
        else:
            impact = "will not"
            datetime = report["arrivalTime"].split("T")
            date = search_results[-1]["cmeInputs"][0]["cmeStartTime"].split("T")[0]
            cme_time = search_results[-1]["cmeInputs"][0]["cmeStartTime"].split("T")[1]
            format_cme_time = cme_time[:-1]
            arrival = ""
            arrival_statement = ""
            cme_speed = search_results[-1]["cmeInputs"][0]["speed"]
            blow = ""
    else:
        impact = "will not"
        date = search_results[-1]['modelCompletionTime'].split("T")[0]
        arrival = ""
        arrival_statement = ""
        cme_speed = search_results[-1]['cmeInputs'][0]['speed']
        cme_time = search_results[-1]["cmeInputs"][0]["cmeStartTime"].split("T")[1]
        format_cme_time = cme_time[:-1]
        blow = ""
 
    return render_template("homepage.html", img_url=img_url, epicdate = epicdate, 
                        impact = impact, date = date, arrival = arrival, cme_speed = cme_speed, 
                        donki_url = donki_url, epic_url = img_url, blow = blow, 
                        arrival_statement = arrival_statement, format_cme_time = format_cme_time)

@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
 
    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        user = crud.create_user(email, password)
        session["user_email"] = user.email #all routes have access to session
       
        flash("Account created! You are logged in. Time to rate this photo of the earth.")

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
    
    #check to see if user has already rated this object
    #SELECT rating_id FROM ratings WHERE session["user_id"] AND epic_object.epic_id;
    if crud.search_ratings(session["user_id"], epic_object.epic_id):
        flash ("Sorry, you have already rated this photo of the earth. Please wait until there is a new one")    
    else:
        #create rating
        crud.create_rating(rating, session["user_id"], rating_date,
                                donki_object.donki_id, epic_object.epic_id, comment)
        average_rating = crud.get_avg_rating(epic_object.epic_id)
        flash ("Success! You have rated this earth photo. Here's what it's been rated on average" + average_rating)  

    return redirect("/")

@app.route("/profile", methods = ["GET"])
def display_profile():
        """display user details"""
        #SELECT * FROM ratings WHERE user_id = session["user_id"]
        #whatever the length of that is = num_rates
        return render_template("profile.html")
        
@app.route("/profile-update", methods = ["POST"])
def update_profile():
        """update email and/or passowrd"""
#         #get email from session object
#         #use get user by email in crud?
#         #then i have the user.password- did i have that before?
#         #display template including input boxes for old password and two new passwords
#         #probably a good example out there
#         #loading screen then redirect to home page?
#         #eventually display all the images the user has rated plus their ratings?
        email = request.form.get("change_email")
        password = request.form.get("change_password")
        new_email = request.form.get("new_email")
        new_password = request.form.get("new_password")
#         # - use customers.get_by_email() to retrieve corresponding User
#         #   object (if any)
        user = crud.get_user_by_email(email) #query to db
#         # - if a Customer with that email was found, check the provided password
#         #   against the stored one
        
        if user:
                if user.password == password:
                        user.password = new_password
                        user.user_email = new_email
                        flash ("Success! Your information has been updated.")
                        return redirect ("/profile")
                else:
                        flash ("FAILURE")
                        return redirect("/profile")
        else:
                flash ("DOES NOT EXIST. PLEASE TRY AGAIN")
                return redirect("/profile")

#         #include these variables in the return eventually num_rates = num_rates, user.user_email = user.user_email, 
#         return render_template("profile.html")

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)

    app.run(debug=True)
 #app.run(host="0.0.0.0", debug=True)