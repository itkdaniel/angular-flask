from flask import Blueprint, jsonify, request
from src.entities.post import Post, PostSchema
from src.entities.entity import get_time_since_created
from flask_jwt_extended import current_user, jwt_required
from src.auth import authenticate_user, get_authenticated_user 
from src import mongo, bcrypt

posts_blueprint = Blueprint('posts', __name__)

@posts_blueprint.route('/api/posts', methods=["GET"])
def get_posts():
	# posts = [PostSchema().load(post) for post in mongo.db.posts.find({})]
	posts = [post for post in mongo.db.posts.find({})]
	for post in posts: post['time_since_created'] = get_time_since_created(post['created_at'])
	response = {"status": "success",
				"posts": posts}
	return jsonify(response), 200

@posts_blueprint.route('/api/posts', methods=["POST"])
def add_post():
	json_data = request.get_json()
	post = PostSchema().dump(json_data)
	# data = mongo.db.posts.insert_one(PostSchema().dump(Post(post)))
	data = mongo.db.posts.insert_one(Post(post).__dict__)
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


