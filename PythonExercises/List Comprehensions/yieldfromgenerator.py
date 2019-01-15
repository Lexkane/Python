def main():
    pass


def subgenerator():
    yield '[subgenerator] hello'
    yield '[subgenerator] world'


def generator():

    yield '[generator] start'
    yield from range(10)
    yield from (x**3 for x in range(5))
    yield from subgenerator()
    yield '[generator] hello'


for value in generator():
    print(value)
