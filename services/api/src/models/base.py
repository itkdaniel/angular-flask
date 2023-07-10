import uuid
from datetime import datetime, timezone, timedelta
from redis_om import JsonModel, HashModel, Field
from typing import Optional

date_fmt = '%a, %b %d %Y %I:%M:%S%p'

def create_date():
	return datetime.now().astimezone(timezone(timedelta(hours=-7)))

def get_time_passed(created_at:datetime)-> dict:
	now = datetime.now().astimezone(timezone(timedelta(hours=-7)))
	time_passed = now - created_at
	d = {'days':time_passed.days, 
		'hours':time_passed.seconds//3600,
		'minutes':(time_passed.seconds%3600)//60,
		'seconds':time_passed.seconds%60}
	return d

class BaseModelOM(JsonModel):
	created_by: str
	created_at: datetime = Field(default=create_date())
	tstamp: Optional[float] = Field(default=create_date().timestamp())

	def get_create_date(self):
		return datetime.strptime(self.created_at, date_fmt)

class BaseModel(object):

	def __init__(self,created_by:str):
		self.uid = uuid.uuid4().hex
		self.created_by = created_by
		self.created_at = datetime.now().astimezone(timezone(timedelta(hours=-7)))


