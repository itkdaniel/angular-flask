from flask import current_app
from flask_testing import TestCase
from src import create_app
import unittest
import os


app = create_app()

class TestDevelopmentConfig(TestCase):
	def create_app(self):
		app.config.from_object("src.config.DevelopmentConfig")
		return app

	def test_app_is_development(self):
		self.assertTrue(app.config['SECRET_KEY'] == "lostinthesauce")
		self.assertFalse(current_app is None)
		self.assertTrue(app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get("DATABASE_URL"))
		self.assertTrue(app.config['MONGO_URI'] == os.environ.get("MONGO_URL"))


class TestTestingConfig(TestCase):
	def create_app(self):
		app.config.from_object("src.config.TestingConfig")
		return app

	def test_app_is_testing(self):
		self.assertTrue(app.config['SECRET_KEY'] == "lostinthesauce")
		self.assertTrue(app.config['TESTING'])
		self.assertTrue(app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get("DATABASE_TEST_URL"))
		self.assertTrue(app.config['MONGO_URI'] == os.environ.get("MONGO_TEST_URL"))


class TestProductionConfig(TestCase):
	def create_app(self):
		app.config.from_object("src.config.ProductionConfig")
		return app

	def test_app_is_production(self):
		self.assertTrue(app.config['SECRET_KEY'] == "lostinthesauce")
		self.assertFalse(app.config['TESTING'])
		self.assertTrue(app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get("DATABASE_URL"))
		self.assertTrue(app.config['MONGO_URI'] == os.environ.get("MONGO_URL"))



if __name__ == '__main__':
	unittest.main()