from flask import Blueprint, jsonify, request
from src.entities.user import User, UserSchema#, db
from src import bcrypt, login_manager
from src.auth import authenticate_user, get_authenticated_user
from sqlalchemy import exc
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required
from src import db

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/api/users/login', methods=['POST'])
def login():
	response = {
		'status':'success',
		'message':'',
		'user': '',
		'access_token': '',
		'refresh_token': ''
	}
	json_data = request.get_json()
	data = UserSchema(only=('username','password')).load(json_data)
	username, password = data["username"], data["password"]
	# user = db.query(User).filter_by(username=username).first()
	# user = User.query.filter_by(username=username).first()
	user = User.query.filter_by(username=username).first()
	if user and bcrypt.check_password_hash(user.password, password):
		# login_user(user,remember=True)
		access_token, refresh_token = authenticate_user(user)
		# user = db.query(User).filter_by(username=username).first()
		user = User.query.filter_by(username=username).first()
		response['access_token'] = access_token
		response['refresh_token'] = refresh_token
		response['user'] = user.username
		response['message'] = f"user: {user.username} is logged in"
		return jsonify(response)
	else:
		response['status'] = "failed"
		response['message'] = "Please try again"
		return jsonify(response)


@users_blueprint.route('/api/users', methods=['GET'])
def get_users():
	# user_list = db.query(User).all()
	user_list = User.query.all()
	schema = UserSchema(many=True)
	users = schema.dump(user_list)
	response = jsonify(users)

	return response, 200

def create_user(username, password):
	# user = db.query(User).filter_by(username=username).first()
	user = User.query.filter_by(username=username).first()
	if user is None:
		hashed_pw = bcrypt.generate_password_hash(password).decode("utf-8")
		user = User(username=username,password=hashed_pw,created_by='HTTP post request')
		db.session.add(user)
		db.session.flush()
		db.session.commit()
		new_user = UserSchema().dump(user)
		return new_user
	else:
		db.session.rollback()
	return None

@users_blueprint.route('/api/users/register', methods=['POST'])
def register():
	response = {
		'user': '',
		'message': '',
		'status': 'failed',
	}
	json_data = request.get_json()
	data = UserSchema(only=('username','password')).load(json_data)
	username, password = data['username'], data['password']
	user = create_user(username,password)
	if user:
		response['user'] = user
		response['status'] = 'success'
		response['message'] = f'user: {username} created'
		return jsonify(response), 201
	else:
		response['message'] = f'user: {username} already exists'
		return jsonify(response), 409


@users_blueprint.route("/api/users/status", methods=["POST"])
def check_status():
	json_data = request.get_json()
	username = json_data.get("username")
	try:
		user = get_authenticated_user(username)
	except ValidationError as e:
		return e.messages, 422
	if user.is_authenticated:
		return jsonify({"user": user.username,"status": True})
	return jsonify({"status": False})

@users_blueprint.route("/api/users/logout", methods=["GET"])
@jwt_required()
def logout():
	# logout_user()
	return jsonify({"logout": True})

