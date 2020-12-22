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





	def get_all_by_store_id(self, str_id):
		return self.query.filter_by(store_id=str_id).all()




	def get_by_ids(self, prod_id, str_id):
		res = self.query.filter_by(product_id=prod_id, store_id=str_id).all()
		if len(res) > 0:
			return res[-1]
		else:
			return []




	def add_one(self):
		
		res = 0

		try:
			db.session.add(self)
		except:
			pass
		db.session.commit()
		

		return res