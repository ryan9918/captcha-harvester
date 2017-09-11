"""

Manual Captcha Harvester
Made by @TheRealChefUK

"""

from utils import n_logging, c_logging

from flask import Flask, request, jsonify, render_template, redirect
import logging
import _thread
from datetime import datetime
from time import sleep
import webbrowser
import json


tokens = []


def manageTokens():
	while True:
		for token in tokens:
			if token['expiry'] < datetime.now().timestamp():
				tokens.remove(token)
				c_logging("Token expired and deleted.", "red")
		sleep(5)


def sendToken():
	while not tokens:
		pass
	token = tokens.pop(0)
	return token['token']


app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/')
def home():
	return render_template('index.html', sitekey=config['sitekey'], domain=config['domain'])

@app.route('/submit', methods=['POST'])
def submit():
	token = request.form['g-recaptcha-response']
	expiry = datetime.now().timestamp() + 115
	tokenDict = {
		'token': token,
		'expiry': expiry
	}
	tokens.append(tokenDict)
	c_logging("Token harvested and stored.", "green")
	return redirect('/')

@app.route('/count')
def count():
	count = len(tokens)
	return jsonify(count=count)

@app.route('/token')
def fetch_token():
	try:
		token = tokens.pop(0)
		c_logging("Token requested and returned to user.", "blue")
		return token['token']
	except:
		c_logging("Token requested but none available.", "yellow")
		return "ERROR"


if __name__ == '__main__':
	_thread.start_new_thread(manageTokens, ())
	with open('config.json') as file:
		config = json.load(file)
		file.close()
	n_logging("*****************************************************")
	n_logging("Manual Captcha Harvester | theRealChefUK")
	n_logging("*****************************************************")
	n_logging("Server running at cartchefs.{}:5000".format(config['domain']))
	webbrowser.open('http://cartchefs.{}:5000/'.format(config['domain']))
	app.run()