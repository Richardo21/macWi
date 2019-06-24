from . import db
from werkzeug.security import generate_password_hash

class User(db.Model):
    
    __tablename__= "user"
    
    id = db.Column(db.Integer, primary_key= True)
    firstname = db.Column(db.String(40))
    lastname = db.Column(db.String(40))
    username = db.Column(db.String(40), unique = True)
    dob = db.Column(db.String(20))
    profile_img = db.Column(db.String(100))
    password = db.Column(db.String(20))
    
    def __init__(self,firstname,lastname,username,dob,profile_img,password):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.dob = dob
        self.profile_img = profile_img
        self.password = generate_password_hash(password, method= 'pbkdf2:sha256')
        
        
        
        
        