from flask import Flask, request, json


"""
	Environment variables
"""
ENV = 'dev'

app = Flask(__name__)
#=================================



"""
	Importing routes
"""
import router.routes.root_route
#=================================




"""
	Starting up the server
"""
if __name__ == '__main__':
	app.run(debug=True)