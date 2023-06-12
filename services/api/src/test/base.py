from flask_testing import TestCase
# from src.entities.entity import engine, Base
from src.entities.user import User#, db as user_db
from src.entities.exam import Exam#, db as exam_db
# from src.auth import authenticate_user
from src import create_app, db, mongo
import json
import os

class BaseTestCase(TestCase):
	app = create_app()
	# mongo = mongo.init_app(app)	
	
	def create_app(self):
		self.app.config.from_object("src.config.TestingConfig")
		return self.app

	def setUp(self):
		self.users, self.exams = User.__table__, Exam.__table__
		# with self.app.app_context():
		db.session.remove()
		db.drop_all()
		db.create_all()
		db.session.commit()
		mongo.init_app(self.app)
		# mongo.db.drop_collection("posts")




	def tearDown(self):
		# user_db.close()
		# exam_db.close()
		# self.users.drop(bind=engine)
		# self.exams.drop(bind=engine)
		# self.users.create(engine)
		# self.exams.create(engine)
		# with self.app.app_context():
		db.session.remove()
		db.drop_all()
		db.create_all()
		db.session.commit()
		db.session.close()
		mongo.db.drop_collection("test")
		mongo.db.drop_collection("posts")

	def register_user(self):
		with self.client:
			response = self.client.post(
				'/api/users/register',
				data=json.dumps({'username':'test@test.com','password':'test123'}),
				content_type='application/json')
			return response

	def login_user(self):
		with self.client:
			response = self.client.post(
				'/api/users/login',
				data=json.dumps({'username':'test@test.com','password':'test123'}),
				content_type='application/json')
			data = json.loads(response.data.decode())
			return data['access_token'], data['user']


	