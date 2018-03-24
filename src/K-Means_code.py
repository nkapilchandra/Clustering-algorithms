'''                                     K-MEANS ALGORITHM                       '''
'''                                    Written in Python 2                      '''

# Import required libraries
import numpy as np
import matplotlib.pyplot as plt
from random import *
from math import *
import os

# Taking data from the file
path = os.getcwd()
path = path.strip('src') + 'example_data/PA1.txt'
data = np.loadtxt(path,usecols = (0,1))

# plt.scatter(data[:,0],data[:,1])

# Take two random points
c1 = choice(data)
c2 = choice(data)

'''Initializing clusters and centroids'''
C1 = [];
C2 = [];
centroids = [[0,0]];
c1o = [0.0,0.0]; #Old centroid 1
c2o = [0.0,0.0]; #Old centroid 2

k=0 # This is a counter


'''                                 COMPUTATION                                 '''

while (True):
    C1 = []
    C2 = []

    # Assignment of each data point to clusters
    for i in data:
        d1 = sqrt((c1[0]-i[0])**2 + (c1[1]-i[1])**2)
        d2 = sqrt((c2[0]-i[0])**2 + (c2[1]-i[1])**2)

        if (d1 < d2):
            C1.append(i)
        else:
            C2.append(i)

    ''' Calculation of new centroids '''
    c1o = c1; # Saving old centroids before updating
    c2o = c2;
    s1x,s1y = 0.0,0.0
    s2x,s2y = 0.0,0.0

    for i in C1:
        s1x = s1x + i[0]
        s1y = s1y + i[1]
    for i in C2:
        s2x = s2x + i[0]
        s2y = s2y + i[1]

    c1[0] = s1x/float(len(C1)); # X-coordinate of centroid 1
    c1[1] = s1y/float(len(C1)); # Y-coordinate of centroid 1
    c2[0] = s2x/float(len(C2)); # X-coordinate of centroid 2
    c2[1] = s2y/float(len(C2)); # Y-coordinate of centroid 2

    centroids = np.vstack([centroids,c1])

    print c1 # To check the values of centroids
    k = k+1

    if (centroids[k-1][0]-c1[0])**2+(centroids[k-1][1]-c1[1])**2 == 0: # Condition to see change in centroids
        break

print len(C1),len(C2)


'''                                       PLOTTING                              '''

x1 = []
y1 =[]
x2 = []
y2 =[]

for i in C1:
    x1.append(i[0])
    y1.append(i[1])
for i in C2:
    x2.append(i[0])
    y2.append(i[1])

clus1 = plt.scatter(x1,y1,color='red',label='Cluster 1');
clus2 = plt.scatter(x2,y2,color='blue',label = 'Cluster 2');
cen1 = plt.scatter(c1[0],c1[1],color='green',label = 'Centroid 1')
cen2 = plt.scatter(c2[0],c2[1],color='yellow',label = 'Centroid 2')
plt.legend(handles = [clus1,clus2,cen1,cen2])
plt.title('Scatter plot after K-Means')
plt.show()
