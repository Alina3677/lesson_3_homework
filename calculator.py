class Calculator:
    def __init__(self):
        self.base_numeral_system = 10

    def add(self, x, y):
        """This function adds two numbers"""
        try:
            return float(x)+float(y)
        except ValueError:
            raise

    def subtract(self, x, y):
        """This function subtracts two numbers"""

        try:
            return float(x)-float(y)
        except ValueError:
            raise

    def multiply(self, x, y):
        """This function multiplies two numbers"""

        try:
            return float(x)*float(y)
        except ValueError:
            raise

    def divide(self, x, y):
        """This function divides two numbers"""
        if y == 0:
            raise ValueError('Error! Division by zero is impossible!')
        try:
            return float(x)/float(y)
        except ValueError:
            raise


    def evaluate(self, expression):
        """This function evaluate expression"""

        return eval(expression)

