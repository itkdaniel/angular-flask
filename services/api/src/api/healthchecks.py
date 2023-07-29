from flask import request, Blueprint, jsonify
from src.configs.colors import Colors 
from src import logger
import requests
import asyncio
import json

logger = logger.create_logger('HealthLogger')
healthchecks_blueprint = Blueprint('healthchecks', __name__)

@healthchecks_blueprint.route('/api/frontend/healthcheck/',methods=['GET'])
def healthcheck_frontend():
	"""
		Endpoint used for frontend angular docker healthcheck
	"""
	response = {'healthstatus':'healthy','message':'ok 😀'}
	return jsonify(response)
	# 😀😵

@healthchecks_blueprint.route('/healthcheck',methods=['GET'])
def healthcheck_api():
	"""
		Endpoint used for api docker healthcheck
	"""
	response = '200 OK 😀'
	return jsonify(response)
	
