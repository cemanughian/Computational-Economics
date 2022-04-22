"""
CS 532 Assignment 5
Due Oct 29, 2019
Celeste Manughian-Peter
No. 1 - Investment Profile
"""
from ortools.linear_solver import pywraplp

if __name__ == "__main__":
    # Project mgr at an investment bank company that is considering 10 investments
    # Each investment has some expected profit and a cost or capital requirement
    Q = 123  # Million
    P = [52, 81, 57, 57, 93, 97, 72, 53, 14, 78]  # long run profit of each investment
    C = [16, 47, 49, 22, 25, 17, 26, 24, 9, 10]  # capital required for each investment

    # Define solver
    solver = pywraplp.Solver("Maximize profits given investment constraints",
                             pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)  # Name and type of solver

    # Define variables that we want to solve for
    investments = [solver.IntVar(0, 1, 'Yes or no on investment ' + str(i)) for i in range(10)]  # 1467810, 409

    # Create Objective - Maximize profit
    solver.Maximize(sum([investment * profit for investment, profit in zip(investments, P)]))

    # Constraints
    solver.Add(sum([investment * capital for investment, capital in zip(investments, C)]) <= Q)
    solver.Add(investments[2] + investments[3] <= 1)  # Investment opportunity 3 and 4 are mutually exclusive
    solver.Add(investments[4] + investments[5] <= 1)  # Investment opportunity 5 and 6 are mutually exclusive
    solver.Add(investments[4] + investments[5] <= investments[2] + investments[
        3])  # Neither 5 or 6 can be undertaken unless 3 or 4 is undertaken
    # At least two and at most four investments from the set 1,2,3,7,8,9,10 have to be undertaken
    l = [1, 2, 3, 7, 8, 9, 10]
    solver.Add(sum([investments[i - 1] for i in l]) <= 4)
    solver.Add(sum([investments[i - 1] for i in l]) >= 2)

    # Solve
    status = solver.Solve()

    opt_soln = solver.Objective().Value()  # 409
    print('Number of variables =', solver.NumVariables())
    print('Number of constraints =', solver.NumConstraints())
    # The value of each variable in the solution.
    print('Solution:')
    for i in range(len(investments)):
        if investments[i].solution_value() == 1:
            print('Invested in investment opportunity ', i)

    # The objective value of the solution.
    print('Optimal objective value (total profit) with specified investments:', opt_soln)

    print("___")
