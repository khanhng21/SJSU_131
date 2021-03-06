"""
Calculate the value of the result based on the numbers and operator
Parameter: 
number1: int
First number
number2: int
Second number
Operator: str
- + * /
Result is the number after calculate with the operator
"""
def calculator(number1, number2, operator):
    if operator == '*':
        return number1 * number2
    elif operator == '+':
        return number1 + number2
    elif operator == '**':
        return float(number1 * number2)
    elif operator == '/':
        return number1 / number2
    elif operator == '-':
        return number1 - number2
    else:
        return 'invalid operator'

"""
Take the user input and print out the result
"""
def input_output():
    while True:
        try:
            number1 = float(input('Enter the first number: '))
            number2 = float(input('Enter the second number: '))
            operator = input('Enter the operation: ')
            print(calculator(number1, number2, operator))
            calc_again = input('Do you wish to exit? ')
            if calc_again == 'y':
                print(input_output())
            elif calc_again  == 'n':
                print('exit')
                quit()
            else:
                input_output('exit')
                quit()
        except ValueError:
            print('False')
input_output()
      