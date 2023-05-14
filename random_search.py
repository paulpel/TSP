from cities_gen import generate_distance_matrix
import numpy as np
import random as rd


def random_search(n_cities, iterations):
    distance_matrix = generate_distance_matrix(n_cities)
    random_starting_solution = np.random.permutation(n_cities)

    best_solution = None
    best_distance = np.inf

    for _ in range(iterations):
        total_distance = calc_distance(distance_matrix, random_starting_solution)
        if total_distance < best_distance:
            best_distance = total_distance
            best_solution = random_starting_solution.copy()

        neighbour_switch(random_starting_solution)

    return best_solution, best_distance


def neighbour_switch(solution):
    i, j = 0, 0
    while i == j:
        i, j = rd.randint(0, len(solution) - 1), rd.randint(0, len(solution) - 1)
    solution[i], solution[j] = solution[j], solution[i]


def calc_distance(distance_matrix, solution):
    N = distance_matrix.shape[0]
    total_distance = 0
    for i in range(N-1):
        total_distance += distance_matrix[solution[i], solution[i+1]]
    total_distance += distance_matrix[solution[N-1], solution[0]]

    return total_distance


if __name__ == "__main__":
    n_cities = 5
    iterations = 100
    bs, bd = random_search(n_cities, iterations)
    print(f"Best solution: {bs}")
    print(f"Best distance: {bd}")
