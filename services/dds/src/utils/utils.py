import uuid
from faker import Faker
from datetime import datetime, timezone, timedelta

utcfmt = '%Y-%m-%dT%H:%M:%S.%f%z'
dtfmt = '%x %r - %c'

currentdatetime = lambda: datetime.now(timezone(timedelta(hours=-7), 'PDT'))

uid = lambda: uuid.uuid4().hex

def get_time_passed(created_at:datetime)-> dict:
	now = datetime.now().astimezone(timezone(timedelta(hours=-7)))
	time_passed = now - created_at
	d = {'days':time_passed.days, 
		'hours':time_passed.seconds//3600,
		'minutes':(time_passed.seconds%3600)//60,
		'seconds':time_passed.seconds%60}
	return d

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
						"bsonType": ["date","string"],
						"description": "required date type"
					},
					"email": {
						"bsonType": "string",
						"description": "required string type"
					},
					"joined": {
						"bsonType": ["date","string"],
						"description": "required datetime type"
					}
				}
			}
		}