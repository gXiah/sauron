from flask import Flask, request, json
from flask_sqlalchemy import SQLAlchemy

import os
from datetime import datetime

from utils.IO_ops.logger_engine.logger import Logger
Logger = Logger()

"""
	Environment variables
"""

URI_PREFIX = '/api' # The prefix to be put before each URI (eg: '/api/lookup?param=...')
DEBUG = True

DEV_DB_URI = 'postgresql://adam:fml@localhost/sauron'
PROD_DB_URI = 'postgres://selectonly:readonly@ec2-35-180-192-221.eu-west-3.compute.amazonaws.com:5432/postgres' # Cleed's database url (for security reasons, we are using the local url)

# Environment
DEV_ENV = 'dev'
PROD_END = 'prod'
ENV = PROD_END

# Temporary : Pictures URLs are saved here
DEV_MIN_PATH = 'utils/extractor/pictures_urls_min.txt'
DEV_PATH = 'utils/extractor/pictures_urls.txt'
PROD_PATH = ''
PIC_URLS_LIST_PATH = DEV_PATH

# .npz save path (feature extraction @ /api/vectorize)
DEV_SAVE_PATH = 'data/npz/' + datetime.now().strftime("%Y-%B-%d--%H-%M-%S")
PROD_SAVE_PATH = '/home/ubuntu/stylenet/embeddings/fendi.npz'
EMBEDDINGS_SAVE_PATH = DEV_SAVE_PATH 

# Enabeling / Disabeling local saving of the .npz
DEV_SAVE_LOCALLY = True
PROD_SAVE_LOCALLY = False
SAVE_LOCALLY = PROD_SAVE_LOCALLY

MIN_SIMILARITY = 0.8

app = Flask(__name__)



#=================================

if ENV == DEV_ENV: # Local env
	
	DEBUG = True
	app.config['SQLALCHEMY_DATABASE_URI'] = DEV_DB_URI

elif ENV == PROD_END: # Prod env

	DEBUG = False
	app.config['SQLALCHEMY_DATABASE_URI'] = PROD_DB_URI 


else:
	die('Unrecognized environment (@ ./app.py)')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Suppressing SQLAlchemy warnings
database = SQLAlchemy(app)

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
	Importing models
"""
import scribe.postgresql.models.product_feature # product_feature table
import scribe.postgresql.models.product # products table (sized down version)

database.create_all()

"""
	Starting up the server
"""
HOST = '0.0.0.0'
PORT = 8080

if __name__ == '__main__':
	app.run(debug=True, host=HOST, port=PORT)
