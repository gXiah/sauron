"""
	Product model
"""

from __main__ import database as db

class Product(db.Model):

	__tablename__ = 'products'

	product_id = db.Column(db.Text(), primary_key=True)
	store_id = db.Column(db.Integer, primary_key=True)

	picture_url = db.Column(db.Text())

	def __init__(self, product_id, store_id, picture_url):
		pass

	"""
		Returns the pictures along with the product_id and store_id
	"""
	def get_all_min(self):
		return self.query.all()

"""
	description = db.Column(db.Text())
	color = db.Column(db.Text())
	url = db.Column(db.Text())

	price = db.Column(db.Numeric(2, 12))
	price_old = db.Column(db.Numeric(2, 12))

	category = db.Column(db.Text())

	thumbnail_url = db.Column(db.Text())
	sizes = db.Column(db.Text())
	brand = db.Column(db.Text())
	name = db.Column(db.Text())

	updated_at = db.Column(db.)
	created_at = db.Column(db.)

	alternate = db.Column(db.Array(db.Text()))
	alternate_thumbnail = db.Column(db.Array(db.Text()))

	shipping_cost = db.Column(db.Numeric(2, 12))
	quantity = db.Column(db.)
	
	stock = db.Column(db.Text())

	material = db.Column(db.Array(db.Text()))
	
	on_sale = db.Column(db.)
	details = db.Column(db.)
	gender = db.Column(db.)
	
	category_name = db.Column(db.Text())

	style = db.Column(db.)
	variation = db.Column(db.)
	excluded = db.Column(db.)
	custom = db.Column(db.)
	normalized_category = db.Column(db.)
	normalized_sizes = db.Column(db.)

	discount = db.Column(db.Text())
	name_fr = db.Column(db.Text())
	
	categories = db.Column(db.Array(db.Text()))
	colors = db.Column(db.Array(db.Text()))
	pattern = db.Column(db.Array(db.Text()))
"""