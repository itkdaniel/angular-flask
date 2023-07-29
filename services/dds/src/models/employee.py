import json
from dataclasses import dataclass, field, asdict
from functools import singledispatchmethod
from bson import ObjectId, Optional
from datetime import date, datetime
from faker import Faker
from src import mongo
from src.utils.utils import currentdatetime, uid

fake = Faker()
# db = mongo.db

@dataclass
class Employee:
	fname:str
	lname:str
	uid:str=field(default=None)
	dob:date=field(default=None)
	email:str=field(default=None)
	joined:datetime=field(default=currentdatetime())
	role:Optional[str]=None
	patients:Optional[list[str]]=None

	@singledispatchmethod
	def __init__(self,fname:str,lname:str,dob:date=None,email:str=None,role:Optional[str]=None,patients:Optional[list[str]]=[]):
		self.fname=fname
		self.lname=lname
		self.uid=uid()
		self.dob=fake.passport_dob() if dob is None or not isinstance(dob,date) else dob
		self.email=f'{lname}.{fname}@test.com' if email is None else email
		self.joined=currentdatetime()
		self.role=role
		self.patients=patients
	@__init__.register
	def _(self,dargs: dict):
		if 'fname' in dargs:
			self.fname = dargs['fname']
		if 'lname' in dargs:
			self.lname = dargs['lname'] 
		if 'dob' in dargs:
			self.dob = fake.passport_dob() if dargs['dob'] is None else datetime.strptime(dargs['dob'], '%m/%d/%Y') if dargs['dob'] and not isinstance(dargs['dob'],date) else dargs['dob']
		if 'uid' in dargs:
			self.uid = dargs['uid'] if dargs['uid'] is not None else uid()
		if 'email' in dargs:
			self.email = dargs['email']
		if 'joined' in dargs:
			self.joined = dargs['joined'] if isinstance(dargs['joined'], datetime) else datetime.strptime(dargs['joined'], '%m/%d/%Y %I:%M:%S %p')
		if 'role' in dargs:
			self.role = dargs['role']
		if 'patients' in dargs:
			self.patients = dargs['patients']
	
# from src import mongo; from manage import app; from src.models.employee import Employee
# {'fname': 'Susan', 'lname': 'Garcia', 'uid': '005a054c92a244cd996f6af0b7f92e89', 'dob': '12/13/1910', 'email': 'Garcia.Susan@test.com', 'joined': '07/22/2023 12:33:47 AM', 'role': None, 'patients': []}
# {'fname': 'Diane', 'lname': 'Moreno', 'uid': '64d66b4842f3484996c95526817f2999', 'dob': '02/21/2008', 'email': 'Moreno.Diane@test.com', 'joined': '07/21/2023 11:14:42 PM', 'role': None, 'patients': [], '_id': ObjectId('64bbbaf9eb7b505d7f3ba205')}
# groups = groupby([*zip([*tmp2.keys()],[*tmp2.values()])], lambda item: item[0])
# for group in groups: print(*group[1])
# unpk = [tuple(*group[1]) for group in groups]
# unpk = [(*group[1]) for group in groups]
# unpk = [*group[1] for group in groups]
# unpk = [group[1] for group in groups]
# unpkit = listen(unpk)
# unpkitr = iter(unpkit)

	@singledispatchmethod
	def todict(self,*args):
		return asdict(self)

	@todict.register
	@classmethod
	def _(cls,arg:type):
		emp = object.__new__(cls)
		return asdict(emp)

	@todict.register
	@classmethod
	def _(cls,arg:str):
		emp = json.loads(arg)
		return emp

	@singledispatchmethod
	def tojson(self,*args):
		"""
			Method converts <class 'src.models.employee.Employee'> to json string.
		"""
		# self.dob = self.dob.strftime('%m/%d/%Y')
		# self.joined = self.joined.strftime('%m/%d/%Y %I:%M:%S %p')
		emp = Employee(self.todict(*args))
		emp.dob = emp.dob.strftime('%m/%d/%Y')
		emp.joined = emp.joined.strftime('%m/%d/%Y %I:%M:%S %p')
		return json.dumps(emp.todict(*args))
	
	@tojson.register
	@classmethod
	def _(cls,arg:type):
		cls.dob = cls.dob.strftime('%m/%d/%Y')
		cls.joined = cls.joined.strftime('%m/%d/%Y %I:%M:%S %p')
		return json.dumps(cls.todict(cls))

	@singledispatchmethod
	def fromjson(self,*args):
		"""
			Method converts employee json string to <class 'src.models.employee.Employee'>
		"""
		raise NotImplementedError(f'Cannot convert {self.__class__.__name__}')

	@fromjson.register
	@classmethod                                           
	def fromjson(cls,emp:str):                             
		emp = json.loads(emp)                              
		# emp['dob'] = datetime.strptime(emp['dob'], '%m/%d/%Y')            
		# emp['joined'] = datetime.strptime(emp['joined'], '%m/%d/%Y %I:%M:%S %p')
		cls.dob, cls.joined = datetime.strptime(emp['dob'], '%m/%d/%Y'), datetime.strptime(emp['joined'], '%m/%d/%Y %I:%M:%S %p')
		return emp

	@singledispatchmethod
	@classmethod
	def save(cls,emp):
		"""
			method-1-steps:
				1. convert employee object to json -> jemp = emp.tojson(emp)
				2. convert json to dict -> jemp = emp.todict(jemp)
				3. save converted dict -> res = emp.save(jemp)
			method-2-steps:
				1. convert employee object to dict -> jemp = emp.todict({})
				2. save converted dict -> res = emp.save(jemp)
		"""
		if isinstance(emp, cls):
			result = mongo.db.employees.insert_one(emp.todict(1))
			return result.inserted_id
		return None	

	@save.register
	@classmethod
	def _(cls,emp:dict):
		result = mongo.db.employees.insert_one(emp)
		return result.inserted_id

	@save.register
	@classmethod
	def _(cls,emp:str):
		result = mongo.db.employees.insert_one(cls.fromjson(emp))
		return result.inserted_id

	@save.register
	@classmethod
	def _(cls,emp:type):
		result = mongo.db.employees.insert_one(cls.fromjson(cls.tojson(emp)))
		return result.inserted_id

	@singledispatchmethod
	@classmethod
	def get(cls,arg):
		raise NotImplementedError(f'Cannot get {cls.__name__}')

	@get.register
	@classmethod
	def _(cls,arg:str):
		result = mongo.db.employees.find_one({'fname':arg}) if mongo.db.employees.find_one({'lname':arg}) is None else mongo.db.employees.find_one({'lname':arg})
		return result if result else None

	@get.register
	@classmethod
	def _(cls,arg:ObjectId):
		result = mongo.db.employees.find_one({'_id':arg})
		return result
		
	def addpatient(self, *args):
		self.patients.extend(args)

	@classmethod
	def fake(cls):
		cls.__init__(cls, fake.first_name(),fake.last_name())
		# fakeemp = object.__new__(cls)
		result = cls.save(cls)
		return result

	@staticmethod
	def create_collection():
		try:
			db.create_collection("employees")
		except Exception as e:
			print(e)
		employee_validator = {
			"$jsonSchema": {
				"bsonType": "object",
				"required": ["fname","lname","uid","dob","email","joined"],
				"properties": {
					"fname": {
						"bsonType": "string",
						"description": "required string type"
					},
					"lname": {
						"bsonType": "string",
						"description": "required string type"
					},
					"uid": {
						"bsonType": "string",
						"description": "required string type"
					},
					"dob": {
						"bsonType": "date",
						"description": "required date type"
					},
					"email": {
						"bsonType": "string",
						"description": "required string type"
					},
					"joined": {
						"bsonType": "datetime",
						"description": "required datetime type"
					}
				}
			}
		}
		db.command("collMod", "employees", validator=employee_validator)
	
	
