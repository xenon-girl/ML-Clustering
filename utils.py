import numpy as np


def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2)**2))


def accuracy(y1, y2):
	count=0
	for i in range(len(y1)):
		if y1[i]==y2[i]:
			count+=1

	return count/len(y1)*100
    

def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred)**2)
