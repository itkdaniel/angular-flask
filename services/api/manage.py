import unittest
import json
import click
from flask.cli import FlaskGroup
from flask_whooshee import Whooshee
from flask_migrate import command
from src import create_app, db, logger, migrate
from src.entities.exam import Exam
# from src.entities.entity import engine, Base


app = create_app()
# Base.metadata.create_all(engine)
cli = FlaskGroup(create_app=create_app)

# with app.app_context():
	# db.create_all()
	# db.session.commit()

# cli.add_command('db', migrate)

@cli.command()
def recreate_db():
	db.drop_all()
	db.create_all()
	db.session.commit

@cli.command()
def reindex():
	whooshee = Whooshee(app)
	whooshee.reindex()

@cli.command()
@click.option('-n','--number',type=int,prompt=True,prompt_required=False,default=1,help='number of data(fakes) to add')
def add_test_data(number):
	import requests
	from src import logger
	from faker import Faker
	from random import seed
	logger = logger.create_logger('ManageLogger')
	fake = Faker()
	headers = {'charset':'utf-8'}
	url = 'http://localhost/api/exams/ping'
	response = requests.request('GET',url)
	print(response.json())
	logger.debug("{}\n".format(response.json()))
	seed()
	url = 'http://localhost/api/exams'
	# data = {'title':'Test Exam 1', 'description':'This is a test exam 1'}
	exams = [{'title':f'Test Exam {fake.domain_word()}','description':f'{fake.sentence()}'} for i in range(number)]
	for i in range(len(exams)): 
		response = requests.post(url,json=exams[i],headers=headers)
		print(response.status_code)
		print(response.json())
		logger.debug("{}\n".format(response.json()))
	url = 'http://localhost/api/users/register'
	# data = {'username':'test@test.com', 'password':'test123'}
	users = [{'username':fake.email(), 'password':'test123'} for i in range(number)]
	for i in range(len(users)):
		response = requests.post(url,json=users[i],headers=headers)
		print(response.status_code)
		print(response.json().get('user'))
		logger.debug("{}\n".format(response.json().get('user')))
	return 0



if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=True)
    cli()