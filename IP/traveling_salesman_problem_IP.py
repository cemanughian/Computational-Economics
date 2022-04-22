# Given a list of cities, and locations, what is the shortest possible route to
# visit each city and return to new york, city of origin
# Minimize distance
# Variables - distance between each pair of points
# Matrix of all paths , directional or directionless

# Most intuitive - directional edges
# Objective - minimize di,j (start, end city)   zum(i=1, n) sum(j=1,n) c_ij*d_ij where c is the cost of traveling between
# Constraints
# # Every city only once (no going back and no missing) - arrived at once and departed at once - i and j
# Arrival constraint : (sum(i=1, n) of d_ij )= 1 for all J
# Departure constraint : (sum(j=1, n) of d_ij )= 1 for all I
# Only these constraints allows for separate enclosed paths. To fix this, add additional vars per each city
# u_i - u_j + n*d_ij <= n-1; 2<= i != j <= n # Makes sure the paths continue and not loop in on themselves

