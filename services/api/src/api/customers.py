from flask import request, Blueprint, jsonify
from redis_om import Migrator
from src import redisdb, logger
from src.models.base import create_date, get_time_passed
from src.models.customer import Customer, CustomerOM
from src.configs.colors import Colors 
from .utils import create_customer, mapper, transformer,logcustomer
import json

logger = logger.create_logger('CustomerLogger')
customers_blueprint = Blueprint('customers', __name__)

@customers_blueprint.route('/api/customers/ping', methods=['GET'])
def ping_pong():
	"""
		Endpoint used to check the health of the customers API service
	"""
	response = {'status':'success',
				'message':'pong'}
	logger.info('Test customer ping - {} success {}'.format(Colors.LIGHT_GREEN,Colors.DEFAULT))
	return jsonify(response), 200

@customers_blueprint.route('/api/customers/test',methods=['POST'])
def test_customer_create():
	"""
		Endpoint used to test customer creation
	"""
	response = {'status':'failed'}
	test_customerOM = CustomerOM(first_name='Betty',
							last_name='Gore',
							email='betty.gore@test.com',
							age=37,
							bio='Test bio info 🔥',
							created_by='HTTP post request',
							created_at=create_date())
	
	test_customerOM.save()
	test_customerOM.incr('person_counter')
	CustomerOM.db().json().set('person:{}'.format(CustomerOM.db().get('person_counter')), '$', test_customerOM)
	assert CustomerOM.get(test_customerOM.pk) == test_customerOM
	logger.debug('Assert db.get(customer) - {} passed{}'.format(Colors.LIGHT_GREEN,Colors.DEFAULT))
	logger.info('Test customer creation: {} {} - {}success{}'.format(test_customerOM.first_name,
																	test_customerOM.last_name,
																	Colors.LIGHT_GREEN,
																	Colors.DEFAULT))
	logger.info('Test customer pk -{} {}{}'.format(Colors.YELLOW,test_customerOM.pk,Colors.DEFAULT))
	response['status'] = 'success'
	response['message'] = '{} {} is a valid customer'.format(test_customerOM.first_name,
															test_customerOM.last_name)
	return jsonify(response), 201

@customers_blueprint.route('/api/customers',methods=['POST'])
def customer_create():
	"""
		Endpoint used to create a customer and save to redis
	"""
	# get_data = lambda json_data: [value for value in json_data.values()]
	response = {'status':'failed'}
	json_data = request.get_json()
	logger.debug('json_data: {}'.format(json_data))
	# data = get_data(json_data)
	# first_name, last_name, email, age, bio = [*get_data(json_data)]
	# [*json_data] = [*json_data.values()]
	customer = create_customer(**json_data)
	customer.save()
	CustomerOM.db().incr('customer_counter')
	CustomerOM.db().json().set('customer:{}'.format(CustomerOM.db().get('customer_counter')), '$', customer.json())
	mapping = mapper(**json_data)
	# logger.debug('first_name: {}, last_name: {}, email: {}, age: {}, bio: {}'.format(customer.first_name, 
	# 																				customer.last_name, 
	# 																				customer.email, 
	# 																				customer.age, 
	#																				customer.bio))
	
	transform = transformer(*mapping)																		
	logger.debug('{}, {}, {}, {}, {}'.format(*transform))
	response['status'] = 'success'
	response['customer'] = json.loads(customer.json())
	return jsonify(response)

@customers_blueprint.route('/api/customers/test/<lname>',methods=['GET'])
def test_get_customers_by_last_name(lname):
	"""
		Endpoint used to test fetch customers from redis - by last name and age
	"""
	response = {'status':'failed'}
	Migrator().run()
	result = CustomerOM.find((CustomerOM.last_name == lname)).all()
	# cust_hash = CustomerOM.get("01H3PZPXN5VR1T930FGZE8A6J0")
	# result = CustomerOM.find((CustomerOM.pk == '01H3MGCMXJ8WQWBBXD0XQK7CEC')).all()
	# result = CustomerOM.get('01H3MGCMXJ8WQWBBXD0XQK7CEC').json()
	result = [{**json.loads(r.json())} for r in result]
	response['status'] = 'success'
	response['customers'] = result
	# response['customter hash'] = json.loads(cust_hash.json())
	logger.debug("result: ",result)
	# logger.debug("customer hash: ", cust_hash)
	# logger.debug(response)
	return jsonify(response)

@customers_blueprint.route('/api/customers/<pk>',methods=['GET'])
async def get_customer(pk):
	"""
		Endpoint used to fetch a customer from redis by pk
	"""
	response = {'status':'failed'}
	customer = CustomerOM.get(pk)
	customer.__dict__['time_passed'] = get_time_passed(customer.created_at)
	# customer = CustomerOM.db().json().get('customer:3')
	# response['customer'] = customer
	logcustomer(customer)
	response['status'] = 'success'
	response['customer'] = json.loads(customer.json())
	# response['time_passed'] = get_time_passed(customer.created_at)
	return jsonify(response)

@customers_blueprint.route('/api/customers/update/<pk>',methods=['PATCH'])
def update_customers(pk):
	"""
		Endpoint used to update models matching the query to the given field value pairs
		**CURRENTLY** only manually updates with timestamp 
	"""
	"""
		patch for pk<01H3MGCMXJ8WQWBBXD0XQK7CEC> - tstamp: 1687536686.001702
	"""
	response = {'status':'failed'}
	# Migrator().run()
	customer = CustomerOM.get(pk)
	customer.update(tstamp=customer.created_at.timestamp())
	response['status'] = 'success'
	response['updated_customer'] = json.loads(customer.json())
	return jsonify(response)

@customers_blueprint.route('/api/customers/timepassed/<pk>',methods=['GET'])
async def time_passed(pk):
	"""
		Endpoint usded to get time passed since creation
	"""
	response = {'status':'failed'}
	customer = CustomerOM.get(pk)
	time_passed = get_time_passed(customer.created_at)
	response['status'] = 'success'
	response['time_passed'] = time_passed
	return jsonify(response)