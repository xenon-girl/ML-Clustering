from data import *
from LinearRegression import linear_regression
from LogisticRegression import logistic_regression
from KMC import k_means_clustering
import matplotlib.pyplot as plt
from utils import mean_squared_error, accuracy

#UNCOMMENT TO RUN

# multiple linear regression

##x,y = multiple_data(100,1)
##plt.scatter(x,y)
##plt.show
##reg_linear = linear_regression()
##reg_linear.fit(x,y)
##pred = reg_linear.predict(x)
##error = mean_squared_error(pred, y)
##print(error)


# logistic_regression

##x,y = logistic_data(100,2)
##plt.scatter(x[:,0],x[:,1],c=y)
##plt.show()
##clf_log = logistic_regression()
##clf_log.fit(x,y)
##pred = clf_log.predict(x)
##print(f'accuracy = {accuracy(pred,y)}')


# kmeans_clustering

x,y = kmeans_data(100,2,3)
plt.scatter(x[:,0],x[:,1],c=y)
plt.title("original_plot")
plt.show()
clusters = len(np.unique(y))
print(f'Number of clusters = {clusters}')
k = k_means_clustering(clusters)
y_pred = k.predict(x)
k.plot()
