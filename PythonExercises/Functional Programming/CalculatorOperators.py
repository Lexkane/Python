from operator import add, sub, mul, truediv, pow


def main():
    pass


operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
    '^': pow
}

try:
    first = float(input('First number:'))
    operation = input('Operation:')
    second = float(input('Second number:'))
    result = operations[operation](first, second)
except ValueError:
    print('Incorect input')
except KeyError:
    print('Unsupported operation')
except ZeroDivisionError:
    print('Division by zero')
else:
    print('Result', result)
