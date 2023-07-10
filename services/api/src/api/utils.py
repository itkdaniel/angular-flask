from datetime import datetime, timezone, timedelta
from src.models.customer import CustomerOM
from src.models.base import create_date
from src.configs.colors import Colors
from itertools import starmap
from functools import wraps
from src import logger
import platform
import time
import os

datefmt = '%a, %b %d %Y %I:%M:%S%p'
rdatefmt = '%Y-%m-%dT%H:%M:%S.%f%z'
uidfor = lambda c: setattr(c, 'uuid', uuid.uuid4().hex)
tstamp = lambda c: setattr(c, 'tstamp', c.created_at.timestamp())
# creates a redis customer object from request json data
# ex: customer = create_customer(**args)
create_customer = lambda **kwargs: CustomerOM(
									**kwargs, 
									created_by='HTTP post request')
									# created_at=create_date().strftime('%a, %b %d %Y %I:%M:%S%p'))
									# created_at=datetime.now().astimezone(timezone(timedelta(hours=-7))))

# return datetime obj from redis datetime str
# datetime.strptime(CustomerOM.db().hgetall(":src.models.customer.CustomerOM:01H3MFJ0G5SGNQYRPH5A0VDAQ5")['created_at'],'%Y-%m-%dT%H:%M:%S.%f%z').strftime('%x %r [%c]')
dtpstr = lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S.%f%z')
# return formatted datetime from redis datetime str
dtfstr = lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S.%f%z').strftime('%x %r - %c')

# return the list of sets of (key,value) pairs from **args map/dict
# ex: json_data = {'first_name': 'Jesus', 'last_name': 'Christ', 'email': 'j.christ@heaven.com', 'age': 2023, 'bio': 'I am Jesus'} 
# 		mapper(**json_data) -> [('first_name', 'Jesus') ('last_name', 'Christ') ('email', 'j.christ@heaven.com') ('age', 2023) ('bio', 'I am Jesus')]
mapper = lambda **kwargs: zip([*kwargs.keys()],[*kwargs.values()])

# transformer = lambda **args: map(fn, lst)
# starmap(lambda n,v: f'{n}={v}', [*mapper(**json_data)])
# print(*starmap(lambda n,v: f'{n}={v}', [*mapper(**json_data)]))
transformer = lambda *args: starmap(lambda n,v: f'{n}={v}', [*args]) 


logcustomer = lambda c: logger.create_logger(
				f'{c.__class__.__name__}').debug(
					"\n{:*^30s}  {:*^30s}  {:*^30s} \n{: ^30s}  {: ^30f}  {: ^30s}".format(
					'name','timestamp','created',
					f'{c.last_name},{c.first_name}',
					c.created_at.timestamp(),
					c.created_at.strftime(datefmt)))

# json_data1 = {"first_name": "Walter", "last_name": "White", "email": "w.white@crystal.com", "age": 65, "bio": "I am the one who knocks"}
# json_data2 = {"first_name": "Jesse", "last_name": "Pinkman", "email": "j.pinkman@magnets.com", "age": 32, "bio": "Science bitch!"}
# json_data3 = {"first_name": "Gustavo", "last_name": "Fring", "email": "g.fring@chicken.com", "age": 50, "bio": "I am the cartel"}
# custs = [json_data1,json_data2,json_data3]
# youngins(custs)
# json_data1 = {'first_name': 'Walter', 'last_name': 'White', 'email': 'w.white@crystal.com', 'age': 65, 'bio': 'I am the one who knocks'};json_data2 = {'first_name': 'Jesse', 'last_name': 'Pinkman', 'email': 'j.pinkman@magnets.com', 'age': 32, 'bio': 'Science bitch!'};json_data3 = {'first_name': 'Gustavo', 'last_name': 'Fring', 'email': 'g.fring@chicken.com', 'age': 50, 'bio': 'I am the cartel'}
# cust1, cust2, cust3,cust = create_customer(**json_data1),create_customer(**json_data2),create_customer(**json_data3),create_customer(**json_data)
youngins =  lambda custs: map(lambda x: f'{x.last_name},{x.first_name}', [*filter(lambda c: c.age < 60, custs)])

