from flask import Flask, request, json
import os
from utils.IO_ops.logger_engine.logger import Logger
Logger = Logger()

"""
	Environment variables
"""

URI_PREFIX = '/api' # The prefix to be put before each URI (eg: '/api/lookup?param=...')
DEBUG = True

DEV_DB_URI = 'postgresql://adam:fml@localhost/sauron'
PROD_DB_URI = DEV_DB_URI # Cleed's database url (for security reasons, we are using the local uri)

DEV_ENV = 'dev'
PROD_END = 'prod'

ENV = DEV_ENV

DEV_MIN_PATH = 'utils/extractor/pictures_urls_min.txt'
DEV_PATH = 'utils/extractor/pictures_urls.txt'
PROD_PATH = ''
PIC_URLS_LIST_PATH = DEV_MIN_PATH

DEV_SAVE_PATH = 'data/npz'
PROD_SAVE_PATH = '/home/ubuntu/stylenet/embeddings/fendi.npz'
EMBEDDINGS_SAVE_PATH = DEV_SAVE_PATH 


app = Flask(__name__)



#=================================

if ENV == DEV_ENV: # Local env
	
	DEBUG = True
	app.config['SQLALCHEMY_DATABASE_URI'] = DEV_DB_URI

elif ENV == PROD_END: # Prod env

	DEBUG = False
	app.config['SQLALCHEMY_DATABASE_URI'] = PROD_DB_URI 


else:
	die('Unrecognized environment (@app.py)')

#=================================


#Suppressing INFO and WARNING messages (because of Tensorflow)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
Logger.print("Suppressing WARNING and INFO messages")



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