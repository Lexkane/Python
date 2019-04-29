import functools
def main():
 pass

@functools.lru_cache(None)
def fib(n):
    if (list(a))[1::]%2==0:
        if n < 2:
            return n
        return fib(n-1) + fib(n-2)
    else:pass    


 


a=int(input('Input number'))
print((fib(a)))
