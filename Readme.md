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
Naming the main function to be as ```{route name}\_{route_method}()``` is **STRONGLY** encouraged
<br>
After adding a route you should import it directly in the ```app.py``` :
```
import router.routes.root_route
```

### /api/lookup

**Note** Has not yet been implemented

Access to the route, however, is possible.
<br>
<br>
By calling this route and providing the ```product_id``` and ```store_id``` aparameters (/api/lookup?product_id=99&store_id=11), the API should return (for versions >=1.1) the closest matching products to looked up product, from the store's database.

### /api/vectorize

**Note** The .npz files are saved locally for now (V1.0)

<br>
<br>
This route, as of V1.0, retrieves a first set of data from 
```
./utils/extractor/pictures_urls_min.txt
``` 
(The \_min file is used for testing speed improvement, feel free to change to environement variable ```PIC_URLS_LIST_PATH``` in ```app.py``` to ```DEV_PATH``` in order to use a much larger, and thus longer to analyse, file).