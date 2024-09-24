# K-Means
 
### About ###
The following module implements clustering algorithm that test multiple models of randomly chosen data.


### Algorithm ###

__Given__ a list of *N* vectors $x_1, ..., x_N$.

*Randomly sample* k *vectors from the given list of vectors $x_i$ into centroids.*
- *centroids*. $c_j$ is a randomly sample vector $x_m$, where $1 < j < k$ and $1 < m < N$


1. *Cluster the data into* k *groups*. For each vector $x_1, ..., x_N$, assign $x_i$ to the group $G_j$ associated with the nearest representative.
- where $1 < j < k$
- nearest representative is $min(||x_i-c_1||, ..., ||x_i-c_{k}||)$


2. *Update representatives*. For each group $g_j$, $j=1,...,k$, set $c_j$ to the mean of the group vectors.
- Mean of the group vectors is defined as, $\frac{\sum{x_i}}{l}$, where $x_i \in G_j$ and $l = card\{x_i, x_i \in G_j\}$