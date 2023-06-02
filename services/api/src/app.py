from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_cors import cross_origin
from sqlalchemy import exc
from .entities.entity import Session, engine, Base
from .entities.exam import Exam, ExamSchema
from .entities.user import User, UserSchema
from marshmallow import ValidationError
import bcrypt

# creating the flask app
app = Flask(__name__)

# if needed generate db schema
Base.metadata.create_all(engine)

CORS(app) # support_credentials=True - (optional)

@app.route('/api/users', methods=['GET'])
def get_users():
	session = Session()
	user_objects = session.query(User).all()
	schema = UserSchema(many=True)
	users = schema.dump(user_objects)
	session.close()
	response = jsonify(users)

	return response, 200

@app.route('/api/users/register', methods=['POST'])
def register():
	response_object = {
		'status': 'success',
		'user': '',
		'message': ''
	}
	json_data = request.get_json()
	if not json_data:
		return {"message": "No input data provided"}, 400
	try:
		data = UserSchema(only=('username', 'password')).load(json_data)
	except ValidationError as err:
		return err.messages, 422
	username, password = data['username'], data['password']
	# check if username exists in db
	session = Session()
	user = session.query(User).filter_by(username=username).first()
	if user:
		response_object['username'] = username
		response_object['status'] = 'failed'
		response_object['message'] = 'Username already exists'
		return jsonify(response_object), 409

	# convert pw to array of bytes
	pwd_bytes = password.encode('utf-8')
	# generate salt
	salt = bcrypt.gensalt()
	# hash the pw
	hashed_pw = bcrypt.hashpw(pwd_bytes, salt)
	# create new user
	user = User(username=username, password=hashed_pw, salt=salt, created_by='HTTP post request')
	session.add(user)
	session.commit()
	# return created user and response object
	new_user = UserSchema().dump(user)
	session.close()
	response_object['user'] = new_user
	response_object['message'] = f'user: {username} created'

	return jsonify(response_object), 201


@app.route('/api/exams', methods=['GET'])
def get_exams():
	
	# fetching from db
	session = Session()
	exam_objects = session.query(Exam).all()

	# transform into JSON serializable obj
	schema = ExamSchema(many=True)
	exams = schema.dump(exam_objects)

	# serializing as JSON
	session.close()

	# build response
	response = jsonify(exams)

	#Enable Access-Control-Allow-Origin
	# response.headers.add("Access-Control-Allow-Origin", "*")
	# response.headers.add("Access-Control-Allow-Origin", "GET,POST,OPTIONS,DELETE,PUT")

	return response, 200

@app.route('/api/exam/<id>', methods=['GET'])
def get_exam(id):
	session = Session()

	try:
		exam = session.query(Exam).filter_by(id=id).first()
	except exc.ProgrammingError as err:
		return err.messages, 501
	
	schema = ExamSchema()
	exam = schema.dump(exam)
	response = jsonify(exam)

	return response, 200



# @cross_origin(origins = "http://localhost:4200") # optionl
@app.route('/api/exams', methods=['POST'])
def add_exam():

	# get json data
	json_data = request.get_json()
	if not json_data:
		return {"message": "No input data provided"}, 400

	# Validate and deserialize input
	# mount exam obj
	try:
		data = ExamSchema(only=('title', 'description')).load(json_data)
	except ValidationError as err:
		return err.messages, 422

	# check if exam already exists in db
	title, description = data["title"], data["description"]
	session = Session()
	exam = session.query(Exam).filter_by(title=title, description=description).first()
	if exam is None:
		# create new exam
		exam = Exam(title=title, description=description, created_by="HTTP post request")
		# persist exam
		session.add(exam)

	# commit current transaction to db	
	session.commit()

	# return created exam
	new_exam = ExamSchema().dump(exam)
	session.close()

	# build response
	response = jsonify(new_exam)

	#Enable Access-Control-Allow-Origin
	# response.headers.add("Access-Control-Allow-Origin", "*")

	return response, 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)