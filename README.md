## Baby Names Project

Simple project to learn flask basics and do baby name research based on SSA government data


### Run Locally
here's how to run locally with gunicorn:
gunicorn 'main:app' --access-logfile=- --error-logfile - --env FLASK_CONFIG=production


### Docker Build Notes
build docker image 
docker login 192.168.17.9:3000
docker build -t 192.168.17.9:3000/zfreeze/baby_flask:latest .
docker push 192.168.17.9:3000/zfreeze/baby_flask:latest

docker run -d -p 5000:5000 --name baby_flask 192.168.17.9:3000/zfreeze/baby_flask

flask --app main (run/shell etc.)
flask --app hello:create_app(local_auth=True) run


flask --app main.py --debug run

### ToDo:

Data Pipeline:
* Move data to proper database (SQLLITE or MySQL) - Use SQL Alchemy
* Bash Script to download the names report on schedule, clear mongo, and insert all to mongo

Report Stuff:
* Add graph labels for M/F
* Show what year a name was most popular total number and by proportion
* Write header/footer details html
* Create basic home page
* Set up MongoDB instead of csv file - cron job or something to pull data yearly?

Docker Stuff:
* Docker Compose File to build and test
* Secure forms

Security:
* HTTPS / token stuff
* Cookie options

@ToDo - Male & Female combined and Male & Female Separated
@ToDo - Names with similar popularity
@ToDo - Top Names of Last Year - Past 5/10/25/50/100 years
@ToDo - Random Name Generator
@ToDo - What year was 'x' name the most popular
@ToDo - Find all similar names to a name graph and table
@ToDo - compare in all lowercase


-- Query to get totals by gender per year:
select fdiq._id, fdiq.year, fdiq.name, fdiq.gender, fdiq.count, sum(fdiq.count)
OVER (PARTITION BY year, gender) AS year_gender_toal
from federal_data fdiq;


-- Query to get data w/ total names in year:
select fd._id, fd.year, fd.name, fd.gender, fd.count, sum(fd.count)
OVER (PARTITION BY fd.year) AS year_total
from federal_data fd;
