"""
	Route '/'
"""

from __main__ import app, request, json

@app.route('/', methods=['GET'])
def root_get():

	store_id = request.args.get('store_id', default=0)
	product_id = request.args.get('product_id', default=0)

	str_response = "Undefined response"
	status = 300

	if store_id == 0 or product_id == 0:
		str_response = ["Missing one or more parameters"]
		status = 300
	else:
		str_response = [{'Response': ['Store id : {}'.format(store_id), 'Product id : {}'.format(product_id)] } ]
		status = 200


	response = app.response_class(
		response = json.dumps(str_response),
		status = status, # OK
		mimetype='application/json'
	)

	return response