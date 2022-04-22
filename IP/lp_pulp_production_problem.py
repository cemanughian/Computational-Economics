import pulp
lp = pulp.LpProblem("production problem", pulp.LpMaximize) # Defaults to minimize
x = pulp.LpVariable("BB guns", 0, cat=pulp.LpInteger)
y = pulp.LpVariable("toy cars", 0, cat=pulp.LpInteger)

# define objective
lp += 3.5*x + 4*y

# define constraints
lp += 5.5*x + 6.5*y <= 1570
lp += x + y <= 251

# solve the problem
lp.solve()

for v in lp.variables():
    print(v.name, "=", v.varValue)

print("Total profits = ", pulp.value(lp.objective))  # 62, 189, 973  IP / 61.6, 189.5, 973.25 LP


