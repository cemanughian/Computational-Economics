import random
import math
import matplotlib.pyplot as plt


def knapsack_value(solution):
    value = sum(values[i] * solution[i] for i in range(len(solution)))
    total_weight = sum(weight[i] * solution[i] for i in range(len(solution)))
    if total_weight > max_weight:
        return max_weight - total_weight
    else:
        return value


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


def generate_neighbor(current_value):
    alpha = 0.05
    neighbor = []
    for v in current_value:
        if random.random() < alpha:
            neighbor.append(1 - v)
        else:
            neighbor.append(v)
    return neighbor


def accept_neighbor(neighbor, current_value, temp, eval_func):
    value_diff = eval_func(neighbor) - eval_func(current_value)
    prob_accept = math.exp(value_diff / temp)
    return random.random() < prob_accept


max_weight = 20
weight = [10, 5, 7, 8, 7, 2, 8]
values = [50, 24, 33, 50, 32, 1, 36]
steps = 100000

results = simulated_annealing(steps, [0 for i in range(len(values))], knapsack_value)

print(results[-1])
print(knapsack_value(results[-1]))
