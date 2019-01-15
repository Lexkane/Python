from itertools import product, chain
from itertools import permutations, combinations, combinations_with_replacement
from itertools import takewhile, dropwhile


def main():
    pass


for i, j in product(range(1, 5), range(1, 5)):
    print('{}x{}={}'.format(i, j, i*j))


print('-------')

for i in chain(range(1, 5), range(1, 5)):
    print(i)

string = 'ABC'
elements = 2


print('-------')
print(list(permutations(string, elements)))
print(list(combinations(string, elements)))
print(list(combinations_with_replacement(string, elements)))


values = [1, 4, 3, 5, 2, 2, 8]


def predicate(x): return x < 5


print('-------')
for elem in takewhile(predicate, values):
    print(elem)

print('-------')
for elem in dropwhile(predicate, values):
    print(elem)
