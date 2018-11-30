import sys;

def main():
    pass

x=int(sys.argv[1])


def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

if x==0 :print ("0")
else :print (list(fib(x))[-1])     