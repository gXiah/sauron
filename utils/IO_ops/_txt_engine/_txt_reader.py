"""
	This is the function that returns the pictures urls
	For developments purposes, the urls are already stored in a file
	(utils/extractor/pictures_urls.txt)

	The next step would be to ask this function to get the urls directly from the database
"""
def get_lines(filepath):

	with open(filepath) as f:
			lines = f.readlines()

	content = [l.strip() for l in lines]

	return content