from sklearn.metrics.pairwise import cosine_similarity
import pickle
import numpy as np

def compare(m1, m2):
	
	v1 = np.array([bytearray(m1)])
	v2 = np.array([bytearray(m2)])

	sim_result = cosine_similarity(v1, v2)

	if sim_result and sim_result[0]:
		return sim_result[0][0]
	else:
		return 0