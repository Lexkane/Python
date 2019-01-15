from functools import lru_cache
from functools import partial


def main():
    pass


@lru_cache(maxsize=None)
def fibonacci(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


for i in range(1, 100):
    print(fibonacci(i))


print_with_coma = partial(print, sep=',')
print_with_coma(1, 2, 3)
