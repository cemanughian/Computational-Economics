""" Sept 19 2019
Stratefied sampling

"""
import math
import random
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def g(x):
    return math.pow(x, 2)


if __name__ == "__main__":
    # Integrate from a to b, g(x) = x^2
    # Simulation for expected value of g(x) = x^2
    runs = 1000
    results = []
    a = 1
    b = 4
    for run in range(0, runs):
        x = random.uniform(a, b)
        results.append(g(x))
    # Get the expected value of the quadratic
    expd_value_g = sum(results) / runs
    print(expd_value_g*(b-a))

    # Let's estimate this integral using simple random sampling and stratified random sampling
    # Compare accuracy vs sample size for different sampling strategies
    # Larger sample size = smaller variance

    # New stuff - convert to my language
    bounds = [1,4]
    trials = 100
    num_samples = 10
    # Each trial well draw 10 samples from our uniform disn
    # Take those samples and do our MC integration
    estimates = []
    for i in range(trials):
        y_is = [g(random.uniform(*bounds)) for _ in range(num_samples)]
        estimates.append((bounds[1] - bounds[0]) * sum(y_is)/num_samples)
    # sns.distplot(estimates)
    plt.hist(estimates)
    print(np.mean(estimates))

    # Now lets make our draws using stratefied sampling from the uniform disn
    # Want them equal segments because we want it representative of the disn were drawing from

    delta = (bounds[1] - bounds[0])/num_samples  # difference between the size of each segment
    stratefied_bounds_for_draws = [(bounds[0]+i*delta, bounds[0]+(i+1)*delta) for i in range(num_samples)]

    # Need our draws to draw from those intervals from stratefied_bounds_for_draws
    stratefied_estimates = []
    for i in range(trials):
        draws = []
        for bound in stratefied_bounds_for_draws:
            # Draw a random number from the bound, plug it into our quadratic function g, and save that
            draws.append(g(random.uniform(*bound)))
        stratefied_estimates.append((bounds[1] - bounds[0]) * (sum(draws)/num_samples))

    plt.hist(stratefied_estimates)
    # This one is much better than the previous one



    # Antithetic Sampling
    # Integrate x^3  between 0 and 1
    def cubic(x):
        return x**3

    # Refactor
    def uniform_sample_from_fct(fct, bounds, sample_size):
        draws = [random.uniform(*bounds) for _ in range(sample_size)]
        return [fct(draw) for draw in draws]

    def antithetic_sample(fct, bounds, sample_size):
        draws = []
        for i in range(sample_size//2):  # // = Number of whole times you can divide it by
            draw = random.uniform(*bounds)
            draws.append(draw)
            draws.append(sum(bounds) - draw)  # sum(bounds) is the avg for uniform
        # Acount for //
        if sample_size % 2 == 1:
            draws.append(random.uniform(*bounds))
        return [fct(draw) for draw in draws]

    # TODO: Finish dis
    bounds = [0, 1]
    antithetic_estimates = []
    for i in range(trials):
        draws = antithetic_sample(cubic, bounds, num_samples)
        antithetic_estimates.append(draws)
    plt.hist(antithetic_estimates)


