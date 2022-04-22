"""
CS 532 Assignment 5
Due Oct 29, 2019
Celeste Manughian-Peter
No. 2 - Oil Blend
"""
from ortools.linear_solver import pywraplp

if __name__ == "__main__":

    # Data
    names = ["VEG1", "VEG2", "OIL1", "OIL2", "OIL3"]
    prices = [115, 128, 132, 109, 114]
    hardnesses = [8.8, 6.2, 1.9, 4.3, 5.1]
    final_selling_price_per_tonne = 180

    # Define solver
    solver = pywraplp.Solver("Maximize profits given cooking oil blends",
                             # pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
                             pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

    # Define variables that we want to solve for
    oils = [solver.IntVar(0, solver.infinity(), 'Amount of ' + str(oil) + " to blend, in tonnes") for oil in names]
    oils_used = [solver.IntVar(0, 1, 'Used ' + str(oil) + " in blend") for oil in names]

    # Create Objective - Maximize profit by minimizing the cost of oils
    #solver.Minimize(sum([oil_amt * oil_price for oil_amt, oil_price in zip(oils, prices)]))
    revenue = final_selling_price_per_tonne*sum([oil_amt for oil_amt in oils])
    cost = sum([oil_amt * oil_price for oil_amt, oil_price in zip(oils, prices)])
    solver.Maximize(revenue - cost)

    # Constraints
    for oil_used, oil in zip(oils_used, oils):
    # for oil in oils:
        # Activate oil used if oil is greater than 0 # This is actually big M
        if 'VEG' in oil.name():
            solver.Add(oil <= 210*oil_used)
        else:
            solver.Add(oil <= 260*oil_used)
        # solver.Add(oil_used >= oil)
        # solver.Add(oil +1 >= oil_used)
        # solver.Add(sum([oil/oil for oil in oils]) <= 3)  # Used or not used  is oil/oil => 1 or 0 if used or not... cant do this, nonlinear

        # If an oil is used, at least 30 tonnes must be used
        solver.Add(oil >= 30*oil_used)
        # solver.Add(30 <= oil)
        # solver.Add(oil <= 0)

    # Make sure we dont use more than 3 oils
    solver.Add(sum([o for o in oils_used]) <= 3)
    # Make sure we dont make more than this amount per oil type
    solver.Add(sum([oil for oil in oils if 'OIL' in oil.name()]) <= 260)
    solver.Add(sum([oil for oil in oils if 'VEG' in oil.name()]) <= 210)

    # solver.Add(oils[0] <= oils[3])  # if either veg1 or veg2 are used then oil2 must also be used
    # solver.Add(oils[1] <= oils[3])  # if either veg1 or veg2 are used then oil2 must also be used
    solver.Add(oils_used[0] <= oils_used[3])  # if either veg1 or veg2 are used then oil2 must also be used
    solver.Add(oils_used[1] <= oils_used[3])  # if either veg1 or veg2 are used then oil2 must also be used

    # Not sure - hardness constraint
    # Percentage of hardness contributed is proportional to percentage of oil in mixture 
    solver.Add(sum([(hardness*oil) for oil, hardness in zip(oils, hardnesses)]) <= 6.2*sum([oil for oil in oils]))
    solver.Add(sum([hardness*oil for oil, hardness in zip(oils, hardnesses)]) >= 3.5*sum([oil for oil in oils]))

    # Solve
    status = solver.Solve()

    # Results
    opt_soln = solver.Objective().Value()  # 409
    print('Number of variables =', solver.NumVariables())
    print('Number of constraints =', solver.NumConstraints())
    # The value of each variable in the solution.
    print('Solution:')
    for oil in oils:
        print('Amount of oil', oil.name())
        print(oil.solution_value())

    # The objective value of the solution.
    print('Optimal objective value:', opt_soln)

    print("___")
