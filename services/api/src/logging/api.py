import os
import logging
import logging.config
from logging.handlers import RotatingFileHandler


LOG_DIRECTORY = os.path.dirname('tmp/logs/')
class ApiLogger:
	def __init__(self,name='ApiLogger'):
		if not os.path.exists(LOG_DIRECTORY):
			os.makedirs(LOG_DIRECTORY)
		log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logging.conf')
		logging.config.fileConfig(log_file_path)
		self.logger = self.get_logger(name=name)

	def create_logger(self,name=None):
		logger = logging.getLogger(name)
		logger.setLevel(logging.DEBUG)

		# create console handler and set level to debug
		console = logging.StreamHandler()
		console.setLevel(logging.DEBUG)
		formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		console.setFormatter(formatter)
		logger.addHandler(console)

		# create file handler
		fh = RotatingFileHandler('tmp/logs/app.log')
		fh.setLevel(logging.DEBUG)
		fh.setFormatter(formatter)
		logger.addHandler(fh)
		return logger

	def get_logger(self, name=None):
		# create logger
		logger = logging.getLogger(name)
		return logger


