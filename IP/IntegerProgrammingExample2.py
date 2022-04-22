# max y
# x,y
#
# -x + y <=1
# 3x +2y <= 12
# 2x + 3y <=12
# x, y >= 0
# x, y E Z

import pulp
lp = pulp.LpProblem("example 2 problem", pulp.LpMaximize)  # Defaults to minimize
x = pulp.LpVariable("x", 0, cat=pulp.LpInteger)
y = pulp.LpVariable("y", 0, cat=pulp.LpInteger)

# define objective
lp += y

# define constraints
lp += -x + y <=1
lp += 3*x +2*y <= 12
lp += 2*x + 3*y <=12

# solve the problem
lp.solve()

for v in lp.variables():
    print(v.name, "=", v.varValue)

print("Total profits = ", pulp.value(lp.objective))  # 61.6, 189.5, 973.25



