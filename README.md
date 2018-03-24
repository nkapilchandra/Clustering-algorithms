


> # Clustering algorithms
> This repository contains python implementation of K-Means clustering and Density Based clustering algorithms

Example data is provided in the folder 'example_data'. The data looks something like this:
<img src="https://raw.githubusercontent.com/nkapilchandra/Clustering-algorithms/master/images/dataset.png" width="350" height="300"  />

The actual labels of the data set can be seen in this image below:
<img src="https://raw.githubusercontent.com/nkapilchandra/Clustering-algorithms/master/images/actual.png" width="350" height="300"  />


### Notes on K Means clustering
Centroid is randomly initialized in the beginning and then the clustering algorithm in run on the data set. It is evident from the data set that there are two clusters, hence we run the algorithm for two clusters and the result is as shown in the image below:
<img src="https://raw.githubusercontent.com/nkapilchandra/Clustering-algorithms/master/images/kmeans.png" width="350" height="300"  />

### Notes on density based clustering
Density based clustering algorithm was used on the same dataset with different cut off distances and different cut off number of neighbors. The results were as follows:

**For eps = 1.1 and min. points = 4**

<img src="https://raw.githubusercontent.com/nkapilchandra/Clustering-algorithms/master/images/DBSCAN_1.png" width="350" height="300"  />

**For eps = 1.1 and min. points = 5**

<img src="https://raw.githubusercontent.com/nkapilchandra/Clustering-algorithms/master/images/DBSCAN_2.png" width="350" height="300"  />

**For eps = 1.6 and min. points = 4**

<img src="https://raw.githubusercontent.com/nkapilchandra/Clustering-algorithms/master/images/DBSCAN_3.png" width="350" height="300"  />


### Comparison of performance of both algorithms
#### **K Means**
True positive rate for Centroid 1 = 1.0643
True positive rate for Centroid 2 = 1.0693

Number of points in cluster 1 = 215
Number of points in cluster 2 = 216

#### **DBSCAN**
True positive rate for Centroid 1 = 1.0396
True positive rate for Centroid 2 = 1.0247

Number of points in cluster 1 = 210
Number of points in cluster 2 = 207