# @dataclass
# class Employee:
#     fname:str
#     lname:str
#     _id:str=field(default=None)
#     dob:date=field(default=None)
#     email:str=field(default=None)
#     joined:datetime=field(default=None)
#     role:Optional[str]=None
#     patients:Optional[list[str]]=None
#     @singledispatchmethod
#     def __init__(self,fname:str,lname:str,dob:date=None,email:str=None,role:Optional[str]=None,patients:Optional[list[str]]=None):
#             self.fname=fname
#             self.lname=lname
#             self._id=uid()
#             self.dob=fake.passport_dob() if dob is None or not isinstance(dob,date) else dob
#             self.email=f'{lname}.{fname}@test.com' if email is None else email
#             self.joined=currentdatetime()
#             self.role=role
#             self.patients=[]
#     @__init__.register
#     def _(self,dargs: dict):
#             if 'fname' in dargs:
#                self.fname = dargs['fname']
#             if 'lname' in dargs:
#                self.lname = dargs['lname'] 
#             if 'dob' in dargs:
#                self.dob = fake.passport_dob() if dargs['dob'] is None or not isinstance(dargs['dob'],date) else dargs['dob']
#             if '_id' in dargs:
#                self._id = dargs['_id']
#             if 'email' in dargs:
#                self.email = f'{self.lname}.{self.fname}@test.com' if dargs['email'] is None else dargs['email']
#             if 'joined' in dargs:
#                self.joined = dargs['joined']
#             if 'role' in dargs:
#                self.role = dargs['role']
#             if 'patients' in dargs:
#                self.patients = dargs['patients']
#     def todict(self):
#             return asdict(self)
#     def tojson(self):
#             self.dob = self.dob.strftime('%m/%d/%Y')
#             self.joined = self.joined.strftime('%m/%d/%Y %I:%M:%S %p')
#             return json.dumps(self.todict())
#     @classmethod                                           
#     def fromjson(cls,emp:str):                             
#             emp = json.loads(emp)                              
#             emp['dob'] = datetime.strptime(emp['dob'], '%m/%d/%Y')            
#             emp['joined'] = datetime.strptime(emp['joined'], '%m/%d/%Y %I:%M:%S %p')
#             return cls(emp)
#     def addpatient(self, *args):
#             self.patients.extend(args)		
