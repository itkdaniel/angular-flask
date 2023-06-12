import sqlalchemy
from sqlalchemy import Column, String
from .entity import Entity, Base
from marshmallow import Schema, fields
from src import db
import uuid

class Post(Entity):

	__tablename__ = 'posts'

	title = Column(String)
	caption = Column(String)

	def __init__(self, _props):
		Entity.__init__(self, _props['last_updated_by'])
		self.title = _props['title']
		self.caption = _props['caption']
		self._id = uuid.uuid4().hex if '_id' not in _props else _props['_id']

class PostSchema(Schema):
	id = fields.Number()
	_id = fields.Str()
	title = fields.Str()
	caption = fields.Str()
	created_at = fields.DateTime()
	updated_at = fields.DateTime()
	last_updated_by = fields.Str()
