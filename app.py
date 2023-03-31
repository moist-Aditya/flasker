from flask import Flask, render_template, redirect, request

#create a Flask instance
app = Flask(__name__)

@app.route('/')
def index():
    name = "World"
    mylist = ['apple', 'banana', 'mango']
    return render_template("index.html", name=name, mylist=mylist)


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)



#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
