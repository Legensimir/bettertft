from flask import Flask 
from flask import request 
 
def login() :
	if request.method == 'POST': 
		username = request.form['username'] 
		password = request.form['password'] 
		 
		# code that uses the data you've got 
		# in our case, checking if the user exists 
		# and logs them in, if not redirect to sign up 
