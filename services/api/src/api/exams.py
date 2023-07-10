from flask import Blueprint, jsonify, request
# from src.entities.entity import engine, Base
from src.entities.exam import Exam, ExamSchema#, db
from sqlalchemy import exc
from marshmallow import ValidationError
from flask_jwt_extended import current_user, jwt_required, get_jwt_identity
from src.auth import get_authenticated_user
from src import db

exams_blueprint = Blueprint('exams', __name__)

@exams_blueprint.route('/api/exams/ping',methods=['GET'])
def ping_pong():
	return jsonify({'status':'success','message':'pong'})

@exams_blueprint.route('/api/exams', methods=['GET'])
@jwt_required(optional=True)
def get_exams():
	current_identity = get_jwt_identity()
	if current_identity:
		# exam_list = db.query(Exam).filter_by(last_updated_by=current_user.username)
		exam_list = Exam.query.filter_by(last_updated_by=current_user.username)
		schema = ExamSchema(many=True)
		exams = schema.dump(exam_list)
		response = jsonify(exams)
		return response, 200
	else:
		# exam_list = db.query(Exam).all()
		return jsonify({"message": "login to view your exams"})

@exams_blueprint.route('/api/exams/all',methods=['GET'])
def getall_exams():
	exam_list = Exam.query.all()
	schema = ExamSchema(many=True)
	exams = schema.dump(exam_list)
	response = jsonify(exams)
	return response

@exams_blueprint.route('/api/exam/<id>', methods=['GET'])
def get_exam(id):
	try:
		# exam = db.query(Exam).filter_by(id=id).first()
		exam = Exam.query.filter_by(id=id).first()
	except exc.ProgrammingError as e:
		return e.messages, 501
	schema = ExamSchema()
	exam = schema.dump(exam)
	response = jsonify(exam)

	return response, 200

@exams_blueprint.route('/api/exams', methods=['POST'])
def add_exam():
	json_data = request.get_json()
	if not json_data:
		return jsonify({"message": "No input data provided"}), 400
	try:
		data = ExamSchema(only=('title','description')).load(json_data)
	except ValidationError as e:
		return e.messages, 422
	title, description = data['title'], data['description']
	try:
		exam = create_exam(title, description)
		response = jsonify(exam)
		return response, 201
	except exc.IntegrityError as e:
		response = jsonify({'message': 'database error'})
		return response, 201

@jwt_required(optional=True)
def create_exam(title, description):
	try:
		# exam = db.query(Exam).filter_by(title=title,description=description).first()
		exam = Exam.query.filter_by(title=title,description=description).first()
		if exam is None: # add exam to db
			current_identity = get_jwt_identity()
			if current_identity:
				exam = Exam(title=title,description=description,created_by=current_user.username)
			else:
				exam = Exam(title=title,description=description,created_by='HTTP post request')
			db.session.add(exam)
			db.session.flush()
			db.session.commit()
			new_exam = ExamSchema().dump(exam)
			return new_exam
	except exc.IntegrityError as e:
		db.session.rollback()
	return exam
