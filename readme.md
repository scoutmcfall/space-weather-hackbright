

# space_weather
## Hello! and welcome to space_weather (we've been expecting you)
[Watch a demo here!](https://youtu.be/2KJWplzIRFQ)
### Description

**space_weather is a subtle tool for starting your day with a gentle existential reset. The main page shows a photo of Earth from NASA's EPIC API, with the opportunity to rate the photo from 1-5 stars and leave a comment. Accompanying this is the most recent report on coronal mass ejections from NASA's DONKI API. User data is stored in a PostgreSQL database and accessed using SQLAlchemy in Python. The front end is styled with Bootstrap and custom CSS, and utilizes Javascript, HTML, and React.js. Each user's profile describes their rating stats and has the option to change their info. After contemplating their stellar insignificance, the user can create a to-do list so that they're approaching their day with renewed prioritization.**

![login page](/home/hackbright/src/space-weather/static/Screen Shot 2021-11-09 at 3.35.27 PM.png)

> “space_weather is like those meditation or ‘focus’ apps, but instead of becoming present by playing a Tibetan bell or water sounds, you’re confronted with the vastness of the universe and prompted to think about your place in it before setting your life goals. It all makes sense now.” -Sharat Chandra, data scientist

> “Not only is this website the Hot or Not of our beloved planet Earth, but it also helped me get my life in order! The to-do list feature is simple and effective at organizing how I need to spend my day, and I appreciate that the site will alert me if all those earthly schemes are for naught due to an impending coronal mass ejection. It’s a beautifully designed site that is sure to be used and beloved by generations to come!” -Jered Parkin, Renaissance Knower of People

> "This well crafted website is a gentle stroll through the internet of old, featuring motifs and fonts that harken to the days when you would research vikings on vikings.com. One may mistake the year to be 1998 if not for the modern user-friendly interface as well as the large date and time displayed on the homepage." - user, engineer for US government nuclear program

~~The world is flat.~~ The world is a donut?

![main page, rate a photo of the earth!](/home/hackbright/src/space-weather/static/Screen Shot 2021-11-09 at 3.36.08 PM.png)

### Tech Stack
- Python 
- PostgreSQL
- Flask 
- Jinja 
- HTML 
- CSS 
- React 
- Bootstrap 
- Javascript 
- JQuery

![main page, gif of coronal mass ejection](/home/hackbright/src/space-weather/static/Screen Shot 2021-11-09 at 3.36.18 PM.png)

### Features
- Users can access current and historical data from NASA's OPEN APIs (EPIC & DONKI) in a pleasant and userful format.
- Users can use the to-do list to organize their life.
- Users can review their average Earth photo ratings on their unique profile page.

![profile page](/home/hackbright/src/space-weather/static/Screen Shot 2021-11-09 at 3.36.52 PM.png)

### Installation Instructions

1. `git clone` the url for this project
2. Create a virtual environment: `virtualenv env`
3. Activate your virtual environment: `source env/bin/activate`
4. `pip3 install -r requirements.txt`
5. Start the server: `python3 server.py`
6. You can get your own API key from NASA [here](https://api.nasa.gov/)
7. Or just use their demo key.
8. Make a `secrets.sh` file to hold the API key

![react to-do list](/home/hackbright/src/space-weather/static/Screen Shot 2021-11-09 at 3.37.18 PM.png)


*The incredible loading gif comes from digital artist: [Lin Jacqueline](https://linjacqueline.com/) *

### About the Developer
Scout is driven to understand their world and to build relationships. This has taken them from bicycle advocacy in Seattle to divinity school in Nashville,  from English instruction in Barcelona to tax preparation in Oregon. Scout is curious, adaptable, and a quick learner, and they're looking for the security and dignity that software development work offers. Ready for a stable career in a developing field, Scout loves  coding so far and is ready to take this step to live their life the way they want.


<!-- 
### Horizontal Rule

--- -->
