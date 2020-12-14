"""
	Route '/vectorize'
"""

from __main__ import app, request, json
from __main__ import URI_PREFIX, PIC_URLS_LIST_PATH, EMBEDDINGS_SAVE_PATH

import utils.extractor.features_extractor as extractor


route = URI_PREFIX + '/vectorize'
@app.route(route, methods=['GET'])
def vectorize_get():

	str_response = "Vectorize ..."
	status = 200


	extractor.init(PIC_URLS_LIST_PATH, EMBEDDINGS_SAVE_PATH)


	response = app.response_class(
		response = json.dumps(str_response),
		status = status, # OK
		mimetype='application/json'
	)

	return response