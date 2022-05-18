from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine
# from flask_restx import Api
from flask_admin import Admin
from flask_admin import AdminIndexView
from flask import redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash

from flask_admin.contrib.mongoengine import ModelView
from flask_admin.menu import MenuLink
from flask_security import Security, current_user, MongoEngineUserDatastore, \
    auth_required

# api = Api()

app = Flask(__name__)
app.config.from_object(Config)

security = Security()

db = MongoEngine()
db.init_app(app)
# api.init_app(app)

from application.models import User, Role
app.user_datastore = MongoEngineUserDatastore(db, User, Role)
security.init_app(app, app.user_datastore)

from application import routes
from application import models


# class AdminView(ModelView):
#     def is_accessible(self):
#         return current_user.has_role('admin')

#     def inaccessible_callback(self, name, **kwargs):
#         return redirect (url_for('signIn', next=request.url))

# class HomeAdminView(AdminIndexView):
#     def is_accessible(self):
#         return current_user.has_role('admin')

#     def inaccessible_callback(self, name, **kwargs):
#         return redirect (url_for('security.login', next=request.url))


# admin = Admin(app, 'UTA_Enrollment Admin Dashboard', url='/admin',
# index_view=HomeAdminView(name='Home'))

admin = Admin(app)
admin.add_view(ModelView(User))
admin.add_view(ModelView(Role))
admin.add_view(ModelView(models.Course))
admin.add_view(ModelView(models.Enrollment))

admin.add_link(MenuLink(name='Logout', category='', url='/logout'))

# admin.add_view(AdminView(models.User))
# admin.add_view(AdminView(Role))
# admin.add_view(AdminView(models.Course))
# admin.add_view(AdminView(models.Enrollment))

# admin.add_link(MenuLink(name='Logout', category='', url='/logout'))

# @app.before_first_request
# def create_user():
#     if not app.user_datastore.find_user(email="test@me.com"):
#         app.user_datastore.create_user(email="test@me.com", password=generate_password_hash("password"))
