from arithmetic1 import *

while True:
    prompt = '''Enter the math operator:
    (add, sub, mul, div, square, cube, pow or mod)
    or "q" to quit, and the numbers:
    '''
    user_input = raw_input(prompt)

    calculator = user_input.split(" ")
    operator = calculator[0]
    numbers = calculator[1:]
    numbers = [int(i) for i in numbers]

    if operator == 'q':
        break

    # if ' ' in user_input == False:
    #     print "Entry is not in a valid format, please try again"
    #     break

    num1 = int(calculator[1])
    if len(calculator) == 2:
        if operator == 'square':
            print square(num1)
        elif operator == 'cube':
            print cube(num1)
    else:
        num2 = int(calculator[2])
        if operator == 'add':
            print add(numbers)
        elif operator == 'sub':
            print subtract(num1, num2)
        elif operator == 'mul':
            print multiply(numbers)
        elif operator == 'div':
            num1 = float(calculator[1])
            num2 = float(calculator[2])
            print divide(num1, num2)
        elif operator == 'pow':
            print power(num1, num2)
        elif operator == 'mod':
            print mod(num1, num2)
