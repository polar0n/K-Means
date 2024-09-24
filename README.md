# K-Means
 
### About ###
The following module implements clustering algorithm that test multiple models of randomly chosen data.


### Algorithm ###

__Given__ a list of _N_ vectors $x_1, ..., x_N$.

1. _Randomly sample k vectors from the given list of vectors_ $x_i$ _into centroids._

- _centroids (representatives)_. $z_{c_i}$ is a randomly sampled vector $x_m$, where $1 < c_i < k$ and $1 < m < N$

_Repeat until convergence_. I.e., $J_{clust}$ _doesn't change._

2. _Cluster the data into_ k _groups_. For each vector $x_1, ..., x_N$, assign $x_i$ to the group $G_j$ associated with the nearest representative.
- where $1 < j < k$
- nearest representative is $min(||x_i-z_{c_i}||, ..., ||x_i-z_{c_N}||)$


3. _Update representatives_. For each group $g_j$, $j=1,...,k$, set $c_j$ to the mean of the group vectors.
- Mean of the group vectors is defined as, $\frac{\sum{x_i}}{l}$, where $x_i \in G_j$ and $l = card\{x_i, x_i \in G_j\}$

_Clustering objective_ is the score assigned to a clustering. The score represents the mean of the squared norm of distances between vectors and their representatives.
$J_{clust} = \frac{1}{N}\sum_{i}^{N}{||x_i-z_{c_i}||^2}$
