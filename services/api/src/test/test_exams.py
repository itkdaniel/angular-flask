import os
import json
import unittest
import datetime
from src.test.base import BaseTestCase

class TestExamService(BaseTestCase):

	def test_app_is_testing(self):
		self.assertTrue(self.app.config['SECRET_KEY'], "lostinthesauce")
		self.assertTrue(self.app.config['TESTING'])
		self.assertTrue(self.app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get("DATABASE_TEST_URL"))

	def test_add_exam_not_logged_in(self):
		with self.client:
			response = self.client.post(
				'/api/exams', 
				data=json.dumps({'title':'Test Exam','description':'This is a test'}), 
				content_type='application/json')
			data = json.loads(response.data.decode())
			self.assertEqual(response.status_code, 201)
			self.assertIn('HTTP post request', data['last_updated_by'])

	def test_add_exam_logged_in(self):
		self.register_user()
		access_token, username = self.login_user()
		headers = {'Authorization': "Bearer {}".format(access_token)}
		with self.client:
			# add exam after login
			response = self.client.post(
				'/api/exams',
				data=json.dumps({'title':'Test Exam 2','description':'This is a test exam'}),
				headers=headers,
				content_type='application/json')
			data = json.loads(response.data.decode())
			self.assertIn('Test Exam 2',data['title'])
			self.assertIn(username, data['last_updated_by'])

	def test_exams_not_logged_in(self):
		with self.client:
			response = self.client.get('/api/exams')
			data = json.loads(response.data.decode())
			self.assertIn('login to view your exams', data['message'])

	def test_exams_logged_in(self):
		self.register_user()
		access_token, username = self.login_user()
		headers = {'Authorization': "Bearer {}".format(access_token)}
		self.add_with_login(headers)
		with self.client:
			response = self.client.get(
				'/api/exams',
				headers=headers)
			data = json.loads(response.data.decode())
			print(data)
			self.assertGreaterEqual(len(data), 1, "data is empty")

	def add_with_login(self, headers):
		with self.client:
			# add exam after login
			response = self.client.post(
				'/api/exams',
				data=json.dumps({'title':'Test Exam 3','description':'This is a test exam'}),
				headers=headers,
				content_type='application/json')
			data = json.loads(response.data.decode())



