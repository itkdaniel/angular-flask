import requests
from flask import request, Blueprint, jsonify, session
from flask_session import Session
from src.configs.colors import Colors
from src import logger, redisdb, mongo

logger = logger.create_logger(__name__)

healthchecks_blueprint = Blueprint('healthchecks', __name__)

@healthchecks_blueprint.route('/dds/healthcheck',methods=['GET'])
def healthcheck():
	"""
		Endpoint used to check endpoints health
	"""
	response = '200 OK 😀'
	logger.info(f'status: {response}')
	return jsonify(response)

@healthchecks_blueprint.route('/dds/healthcheck/mongo', methods=['GET'])
def mongo_healthcheck():
	"""
		Endpoint to check health of mongo flask service
	"""
	response = '200 OK 😀'
	collection = mongo.db.list_collection_names()
	logger.debug(f'collections: {collection}' if collection is not None else f'Not connected to mongo.db')
	return jsonify(response)
