def main():
    pass


def generator_function():
    for x in range(5):
        for y in range(3):
            if (x+y) % 2 == 0:
                yield x*y


generator = generator_function()
for value in generator:
    print(value)

generator2 = (x*y for x in range(1, 5) for y in range(3) if (x+y) % 2 == 0)
for value2 in generator2:
    print(value2)

print(sum(x**2 for x in range(10)))
