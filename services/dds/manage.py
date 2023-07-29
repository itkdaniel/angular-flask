import click
from flask.cli import FlaskGroup
from src import create_app, logger
from src.configs.colors import Colors
from src.models.employee import Employee
# from src.models.patient import Patient

app = create_app()
cli = FlaskGroup(create_app=create_app)
logger = logger.create_logger(__name__)

@cli.command()
def create_collections():
	logger.debug(f'{Colors.GREEN}creating collections...{Colors.DEFAULT}')
	Employee.create_collection()

@cli.command()
@click.option('-n','--number',type=int,prompt=True,prompt_required=False,default=1,help='number of data(fakes) to add')
def add_test_data(number):
	fakes = []
	for i in range(number):
		fakes.extend([Employee.fake()])
	print(fakes)
	logger.debug(f'fake uids: {fakes}')

if __name__ == '__main__':
	cli()
