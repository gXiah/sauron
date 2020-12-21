"""
	Route '/lookup'
"""

from __main__ import app, request, json
from __main__ import URI_PREFIX, MIN_SIMILARITY

from scribe.postgresql.models.product_feature import ProductFeature
from utils.comparator.cosine_distance import compare

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

		# Fetching requested product data (from table 'product_feature')

		all_products_features = ProductFeature.get_all(ProductFeature)
		product_features = ProductFeature.get_by_ids(ProductFeature, product_id, store_id)
		
		if product_features:
			
			str_response = []
			str_response.append({'Request': {'Store id': store_id, 'Product id': product_id } })
			str_response.append({'Response' : {'picture url':product_features.picture_url, 'data size': len(product_features.feature_data), 'minimum similarity required': MIN_SIMILARITY } })
			status = 200

			comparison_results = []

			for p in all_products_features:
				similarity = compare(p.feature_data,product_features.feature_data)

				if similarity >= MIN_SIMILARITY:
					comparison_results.append({'product id': p.product_id, 'store_id': p.store_id, 'similarity':similarity })

			str_response.append({'similar products' :comparison_results})

		else:
			pass
		


	response = app.response_class(
		response = json.dumps(str_response),
		status = status, # OK
		mimetype='application/json'
	)

	return response