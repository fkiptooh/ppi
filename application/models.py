import flask
from flask_security import RoleMixin, UserMixin
from application import db
from werkzeug.security import generate_password_hash, check_password_hash

class Role(db.Document, RoleMixin):
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)

    def __unicode__(self):
        return self.name

class User(db.Document, UserMixin):
    user_id     =   db.IntField( unique=True )
    first_name  =   db.StringField( max_length=50 )
    last_name   =   db.StringField( max_length=50 )
    email       =   db.StringField( max_length=30, unique=True )
    active = db.BooleanField(default=True)
#     fs_uniquifier = db.StringField(max_length=64, unique=True)
    confirmed_at = db.DateTimeField()
    password    =   db.StringField( )
    roles = db.ListField(db.ReferenceField(Role), default=[])

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def get_password(self, password):
        return check_password_hash(self.password, password)    

class Course(db.Document):
    courseID   =   db.StringField( max_length=10, unique=True )
    title       =   db.StringField( max_length=100 )
    description =   db.StringField( max_length=255 )
    credits     =   db.IntField()
    term        =   db.StringField( max_length=25 )

class Enrollment(db.Document):
    user_id     =   db.IntField()
    courseID    =   db.StringField( max_length=10 )
    courseTitle       =   db.StringField( max_length=100 )