def exectimer(fn):
	@wraps(fn)
	def wrapper(*args,**kwargs):
		start = time.time()
		result = fn(*args,**kwargs)
		tpass = time.time() - start
		print("{} execution time: {}".format(fn.__name__,tpass))
		logger.logger.info(f'{Colors.YELLOW}{fn.__name__} execution time: {tpass}{Colors.DEFAULT}')
		return result
	return wrapper

class WifiManager:

	def __init__(self,ssid=None,name=None):
		self.ssid = ssid
		self.name = name

	@staticmethod
	@exectimer
	def displayAvailableNetworks():
		if platform.system() == "Windows":
			command = "netsh wlan show networks interface=Wi-Fi"
		elif platform.system() == "Linux":
			command = "nmcli dev wifi list"
		os.system(command)

	@staticmethod
	@exectimer
	def connect(name=None, SSID=None):
		if platform.system() == "Windows":
			command = "netsh wlan connect name=\""+name+"\" ssid=\""+SSID+"\" interface=Wi-Fi"
		elif platform.system() == "Linux":
			command = "nmcli con up "+SSID
		os.system(command)

	@staticmethod
	@exectimer
	def createNewConnection(name=None, SSID=None, key=None):
		config = """<?xml version=\"1.0\"?>
		<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
			<name>"""+name+"""</name>
			<SSIDConfig>
				<SSID>
					<name>"""+SSID+"""</name>
				</SSID>
			</SSIDConfig>
			<connectionType>ESS</connectionType>
			<connectionMode>auto</connectionMode>
			<MSM>
				<security>
					<authEncryption>
						<authentication>WPA2PSK</authentication>
						<encryption>AES</encryption>
						<useOneX>false</useOneX>
					</authEncryption>
					<sharedKey>
						<keyType>passPhrase</keyType>
						<protected>false</protected>
						<keyMaterial>"""+key+"""</keyMaterial>
					</sharedKey>
				</security>
			</MSM>
		</WLANProfile>"""
		if platform.system() == "Windows":
			command = "netsh wlan add profile filename=\""+name+".xml\""+" interface=Wi-Fi"
			with open(name+".xml", 'w') as file:
				file.write(config)
		elif platform.system() == "Linux":
			command = "nmcli dev wifi connect '"+SSID+"' password '"+key+"'"
		os.system(command)
		if platform.system() == "Windows":
			os.remove(name+".xml")

	@classmethod
	def run(self):
		try:
			self.displayAvailableNetworks()
			option = input('New connection (y/N)? ')
			if option =='N' or option == "":
				name = input('Name: ')
				self.connect(name,name)
				print('If not connected to this network, try connecting w correct creds')
			elif option == 'y':
				name = input('Name: ')
				key = getpass.getpass('Password: ')
				self.createNewConnection(name,name,key)
				self.connect(name,name)
				print('If not connected to this network, try connecting w correct creds')
			self.name = name
			self.ssid = name
		except KeyboardInterrupt as e:
			print('\nExiting...')
		else:
			self.network_name = ssid


# logcustomer = lambda c: logger.create_logger(f'{c.__class__.__name__}').debug("\n{:-^30s}  {:-^30s}  {:-^30s} \n{: ^30s}  {: ^30f}  {: ^30s}".format('name','timestamp','created',f'{c.last_name},{c.first_name}',c.created_at.timestamp(),c.created_at.strftime(datefmt)))


"""
from src.models.customer import CustomerOM; from src.api.utils import create_customer, mapper, transformer, uidfor, tstamp;import json; from datetime import datetime,timezone,timedelta;json_data = {'first_name': 'Jesus', 'last_name': 'Christ', 'email': 'j.christ@heaven.com', 'age': 2023, 'bio': 'I am Jesus'}; from src.models.base import get_time_passed, date_fmt,create_date
from src.models.customer import CustomerOM; from src.api.utils import create_customer, mapper, transformer, uidfor, tstamp;import json; from datetime import datetime,timezone,timedelta;json_data = {'first_name': 'Jesus', 'last_name': 'Christ', 'email': 'j.christ@heaven.com', 'age': 2023, 'bio': 'I am Jesus'}; from src.models.base import get_time_passed, date_fmt,create_date; from itertools import starmap; from collections import defaultdict,OrderedDict;import heapq;from functools import wraps; from src import logger; from pprint import pprint; import asyncio;from src.api.utils import logcustomer;json_data1 = {'first_name': 'Walter', 'last_name': 'White', 'email': 'w.white@crystal.com', 'age': 65, 'bio': 'I am the one who knocks'};json_data2 = {'first_name': 'Jesse', 'last_name': 'Pinkman', 'email': 'j.pinkman@magnets.com', 'age': 32, 'bio': 'Science bitch!'};json_data3 = {'first_name': 'Gustavo', 'last_name': 'Fring', 'email': 'g.fring@chicken.com', 'age': 50, 'bio': 'I am the cartel'};cust1, cust2, cust3,cust = create_customer(**json_data1),create_customer(**json_data2),create_customer(**json_data3),create_customer(**json_data); from src.api.utils import youngins
"""


