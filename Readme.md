# Sauron

Sauron is a micro-API tailor made for Cleed's use. It was designed, in its first version, to meet two simple requirements :
- Be able to fetch, analyse (Features extraction), and save in a convenient format - data related to stores products
- Give access (via a GET request) as an API for a user to request a match-search of a particular product (The API would then return the closest matching products it could find)

## Installation
```
$ pip install 
``` 
Or
```
$ pip3 install 
```
## Launching the development server
Simply use
```
$ python3 app.py
```
(Python 3 is recommended)

## Usage


### Adding Routes
Each route is described by a single ```.py``` file. The routes should be located (for organizational purposes) at ```./router/routes/``` 
<br>
Here is an example of a route file : 
```
"""
	Route '/'
"""

from __main__ import app, request, json

route = '/' # The route's URI
@app.route(route, methods=['GET']) # The route is made of an URI and an access method
def root_get(): 

	str_response = "API ON" 
	status = 200

	# Send the response minimal data
	response = app.response_class(
		response = json.dumps(str_response),
		status = status,
		mimetype='application/json'
	)

	return response
```
Naming the main function ```{route name}_{route_method}()``` is **STRONGLY** recommended
<br>
After adding a route you should import it directly in the ```app.py``` :
```
import router.routes.root_route
```

### Search for matching pictures
```
/api/lookup?product_id&store_id
```

By calling this route and providing the ```product_id``` and ```store_id``` GET parameters, the API should return the closest matching products to the looked up product, from the store's database.

### Feature extraction
```
/api/vectorize
```
*Disabled for now*

Retrieves the picture URLs from the database (table *products*) and applies a feature extraction algorithm on each picture. The results are then stored in the *product_feature* table.

### Adding data using an external API
```
/api/add
```

Data can be added by sending a POST request to the api with the following body
```
{
    "store_id": INT,
    "product_id": STRING,
    "picture_url": STRING,
    "feature_data": [INT]
}
``` 
**Note** that the feature_data has to be a *bytearray* friendly array, in other words the values should be in a way that makes it possible for *byte* conversion (ie. less that 256)

This route adds, in case of *success*, the product feature object to the database.
And it always returns, on top of the status, a JSON string response containing the status and the error, if any, that has been raised.