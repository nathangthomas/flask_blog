# Welcome to Flask Blog
This application was created as an exercise to further explore the Python framework Flask.

## Table of Contents
<!--ts-->
   * [Set Up](#set-up)
   * [Live App](#live-app)
   * [Tech Stack](#tech-stack)
<!--te-->

## **Set Up**

### Clone repo
```
https://github.com/nathangthomas/flsk_blog
```
### Run flask_blog Locally
- Type `python3 run.py` in your terminal to spin up your server.
- Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser to interact with the app.
- Run the test suite ...

## Live App
(This functionality is not currently set up.)
You can also interact with a live version of Flask Blog hosted on Heroku [HERE](https://canteen-chronicles.herokuapp.com).

## Tech Stack:
### This app was built with the following:
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [SQLite(development DB)](https://www.sqlite.org/index.html)
- [PostgresQL(production DB)](https://www.postgresql.org/)

## Deploying a Flask App to Heroku:
- `pip install gunicorn`
- `pip freeze > requirements.txt`
- Ensure your requirements.txt is in the project root folder, else your heroku application will fail to deploy.
- Create a Procfile in the project root folder and add the following line:
`web: gunicorn run:flask_blog`
- Save and commit all changes then ... `git push heroku master`
