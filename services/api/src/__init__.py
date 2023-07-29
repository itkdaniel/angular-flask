import os
from flask import Flask
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_pymongo import PyMongo
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_whooshee import Whooshee
from flask_session import Session
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from src.logging.api import ApiLogger
from flask_redis import Redis

logger = ApiLogger()

cors = CORS()
bcrypt = Bcrypt()
jwt = JWTManager()
login_manager = LoginManager()
db = SQLAlchemy()
fksession = Session() 
whooshee = Whooshee()
mongo = PyMongo()
redisdb = Redis()
migrate = Migrate()


UPLOAD_DIRECTORY = os.getenv('UPLOAD_DIR')
# LOG_DIRECTORY = os.path.dirname(os.path.realpath(__file__)) + '/tmp/logs/'
# if not os.path.exists(UPLOAD_DIRECTORY):
#     os.makedirs(UPLOAD_DIRECTORY)

def create_app(script_info=None):

	# instantiate the app
	app = Flask(__name__)
	# app_settings = os.getenv("APP_SETTINGS") if os.getenv("ENVIRONMENT") == "compose" else os.getenv("APP_SETTINGS_DOCKER")
	app_settings = os.getenv("APP_SETTINGS")
	app.config.from_object(app_settings)

	bcrypt.init_app(app)
	login_manager.init_app(app)
	jwt.init_app(app)
	cors.init_app(app)
	db.init_app(app)
	whooshee.init_app(app)
	mongo.init_app(app)
	redisdb.init_app(app)
	migrate.init_app(app,db)
	fksession.init_app(app)

	if not os.path.exists(UPLOAD_DIRECTORY):
		os.makedirs(UPLOAD_DIRECTORY)

	# if not os.path.exists(LOG_DIRECTORY):
	# 	os.makedirs(LOG_DIRECTORY)


	with app.app_context():
		db.create_all()
		db.session.commit()

	# register blueprints
	from src.api.exams import exams_blueprint
	app.register_blueprint(exams_blueprint)
	from src.api.users import users_blueprint
	app.register_blueprint(users_blueprint)
	from src.api.posts import posts_blueprint
	app.register_blueprint(posts_blueprint)
	from src.api.files import files_blueprint
	app.register_blueprint(files_blueprint)
	from src.api.chatgpt import chatgpt_blueprint
	app.register_blueprint(chatgpt_blueprint)
	from src.api.customers import customers_blueprint
	app.register_blueprint(customers_blueprint)
	from src.api.healthchecks import healthchecks_blueprint
	app.register_blueprint(healthchecks_blueprint)

	@app.shell_context_processor
	def ctx():
		return {'app':app,'db':db}

	return app