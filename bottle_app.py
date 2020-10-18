# A very simple Bottle Hello World app for you to get started with...
import os
import sqlite3
from bottle import get, post, template, request, redirect

# are we executing at PythonAnywhere?
ON_PYTHONANYWHERE = "PYTHONANYWHERE_DOMAIN" in os.environ

# assert ON_PYTHONANYWHERE == True

if ON_PYTHONANYWHERE:
    # on PA, set up to connect to the WSGI server
    from bottle import default_app
else:
    # on the development environment, import the development server
    from bottle import run, debug


@get('/')
def get_colors_list():
    connection = sqlite3.connect("colors.db")
    cursor = connection.cursor()
    cursor.execute("select * from colors")
    result = cursor.fetchall()
    cursor.close()
    return template("show_colors_list", rows=result)




@get("/get_add_color")
def get_add_color():
    return template("add_color")


@post("/add_color")
def add_color_to_db():
    color = request.forms.get("color").strip()
    flower = request.forms.get("flower").strip()
    connection = sqlite3.connect("colors.db")
    cursor = connection.cursor()
    cursor.execute("insert into colors (color, flower) values (?,?)", (color, flower))
    # cursor.lastrowid
    connection.commit()
    cursor.close()
    redirect("/")





if ON_PYTHONANYWHERE:
    # on PA, connect to the WSGI server
    application = default_app()
else:
    # on the development environment, run the development server
    debug(True)
    run(host='localhost', port=8080)

