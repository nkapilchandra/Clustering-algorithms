"""                                  DBSCAN Algorithm for clustering                   """
"""                                       Written in Python 2                          """

#Import required libraries
import numpy as np
import matplotlib.pyplot as plt
from random import *
from math import *
import os

# Taking data from the file
path = os.getcwd()
path = path.strip('src') + 'example_data/PA1.txt'
data = np.loadtxt(path, usecols = (0,1))
data1 = np.loadtxt(path, usecols = (2))

# plt.scatter(data[:,0],data[:,1],)

# Functions defined to use in the code further

def distance(x,y):
    """
    Function to calculate distance between two points.

    Args:
    x (tuple): Point 1
    y (tuple): Point 2

    Returns:
    dist (float): Distance between two points
    """

    dist = sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)
    return dist

def neighbors(point,e,d):
    """
    Function to determine neighbors of a given point.

    Args:
    point (tuple): Point
    e (float): Cut off radius
    d (list): List of all points, basically, all the data points

    Returns:
    pts (list): A list point in the neighborhood of point
    """

    pts = []
    for i in range(0,len(d)-1):
        if (distance(point,data[i]) <= e):
            pts.append(i)

    return pts


# Defining all the variable needed in the code

e = float(raw_input('enter the value of eps'))
n = float(raw_input('enter the value of min points'))
core = []
noise = []
border = []
others = []
clusters = []
k = -1 # Index of the cluster
v = [] # Contains indices of the points already visited in PART 2 of code


'''                                      PART 1                                 '''
'''                       To identify core, border and noise points              '''

for i in range(0,431):
    counter = 0

    for j in range(0,431):
        if (distance(data[i],data[j]) <= e):
            counter += 1
    if counter >= n:
        core.append(i)
    else:
        others.append(i)

for i in others:
    flag = 0
    for j in core:
        if (distance(data[i],data[j]) <= e):
            flag = 1
            break
    if flag == 1:
        border.append(i)
    else:
        noise.append(i)



'''                                       PART 2                                '''
'''                To interate through core and border points and cluster them  '''

onpoints = [] # A temporary variable used to check if the variable npoints has changed

for i in core:
    if i not in v:
        v.append(i)
        k += 1
        clusters.append([])
        clusters[k].append(i)
        npoints = neighbors(data[i],e,data)
        while True:
            onpoints = npoints
            for point in npoints:
                if point not in v:
                    v.append(point)
                    npoints2 = neighbors(data[point],e,data)
                    if (len(npoints2) >= n):
                        npoints = npoints + npoints2
                if point not in (j for j in clusters):
                    clusters[k].append(point)
            if len(onpoints) == len(npoints):
                break


# Print the final data to the screen
print ''
print "RESULTS:"
print 'No. of clusters = ', len(clusters)
c1 = list(set(clusters[0])) # Cluster 1
c2 = list(set(clusters[1])) # Cluster 2
print 'No. of points in cluster 1 = ',len(c1)
print 'No. of points in cluster 2 = ',len(c2)



'''                                      PART 3                                 '''
'''                             Plotting scatter points                         '''

x1,y1 = [],[]
x2,y2 = [],[]
x,y = [],[]

for i in c1:
    x1.append(data[i][0])
    y1.append(data[i][1])
for j in c2:
    x2.append(data[j][0])
    y2.append(data[j][1])
for k in noise:
    x.append(data[k][0])
    y.append(data[k][1])

clus1 = plt.scatter(x1,y1,color='green',label='Cluster 1') #Cluster 1
clus2  = plt.scatter(x2,y2,color='blue',label='Cluster 2') #Cluster 2
s = plt.scatter(x,y,color='red',label='Noise') #Noise points
plt.legend(handles=[clus1,clus2,s])
plt.title('Plot after DBSCAN')
plt.show()
