from Prac3_equation_solver import EquationSolver

equation_solver = EquationSolver()
equation = input("Please enter an equation to solve: ")

print("Input Infix Equation:", equation)

postfix = equation_solver._parseInfixToPostfix(equation)
postfix_expression = " ".join(str(token) for token in postfix.queue)
print("Converted Postfix Expression:", postfix_expression)

result = equation_solver.solves(equation)
print("Result:", result)
