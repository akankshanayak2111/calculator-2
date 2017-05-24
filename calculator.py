from arithmetic import *

while True:
    user_input = raw_input('Enter the math operator: \n(add, sub, mul, div, square, cube, pow or mod)\nor "q" to quit, and the numbers: \n')
    calculator = user_input.split(" ")
    operator = calculator[0]
    

    
    if operator == 'q':
        break

    elif operator == 'square':
        num1 = int(calculator[1])
        print square(num1)
    elif operator == 'cube':
        num1 = int(calculator[1])
        print cube(num1)

    else:
        num1 = int(calculator[1])
        num2 = int(calculator[2])

        if operator == 'add':
            print add(num1, num2)
        elif operator == 'sub':
            print subtract(num1, num2)
        elif operator == 'mul':
            print multiply(num1, num2)
        elif operator == 'div':
            num1 = float(calculator[1])
            num2 = float(calculator[2])
            print divide(num1,num2)

        elif operator == 'pow':
            print power(num1,num2)
        elif operator == 'mod':
            print mod(num1,num2)


