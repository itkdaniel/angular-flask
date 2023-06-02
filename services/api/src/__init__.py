import os
from flask import Flask
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_jwt_extended import JWTManager

cors = CORS()
bcrypt = Bcrypt()
jwt = JWTManager()
login_manager = LoginManager()

def create_app(script_info=None):
	# instantiate the app
	app = Flask(__name__)

	app_settings = os.getenv('APP_SETTINGS')
	app.config.from_object(app_settings)

	bcrypt.init_app(app)
	login_manager.init_app(app)
	jwt.init_app(app)
	cors.init_app(app)

	# register blueprints
	from src.api.exams import exams_blueprint
	app.register_blueprint(exams_blueprint)
	from src.api.users import users_blueprint
	app.register_blueprint(users_blueprint)

	return app