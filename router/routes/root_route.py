"""
	Route '/'
"""

from __main__ import app, request, json

@app.route('/', methods=['GET'])
def root_get():

	store_id = request.args.get('store_id', default=0)
	product_id = request.args.get('product_id', default=0)

	response = app.response_class(
		response = json.dumps("Returned string"),
		status = 200, # OK
		mimetype='application/json'
	)

	return response