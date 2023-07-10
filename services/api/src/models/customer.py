from src.models.base import BaseModel, BaseModelOM
from redis_om import Field
from typing import Optional
from pydantic import EmailStr

class CustomerOM(BaseModelOM):
	first_name: str
	last_name: str = Field(index=True)
	email: EmailStr
	age: int = Field(index=True)
	bio: Optional[str]

# Indexing HASH documents prefixed by ":src.models.customer.CustomerOM:"
# ":src.models.customer.CustomerOM:index:hash"
# FT.SEARCH ":src.models.customer.CustomerOM:index" @last_name:{Smith}

class Customer(BaseModel):
	def __init__(self,first_name:str,
					email: str,
					created_by:str,
					last_name:str,
					age:int,
					bio:Optional[str]=None):
		BaseModel.__init__(self,created_by)
		self.first_name = first_name
		self.last_name =  last_name
		self.email = email
		self.age = age
		self.bio = bio
