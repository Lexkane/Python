import random
import time


def sleep(seconds):
    start = time.time()
    while time.time()-start < seconds:
        yield


def produce():
    yield from sleep(0.5)
    data = random.randint(1, 100)
    return data


def consume():
    sum_ = 0
    count = 0

    while True:
        data = yield from produce()
        print('Got data', data)

        sum_ += data
        count += 1
        print('Sum', sum_)
        print('Average:', sum_/count)


def another_task():
    while True:
        print()
        print('                 Hello from Another Task')
        print()
        yield from sleep(1)


def main():
    consumer = consume()
    task = another_task()

    while True:
        #print('next iteration')
        next(consumer)
        next(task)


if __name__ == "__main__":
    main()
