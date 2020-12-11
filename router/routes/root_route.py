"""
	Route '/'
"""

from __main__ import app, request, json
from __main__ import URI_PREFIX

route = URI_PREFIX + '/'

@app.route('/', methods=['GET'])
@app.route(route, methods=['GET'])
def root_get():

	str_response = "API ON"
	status = 200


	response = app.response_class(
		response = json.dumps(str_response),
		status = status, # OK
		mimetype='application/json'
	)

	return response