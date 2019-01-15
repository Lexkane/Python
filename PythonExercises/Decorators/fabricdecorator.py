def main():
    pass

def make_decorator(string):
    def decorator(fn):
        def decorated_fn(*args,**kwargs):
            print(string)
            fn(*args,**kwargs)
        return decorated_fn
    return decorator

@make_decorator('Before invokation')
@make_decorator('Another decorator')
def print_hello():
    print('Hello')

print_hello()