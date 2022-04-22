import random
import math
import matplotlib.pyplot as plt


def simulated_annealing(steps, init_value, eval_func):
    current_value = init_value
    values = [init_value]
    for s in range(steps):
        temp = calculate_temp(s, steps)
        current_value = simulated_annealing_step(temp, current_value, eval_func)
        values.append(current_value)

    return values


def calculate_temp(step, num_steps):
    init_temp = 1
    alpha = 5
    return init_temp * (1 - alpha / num_steps) ** step


def simulated_annealing_step(temp, current_value, eval_func):
    neighbor = generate_neighbor(current_value)
    if accept_neighbor(neighbor, current_value, temp, eval_func):
        return neighbor
    else:
        return current_value


def accept_neighbor(neighbor, current_value, temp, eval_func):
    value_diff = eval_func(neighbor) - eval_func(current_value)
    prob_accept = math.exp(value_diff / temp)
    return random.random() < prob_accept


def generate_neighbor(solution):
    neighbor = list(solution)
    nodes = random.sample(range(1, len(solution)), k=2)
    neighbor[nodes[0]] = solution[nodes[1]]
    neighbor[nodes[1]] = solution[nodes[0]]
    return neighbor


def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def tsp_distance(solution):
    total_dist = 0
    current_city = solution[0]
    for city in solution[1:]:
        total_dist += euclidean_distance(current_city, city)
        current_city = city

    total_dist += euclidean_distance(solution[0], solution[-1])
    return -total_dist


def plot_path(path):
    full_path = complete_path(path)
    plt.plot([p[0] for p in full_path], [p[1] for p in full_path])
    plt.show()


def complete_path(path):
    full_path = list(path)
    full_path.append(path[0])
    return full_path


if __name__ == "__main__":

    num_cities = 50
    locations = [(random.random(), random.random()) for _ in range(num_cities)]

    steps = 1000000

    results = simulated_annealing(steps, locations, tsp_distance)

    print("")
    print(tsp_distance(locations))
    plot_path(locations)
    # print(results[-1])
    print(tsp_distance(results[-1]))
    plot_path(results[-1])
    print("")
    print("")
