from datetime import datetime
from termcolor import cprint, colored

import colorama


class Logger():

	def __init__(self):
		colorama.init()

	def __timestamp(self):
		timestamp = str("["+datetime.now().strftime("%H:%M:%S.%f")[:-3]+"]")
		return timestamp

	def log(self, text):
		print("{} {}".format(self.__timestamp(), text))
		return

	def success(self, text):
		print("{} {}".format(self.__timestamp(), colored(text, "green")))
		return

	def warn(self, text):
		print("{} {}".format(self.__timestamp(), colored(text, "yellow")))
		return

	def error(self, text):
		print("{} {}".format(self.__timestamp(), colored(text, "red")))
		return

	def status(self, text):
		print("{} {}".format(self.__timestamp(), colored(text, "magenta")))
		return