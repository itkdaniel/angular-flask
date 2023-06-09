import sqlalchemy
from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import ARRAY
from .entity import Entity, Base#, Session
from marshmallow import Schema, fields
# from flask_login import UserMixin
from src import login_manager, jwt
from src import db

# db = Session()

class User(db.Model,Entity, Base):
	__tablename__ = 'users'

	username = Column(String)
	password = Column(String)
	is_active = Column(Boolean)
	is_authenticated = Column(Boolean)
	is_anonymous = Column(Boolean)


	def __init__(self, username, password, created_by):
		Entity.__init__(self, created_by)
		self.username = username
		self.password = password
		self.is_active = True
		self.is_authenticated = False
		self.is_anonymous = False

@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
	identity = jwt_data["sub"]
	# return db.query(User).filter_by(id=identity).first()
	return User.query.filter_by(id=identity).first()

class UserSchema(Schema):
	id = fields.Number()
	username = fields.Str()
	password = fields.Str()
	created_at = fields.DateTime()
	updated_at = fields.DateTime()
	last_updated_by = fields.Str()
	is_active = fields.Boolean()
	is_authenticated = fields.Boolean()
	is_anonymous = fields.Boolean()