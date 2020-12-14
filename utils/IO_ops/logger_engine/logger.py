"""
	Utility for logging messages (console, database, ...)
"""

class Logger:

	separator = "-"

	def __init__(self):
		pass


	def print(self, message, separate=False):

		try:
			length = len(message)
		except TypeError as e:
			length = 20
		finally:
			pass

			
		separation = self.gen_separation(length)

		print()
		print(separation)
		print(message)
		print(separation)
		print()

	def gen_separation(self, messageLength):

		ret = ''

		for i in range(0, messageLength):
			ret += self.separator

		return ret