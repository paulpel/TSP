import numpy as np
import random

def simulated_annealing(n_cities, iterations, initial_temperature, cooling_rate):
    distance_matrix = generate_distance_matrix(n_cities)
    current_solution = np.random.permutation(n_cities)
    best_solution = current_solution.copy()

    current_distance = calc_distance(distance_matrix, current_solution)
    best_distance = current_distance

    temperature = initial_temperature

    for _ in range(iterations):
        # Generate a neighboring solution
        new_solution = neighbour_switch(current_solution)

        # Calculate the distances of the current and new solution
        current_distance = calc_distance(distance_matrix, current_solution)
        new_distance = calc_distance(distance_matrix, new_solution)

        # Accept the new solution with a probability based on the current temperature
        if accept_solution(current_distance, new_distance, temperature):
            current_solution = new_solution
            current_distance = new_distance

        # Update the best solution if necessary
        if current_distance < best_distance:
            best_solution = current_solution.copy()
            best_distance = current_distance

        # Cool down the temperature
        temperature *= cooling_rate

    return best_solution, best_distance


def accept_solution(current_distance, new_distance, temperature):
    if new_distance < current_distance:
        return True
    else:
        acceptance_probability = np.exp((current_distance - new_distance) / temperature)
        return random.random() < acceptance_probability


# Rest of the code remains the same

if __name__ == "__main__":
    n_cities = 5
    iterations = 1000
    initial_temperature = 100.0
    cooling_rate = 0.95

    best_solution, best_distance = simulated_annealing(n_cities, iterations, initial_temperature, cooling_rate)

    print("Best solution:", best_solution)
    print("Best distance:", best_distance)