"""
getting monthly spendings through grouping and mapping
spendings = [('January', 25), ('February', 47), ('March', 38), ('March', 54), ('April', 67), ('January', 56), ('February', 32), ('May', 78), ('January', 54), ('April', 45)]
monthly_spend = groupby(sorted(spendings, key=fn), fn)

# following 2 ways to build spendings_dict
(1)		spendings_dict = {k:[*g] for k,g in monthly_spend}

(2)		for key, group in groupby(sorted(spendings, key=func), func):
			spendings_dict[key] = list(group)


mapper(**spendings_dict)
for item in starmap(lambda key, group: f'{key}={map(lambda g: g[1], group)}', mapper(**spendings_dict)): print(item)
for item in starmap(lambda key, group: f'{key}={sum(map(lambda g: g[1], group))}', mapper(**spendings_dict)): print(item)
print(*starmap(lambda key, group: f'{key:*^30s}\n{list(map(lambda g: g[1], group))}\n', mapper(**spendings_dict)))
print(*starmap(lambda key, group: f'{key:*^30s}\n{sum(list(map(lambda g: g[1], list(group))))}\n', mapper(**spendings_dict)))
print(*starmap(lambda key, group: f'\n{key:*^30s}\n{sum(list(map(lambda g: g[1], group))):^30d}\n', mapper(**spendings_dict)))

** Same as above steps using starmap **
- Apply map() to sum the monthly spendings
sum_spending_by_month = {key:sum(map(lambda x: x[1], group)) for key,group in spendings_dict.items()}


***formattedprint***
		int
print(
		"{:*^20s} {:*^20s} {:*^20s} {:*^20s} {:*^20s}\n".format(
													*{key:sum(map(lambda x: x[1], value)) for key,value in spendings_dict.items()}.keys()), 
		"{:^20d} {:^20d} {:^20d} {:^20d} {:^20d}\n".format(
													*{key:sum(map(lambda x: x[1], value)) for key,value in spendings_dict.items()}.values()))
"""


# def put(self,key,val):
# 	if key in self.datadict:
# 		del self.datadict[key]
# 		self.lru.pop(key)
# 		heapq.heapify(self.lru)
# 		self.datadict[key]=val
# 		heapq.heappush(self.lru, (key,val))
# 		return (key,val)
# 	if self.isfull():
# 		while self.isfull():
# 			data = heapq.heappop(self.lru)
# 			del self.datadict[data[0]]
# 		self.datadict[key] = val
# 		heapq.heappush(self.lru,(key,val))
# 		return (key,val)
# 	heapq.heappush(self.lru, (key,val))
# 	self.datadict[key]=val
# 	return (key,val)

	# def get(self,key):
	# 	if key in self.datadict:
	# 		data = self.datadict[key]
	# 		del self.datadict[key]
	# 		self.datadict[key+1] = data[1]
	# 		data = self.lru.pop(key)
	# 		heapq.heapify(self.lru)
	# 		self.put(key+1,data[1])
	# 		return (key+1,data[1])
	# 	return key





# @exectime
# async def func(*args,**kwargs):
# 	for arg in args: print(arg, end=" ")
# 	print()
# 	for k,v in kwargs.items(): print(k,':',v,',',end=" ")
# 	print()
# 	for k in kwargs.keys():
# 	        if k == 'url': response = requests.get(kwargs[k])
# 	return response.json()	


# Completion = make_dataclass('Completion',[('model',str,"gpt-3.5-turbo"),('n',int,2),('messages',list[dict], field(default=list[dict]))], bases=(object,))