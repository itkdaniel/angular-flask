# from .entities.entity import Session, engine, Base
# from .entities.entity import Base
from .entities.exam import Exam
from .entities.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.api.users import create_user
from src import db


# generate db schema
# Base.metadata.create_all(engine)

# test db table exams
def test_exams():
	# start session
	# session = Session()
	# check for existing data
	exams = Exam.query.all()
	if len(exams) == 0:
		# create and persist mock exam
		python_exam = Exam("SQLAlchemy Exam", "Test about SQLAlchemy", "script")
		db.session.add(python_exam)
		db.session.commit()
		db.session.close()
		# reload exams
		exams = Exam.query.all()
	# show existing exams
	print('### Exams: ')
	for exam in exams:
		print(f'({exam.id}) {exam.title} - {exam.description}')

# test db table users
def test_users():
	# start session
	# session = Session()
	users = User.query.all()
	if len(users) == 0:
		# create and persist mock user
		python_user = User("testuser", "testpassword", "script")
		python_user = create_user(python_user.username,python_user.password)
		# session.add(python_user)
		# session.commit()
		# session.close()
		# reload existing users
		users = User.query.all()
	# show existing users
	print('### Users: ')
	for user in users:
		print(f'({user.id}) {user.username} - {user.password}')

test_exams()
test_users()