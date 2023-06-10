import os
import json
import unittest
import datetime
from src.test.base import BaseTestCase
from src import mongo

class TestMongoDB(BaseTestCase):

	def test_mongo_database_exists(self):
		self.assertFalse(mongo.db == None)

	def test_mongo_collection_insert_one(self):
		result = mongo.db.test.insert_one({"x": 1})
		self.assertTrue(mongo.db.test.count_documents({}) == 1)

	def test_mongo_collection_insert_many(self):
		result = mongo.db.test.insert_many([{"x": i} for i in range(10)])
		self.assertTrue(mongo.db.test.count_documents({}) == 10)
		self.assertEqual(mongo.db.test.count_documents({}), 10)

	def test_mongo_collection_delete_one(self):
		result = mongo.db.test.insert_many([{"x": 1} for i in range(10)])
		result = mongo.db.test.delete_one({"x": 1})
		self.assertTrue(result.deleted_count == 1)
		self.assertTrue(mongo.db.test.count_documents({"x": 1}) == 9)

	def test_mongo_collection_delete_many(self):
		result = mongo.db.test.insert_many([{"x": 1} for i in range(10)])
		result = mongo.db.test.insert_many([{"x": 2} for i in range(10)])
		result = mongo.db.test.insert_many([{"x": 3} for i in range(10)])
		result = mongo.db.test.delete_many({"x": 2})
		self.assertTrue(result.deleted_count == 10)
		self.assertTrue(mongo.db.test.count_documents({}) == 20)

	def test_mongo_collection_find(self):
		result = mongo.db.test.insert_many([{"x": 1} for i in range(5)])
		result = mongo.db.test.insert_many([{"x": 2} for i in range(5)])
		self.assertEqual(len([doc for doc in mongo.db.test.find({"x":1})]), 5)
		self.assertEqual(mongo.db.test.count_documents({"x": 1}), 5)
		result = mongo.db.test.insert_one({"x":3})
		self.assertEqual(len([doc for doc in mongo.db.test.find({"x":3})]), 1)
		self.assertEqual(len([doc for doc in mongo.db.test.find({"y":1})]), 0)

	def test_mongo_collection_find_one(self):
		result = mongo.db.test.insert_many([{"x":1} for i in range(5)])
		result = mongo.db.test.insert_many([{"y":2} for i in range(5)])
		self.assertEqual(len([mongo.db.test.find_one({"x":1})]), 1)
		self.assertEqual(len([mongo.db.test.find_one({"y":2})]), 1)
		self.assertEqual(mongo.db.test.find_one({"z":3}), None)

	def test_mongo_collection_update_many(self):
		result = mongo.db.test.insert_many([{"x":1} for i in range(3)])
		result = mongo.db.test.insert_many([{"x":2} for i in range(3)])
		result = mongo.db.test.insert_many([{"x":3} for i in range(3)])
		result = mongo.db.test.update_many({"x":1},{"$inc": {"x":6}})
		self.assertEqual(result.modified_count, 3)
		self.assertEqual(result.matched_count, 3)
		self.assertEqual(len([doc for doc in mongo.db.test.find({"x":7})]), 3)

	def test_mongo_collection_update_one(self):
		result = mongo.db.test.insert_many([{"x":1} for i in range(3)])
		result = mongo.db.test.update_one({"x":1},{"$inc":{"x":6}})
		self.assertEqual(result.modified_count, 1)
		self.assertEqual(result.matched_count, 1)
		self.assertEqual(len([doc for doc in mongo.db.test.find({"x":7})]), 1)
		self.assertEqual(len([doc for doc in mongo.db.test.find({"x":1})]), 2)

	def test_mongo_collection_replace_one(self):
		result = mongo.db.test.insert_many([{"x":1} for i in range(5)])
		result = mongo.db.test.replace_one({"x":1},{"y":3})
		self.assertEqual(result.modified_count, 1)
		self.assertEqual(result.matched_count, 1)
		self.assertEqual(len([doc for doc in mongo.db.test.find({"y":3})]), 1)
		self.assertEqual(len([doc for doc in mongo.db.test.find({"x":1})]), 4)

	def test_mongo_collection_replace_upsert(self):
		result = mongo.db.test.insert_many([{"x":1} for i in range(5)])
		result = mongo.db.test.replace_one({"y":3}, {"z":5}, upsert=True)
		self.assertEqual(result.matched_count, 0)
		self.assertEqual(result.modified_count, 0)
		self.assertTrue(result.upserted_id)
		self.assertEqual(len([doc for doc in mongo.db.test.find({"y":3})]), 0)
		self.assertEqual(len([doc for doc in mongo.db.test.find({"x":1})]), 5)
		self.assertEqual(len([doc for doc in mongo.db.test.find({"z":5})]), 1)
		self.assertEqual(mongo.db.test.count_documents({}), 6)

	def test_mongo_collection_count_documents(self):
		result = mongo.db.test.insert_many([{"x":1} for i in range(5)])
		self.assertEqual(mongo.db.test.count_documents({}), 5)
		result = mongo.db.test.delete_many({"x":1})
		self.assertEqual(result.deleted_count, 5)
		self.assertEqual(mongo.db.test.count_documents({}), 0)

	def test_mongo_collection_drop(self):
		result = mongo.db.test.insert_many([{"x": i} for i in range(10)])
		mongo.db.test.drop()
		self.assertTrue(mongo.db.test.count_documents({}) == 0)
		self.assertFalse('test' in mongo.db.list_collection_names())



