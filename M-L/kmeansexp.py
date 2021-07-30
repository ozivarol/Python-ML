import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from sklearn.cluster import KMeans

class Kmeans1:
 def Alg(self):
    dataset = pd.read_csv('EPL_20_21.csv')
    X = dataset.iloc[:,[7,8]].values
    wcss = []
    kume_sayisi_listesi = range(1, 12)
    for i in kume_sayisi_listesi :
        kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 500, n_init = 20, random_state = 0)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)
    
    kmeans = KMeans(n_clusters = 5, init = 'k-means++', max_iter = 500, n_init = 20, random_state = 0)
    y_kmeans = kmeans.fit_predict(X)
    plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Küme 1')
    plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Küme 2')
    plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Küme 3')
    plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Küme 4')
    plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Küme 5')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 200, c = 'yellow', label = 'Küme Merkezleri')
    plt.title('Goal-Mins')
    plt.xlabel('Mins')
    plt.ylabel('Goals')
    plt.legend()
    plt.show()

