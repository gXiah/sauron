"""
	Route '/vectorize'
"""

from __main__ import app, request, json
from __main__ import URI_PREFIX

#Temporary
from flask import send_file

route = URI_PREFIX + '/vectorize'
@app.route(route, methods=['GET'])
def vectorize_get():

	str_response = "Vectorize ..."
	status = 200


	response = send_file(
		'vectored.jpg',
		mimetype='image/gif'
	)

	return response