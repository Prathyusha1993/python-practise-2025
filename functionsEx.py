# function is a reusable block of code that performs a specific task.

def function_name(parameters):
    """Doc String describing the function."""
    # function body
    # return value


def greet():
    print('Hello, World!')

greet()

# positional parameters ex
def add(a, b):
    return a+b

print(add(10, 20))

# default parameters
def greetings(name='Guest'):
    return f'Hello, {name}'

print(greetings())
print(greetings('Alice'))

# *args - variable length positional arguments
# collects extra positional arguments into a tuple
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1,2,3,4))

# **kwargs - variable length keyword arguments
# collects extra positional arguments into a dictionary
def person_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

print(person_info(name='Pinky', age=31, gender='female'))

def list_sum(lst):
    return sum(lst)

print(list_sum([1,2,3,4]))

# mixing parameters
# order should be - positional, -> default, -> *args -> **kwargs
def mixed_example(a, b=2, *args, **kwargs):
    print(a, b, args, kwargs)

print(mixed_example(1, 3, 4, 5, x=10, y=20))

# multiple return values
# fnctions acn return single value and multiple return values
# multiple return value as tuple
def get_stats(a,b):
    total = a+b
    product = a*b
    return total, product  #returns tuple

print(get_stats(10, 5))  #do it in either way
sum_val, prod_val = get_stats(10, 5)
print(sum_val, prod_val)
