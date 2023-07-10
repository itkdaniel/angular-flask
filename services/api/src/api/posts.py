from flask import Blueprint, jsonify, request
from src.configs.colors import Colors
from src.entities.post import Post, PostSchema, PostManager
from src.entities.entity import get_time_since_created
from src.api.utils import exectimer
from flask_jwt_extended import current_user, jwt_required
from src.auth import authenticate_user, get_authenticated_user 
from src import mongo, bcrypt, logger
from aiohttp import ClientSession
import asyncio
import requests
import json

urls = ['http://localhost/api/posts/location','http://localhost/api/posts/time','http://localhost/api/posts/locate/address','http://localhost/api/posts/all/posts']

posts_blueprint = Blueprint('posts', __name__)

@posts_blueprint.route('/api/posts', methods=["GET"])
def get_posts():
	# posts = [PostSchema().load(post) for post in mongo.db.posts.find({})]
	posts = [post for post in mongo.db.posts.find({})]
	for post in posts: post['time_since_created'] = get_time_since_created(post['created_at'])
	response = {"status": "success",
				"posts": posts}
	return jsonify(response), 200

@posts_blueprint.route('/api/posts/all/posts',methods=['GET'])
def get_all_posts():
	manager = PostManager()
	posts = manager.get_all()
	for post in posts: post['time_since_created'] = get_time_since_created(post['created_at'])
	return jsonify(posts)

@posts_blueprint.route('/api/posts', methods=["POST"])
def add_post():
	json_data = request.get_json()
	post = PostSchema().dump(json_data)
	# data = mongo.db.posts.insert_one(PostSchema().dump(Post(post)))
	data = mongo.db.posts.insert_one(Post(_props=post).__dict__)
	response = {"status": "success",
				"num_posts": mongo.db.posts.count_documents({})}
	return jsonify(response), 201 

@posts_blueprint.route('/api/posts/many', methods=["POST"])
def add_posts():
	json_data = request.get_json()
	posts = PostSchema(many=True).dump(json_data)
	data = mongo.db.posts.insert_many([Post(post).__dict__ for post in posts])
	# data = mongo.db.posts.insert_many([PostSchema().dump(Post(post)) for post in posts])
	response = {"status": "success",
				"num_posts": mongo.db.posts.count_documents({})}
	return jsonify(response), 201 

@posts_blueprint.route('/api/posts/get', methods=['GET'])
def fetch_posts():
	logger.logger.info('Fetching posts from api endpoint - posts')
	location = requests.request('GET', 'http://localhost/api/posts/location')
	time = requests.request('GET',' http://localhost/api/posts/time')
	address = requests.request('GET',' http://localhost/api/posts/locate/address')
	manager = PostManager()
	posts = manager.get_all()
	for post in posts: post['time_since_created'] = get_time_since_created(post['created_at'])
	response ={"status":"success",
				"posts": posts,
				'location': location.json(),
				'time': time.json(),
				'address': address.json()
				}
	return jsonify(response), 200

async def fetch_url(session, url):
	response = await session.get(url)
	logger.logger.debug('async response:{} {}, {}{}'.format(Colors.YELLOW, response.status,response.url,Colors.DEFAULT))
	# logger.logger.debug('async response url dir: {} {}'.format(Colors.LIGHT_PURPLE, dir(response.url)))
	endpoint = str(response.url).split('/')[-1]
	content = await response.text()
	content = json.loads(content)
	# logger.logger.info(f'Response[url:{response.url},endpoint:{endpoint},content:{content},status:{response.status}]')
	# logger.logger.info(f'{Colors.YELLOW}dir(content) - {Colors.GREEN}{dir(content)}{Colors.DEFAULT}')
	return {'endpoint': endpoint,'content':content,'status':response.status}

@exectimer
@posts_blueprint.route('/api/posts/get/async', methods=['GET'])
async def fetch_posts_async():
	response={'status':'success'}
	# logger.logger.debug(f'{Colors.LIGHT_BLUE} urls [{urls}]')
	try:
		async with ClientSession() as session:
			tasks = []
			for url in urls:
				logger.logger.info(f'Fetching from endpoint: {Colors.LIGHT_BLUE}{url}{Colors.DEFAULT}')
				task = asyncio.create_task(fetch_url(session,url))
				tasks.append(task)
			responses = await asyncio.gather(*tasks)
	except Exception as e:
		response['status'] = 'failed'
		response['error'] = type(e).__name__
		response['message'] = e
		print(response)
		logger.logger.error(f'{Colors.LIGHT_RED} {response}')
		return jsonify(response)
	else:
		for r in responses:
			response[r['endpoint']] = {'content':r['content'],'status_code':r['status']}
	# response = json.dumps(response)
	# logger.logger.info(f'{Colors.LIGHT_PURPLE}{response}{Colors.DEFAULT}')
	return jsonify(response), 200

@posts_blueprint.route('/api/posts/add', methods=['POST'])
def create_post():
	json_data = request.get_json()
	r = requests.request('GET', 'http://localhost/api/posts/get')
	manager = PostManager()
	# title, caption = json_data.get('title'), json_data.get('caption')
	# post_data = {'title':title,'caption':caption}
	# post = Post(title=title,caption=caption,created_by='HTTP post request')
	# post = PostSchema().dump(post.__dict__)
	post = manager.api_save(json_data,created_by='HTTP post request')
	# post = PostSchema().load(Post(post))
	response = {'status':'success',
				'post': manager.collection.find_one({'title':json_data.get('title')})
				}
	return jsonify(response), 201

@posts_blueprint.route('/api/posts/get/<id>', methods=['GET'])
def get_post_by_id(id):
	manager = PostManager()
	post = manager.get_post_by_id(id=id)
	post['time_since_created'] = get_time_since_created(post['created_at'])
	response = jsonify(post)
	return response, 200

@posts_blueprint.route('/api/posts/location', methods=['GET'])
def get_location():
	# from urllib.request import urlopen; import json
	# from geopy.geocoders import Nominatim
	# data = json.load(urlopen("http://ipinfo.io/json"))
	response = requests.request('GET', 'http://ipinfo.io/json').json()
	return jsonify(response), 200

@posts_blueprint.route('/api/posts/time', methods=['GET'])
def get_time():
	response = requests.request('GET', 'http://worldtimeapi.org/api/ip').json()
	return jsonify(response)		

@posts_blueprint.route('/api/posts/locate/address', methods=['GET'])
def get_address():
	from geopy.geocoders import Nominatim
	geolocator = Nominatim(user_agent="angular-flask-api")
	coordinates = requests.request('GET', 'http://localhost/api/posts/location').json()['loc']
	location = geolocator.reverse(coordinates)
	address = location.address
	# response = {'location': location.raw,
			# 'address': address}
	response = location.raw['address']

	return jsonify(response), 200


# def tryfn(*args):
#      try:
#              l = list(*args)
#              print(f'valid args, expected 1, got->{len(args)}')
#              print(f'forcing error type error int + str')
#              print(f's = 1 + args[0] == {1 + args[0]}')
#              s = 1 + args[0]
#              print(f'valid expression, expected type agreement, got {type(1)} + {type(args[0])}')
#              t = 1 + args[0]
#      except Exception as e:
#              print(f'invalid expression, cannot add {type(1)} and {type(args[0])}')
#              print(f'got exception error name {e}')
#              print(f'e is type->{type(e)}')
#              print(f'error type -> {type(e).__name__}')
#              dir(e)
#              print(f'printing and raising exception e')
#              print(e)
#              raise e
#      return args

