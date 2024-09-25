import numpy as np


def k_means(data: np.array, k:int, iterations: int=5) -> list[np.array]:
    '''
    Clusters `data` into `k` groups.

    Input:

    `data`: `np.array` - a numpy array with the data.

    `k`: `int` - number of partitions.

    `iterations`: `int` - number of models to test.

    Output:
    
    `[objective, centers, groups]`
    
    `objective`: `np.array[dtype=float]` - clustering objective scores for each iteration
    
    `centers`: `np.array[dtype=float]` - the representatives (centroids) for each grouping (clustering) with the shape `(k,)`.
    
    `groups`: `np.array[dtype=int]` - the group to which each data belongs with the shape (data.shape[0],) and with values between `0` and `k-1`.
    
    '''
    # Initialize the list of objectives and clusters for multiple random choices of representatives
    objectives = list()
    clusters = list()

    # Run five iterations with 5 randomly chosen representatives
    for _ in range(iterations):
        objective = list()
        # Randomly choose k representative for each ki-group
        centers = data[np.random.choice(np.arange(data.shape[0]), k, replace=False)]
        # Partition the data into k-groups based on the randomly selected representatives
        groups = np.array([np.argmin([np.linalg.norm(center - x) for center in centers]) for x in data])
        # Append initial objective
        objective.append(
            np.array([np.linalg.norm(data[i] - centers[groups[i]]) for i in range(data.shape[0])]).sum()
        )

        i = 0
        # Run infinitely
        while True:
            # Calculate the centroids based on the partitioned data
            centers = np.array([data[groups == g].mean(axis=0) for g in range(k)])
            # Group the data based on the new centroids
            groups = np.array([np.argmin([np.linalg.norm(center - x) for center in centers]) for x in data])
            # Append the calculated objective of the current clustering
            objective.append(
                np.array([np.linalg.norm(data[i] - centers[groups[i]]) for i in range(data.shape[0])]).mean()
            )
            if i > 2 and ((objective[-1] - objective[-2]) + (objective[-2] - objective[-3])) < 1.0:
                # If the sum of the differences between the last two pairs of objectives is less than 1.0
                # then the model is not improving and the centroids were identified
                break
            i += 1
        # If the model does not improve append the last clustering objective score
        objectives.append(objective[-1])
        # and append the model's data
        clusters.append([objectives, centers, groups])

    # Return the model with the smallest clustering objective score
    return clusters[np.argmin(objectives)]


if __name__ == '__main__':
    from sklearn.datasets import make_blobs
    import matplotlib.pyplot as plt
    data, _ = make_blobs(1000, 5)
    objective, centers, groups = k_means(data, 5)
    plot1 = plt.subplot2grid((2, 1), (0, 0), colspan=2)
    plot2 = plt.subplot2grid((2, 1), (1, 0), colspan=2)
    plot1.set_title(f'Clustered Data (k={5})')
    plot1.scatter(data[:,0], data[:,1], cmap='Set1', c=groups, s=1)
    plot1.scatter(centers[:,0], centers[:,1], c='black', marker='v')
    plot2.set_title('Clustering Objective')
    plot2.plot(objective)
    plt.show()
