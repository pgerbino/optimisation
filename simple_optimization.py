from scipy.optimize import linprog

# Coefficients of the objective function
c = [1, 1]  # Minimize x + y

# Coefficients of the inequality constraints
A = [[-1, -2],  # -x - 2y <= -4
     [-4, -1]]  # -4x - y <= -8

# Constants on the right-hand side of the inequality constraints
b = [-4, -8]

# Bounds for x and y (x >= 0, y >= 0)
x_bounds = (0, None)
y_bounds = (0, None)

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Print the results
if result.success:
    print(f"Optimal value: {result.fun}")
    print(f"Optimal point: x = {result.x[0]}, y = {result.x[1]}")
else:
    print("Optimization failed:", result.message)

