import numpy as np 
import matplotlib.pyplot as plt 


def multiple_data(n_samples, n_features):
  X=list()
  E=list()

  alpha = np.abs(np.random.uniform(0.1,1, size=n_features))
  constant = np.random.uniform(0.1,1, size=n_features)
  for i in range(n_features):
      E.append(np.random.normal(0,np.abs(np.random.normal()), size=n_samples)) #noise generator
      X.append(np.random.normal(0,5,size=n_samples)) #single n_features random variable generation
      
  X = np.array(X).T
  E = np.array(E).T
  Y = np.sum(X*alpha + constant, axis=1)
  X = X+E
  return(X,Y)



def logistic_data(n_samples, n_features):

	mean1, mean2 = np.zeros(n_features) - 1, np.zeros(n_features) + 1
	cov_mat = np.identity(n_features)
##	cov_mat = np.array([[0.2,0.9],[0.4,0.7]])
	size1 = n_samples//2
	size2 = n_samples - size1
	x1 = np.random.multivariate_normal(mean1, cov_mat, size1)
	x2 = np.random.multivariate_normal(mean2, cov_mat, size2)

	y1 = np.zeros(size1)
	y2 = np.zeros(size2)+1

	y=np.hstack((y1,y2))
	x=np.vstack((x1,x2))
	
	return(x,y)


def kmeans_data(n_samples, n_features, n_clusters):
	cov_mat = np.identity(n_features)
	size = n_samples//n_clusters
	mean=np.random.multivariate_normal(np.zeros(n_features), cov_mat*n_clusters)
	x=np.random.multivariate_normal(mean, cov_mat, (n_samples-(size*(n_clusters-1))))
	y=np.zeros(n_samples-(size*(n_clusters-1)))
	size = n_samples//n_clusters

	for i in range(n_clusters-1):
		mean=np.random.multivariate_normal(np.zeros(n_features), cov_mat*n_clusters)
		x = np.vstack((x,np.random.multivariate_normal(mean, cov_mat, size)))
		y = np.hstack((y,(np.zeros(size)+i+1)))


	return(x,y)




# x,y = multiple_data(10,1)
# print(x.shape)
# print(y.shape)
# plt.scatter(x,y)

# x,y = kmeans_data(1000,2,4)
# print(x.shape)
# print(y.shape)
# plt.scatter(x[:,0],x[:,1],c=y)
# plt.show()


# x,y = logistic_data(100,2)
# print(x.shape)
# print(y.shape)
# plt.scatter(x[:,0], x[:,1], c=y)
# plt.show()
