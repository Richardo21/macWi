import os
from app import app,db
from flask import redirect, render_template, url_for, request, flash
from app import mail
from datetime import datetime
from flask_mail import Message
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import RegistrationForm, LoginForm, Dashboard, ContactForm
from app.models import User
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash


def resource():
    return ""


@app.route("/")
def home():
    return render_template('home.html')
    
@app.route("/newaccount", methods= ['GET','POST'])
def newaccount():
    form = RegistrationForm()
    if (request.method == "POST") and (form.validate_on_submit()):
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        username = request.form['username']
        dob = request.form['dob']
        file = request.files['profile_img']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['PROFILE_IMAGES'], filename))
        password = request.form['password']
        
        user = User.query.filter_by(username = username).first()
        
        for newuser in user:
            if newuser == user:
                flash('Username already exits. Choose another username', 'danger')
                return redirect(url_for('newaccount'))
            else:
                newUser = User(firstname = firstname, lastname = lastname, username = username, dob = dob, profile_img = filename, password = password)
                db.session.add(newUser)
                db.session.commit()
                flash('Profile created successfully!', 'success')
                return redirect(url_for('dashboard'))
    return  render_template("newaccountform.html", form = form)

@app.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if (request.method == 'POST') and (form.validate_on_submit()):
        username = request.form['username']
        password = request.form['password']
        
        # user = User.query.filter_by(username = username).first()
        # if user is not None and check_password_hash(user.password, password):
        login_user(user)
        flash('Logged in successfully!','success')
        return redirect(url_for('dashboard'))
        # else:
        #     flash('User is not found.','danger')
    return render_template("loginform.html", form = form)

@app.route("/about")
def about():
    return render_template("about.html")
    
@app.route("/dashboard", methods= ['GET','POST'])
def dashboard():
    form = Dashboard()
    # date = datetime.now()
    date = datetime.today().strftime('%Y-%m-%d')
    if (request.method == "POST"):
        return render_template("dashboard.html", form = form, date = date)
        
@app.route("/contact", methods = ['GET','POST'])
def contact():
    form = ContactForm()
    if (request.method == 'POST') and (form.validate_on_submit()):
        msg = Message(request.form['subject'], sender = (request.form['email']), recipients = ['richardocraigstewart@gmail.com'])
        msg.body = request.form['message']
        mail.send(msg)
        flash('Message sent successfully! We will get back to you within a day','success')
    return render_template("contactform.html", form = form)
    

# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
# @login_manager.user_loader
# def load_user(id):
#     return UserProfile.query.get(int(id))

###
# The functions below should be applicable to all Flask apps.
###

# @app.route('/<file_name>.txt')
# def send_text_file(file_name):
#     """Send your static text file."""
#     file_dot_text = file_name + '.txt'
#     return app.send_static_file(file_dot_text)


# @app.after_request
# def add_header(response):
#     """
#     Add headers to both force latest IE rendering engine or Chrome Frame,
#     and also to cache the rendered page for 10 minutes.
#     """
#     response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
#     response.headers['Cache-Control'] = 'public, max-age=0'
#     return response


# @app.errorhandler(404)
# def page_not_found(error):
#     """Custom 404 page."""
#     return render_template('404.html'), 404
    

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port="8080")