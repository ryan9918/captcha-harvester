from datetime import datetime
from termcolor import cprint, colored

import colorama
colorama.init()

## normal logging function - time and text
def n_logging(text):
	print("{} {}".format(b_(), text))

## coloured logging function - time and text in colour
def c_logging(value, colour):
	text = colored(value, colour)
	print("{} {}".format(b_(), text))

## coloured printing function - text in colour
def c_print(value, colour):
	text = colored(value, colour)
	print(text)

## used to get the time wrapped in square brackets
def b_():
    timestamp = str("["+datetime.now().strftime("%H:%M:%S.%f")[:-3]+"]")
    return timestamp

## just fetches the time (no square brackets)
def stamp():
	timestamp = datetime.now().strftime("%H:%M:%S")
	return timestamp