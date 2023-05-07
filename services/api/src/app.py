from flask import Flask, jsonify, request
from flask_cors import CORS

from .entities.entity import Session, engine, Base
from .entities.exam import Exam, ExamSchema

# creating the flask app
app = Flask(__name__)

# if needed generate db schema
Base.metadata.create_all(engine)

CORS(app)

@app.route('/exams', methods=['GET'])
def get_exams():
	
	# fetching from db
	session = Session()
	exam_objects = session.query(Exam).all()

	# transform into JSON serializable obj
	schema = ExamSchema(many=True)
	exams = schema.dump(exam_objects)

	# serializing as JSON
	session.close()

	return jsonify(exams)

@app.route('/exams', methods=['POST'])
def add_exam():

	# mount exam obj
	posted_exam = ExamSchema(only=('title', 'description')).load(request.get_json())

	exam = Exam(**posted_exam.data, created_by="HTTP post request")

	# persist exam
	session = Session()
	session.add()
	session.commit()

	# return created exam
	new_exam = ExamSchema().dump(exam).date
	session.close()

	return jsonify(new_exam), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


# curl -X POST -H 'Content-Type: application/json' -d '{"title": "TypeScript Advanced Exam","description": "Tricky questions about TypeScript."}' http://localhost:5000/exams