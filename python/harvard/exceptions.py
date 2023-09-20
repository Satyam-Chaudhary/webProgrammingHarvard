import sys 

try:
    x = int(input('x: '))
    y = int(input('y: '))
except ValueError:
    print("Can't take string")
    sys.exit(1)


try:
    result = x / y
    print(f'result is {result}')
except ZeroDivisionError:
    print('Cannot divide by zero')
    sys.exit(1)
