config = {
	'browser': 'chrome',
	'URL': 'http://localhost:4200'
	}

class Config(object):
	def __init__(self):
		self.config = config

	def get_property(self,property_name:str) -> str:
		return self.config.get(property_name)

	@property
	def browser(self)-> str:
		return self.get_property('browser')

	@property
	def URL(self)->str:
		return self.get_property('URL')
	
	