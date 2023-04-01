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


# Logged in successfully (Main home page)
@app.route('/user/<username>')
def loggedin(username):
    return render_template('user.html', username=username)


# New user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    msg=''

    # Temporary database
    # Delete after mySQL database setup
    emails=['abcd@gmail.com']
    usernames=['aditya']
    
    if request.method == 'POST':

        # Store inputs in variables
        f_name = request.form['f_name']
        l_name = request.form['l_name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        
        # Print the data entered
        print("Name - "+f_name+l_name+"\nEmail - "+email+"\nUsername - "+username+"\nPassword - "+password)


        # Code for checking credential goes here
        # Change this to work with mySQL instead of list
        if not f_name or not l_name or not email or not username or not password:
            msg='Please fill all data correctly'
        elif email in emails:
            msg='<strong>Sorry!</strong> - This Email is already registered with us'
        elif username in usernames:
            msg='<strong>Sorry!</strong> - This Username is already in use'
        elif email not in emails or username not in usernames:
            msg='<strong>Registration Successful!</strong> - Please Login'
            bs='alert-success'

            # Enter code to add data to mySQL below
            # 
            # 
            # 
            # Code above

    return render_template('register.html', msg=msg)


# Error Handling --------------------------------

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500