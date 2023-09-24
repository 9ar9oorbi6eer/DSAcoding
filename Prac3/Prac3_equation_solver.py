from Prac3_queues import DSA_queue
from Prac6.stack import DSA_stack
from Prac3_circular_queue import CircularDSA_queue

class EquationSolver(DSA_stack, CircularDSA_queue, DSA_queue):
    def solve(self, equation):
        postfix = self._parseInfixToPostfix(equation)
        
        result = self._evaluatePostfix(postfix)
        return result

    def _parseInfixToPostfix(self, equation):
        postfix = CircularDSA_queue(len(equation))
        opStack = DSA_stack()

        operators = {'+': 1, '-': 1, '*': 2, '/': 2}

        def precedenceOf(op):
            return operators[op]

        def executeOperation(op, op1, op2):
            if op == '+':
                return op1 + op2
            elif op == '-':
                return op1 - op2
            elif op == '*':
                return op1 * op2
            elif op == '/':
                return op1 / op2

        def isOperator(token):
            return token in operators

        tokens = equation.split()  # Split the equation into tokens

        for term in tokens:
            if term == '(':
                opStack.setpush('(')
            elif term == ')':
                while opStack.top() != '(':
                    postfix.enqueue(opStack.setpop())
                opStack.setpop()
            elif isOperator(term):
                while not opStack.isEmpty() and opStack.top() != '(' and precedenceOf(opStack.top()) >= precedenceOf(term):
                    postfix.enqueue(opStack.setpop())
                opStack.setpush(term)
            else:
                postfix.enqueue(float(term))  # Convert valid numbers to float

        while not opStack.isEmpty():
            postfix.enqueue(opStack.setpop())

        return postfix


    def _evaluatePostfix(self, postfix):
        operandStack = DSA_stack()

        while not postfix.isEmpty():
            token = postfix.dequeue()
            if isinstance(token, float):
                operandStack.setpush(token)
            else:
                op2 = operandStack.setpop()
                op1 = operandStack.setpop()
                result = self._executeOperation(token, op1, op2)
                operandStack.setpush(result)

        return operandStack.top()

    def _executeOperation(self, op, op1, op2):
        if op == '+':
            return op1 + op2
        elif op == '-':
            return op1 - op2
        elif op == '*':
            return op1 * op2
        elif op == '/':
            return op1 / op2

