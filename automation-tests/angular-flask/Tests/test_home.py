import sys, os
from Pages.HomePage import HomePage
from Base.base import Base
from Config.colors import Colors 
import pytest
import unittest

@pytest.mark.usefixtures('set_up')
class TestHome(Base, unittest.TestCase):
	def test_home_success(self):
		driver = self.driver
		home = HomePage(driver)
		self.assertTrue(3 == 3) # sanity test
		try:
			self.assertEqual(self.driver.title, 'AngularFlask-Home')
			print(f"{Colors.LIGHT_GREEN} PASSED - {self.driver.title} == AngularFlask-Home")
			self.assertTrue(driver is self.driver)
			print("{} PASSED - driver {}is {}self.driver".format(Colors.LIGHT_GREEN, Colors.YELLOW, Colors.LIGHT_GREEN))
		except Exception as e:
			print("{} Title `{}` was not expected".format(Colors.LIGHT_RED, self.driver.title))
			raise e