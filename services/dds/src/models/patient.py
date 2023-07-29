import json
from dataclasses import dataclass, asdict, field
from bson import ObjectId, Optional
from datetime import datetime, date
from faker import Faker
from src import mongo, logger
from src.utils.utils import currentdatetime, uid

fake = Faker()
typeerrormsg = lambda cls,attr,*args: map(lambda arg: f"TypeError: attribute '{attr}' for {cls.__name__} objects is incompatible for {type(arg).__name__} object", args)

@dcs.dataclass
class Patient:
	fname:str
	lname:str
	uid:str=dcs.field(default_factory=uid)
	dob:date=dcs.field(default=None)
	email:str=dcs.field(default=None)
	appointments:list[date]=dcs.field(default_factory=list[date])
	doctor:(ObjectId,str,type(None))=dcs.field(default=None)
	record:(ObjectId,str,type(None))=dcs.field(default=None)

	def __new__(cls,fname,lname,*dargs,**kwargs):
		def ins(__new__):
	             args = inspect.signature(__new__)
	             return [*args.parameters][1:3]
		args = ins(__new__)
		args = {item[0]:item[1] for item in zip(args,[fname,lname])}
		errors = []
		for k,v in args.items():
			try:
				if not isinstance(v,str): raise TypeError(*typeerrormsg(cls,k,v))
			except Exception as e:
				errors.append(e)
			else:
				return object.__new__(cls)
			finally: 
				if errors: 
					for err in errors: 
						print(err)
				else:
					return object.__new__(cls) 


def fibo(n,memo):
     start = time()
     if memo[n] != None:
             return memo[n]
     if n <= 1: return n
     else:
             res = fibo(n-1,memo) + fibo(n-2,memo)
             memo[n] = res
             return res

def fibof(n,timer=[]):
	start = time()
	if n <= 1: timer.append(time()-start); return n, max(timer)
	return fibof(n-1)+fibof(n-2)