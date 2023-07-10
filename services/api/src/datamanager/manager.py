from src import mongo

"""
from post module

from manager import DataManager

class Post(...)
	
	pm = PostManager().get_manager()
	pm.save(json_data)

class PostManager(DataManager):
	def __init__(self):
		self.collection_name = "posts"
		self.manager = None

	def save(self, post):
		post = PostSchema().dump(json_data)	
		mongo.db.posts.insert_one(Post(post).__dict__)
		self.manager.insert_one(PostSchema().dump(post.__dict__))
		return True

	def get_post_by_id(self, id):
		post = self.manager.find_one({'_id':id})
		post = Post(post)
		return post

	def get_all(self):
		all_posts = [Post(post) for post in self.manager.get_data()]
		return all_posts

	def get_manager(self):
		if self.manager == None:
			self.manager = self.get_manager_for_class(self.collection_name)
		return self.manager


"""

class DataManager():

	def __init__(self):
		self.collection_name = None
		self.collection = None
		self.data = None

	def get_manager_for_class(self):
		# self.data_manager = mongo.db.get_collection(collection_name)
		self.collection = mongo.db.get_collection(self.collection_name)
		return self

	def get_collection(self):
		if self.collection_name:
			self.collection = mongo.db.get_collection(self.collection_name)
			return self.collection
		return "Please set data_manager first: DataManager.get_manager_for_class(collection_name=collection_name)"
	def get_data(self):
		self.data = self.collection.find({}) 
		return self.data 

	def is_empty(self):
		return self.collection.find_one({}) == None