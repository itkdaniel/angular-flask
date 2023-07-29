import os 
import logging
import logging.config
from logging.handlers import RotatingFileHandler

LOG_DIR = os.path.dirname('tmp/logs/')

class Logger:
	def __init__(self,name='logger', filename='logging.conf'):
		if not os.path.exists(LOG_DIR):
			os.makedirs(LOG_DIR)
		log_config = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
		logging.config.fileConfig(log_config)
		self.logger = self.get_logger(name=name)

	def create_logger(self,name='logger'):
		"""Creates logger with default name 'logger'"""
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

	def get_logger(self,name=None):
		logger = logging.getLogger(name)
		return logger