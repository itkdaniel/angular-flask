import os

class BaseConfig:
	"""Base Configuration"""
	SECRET_KEY = "lostin_thesauce"
	SESSION_TYPE = "filesystem"

class DevelopmentConfig(BaseConfig):
	"""Development Configuration"""
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')