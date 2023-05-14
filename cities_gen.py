import numpy as np


def generate_distance_matrix(N):
    # Generate random distances for each pair of points
    distances = np.random.rand(N, N)

    # Initialize distance matrix with zeros
    distance_matrix = np.zeros((N, N))

    # Assign distances to the matrix, considering both directions
    for i in range(N):
        for j in range(N):
            if i != j:
                distance_matrix[i, j] = distances[i, j]
                distance_matrix[j, i] = distances[j, i]

    return distance_matrix
