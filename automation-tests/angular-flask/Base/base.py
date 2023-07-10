import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Config.config import Config

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

class Base:
	@pytest.fixture(autouse=True)
	def set_up(self):
		config = Config()
		print(f"Initiating {config.browser} Driver")
		if config.browser.lower() == "chrome":
			ChromeDriverManager(path = r".\\Drivers").install()
			self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
		print("-------------------------------------------")
		print('Test is starting')
		self.driver.implicitly_wait(10)
		self.driver.get(config.URL)
		self.driver.maximize_window()
		yield self.driver
		if self.driver is not None:
			print("-------------------------------------------")
			print('Test is finished')
			self.driver.close()
			self.driver.quit()
