import pandas as pd
import numpy as np
from numpy import genfromtxt
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('bp_data_mean.csv', index_col=0)
my_data = genfromtxt('bp_data_mean.csv', delimiter=',')
print(my_data)

kmeans = KMeans(n_clusters=2)  
kmeans.fit(df)  
print(kmeans.cluster_centers_)  

kmeans = KMeans(n_clusters=3)  
kmeans.fit(df)  
print(kmeans.cluster_centers_)  

kmeans = KMeans(n_clusters=4)  
kmeans.fit(df)  
print(kmeans.cluster_centers_)  