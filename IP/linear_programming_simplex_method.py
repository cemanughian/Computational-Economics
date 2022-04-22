# Oct 10 2019 CS 532 class work
# Install OR-tools, python3 -m pip install ortools
# https://acrogenesis.com/or-tools/documentation/user_manual/index.html
# Sample code https://developers.google.com/optimization/lp/glop
# Let's program the problem from class in python

from ortools.linear_solver import pywraplp

# Define solver
# The primary OR-Tools linear optimization solver is Glop, Google's linear programming system.
solver = pywraplp.Solver("Studying LP Solver",
                         pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)  # Name and type of solver
# Define variables that we want to solve for
# lbd, ubd, name
h1 = solver.NumVar(0, solver.infinity(), 'hours studying for exam 1')
h2 = solver.NumVar(0, solver.infinity(), 'hours studying for exam 2')

# Create Objective and constraints

objective = solver.Objective()
objective.SetCoefficient(h1, .4)
objective.SetCoefficient(h2, .5)
objective.SetMaximization()

# Constraint 1: h1 + h2 <= 14.
c1 = solver.Constraint(-solver.infinity(), 12)  # Upper bound of 12, no lower bd
c1.SetCoefficient(h1, 1)
c1.SetCoefficient(h2, 1)
# Constraint 2: 0.4h1 < 4
c2 = solver.Constraint(-solver.infinity(), 4)  # Upper bound of 4, no lower bd
c2.SetCoefficient(h1, .4)
# Constraint 3: .5h2 < 4
c3 = solver.Constraint(-solver.infinity(), 4)  # Upper bound of 4, no lower bd
c3.SetCoefficient(h2, .5)

solver.Solve()

opt_soln = .4*h1.solution_value() + .5*h2.solution_value()
print('Number of variables =', solver.NumVariables())
print('Number of constraints =', solver.NumConstraints())
# The value of each variable in the solution.
print('Solution:')
print('h1 = ', h1.solution_value())
print('h2 = ', h2.solution_value())
# The objective value of the solution.
print('Optimal objective value =', opt_soln)

print("done")