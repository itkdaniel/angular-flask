import os
import redis
from flask import Flask
from flask_cors import CORS
from flask_redis import Redis
from flask_pymongo import PyMongo
from flask_session import Session
from src.logging.api import Logger

logger = Logger()

cors = CORS()
# redisdb = redis.Redis(host='redis',port=6379,db=0)
mongo = PyMongo()
redisdb = Redis()
fksession = Session()

def create_app(script_info=None):

	app = Flask(__name__)

	app_settings = os.getenv("APP_SETTINGS")
	app.config.from_object(app_settings)

	cors.init_app(app)
	mongo.init_app(app)
	redisdb.init_app(app, 'REDIS2')
	fksession.init_app(app)

	from src.api.healthchecks import healthchecks_blueprint
	app.register_blueprint(healthchecks_blueprint)

	@app.shell_context_processor
	def ctx():
		return {'app':app,'db':db}

	return app
