import os
import json
import unittest
import datetime
from src.test.base import BaseTestCase

class TestUserService(BaseTestCase):

	def test_app_is_testing(self):
		self.assertTrue(self.app.config['SECRET_KEY'], "lostinthesauce")
		self.assertTrue(self.app.config['TESTING'])
		self.assertTrue(self.app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get("DATABASE_TEST_URL"))

	def test_login(self):
		self.register_user()
		with self.client:
			response = self.client.post(
				'/api/users/login',
				data=json.dumps({'username':'test@test.com','password':'test123'}),
				content_type='application/json')
			data = json.loads(response.data.decode())
			self.assertIn('success',data['status'])
			self.assertEqual(response.status_code, 200)

	def test_register(self):
		response = self.register_user()
		data = json.loads(response.data.decode())
		self.assertIn('success', data['status'])
		self.assertEqual(response.status_code, 201)

	def test_register_duplicate_username(self):
		response = self.register_user()
		response = self.register_user()
		data = json.loads(response.data.decode())
		self.assertEqual(response.status_code, 409)

	def test_get_users(self):
		self.register_user()
		with self.client:
			response = self.client.get('/api/users')
			data = json.loads(response.data.decode())
			self.assertGreaterEqual(len(data), 1, "no registered users")


