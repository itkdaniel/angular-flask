import sqlalchemy
from sqlalchemy import Column, String
from .entity import Entity, Base
from marshmallow import Schema, fields
from src.datamanager.manager import DataManager
from src import db, mongo
import uuid
from random import randint
from datetime import datetime


class Post(Entity):

	__tablename__ = 'posts'

	title = Column(String)
	caption = Column(String)



	def __init__(self, _id:any=None, _props=None, title=None, caption=None, created_by=None,**kwargs):
		Entity.__init__(self, _props['last_updated_by']) if created_by is None and _props is not None and _props['last_updated_by'] else setattr(self, "last_updated_by", created_by), setattr(self, "created_at", self.get_current_time_pdt()), setattr(self, "updated_at", self.get_current_time_pdt())
		print(f'Initializing the Post object...')
		self.title = _props['title'] if title is None and _props is not None else title
		self.caption = _props['caption'] if caption is None and _props is not None else caption
		self._id = uuid.uuid4().hex if _id is None or _props is None or '_id' not in _props else _props['_id'] if _id is None else _id
		if kwargs:
			for name,value in kwargs.items():
				setattr(self,name,value)
		print(f'from Post.__init__():\n\t{self}')


	def __repr__(self):
		class_name = type(self).__name__
		quote = "'"
		open_bracket = "{"
		close_bracket = "}"
		string_id = "'_id':"
		_id = self._id if '_id' in self.__dict__ else None
		string_title = "'title':"
		title = self.title
		comma = ","
		string_caption = "'caption':"
		caption = self.caption
		string_last_updated_by = "'last_updated_by':"
		last_updated_by = self.last_updated_by
		string_created_at = "'created_at':"
		created_at = self.created_at
		string_updated_at = "'updated_at':"
		updated_at = self.updated_at

		return (f'{class_name}(_props={open_bracket}'
				f'{string_id}{quote}{_id}{quote}{comma}'
				f'{string_title}{quote}{title}{quote}{comma}'
				f'{string_caption}{quote}{caption}{quote}{comma}'
				f'{string_last_updated_by}{quote}{last_updated_by}{quote}{comma}'  
				f'{string_created_at}{quote}{created_at}{quote}{comma}'  
				f'{string_updated_at}{quote}{updated_at}{quote}{close_bracket})')
	

	def __str__(self):
		class_name = type(self).__name__
		quote = "'"
		open_bracket = "{"
		close_bracket = "}"
		string_id = "'_id': "
		_id = self._id if '_id' in self.__dict__ else None
		string_title = "'title': "
		title = self.title
		comma = ","
		string_caption = "'caption': "
		caption = self.caption
		string_last_updated_by = "'last_updated_by': "
		last_updated_by = self.last_updated_by
		string_created_at = "'created_at': "
		created_at = self.created_at
		string_updated_at = "'updated_at': "
		updated_at = self.updated_at

		return (f'{open_bracket}\n\t'
				f'{string_id}{_id}{comma}\n\t' 
				f'{string_title}{title}{comma}\n\t' 
				f'{string_caption}{caption}{comma}\n\t' 
				f'{string_last_updated_by}{last_updated_by}{comma}\n\t' 
				f'{string_created_at}{created_at}{comma}\n\t' 
				f'{string_updated_at}{updated_at}\n{close_bracket}')


class PostManager(DataManager):

	class_body = """

	def __init__(self):
		DataManager.__init__(self)
		self.collection_name = 'posts'
		self.manager = self.get_manager_for_class()

	def save(self, json_data):
		# post = PostSchema().dump(json_data)	
		post = Post(json_data)
		post = self.collection.insert_one(post.__dict__)
		return post

	def get_post_by_id(self, id):
		post = self.collection.find_one({'_id':id})
		post = Post(post)
		return post

	def get_all(self):
		all_posts = [Post(post) for post in self.manager.get_data()]
		return all_posts

	def get_manager(self):
		return self.manager

	"""

	class_dict = {}

	def __init__(self):
		DataManager.__init__(self)
		self.collection_name = 'posts'
		self.manager = self.get_manager_for_class()

	def save(self, json_data,created_by):
		post = PostSchema().dump(json_data)	
		post = Post(_props=post, created_by=created_by)
		# post = PostSchema().dump(post.__dict__)
		post = self.collection.insert_one(post.__dict__)
		return post

	def api_save(self,json_data,created_by):
		title, caption = json_data.get('title'), json_data.get('caption')
		# post_data = {'title':title,'caption':caption}
		# post = Post(title=title,caption=caption,created_by=created_by)
		post = Post(_props=json_data,created_by=created_by)
		# post = PostSchema().dump(post.__dict__)
		post = self.collection.insert_one(post.__dict__)
		return post

	def get_post_by_id(self, id):
		post = self.collection.find_one({'_id':id})
		# post = Post(post)
		return post

	def get_all(self):
		# all_posts = [Post(_props={'_id':post['_id'],'title':post['title'],'caption':post['caption'],'created_at':post['created_at'],'updated_at':post['updated_at'],'last_updated_by':post['last_updated_by']}) for post in self.manager.get_data()]
		all_posts = [post for post in self.manager.get_data()]
		return all_posts

	def get_manager(self):
		return self.manager

class PostSchema(Schema):
	id = fields.Number()
	_id = fields.Str()
	title = fields.Str()
	caption = fields.Str()
	created_at = fields.DateTime()
	updated_at = fields.DateTime()
	last_updated_by = fields.Str()
