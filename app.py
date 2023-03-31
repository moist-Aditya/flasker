from flask import Flask, render_template, redirect, request

#create a Flask instance
app = Flask(__name__)


# Index Page
@app.route('/')
def index():
    return render_template("index.html")


# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")





# Error Handling --------------------------------

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500