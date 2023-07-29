import abc
from faker import Faker 
from datetime import date
from dataclasses import dataclass, asdict, field
fake = Faker()

class PersonMeta(abc.ABCMeta):
	"""A person metaclass"""
	def __instancecheck__(cls, instance):
		return cls.__subclasscheck__(type(instance))
	def __subclasscheck__(cls, subclass):
		return (hasattr(subclass, 'fname') and
				hasattr(subclass, 'lname') and
				hasattr(subclass, 'dob') and
				hasattr(subclass, 'email') and
				hasattr(subclass, '__init__') and
				callable(subclass.__init__) and
				hasattr(subclass,'__repr__') and
				callable(subclass.__repr__) and
				hasattr(subclass,'__str__') and
				callable(subclass.__str__))
class PersonInterface(metaclass=PersonMeta):
	@classmethod
	def __subclasshook__(cls, subclass):
			return (cls.__subclasscheck__() and
					hasttr(subclass,'todict') and
					callable(subclass.todict))
	@abc.abstractmethod
	def __init__(self, fname:str, lname:str, dob:date, email:str):
		raise NotImplementedError
	@abc.abstractmethod
	def __repr__(self):
		raise NotImplementedError
	@abc.abstractmethod
	def todict(self):
		raise NotImplementedError
	@property
	@abc.abstractmethod
	def fname(self):
		raise NotImplementedError
	@fname.setter
	@abc.abstractmethod
	def fname(self, val):
		raise NotImplementedError
	@property
	@abc.abstractmethod
	def lname(self):
		raise NotImplementedError
	@lname.setter
	@abc.abstractmethod
	def lname(self, val):
		raise NotImplementedError
	@property
	@abc.abstractmethod
	def dob(self):
		raise NotImplementedError
	@dob.setter
	@abc.abstractmethod
	def dob(self, val):
		raise NotImplementedError
	@property
	@abc.abstractmethod
	def email(self):
		raise NotImplementedError
	@email.setter
	@abc.abstractmethod
	def email(self, val):
		raise NotImplementedError


# >>> type(per1).__dict__['lname'].__get__(per1, type(per1))
# 'Ochoa'
# >>> type(per1).__dict__['fname'].__get__(per1, type(per1))
# 'Michelle'
# >>> per1
# NewPerson(fname='Michelle', lname='Ochoa', dob=datetime.date(1938, 5, 4), email=None)
# >>> type(per1).__dict__['dob'].__get__(per1, type(per1))

class PersonAttr(abc.ABC):
	"""A person attribute metaclass"""
	def __init__(self,*,default):
		print(f'__init__ PersonAttr _default')
		self._default = default() if default is not None else default
	def __set_name__(self,owner,name):
		print(f'__set_name__ PersonAttr _name')
		self._name = f'_{name}'
		owner._name = f'_{name}'
	def __get__(self,obj,type):
		print(f'__get__ PersonAttr _name or _default')
		if obj is None:
			return self._default()
		return getattr(obj,self._name,self._default())
	@abc.abstractmethod
	def __set__(self,obj,val):
		raise NotImplementedError
	@classmethod
	def __subclasshook__(cls,subclass):
		if cls is PersonAttr:
			if any("__set__" in sub.__dict__ for sub in subclass.__mro__):
				return True
		return NotImplemented

class MName(PersonAttr):
	def __set__(self,obj,val):
		if val and isinstance(val,str):
			print(f'__set__ MName attr')
			setattr(obj, self._name, val)
		else:
			if self._name == '_fname':
				setattr(obj,self._name, fake.first_name())
			if self._name == '_lname':
				setattr(obj,self._name, fake.last_name())
	

class MDate(PersonAttr):
	def __set__(self,obj,val):
		print(f'__set__ MDate attr')
		if val and isinstance(val,date):
			setattr(obj,self._name, date(val.year,val.month,val.day))
		elif val and isinstance(val,str):
			dob = datetime.strptime(val,'%m %d %Y')
			if dob and isinstance(dob,date):
				setattr(obj,self._name,dob)
		else:
			setattr(obj,self._name, fake.passport_dob())

class MEmail(PersonAttr):
	def __set__(self,obj,val):
		print(f'__set__ MEmail attr')
		setattr(obj,self._name,val)

@dataclass
class NewPerson:
	fname:MName = MName(default=lambda: fake.first_name)
	lname:MName = MName(default=lambda: fake.last_name)
	dob:MDate = MDate(default=lambda: fake.passport_dob)
	email:MEmail = MEmail(default=lambda: fake.email)
	def __post_init__(self,/,*cls):
		if self.fname and self.lname:
			self.set_email()
	@classmethod
	def __set_email__(self):
		if self.email is None: self.set_email()
	def set_email(self):
		if self.lname and self.fname:
			self.email = f'{self.lname}.{self.fname}@email.com'

@dataclass
class Person(PersonInterface):
	def __init__(self,fname,lname,dob,email):
		self._fname = fname
		self._lname = lname
		self._dob = dob
		self._email = email
	@property
	def fname(self):
		return self._fname
	@fname.setter
	def fname(self, val):
		self._fname = val
	@property
	def lname(self):
		return self._lname
	@lname.setter
	def lname(self, val):
		self._lname = val
	@property
	def dob(self):
		return self._dob
	@dob.setter
	def dob(self, val):
		self._dob = val
	@property
	def email(self):
		return self._email
	@email.setter
	def email(self, val):
		self._email = val

class Employee(PersonInterface):
	...
# PersonInterface.register(Employee)
# @dataclass
# class Employee:
# 	fname:str=None
# 	lname:str=None
# 	dob:date=None
# 	email:str=None
# PersonInterface.register(Employee)
class Patient:
	fname:str=None
	lname:str=None
	dob:date=None
	email:str=None
	def __init__(self,*args,**kwargs):
		if len(args) == 4:
			fname,lname,dob,email = [*args]
		if kwargs:
			for k,v in kwargs.items():
				setattr(self,k,v)
class User(Employee):
	...
# class Buyer(PersonInterface):
# 	fname:str
# 	lname:str
# 	dob:date
# 	email:str
class Buyer:
	fname:str
	lname:str
	dob:date
	email:str
		
	

