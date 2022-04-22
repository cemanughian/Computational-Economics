# Oct 10 2019 CS 532 class work
# Install OR-tools, python3 -m pip install ortools
# https://acrogenesis.com/or-tools/documentation/user_manual/index.html
# Sample code https://developers.google.com/optimization/lp/glop
# Let's program the calculator problem from Oct 8 class in python

from ortools.linear_solver import pywraplp


if __name__ == "__main__":
    # Define solver
    # The primary OR-Tools linear optimization solver is Glop, Google's linear programming system.
    solver = pywraplp.Solver("Optimal Calculator Sales",
                             pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)  # Name and type of solver
    # Define variables that we want to solve for
    # lbd, ubd, name
    c_b = solver.NumVar(100, 200, 'Number of basic calculators shipped per day')
    c_g = solver.NumVar(80, 170, 'Number of graphing caclulators shipped per day')

    # Create Objective and constraints

    # objective = solver.Objective()
    # objective.SetCoefficient(c_b, -2)
    # objective.SetCoefficient(c_g, 5)
    # objective.SetMaximization()
    solver.Maximize(-2*c_b + 5*c_g)

    # Constraint 1: cb_cg >= 200
    # c1 = solver.Constraint(200, solver.infinity())  # Lower bd at least 200 calcs sold per day
    # c1.SetCoefficient(c_b, 1)
    # c1.SetCoefficient(c_g, 1)
    solver.Add(c_b + c_g >= 200)

    status = solver.Solve()

    # opt_soln = -2*c_b.solution_value() + 5*c_g.solution_value()
    opt_soln = solver.Objective().Value()
    print('Number of variables =', solver.NumVariables())
    print('Number of constraints =', solver.NumConstraints())
    # The value of each variable in the solution.
    print('Solution:')
    print('c_b = ', c_b.solution_value())
    print('c_g = ', c_g.solution_value())
    # The objective value of the solution.
    print('Optimal objective value =', opt_soln)

    print("done")






