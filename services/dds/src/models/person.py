import abc
import json
from dataclasses import dataclass, field, asdict
from functools import singledispatchmethod
from bson import ObjectId, Optional
from faker import Faker 
from datetime import datetime, date
from src import mongo, logger
from src.utils.utils import currentdatetime, uid

@dataclass
class Person(object):
	fname:str
	lname:str
	uid:str=field(default=None)
	dob:date=field(default=None)
	email:str=field(default=None)

	@singledispatchmethod
	def __init__(self,fname:str,lname:str,dob:date=None,email:str=None):
		self.fname = fname
		self.lname = lname
		self.uid = uid()
		self.dob = fake.passport_dob() if dob is None or not isinstance(dob,date) else dob
		self.email = f'{lname}.{fname}@email.com' if email is None else email

	@__init__.register
	def _(self,dargs:dict):
		if 'fname' in dargs:
			self.fname = dargs['fname']
		if 'lname' in dargs:
			self.lname = dargs['lname']
		if 'dob' in  dargs:
			self.dob = fake.passport_dob() if dargs['dob'] is None else datetime.strptime(dargs['dob'], '%m %d %Y') if dargs['dob'] and not isinstance(dargs['dob'],date) else dargs['dob']
		if 'uid' in dargs:
			self.uid = dargs['uid'] if dargs['uid'] is not None else uid()
		if 'email' in dargs:
			self.uid = dargs['email'] if dargs['email'] is not None else f'{dargs['lname']}.{dargs['fname']}@email.com' 
