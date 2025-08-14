# varibale scopes: LEGB rule - python looks variables in this order
# local (inside current function)
# enclosing (in outer functions)
# global (at module level)
# built-in (python reserved name)

# local  scope:
def my_func():
    x=10
    print(x)

my_func()
# print(x)  #error x is not defined

# global scope:
x=5
def globally():
    print(x)

globally()

# modifying global variables:
count = 0
def increment():
    global count
    count += 1

increment()
print(count)

# nonlocal keyword
# used to modify variables in the enclosing function's scope
def outer():
    x = 'outer'
    def inner():
        nonlocal x
        x='inner'
    inner()
    print(x)

outer()

# recursion basics: a function calling itself until a base condition is met
# recursion uses the call stac,a nd without a base case it causes recursion error
def factorial(n):
    if n==0:  #base case
        return 1
    return n*factorial(n-1)

print(factorial(5))

# lambda function - anonymous(unnamed) functions defined using lambda
# syntax: lambda arguments: expression
square = lambda x: x ** 2
print(square(5))

nums = [1,2,3,4,5]
print(list(map(lambda x: x * 2, nums)))

# practice challange:
import operator
def calculate(a, b, op, *args, **kwargs):
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }
    if op not in operations:
        raise ValueError(f'invalid operator: {op}.')

    result = operations[op](a,b)

    for num in args:
        result = operations[op](result, num)

    if kwargs.get('round_result', False):
        result = round(result, 2)

    return result

print(calculate(10, 5, '+', 2,4,6, round_result=True))

# fibonnaic iterative
def fib_iterative(n):
    if n <= 1:
        return n
    a, b=0, 1
    for _ in range(2, n+1):
        a, b=b, a+b
    return b

print(fib_iterative(5))

def fib_recursive(n):
    if n <= 1:
        return n

    return fib_recursive(n-1) + fib_recursive(n-2)

print(fib_iterative(15))