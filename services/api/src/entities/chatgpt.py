import sqlalchemy
from sqlalchemy import Column, String, Integer
from .entity import Entity
from marshmallow import Schema, fields
from src.datamanager.manager import DataManager
from src import db, mongo
import uuid


# {
#     "id": "chatcmpl-QXlha2FBbmROaXhpZUFyZUF3ZXNvbWUK",
#     "object": "chat.completion",
#     "created": 0,
#     "model": "gpt-3.5-turbo-0301",
#     "usage": {
#         "prompt_tokens": 0,
#         "completion_tokens": 0,
#         "total_tokens": 0
#     },
#     "choices": [
#         {
#             "index": 0,
#             "message": {
#                 "role": "assistant",
#                 "content": "Hello! How can I assist you today?"
#             },
#             "finish_reason": null
#         }
#     ]
# }

class ChatGPT():
	__tablename__ = 'betterchatgpt'

	_object = Column(String)
	created = Column(Integer)
	model = Column(String)
	prompt_tokens = Column(Integer),
	completion_tokens = Column(Integer)
	total_tokens = Column(Integer)
	usage = {}
	choices = []
	index = Column(Integer)
	role = Column(String)
	content = Column(String)
	finish_reason = Column(String)

	# def __init__(self,_id=None,_object=None,created=None,model=None,
	# 	prompt_tokens=None,completion_tokens=None,total_tokens=None,
	# 	usage=None,choices=None,index=None,role=None,content=None,finish_reason=None):
	# 	self._object = _object
	# 	self._id = _id
	# 	self.created = created
	# 	self.model = model
	# 	self.prompt_tokens = prompt_tokens
	# 	self.completion_tokens = completion_tokens
	# 	self.total_tokens = total_tokens
	# 	self.usage = usage
	# 	self.choices = choices
	# 	self.index = index
	# 	self.role = role
	# 	self.content = content
	# 	self.finish_reason = finish_reason
	def __init__(self,props=None):
		self._id = props['id']
		# self._id = props.id

		self._object = props['object']
		# self._object = props.object
		self.created = props['created']
		# self.created = props.created
		self.model = props['model']
		# self.model = props.model
		
		# self.prompt_tokens = props['prompt_tokens']
		# self.completion_tokens = props['completion_tokens']
		# self.total_tokens = props['total_tokens']
		
		self.usage = props['usage']
		# self.usage = props.usage
		self.choices = props['choices']
		# self.choices = props.choices

		# self.index = props['index']
		# self.role = props['role']
		# self.content = props['content']
		# self.finish_reason = props['finish_reason']


# gpt_obj = {"id": "chatcmpl-QXlha2FBbmROaXhpZUFyZUF3ZXNvbWUK","object": "chat.completion","created": 0,"model": "gpt-3.5-turbo-0301","usage":{"prompt_tokens": 0,"completion_tokens": 0,"total_tokens": 0},"choices":[{"index":0,"message": {"role": "assistant","content": "Hello! How can I assist you today?"},"finish_reason": None}]}
# from src.entities.chatgpt import ChatGPT,ChatGptSchema
# gptobj.choices[0].index("content") + 11 # beginning of message content
# gptobj.choices[0].index("'},") # ending of message content
# gpt = ChatGptSchema().dump(gpt_obj)
# gptobj = ChatGPT(props=gpt)
class ChatGptSchema(Schema):
	id = fields.Str()
	object = fields.Str()
	created = fields.Str()
	model = fields.Str()
	prompt_tokens = fields.Number()
	total_tokens = fields.Number()
	usage = fields.Dict(keys=fields.Str(),values=fields.Number())
	choices = fields.List(fields.Str())
	index = fields.Number()
	role = fields.Str()
	content = fields.Str()
	finish_reason = fields.Str()
