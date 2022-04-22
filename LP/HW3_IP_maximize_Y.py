# Oct 22 2019 CS 532 homework
from ortools.linear_solver import pywraplp

if __name__ == "__main__":
    # Define solver
    # The primary OR-Tools linear optimization solver is Glop, Google's linear programming system.
    solver = pywraplp.Solver("Maximize y given constraints",
                             pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)  # Name and type of solver
    # Define variables that we want to solve for
    # lbd, ubd, name
    x = solver.IntVar(0, solver.infinity(), 'X') # Use IntVar for integer programming
    y = solver.IntVar(0, solver.infinity(), 'Y')

    # Create Objective and constraints
    solver.Maximize(y)

    # Constraints
    solver.Add(-x + y <= 1)
    solver.Add(3*x + 2*y <= 12)
    solver.Add(2*x + 3*y <= 12)

    status = solver.Solve()

    opt_soln = solver.Objective().Value()
    print('Number of variables =', solver.NumVariables())
    print('Number of constraints =', solver.NumConstraints())
    # The value of each variable in the solution.
    print('Solution:')
    print('x (# BB guns) = ', x.solution_value())
    print('y (# toy cars)= ', y.solution_value())
    # The objective value of the solution.
    print('Optimal objective value (total cost):', opt_soln)

    print("done")






