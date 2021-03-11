[//]:# (README file)
Python-Flask-Web-Application-Practice: Blog
==
This repository is a text-only blog web application created using python Flask. Each posts can be view by public, but only registered users are able to create new posts. Only the author of the post can update or delete the post. The user can delete their own account, and all the posts the user authored will be deleted as well.

## Prerequisites
* Python 2.7 or 3.6+
* pip
## Installation
First clone the repository, and start a virtual enviroment. 
```
$ pip install -r requirements.txt
```
```
$ python app.py
```
## Libraries
##### Authentication
* Flask-Login - Flask user session management such as logging in, logging out, and remembering user's session.
* Werkzeug.security - Quick and simple security form Flask applications. It handles salting and hashing the password (not reversable), and authentication. 
##### Database
* Flask_sqlalchemy - Extension for Flask that adds support for SQLAlchemy to application. Two tables are used, one for user accounts and one for blog posts. 
##### Database Migration
* Flask_migrate - SQLAlchemy database migrations for Flask applications using Alembic.
##### Data Vlidation
* Flask_wtf - Simple integration of Flask and WTForms.
* wtform - A flexible forms validation and rendering library for web development. 
##### Image Handling 
* PIL - An image library that adds support for opening, manipulating, and saving many image file formats. 
## Demo
[Application deployed on Heroku](https://flask-blog-sample.herokuapp.com/)

## Versioning
Version 1.0 (First deployment)

## To do list
* Method to retrieve password
* Remove avatar image file when account is being deleted 
* Warning message for failed logins

## License

The contents of this repository are covered under the [MIT](LICENSE) License.

## Acknowledgments
Jose Portilla's [Udemy Course](https://www.udemy.com/course/python-and-flask-bootcamp-create-websites-using-flask/)
