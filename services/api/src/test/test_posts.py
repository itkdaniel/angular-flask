import os
import json
import unittest
import datetime
from src.entities.post import Post, PostSchema
from src.test.base import BaseTestCase
from src import mongo

class TestPostService(BaseTestCase):

	def test_app_is_testing(self):
		self.assertTrue(self.app.config['SECRET_KEY'], "lostinthesauce")
		self.assertTrue(self.app.config['TESTING'])
		self.assertTrue(self.app.config['MONGO_URI'] == os.environ.get("MONGO_TEST_URL"))

	def test_get_posts(self):
		mock_posts = self.mock_posts()
		mock_posts = PostSchema().dump(mock_posts[0])
		with self.client:
			response = self.client.post('/api/posts',data=json.dumps(mock_posts), content_type='application/json')
			response = self.client.get('/api/posts')
			data = json.loads(response.data.decode())
			self.assertEqual(data['status'], 'success')

			self.assertEqual(len(data['posts']), 1)
			self.assertEqual(response.status_code, 200)

	def test_mock_add_post(self):
		mock_posts = self.mock_posts()
		# mock_posts = PostSchema().dump(mock_posts[0])
		mock_posts = PostSchema().dump(mock_posts[0])
		with self.client:
			response = self.client.post('/api/posts', data=json.dumps(mock_posts), content_type='application/json')
			data = json.loads(response.data.decode())
			self.assertEqual(data['status'], 'success')
			self.assertEqual(data['num_posts'], 1)
			self.assertEqual(response.status_code, 201)

	def test_mock_add_posts(self):
		mock_posts = self.mock_posts()
		posts = PostSchema(many=True).dump(mock_posts)
		with self.client:
			response = self.client.post('/api/posts/many', data=json.dumps(posts), content_type='application/json')
			data = json.loads(response.data.decode())
			self.assertEqual(data['status'], 'success')
			self.assertEqual(data['num_posts'], 10)
			self.assertEqual(response.status_code, 201)

	def mock_posts(self):
		return [{'title':'post # ' + str(i),'caption':'caption for post # ' + str(i),'last_updated_by':'HTTP post request'} for i in range(10)]