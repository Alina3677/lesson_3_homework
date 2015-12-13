import re

from calc import Calculator


calculator = Calculator()

while True:
    print("Menu1:\n"
          "1. Simple operation\n"
          "2. Evaluate\n"
          "0. Exit\n")
    option = input("Enter the number of the menu item:")

    if option == '1':
        operation = input("Which operation you want to perform? (+,-,*,/): ")
        if operation in ('+', '-', '*', '/'):
            x = float(input("x="))
            y = float(input("y="))
            if operation == '+':
                result = calculator.add(x, y)
            elif operation == '-':
                result = calculator.subtract(x, y)
            elif operation == '*':
                result = calculator.multiply(x, y)
            elif operation == '/':
                 result = calculator.divide(x, y)
        else:
            print('Error! This operation can not be performed!')
            continue
        print("Result: %.2f" % result)

    elif option == '2':
        expression = input("Enter the expression: ")
        comparison = re.compile('[^\(\)\d\*\+/-]+')
        if comparison.search(expression) is None:
            try:
                print('Result:', calculator.evaluate(expression))
            except IndexError:
                print('Error! You have not entered a mathematical expression , or one of the brackets is empty!')
            except SyntaxError:
                print('Error! Unclosed parentheses !')
            except ZeroDivisionError:
                print('Error! Divide by zero!')

    elif option == '0':
        break
    else:
        print('Error! This menu item does not exist!')
