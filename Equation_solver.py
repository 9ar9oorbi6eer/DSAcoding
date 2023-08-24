from Prac3_equation_solver import EquationSolver

equation_solver = EquationSolver()
equation = input("Please enter an equation to solve: ")
result = equation_solver.solve(equation)
print(result)