from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_cors import cross_origin

from .entities.entity import Session, engine, Base
from .entities.exam import Exam, ExamSchema
from marshmallow import ValidationError

# creating the flask app
app = Flask(__name__)

# if needed generate db schema
Base.metadata.create_all(engine)

CORS(app) # support_credentials=True - (optional)

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

	return response

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
		print(data)
	except ValidationError as err:
		return err.messages, 422

	# check if exam already exists in db
	title, description = data["title"], data["description"]
	session = Session()
	exam = session.query(Exam).filter_by(title=title, description=description).first()
	if exam is None:
		# create new exam
		exam = Exam(title=title, description=description, created_by="HTTP post request")
		print(exam)
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