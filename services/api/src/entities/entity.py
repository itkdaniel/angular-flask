import os
import pytz
import random, uuid
from datetime import datetime, timezone, timedelta
from sqlalchemy import create_engine, Column, String, Integer, DateTime
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base

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
	now = datetime.now(timezone(timedelta(hours=-7),'PDT')).strftime('%a, %d %b %Y %I:%M:%S%p')
	time_passed = datetime.strptime(now, '%a, %d %b %Y %I:%M:%S%p') - datetime.strptime(created_at,'%a, %d %b %Y %I:%M:%S%p')
	d = {'days':time_passed.days, 
		'hours':time_passed.seconds//3600,
		'minutes':time_passed.seconds//60,
		'seconds':time_passed.seconds%60}
	return d

class Entity():
	id = Column(Integer, primary_key=True)
	created_at = Column(DateTime)
	updated_at = Column(DateTime)
	last_updated_by = Column(String)
	# time_since_created = Column(String)

	def __init__(self, created_by):
		# self.created_at = datetime.now(pytz.timezone('America/Los_Angeles'))
		# self.updated_at = datetime.now(pytz.timezone('America/Los_Angeles'))
		# self.created_at = datetime.now(pytz.timezone('US/Pacific'))
		# self.updated_at = datetime.now(pytz.timezone('US/Pacific'))
		# self.created_at = datetime.now().strftime('%a, %d %b %Y %I:%M:%S%p')
		# self.updated_at = datetime.now().strftime('%a, %d %b %Y %I:%M:%S%p')
		# self.created_at = datetime.now(pytz.timezone('US/Pacific')).strftime('%a, %d %b %Y %I:%M:%S%p %Z%z')
		# self.updated_at = datetime.now(pytz.timezone('US/Pacific')).strftime('%a, %d %b %Y %I:%M:%S%p %Z%z')

		# self.id = "{}{:8d}".format(randc(),randuid())
		self.created_at = self.get_current_time_pdt().strftime('%a, %d %b %Y %I:%M:%S%p')
		self.updated_at = self.get_current_time_pdt().strftime('%a, %d %b %Y %I:%M:%S%p')
		# self.created_at = datetime.strptime(datetime.now(pytz.timezone('US/Pacific')).strftime('%a, %d %b %Y %I:%M:%S%p'), '%a, %d %b %Y %I:%M:%S%p')
		# self.updated_at = datetime.strptime(datetime.now(pytz.timezone('US/Pacific')).strftime('%a, %d %b %Y %I:%M:%S%p'), '%a, %d %b %Y %I:%M:%S%p')
		self.last_updated_by = created_by
		# self.time_since_created = self.get_time_since_created()

	def get_current_time_pdt(self):
		return datetime.now(timezone(timedelta(hours=-7),'PDT'))
		# return datetime(datetime.now().year,
		# 				datetime.now().month,
		# 				datetime.now().day,
		# 				12-(7-datetime.now().hour),
		# 				datetime.now().minute,
		# 				datetime.now().second)

	