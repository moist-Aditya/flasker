from flask import Flask, render_template, redirect, request, url_for

#create a Flask instance
app = Flask(__name__)


# Index Page
@app.route('/')
def index():
    return render_template("index.html")


# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg=''
    # if 'login_btn' in request.form:
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Print the data entered
        print(username + ' - ' + password)


        # Code for checking credential goes here
        if username=='aditya' and password=='hello':
            # Redirect to logged in page here
            # msg = 'Login Successful!!'
            return redirect(url_for('loggedin', username=username))
        else:
            msg = 'Login Unsuccessful :('
        # End Code for checking credential


        if not username or not password:
            msg = 'Please fill the correct info'

    return render_template("login.html", msg=msg)


# Logged in successfully
@app.route('/user/<username>')
def loggedin(username):
    return render_template('user.html', username=username)



# Error Handling --------------------------------

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500