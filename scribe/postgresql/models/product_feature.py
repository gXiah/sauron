"""
	Product Features model
	(This model hold the store's ID, the product's ID, and the image URL)
"""

from __main__ import database as db

class ProductFeature(db.Model):
	
	__tablename__ = 'product_feature'

	id = db.Column(db.Integer, primary_key=True)
	product_id = db.Column(db.Text())
	store_id = db.Column(db.Integer)
	picture_url = db.Column(db.Text())
	feature_data = db.Column(db.LargeBinary())

	def __init__(self, product_id, store_id, picture_url, feature_data):
		self.product_id 	= product_id
		self.store_id 		= store_id
		self.picture_url 	= picture_url
		self.feature_data 	= feature_data


	def get_all(self):
		return self.query.all()