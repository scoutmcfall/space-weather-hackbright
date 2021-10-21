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
    if "user_email" in session:
        return redirect ("/main")
    else:
        return render_template("login-signup.html")

@app.route("/main")
def mainpage():    
    """View former homepage containing EPIC photo and DONKI forecast"""
#get most recent epic photo
    file_url = 'https://epic.gsfc.nasa.gov/api/enhanced/'
    #get the filename first
    res = requests.get(file_url)
    search_result = res.json()
    filename = search_result[0]['image']
    filedate = search_result[0]['date'].split()
    epicdate = filedate[0].replace('-','/')
   
    img_url = 'https://epic.gsfc.nasa.gov/archive/enhanced/'+epicdate+'/png/'+filename +'.png'
    # print("******************")
    # print(epicdate, img_url)

#get DONKI forecast
    from datetime import date, timedelta, datetime
    today = date.today()
    startDate = str(today - timedelta(days=30))
    endDate = str(today)
    donki_url = 'https://api.nasa.gov/DONKI/WSAEnlilSimulations?startDate=' + startDate + '&endDate='+ endDate + '&api_key='+ API_KEY
    res = requests.get('https://api.nasa.gov/DONKI/WSAEnlilSimulations?startDate=' + startDate + '&endDate='+ endDate + '&api_key='+ API_KEY)
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
 
    return render_template("main.html", img_url=img_url, epicdate = epicdate, 
                        impact = impact, date = date, arrival = arrival, cme_speed = cme_speed, 
                        donki_url = donki_url, epic_url = img_url, blow = blow, 
                        arrival_statement = arrival_statement, format_cme_time = format_cme_time)


@app.route("/forward-backward-epic")
def forward_backward_epic():
    print(request.args)
    js_date = request.args.get("result")
    print(js_date)
    
    #convert date 
    date = js_date.split(" ")
    date = date[0:4]
    date = (" ").join(date)
    date_obj = (datetime.strptime(date, "%a %b %d %Y"))
    #use a python strftime to reformat date obj
    date_strng = (datetime.strftime(date_obj, "%Y-%m-%d"))
  
    #https://epic.gsfc.nasa.gov/api/enhanced/date/2015-10-31
    file_url = 'https://epic.gsfc.nasa.gov/api/enhanced/date/'+ date_strng
    print(file_url)
    #in order to page back in images, the back or forward buttons on the template
    #would reset the start date as a day forward or backwards 


    #get the filename first
    res = requests.get(file_url)
    print("************************")
    print(res)
    # if res:
    search_result = res.json()
    if search_result:
        filename = search_result[0]['image']
        filedate = search_result[0]['date'].split()
        filedate = filedate[0]
        print(filedate)
        epicdate = filedate.replace('-','/')
        # https://epic.gsfc.nasa.gov/archive/natural/2015/10/31/png/epic_1b_20151031074844.png
        img_url = 'https://epic.gsfc.nasa.gov/archive/enhanced/'+epicdate+'/png/'+filename +'.png'
        print(img_url)
        return {"img_url": img_url}
    else: 
        # put in some sad funny picture
        flash ("No photo for this date- was the Earth even there? Who knows.")
        img_url = "https://www.adgully.com/img/800/201906/earth-is-a-donut.jpg"
        return {"img_url": img_url}
    print(date_strng)
    return date_strng


