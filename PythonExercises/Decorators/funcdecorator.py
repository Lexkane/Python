def main():
    pass

def decorator (fn):
    def decorated_fn(*args,**kwargs):
        print('Starting decorated function')
        fn(*args,**kwargs)
        print('End of the decorated function')
    return decorated_fn

def make_decorator(string):
    def decorator(fn):
        def decorated_fn(*args,**kwargs):
            print(string)
            fn(*args,**kwargs)
        return decorated_fn
    return decorator

 
@decorator
def print_hello():
    print('Hello')

print_hello=decorator(print_hello)



