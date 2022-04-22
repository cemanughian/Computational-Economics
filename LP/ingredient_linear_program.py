# Manufacturer of animal feed
# 2 ingredients i1, i2
# A B C D nutrients, min 90 50 20 2
# How much of each ingredient do we put in to minimize our cost
#                              Cost per kg of ingredient
# Ingredient 1 | 100 80 40 10   40 // grams of each nutrient per kg of i1
# Ingredient 2 | 200 150 20 0   60
# Third filler has no effect on cost or nutrients
# Solve over weekend

# Oct 10 2019 CS 532 homework
from ortools.linear_solver import pywraplp

if __name__ == "__main__":
    # Define solver
    # The primary OR-Tools linear optimization solver is Glop, Google's linear programming system.
    solver = pywraplp.Solver("Minimum nutrients for food",
                             pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)  # Name and type of solver
    # Define variables that we want to solve for
    # lbd, ubd, name
    A = solver.NumVar(90, solver.infinity(), 'Number of grams of nutrient A in food')
    B = solver.NumVar(50, solver.infinity(), 'Number of grams of nutrient B in food')
    C = solver.NumVar(20, solver.infinity(), 'Number of grams of nutrient C in food')
    D = solver.NumVar(2, solver.infinity(), 'Number of grams of nutrient D in food')
    i1 = solver.NumVar(0, solver.infinity(), 'kg of ingredient 1')
    i2 = solver.NumVar(0, solver.infinity(), 'kg of ingredient 2')

    # Create Objective and constraints

    # objective = solver.Objective()
    # objective.SetCoefficient(c_b, -2)
    # objective.SetCoefficient(c_g, 5)
    # objective.SetMaximization()
    solver.Minimize(40*i1 + 60*i2)

    # Constraint 1: cb_cg >= 200
    # c1 = solver.Constraint(200, solver.infinity())  # Lower bd at least 200 calcs sold per day
    # c1.SetCoefficient(c_b, 1)
    # c1.SetCoefficient(c_g, 1)
    solver.Add(A*100 + B*80 + C*40 + D*10 == i1)
    solver.Add(A*200 + B*150 + C*20 + D*0 == i2)

    status = solver.Solve()

    # opt_soln = -2*c_b.solution_value() + 5*c_g.solution_value()
    opt_soln = solver.Objective().Value()
    print('Number of variables =', solver.NumVariables())
    print('Number of constraints =', solver.NumConstraints())
    # The value of each variable in the solution.
    print('Solution:')
    print('i1 = ', i1.solution_value())
    print('i2 = ', i2.solution_value())
    # The objective value of the solution.
    print('Optimal objective value (total cost):', opt_soln)

    print("done")






