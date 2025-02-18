## Baby Names Project

Simple project to learn flask basics and do baby name research based on SSA government data. The
data-dev.sqlite file 


### Run Locally
here's how to run locally with gunicorn:
gunicorn 'main:app' --access-logfile=- --error-logfile - --env FLASK_CONFIG=production


### Run with Docker
1. `docker pull ghcr.io/jackolantern11/baby_flask:latest`
2. `docker run ghcr.io/jackolantern11/baby_flask:latest -d -p 5000:5000`
