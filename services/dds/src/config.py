import os
import redis

redins = redis.Redis(host='redis',port=6379,db=0)

class BaseConfig:
	"""Base Config"""
	TESTING = False
	DEBUG = False
	SESSION_TYPE = os.environ.get('SESSION_TYPE')
	SECRET_KEY = os.environ.get('SECRET_KEY')

class DevelopmentConfig(BaseConfig):
	"""Development Config"""
	DEBUG = True
	SESSION_REDIS = redins
	MONGO_URI = os.environ.get('MONGO_URL')
	REDIS2_URL = os.environ.get('REDIS_OM_URL')

class TestingConfig(BaseConfig):
	"""Testing Config"""
	TESTING = True
	DEBUG = True
	SESSION_REDIS = redins
	MONGO_URI = os.environ.get('MONGO_URL')
	REDIS2_URL = os.environ.get('REDIS_OM_URL')

class ProductionConig(BaseConfig):
	"""Production Config"""
	SESSION_REDIS = redins
	MONGO_URI = os.environ.get('MONGO_URL')
	REDIS2_URL = os.environ.get('REDIS_OM_URL')

