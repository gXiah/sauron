from flask import Flask, request, json


"""
	Environment variables
"""

URI_PREFIX = '/api' # The prefix to be put before each URI (eg: '/api/lookup?param=...')
DEBUG = True

DEV_ENV = 'dev'
PROD_END = 'prod'

ENV = DEV_ENV






#=================================

if ENV == DEV_ENV: # Local env
	
	DEBUG = True

elif ENV == PROD_END: # Prod env

	DEBUG = False

else:
	die('Unrecognized environment (@app.py)')

#=================================



app = Flask(__name__)



"""
	Importing routes
"""
import router.routes.root_route
import router.routes.lookup_route
import router.routes.vectorize_route
#=================================




"""
	Starting up the server
"""
if __name__ == '__main__':
	app.run(debug=DEBUG)