@app.route("/get-historical-data")
def get_historical_data():
    """return donki report and epic photo for prior date range"""

    from datetime import date, timedelta, datetime
    today = date.today()
   

    s_date = str(request.args.get("sdate", today - timedelta(days=10)))
    e_date = str(request.args.get("edate", today))

    #deal with epic photo
    #https://epic.gsfc.nasa.gov/api/enhanced/date/2015-10-31
    file_url = 'https://epic.gsfc.nasa.gov/api/enhanced/date/'+ s_date
    #in order to page back in images, the back or forward buttons on the template
    #would reset the start date as a day forward or backward 

    #get the filename first
    res = requests.get(file_url)

    search_result = res.json()
  
    if search_result:
        filename = search_result[0]['image']
        filedate = search_result[0]['date'].split()
        epicdate = filedate[0].replace('-','/')
        # https://epic.gsfc.nasa.gov/archive/natural/2015/10/31/png/epic_1b_20151031074844.png
        img_url = 'https://epic.gsfc.nasa.gov/archive/enhanced/'+epicdate+'/png/'+filename +'.png'
    else: 
        flash ("Sorry! No EPIC photo of the Earth for that date.")


    #deal with donki forecast
    donki_url = 'https://api.nasa.gov/DONKI/WSAEnlilSimulations?startDate=' + s_date + '&endDate='+ e_date + '&api_key='+ API_KEY
    
    res = requests.get('https://api.nasa.gov/DONKI/WSAEnlilSimulations?startDate=' + s_date + '&endDate='+ e_date + '&api_key='+ API_KEY)
   
    search_results = res.json()
   
    if search_results:
        #pass the object in the render template so i'll have access in the html, and can pass it in the form
        report = search_results[-1]["impactList"] 
    
        if report:
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
    else:
        flash ("Sorry! No reports available for your selected date range. Please try again.")
   
    return render_template("main.html",  img_url=img_url, epicdate = epicdate, 
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

    return redirect("/main")

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
            return redirect ("/main")
        else:
            flash ("FAILURE")
            return redirect("/handle-login")
    else:
        flash ("DOES NOT EXIST. PLEASE TRY AGAIN")
        return redirect("/")

@app.route("/logout")
def handle_logout():
    """log out the user"""
#     session.clear
    for key in list(session.keys()):
        session.pop(key)
    flash ("You have successfully logged out.")
    return redirect("/")

@app.route("/rate", methods = ["POST"])
def handle_rating():
    """Log the rating."""
    from datetime import date
    rating = int(request.form.get("num_stars"))
    user_obj = crud.get_user_by_email(session["user_email"])
    user_id = user_obj.user_id
  
    donki_url = request.form.get("donki_url")
    epic_url = request.form.get("epic_url")
    #date = requests.form.get(date)
    rating_date = date.today()
    comment = request.form.get("comment")
    
    #create donki object 
    donki_object = crud.create_donki(date, donki_url)

    #create epic object: do something about repeats!
    epic_object = crud.create_epic(date, epic_url)
    
    #check to see if user has already rated this object
    if crud.search_ratings(user_id, epic_object.epic_id) == True:
        flash ("Sorry, you have already rated this photo of the earth. Please wait until there is a new one", "msg")  
    else:
        #create rating
        crud.create_rating(rating = rating, user_id = user_id, rating_date = rating_date,
                                donki_id = donki_object.donki_id, epic_id = epic_object.epic_id, comment = comment)
        average_photo_rating = crud.get_avg_photo_rating(epic_object.epic_id)
        flash (f"Success! You have rated this earth photo. Here's what it's been rated on average {average_photo_rating}", "msg")  

    return redirect("/main")

@app.route("/profile")
def display_profile():
        """display user details"""
        user_obj = crud.get_user_by_email(session["user_email"])
        user_id = user_obj.user_id
        
        num_rates = crud.get_total_user_rating(user_id)
        avg_user_rating = crud.get_avg_user_rating(user_id)
        return render_template("profile.html", num_rates = num_rates, avg_user_rating = avg_user_rating)
        
@app.route("/email-update", methods = ["POST"])
def update_email():
        """update email"""
        new_email = request.form.get("new_email")
        user = crud.get_user_by_email(new_email)
        email = session["user_email"]
        #check to see if new_email already in db, and change info if not
        if user:
                flash ("Sorry, taken, try again with a different email address.")
                return redirect("/profile")
        else:
                user = crud.update_user_email(email = email, new_email = new_email)
                session["user_email"] = user.email
                session["user_id"] = user.user_id
                return redirect("/profile")

@app.route("/password-update", methods = ["POST"])
def update_password():
        """update password"""
        email = session["user_email"]
        user = crud.get_user_by_email(email)
        password = request.form.get("change_password")
        new_password = request.form.get("new_password")
        #check to see if old password matches, and change password if it does
        if user.password == password:
                crud.update_user_password(email = email, password = password, new_password = new_password)

                flash ("Success! Your password has been changed.")
                return redirect ("/profile")
        else:
                flash ("FAILURE. Please reenter your current password for confirmation.")
                return redirect("/profile")
        
@app.route("/todo-list")
def todo_list():
    """react app showing interactive todo list"""
    return render_template("todolist.html")

    
if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)

    # app.run(debug=True)
    app.run(host="0.0.0.0", debug=True)