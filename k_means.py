import numpy as np
import matplotlib.pyplot as plt


class KMeans():
  def __init__(self, K, epsilon):
    self.K = K
    self.epsilon = epsilon

  def initialize(self, X, K):
    """
    Initilize K random Centroids
    
    """
    indices = np.arange(len(X))
    np.random.shuffle(indices)
    X = np.array(X)
    X = X[indices]
    Centroids = X[:K]
    return Centroids

  def EuclideanDistance(self, x1, x2):
    """
    The sum of the squared differences of the elements

    """
    dist =np.sqrt(np.sum((x1-x2)**2))
    return dist

  def Classify(self, centroids, X):
    """
    Classify item to the cluster with minimum distance 

    """
    
    distances = np.zeros((len(centroids), len(X)))
    for i in range(len(centroids)):
      for j in range(len(X)):
        distances[i][j] = self.EuclideanDistance(centroids[i], X[j])

    labels= np.argmin(distances, axis=0)
  
    return labels

  def update_centroids(self, Assignments, X):
    """
    Calculate the new means
    
    """
    centroids = np.zeros((self.K , X.shape[1]))
    """
    for i in range(self.K):
      arr = np.array([X[j] for j,q in enumerate(Assignments) if q==i])
      centroids[i] = np.sum(arr, axis=0)/len(arr)
    """
    for i in range(self.K):
      centroids[i] = np.mean(X[Assignments == i], axis = 0)

    return centroids
  

  def fit(self, data):
    """
    Fit the K-Means algorithm untill no changes happens or changes < epsilon
    
    """
    old_centroids = self.initialize(data, self.K)
    assignments = self.Classify(old_centroids, np.array(data))
    
    
    error = 1

    
    while(error >= self.epsilon):

      new_centroids = self.update_centroids(assignments, np.array(data))
      assignments = self.Classify(new_centroids, np.array(data))
      error = np.mean(np.abs(new_centroids-old_centroids))
      print("loss", error)
      old_centroids = new_centroids

    
    return assignments, new_centroids


  def visualize_clusters(self, X, assignments, new_centroids):

      num_centers = max(assignments)

      for i in range(num_centers+1):
        c_= [index for index,value in enumerate(assignments) if value == i]
        c= X.loc[c,:]

        plt.scatter(
            c.iloc[:,0], c.iloc[:,1],
            s=50,
            marker='s', edgecolor='black',
            label='cluster'+str(i+1)
            )

      

    # plot the centroids

      plt.scatter(
        new_centroids[:, 0], new_centroids[:, 1],
        s=250, marker='*',
        c='red', edgecolor='black',
        label='centroids'
       )

      plt.legend(scatterpoints=1)
      plt.grid()
      plt.show()

