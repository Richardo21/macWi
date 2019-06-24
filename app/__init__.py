from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'RANDOM KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://user:macwiusers@localhost/user" #driver://username:password(if any)@server/db-name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USE_SSL'] = True
# app.config.from_pyfile('config.cfg')
app.config['MAIL_USERNAME'] = 'richardocraigstewart'
app.config['MAIL_PASSWORD'] = 'millionssoonsoon'
PROFILE_IMAGES = ".app/static/profile_images"

mail = Mail(app)
db = SQLAlchemy(app)

#Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views