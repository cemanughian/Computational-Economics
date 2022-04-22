"""
CS 532 Assignment 5
Due Oct 29, 2019
Celeste Manughian-Peter
No. 3 - Product Mix
"""
from ortools.linear_solver import pywraplp

if __name__ == "__main__":
    profits = [10, 22, 35, 19, 55, 10, 115]
    production_times = [1, 2, 3.7, 2.4, 4.5, .7, 9.5]
    man_hours_per_week = 720
    p7_penalty_cost = 2000

    # Define solver
    solver = pywraplp.Solver("Maximize profits given production constraints",
                             pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)  # Name and type of solver

    # Define variables that we want to solve for
    product_units = [solver.IntVar(0, solver.infinity(), 'Units to produce of product ' + str(i+1)) for i in
                     range(len(profits))]
    product7_penalty = solver.IntVar(0, 1, 'Penalty for product 7')
    product34_manhour_penalty = solver.IntVar(0, 1, 'Penalty for product 3 and 4')
    product3_produced = solver.IntVar(0, 1, 'Binary indicates any of product 3 produced')
    product4_produced = solver.IntVar(0, 1, 'Binary indicates any of product 4 produced')

    # Each unit of product 2 that is produced over 100 units requires a production time of 3.0 man-hours instead of /
    # 2.0 man-hours
    product2_units_over_100 = solver.IntVar(0, solver.infinity(),
                                            'Number of units of product 2 produced over 100 units')

    # Create Objective - Maximize profit
    solver.Maximize(product_units[0] * profits[0] +
                    product_units[1] * profits[1] +
                    product2_units_over_100 * profits[1] +
                    product_units[2] * profits[2] +
                    product_units[3] * profits[3] +
                    product_units[4] * profits[4] +
                    product_units[5] * profits[5] +
                    product_units[6] * profits[6] -
                    product7_penalty * p7_penalty_cost)
    # solver.Maximize(sum([product_units * profit for investment, profit in
    #                      zip(product_units, profits)]) - product7_penalty*p7_penalty_cost + product2_units_over_100)

    # Constraints
    solver.Add(sum([product_unit * production_time
                    for product_unit, production_time in zip(product_units, production_times)])
               + 3 * product2_units_over_100
               <= man_hours_per_week - 75*product34_manhour_penalty)

    # If units for product 7 > 0, then penalty7 = 1
    solver.Add(product_units[6] <= (man_hours_per_week / production_times[6]) * product7_penalty) # Lowest big M possible

    # Second to last constraint
    solver.Add(product_units[1] <= 100)

    # If both product
    # 3 and product 4 are produced 75 man-hours are needed for production line set-up and hence the
    # (effective) number of man-hours available falls to 720 - 75 = 645.
    solver.Add(product_units[2] <= (man_hours_per_week / production_times[2]) * product3_produced)
    solver.Add(product_units[3] <= (man_hours_per_week / production_times[3]) * product4_produced)  # TODO: double-check
    # product34 pentalty is 1 (activated) if both product3 produced and product 4 produced :
    # p34penalty = p3produced*p4produced represented by two if/thens
    solver.Add(product34_manhour_penalty <= (product3_produced + product4_produced)/2)  # If penalty then both products produced (if 1,0 then 1 <= 1+1/2
    solver.Add(product34_manhour_penalty >= product3_produced + product4_produced-1)  # If both products produced then penalty

    # Solve
    status = solver.Solve()

    opt_soln = solver.Objective().Value()
    print('Number of variables =', solver.NumVariables())
    print('Number of constraints =', solver.NumConstraints())
    # The value of each variable in the solution.
    print('Solution:')
    for product_unit in product_units:
        print(product_unit.name() + ": ")
        print(product_unit.solution_value())

    # The objective value of the solution.
    print('\nOptimal profits given solution: $', opt_soln)

    print("___")
