import os
import pytz
import random, uuid
from datetime import datetime, timezone, timedelta
from sqlalchemy import create_engine, Column, String, Integer, DateTime
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base
import requests

# db_url = 'db:5432'
# db_name = 'online_exam'
# db_user = 'postgres'
# db_password = 'postgres'

# engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
# engine = create_engine(os.environ.get('DATABASE_URL'))

# Session = sessionmaker(bind=engine)

Base = declarative_base()

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
randc = lambda: alpha[random.randrange(0,25)]
randuid = lambda: uuid.uuid4().int % 10000000000

def get_time_since_created(created_at):
	created_at = created_at.astimezone(timezone(timedelta(hours=-7)))
	now = datetime.now().astimezone(timezone(timedelta(hours=-7)))
	time_passed = now - created_at
	d = {'days':time_passed.days, 
		'hours':time_passed.seconds//3600,
		'minutes':(time_passed.seconds%3600)//60,
		'seconds':time_passed.seconds%60}
	return d

class Entity():
	id = Column(Integer, primary_key=True)
	created_at = Column(DateTime)
	updated_at = Column(DateTime)
	last_updated_by = Column(String)

	def __init__(self, created_by):
		print(f'Initalizing Entity object')
		self.created_at, self.updated_at = self.get_current_time_pdt(), self.get_current_time_pdt()
		self.last_updated_by = created_by
		print(f'from Entity.__init__():\n\t{self}')

	def get_current_time_pdt(self):
		return datetime.now(timezone(timedelta(hours=-7),'PDT'))

	