from operator import neg, mul
from functools import reduce


def main():
    pass


values = [5, 2, 1, 3, 8, -3]

print(list(map(neg, values)))

print(list(map(lambda x: -x, values)))

values = [4, -1, 2, 5, 3, -3]
product = reduce(mul, values)
print(product)
