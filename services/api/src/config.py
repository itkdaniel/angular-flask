import os

class BaseConfig:
	"""Base Configuration"""
	TESTING = False
	DEBUG = False
	SESSION_TYPE = "filesystem"
	SECRET_KEY = os.environ.get('SECRET_KEY')
	UPLOAD_DIR = os.environ.get('UPLOAD_DIR')
	POSTGRES_USER = os.environ.get('POSTGRES_USER')
	POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
	MONGODB_DB = os.environ.get('MONGODB_DB')
	MONGODB_HOST = os.environ.get('MONGODB_HOST')
	MONGODB_PORT = os.environ.get('MONGODB_PORT')
	MONGODB_USERNAME = os.environ.get('MONGODB_USERNAME')
	MONGODB_PASSWORD = os.environ.get('MONGODB_PASSWORD')
	MONGODB_AUTH_SOURCE = os.environ.get('MONGODB_AUTH_SOURCE')
	MONGODB_INITDB_ROOT_USERNAME = os.environ.get('MONGODB_INITDB_ROOT_USERNAME')
	MONGODB_INITDB_ROOT_PASSWORD = os.environ.get('MONGODB_INITDB_ROOT_PASSWORD')

class DevelopmentConfig(BaseConfig):
	"""Development Configuration"""
	DEBUG = True
	if os.environ.get("ENVIRONMENT") == "compose":
		SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
		MONGO_URI = os.environ.get('MONGO_URL')
		REDIS_URL = os.environ.get('REDIS_OM_URL')
	else:
		os.environ['DATABASE_URL'] = os.environ.get('JENKINS_DATABASE_TEST_URL')
		os.environ['MONGO_URL'] = os.environ.get('JENKINS_MONGO_TEST_URL')
		SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
		MONGO_URI = os.environ.get('MONGO_URL')
		REDIS_URL = os.environ.get('REDIS_OM_URL')



class TestingConfig(BaseConfig):
	"""Testing Configuration"""
	TESTING = True
	DEBUG = True
	if os.environ.get("ENVIRONMENT") == "compose":
		SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')
		MONGO_URI = os.environ.get('MONGO_TEST_URL')
		REDIS_URL = os.environ.get('REDIS_OM_URL')

	else:
		os.environ['DATABASE_TEST_URL'] = os.environ.get('JENKINS_DATABASE_TEST_URL')
		os.environ['MONGO_TEST_URL'] = os.environ.get('JENKINS_MONGO_TEST_URL')
		SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')
		MONGO_URI = os.environ.get('MONGO_TEST_URL')
		REDIS_URL = os.environ.get('REDIS_OM_URL')



class ProductionConfig(BaseConfig):
	"""Production Configuration"""
	if os.environ.get("ENVIRONMENT") == "compose":
		SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
		MONGO_URI = os.environ.get('MONGO_URL')
		REDIS_URL = os.environ.get('REDIS_OM_URL')

	else:
		os.environ['DATABASE_URL'] = os.environ.get('JENKINS_DATABASE_TEST_URL')
		os.environ['MONGO_URL'] = os.environ.get('JENKINS_MONGO_TEST_URL')
		SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
		MONGO_URI = os.environ.get('MONGO_URL')
		REDIS_URL = os.environ.get('REDIS_OM_URL')
		
	
# class JenkinsDevelopmentConfig(BaseConfig):
	# """Jenkins Development Configuration """
	# SQLALCHEMY_DATABASE_URI = os.environ.get('JENKINS_DATABASE_URL')
	# MONGO_URI = os.environ.get('JENKINS_MONGO_URL')
	# os.environ['DATABASE_URL'] = os.environ.get('JENKINS_DATABASE_URL')
	# os.environ['MONGO_URL'] = os.environ.get('JENKINS_MONGO_URL')
# 
# 
# class JenkinsTestingConfig(BaseConfig):
	# """Jenkins Testing Configuration"""
	# TESTING = True
	# SQLALCHEMY_DATABASE_URI = os.environ.get('JENKINS_DATABASE_TEST_URL')
	# MONGO_URI = os.environ.get('JENKINS_MONGO_TEST_URL')
	# os.environ['DATABASE_TEST_URL'] = os.environ.get('JENKINS_DATABASE_TEST_URL')
	# os.environ['MONGO_TEST_URL'] = os.environ.get('JENKINS_MONGO_TEST_URL')
# 
# class JenkinsProductionConfig(BaseConfig):
	# """Jenkins Production Configuration"""
	# SQLALCHEMY_DATABASE_URI = os.environ.get('JENKINS_DATABASE_URL')
	# MONGO_URI = os.environ.get('JENKINS_MONGO_URL')
	# os.environ['DATABASE_URL'] = os.environ.get('JENKINS_DATABASE_URL')
	# os.environ['MONGO_URL'] = os.environ.get('JENKINS_MONGO_URL')
# 
