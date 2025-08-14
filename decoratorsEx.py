# A decorator is just a function that takes another function and adds extra behavior to it, without changing the originall function's code.
# think of it like gitft wrapping - the origin al item is inside but you've added something extra around it.
def greet():
    print('hello')

def my_decorator(func):
    def wrapper():
        print('Before function runs')
        func()
        print('After function runs')
    return wrapper

decorated_greet = my_decorator(greet)
decorated_greet()

# same example using decorator
def my_decorator(func):
    def wrapper():
        print('Before function runs')
        func()
        print('After function runs')
    return wrapper

@my_decorator
def greet():
    print('Hello!')

greet()


# decorators with arguments:
def my_decor(func):
    def wrapper(*args, **kwargs):
        print('Before function runs')
        result = func(*args, **kwargs)
        print('after function runs')
        return result
    return wrapper

@my_decor
def add(a, b):
    print(a+b)
    return a+b

add(3,4)

# practical exxample:
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end=time.time()
        print(f'{func.__name__} took {end - start:.4f} seconds')
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    print('Done')

slow_function()