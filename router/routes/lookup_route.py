"""
	Route '/lookup'
"""

from __main__ import app, request, json
from __main__ import URI_PREFIX

route = URI_PREFIX + '/lookup'
@app.route(route, methods=['GET'])
def lookup_get():

	store_id = request.args.get('store_id', default=0)
	product_id = request.args.get('product_id', default=0)

	str_response = "Undefined response"
	status = 400

	if store_id == 0 or product_id == 0:
		str_response = ["Missing one or more parameters"]
		status = 400
	else:
		str_response = [{'Response': ['Store id : {}'.format(store_id), 'Product id : {}'.format(product_id)] } ]
		status = 200


	response = app.response_class(
		response = json.dumps(str_response),
		status = status, # OK
		mimetype='application/json'
	)

	return response