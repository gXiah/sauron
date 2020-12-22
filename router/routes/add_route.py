"""
	Route '/api/add'
"""

from __main__ import app, request, json
from __main__ import URI_PREFIX


from scribe.postgresql.models.product_feature import ProductFeature


route = URI_PREFIX + '/add'

MISSING_PARAMS_ERROR = False


@app.route(route, methods = ['POST'])
def add_post():


	status = 200 # Return status
	message = 'No message'

	BYTE_ARRAY_CONV_ERROR = False
	MISSING_PARAMS_ERROR = False

	# Stores the product_feature object 
	feature_object = {}

	try:
		# Fetching post data
		request_data = request.get_json()

		# These are the required keys we want from the request data
		required_key = [
						'store_id',
						'product_id',
						'picture_url',
						'feature_data']

		# Received keys
		sent_keys = request_data.keys()

	except:
		print('Error while adding product - JSON Parse Error')
		message = 'JSON Parse Error'
		status = 400
		MISSING_PARAMS_ERROR = True


	# Checking if all keys have been sent
	for rk in required_key:
		if rk not in sent_keys:
			MISSING_PARAMS_ERROR = True
			break
		else:
			feature_object[rk] = request_data[rk]




	if not MISSING_PARAMS_ERROR:


		try:
			feature_object['feature_data'] = bytearray(feature_object['feature_data'])
		except:
			message = 'Could not convert request data to bytearray'
			status = 400
			BYTE_ARRAY_CONV_ERROR = True
		


		if BYTE_ARRAY_CONV_ERROR == False:

			product_feature_object = ProductFeature(
											feature_object[required_key[1]], # Prod id
											feature_object[required_key[0]], # Store id
											feature_object[required_key[2]], # Pic url
											feature_object[required_key[3]]  # Feat data
										)

			res = ProductFeature.add_one(product_feature_object)
			if res == 0:
				print('Added product - #{} / {}'.format(
							feature_object[required_key[0]],
							feature_object[required_key[2]])
				)
			else:
				print('Error while adding product #{} / {}'.format(
							feature_object[required_key[0]],
							feature_object[required_key[2]])
				)
				status = 500
				message = 'Error while committing to database'



	else:
		status = 400
		message = 'Missing one or more paraeters'

	


	response = app.response_class(
		response = json.dumps('Returned with code {} and message {}'.format(status, message)),
		status = status, # OK
		mimetype='application/json'
	)

	return response