# args, kwargs ex
def demo(*args, **kwargs):
    print('args:', args)
    print('kwargs:', kwargs)

demo(1,2,3, name='ALice', age=31)

# enumerate() and zip():
# enumerate adds an index counter to an iterable
names = ['ALice', 'Bob', 'Charlie', 'David', 'Ester']
for idx, name in enumerate(names):
    print(idx, name)

# zip() - combines two or more iterables into pairs:
names = ['ALice', 'Bob', 'charlie', 'david']
scores = [85, 73, 64, 91]

for name, score in zip(names, scores):
    print(name, score)

# map(),filter(),reduce()
# map(): applies function to all items
# filter(): keep only items where func returns true
#reduce(): applies rolling computation

from functools import reduce

nums = [1,2,3,4,5,6]
squares = list(map(lambda x: x*x, nums))
even = list(filter(lambda x: x % 2 == 0, nums))
total = reduce(lambda x, y: x+y, nums)

print(squares)
print(even)
print(total)

# any()a dn all()
# any(iterable) = returns true if at least one element is true
# all(iterable) - return true if all elements are true
nums = [0, 1,2, 3,4]
print(any(nums))  # True (since 1,2,3 are truthy)
print(all(nums))  # False (0 is falsy)

# is - checks identtiy same object in memory
# == -> checks for same values
a = [1,2,3]
b = [1,2,3]
print(a ==b)
print(a is  b)
c=a
print(a is c)

# mutable default arguments pitfall
# bad example:
def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list

print(add_item(1))
print(add_item(2))  #bug samelist is reused

# fix:
def add_item(item, my_list=None):
    if my_list is None:
        my_list =[]
    my_list.append(item)
    return my_list

print(add_item(1))
print(add_item(2))

# why __name__ == '__main__':
# In Python, every file (module) has a built-in variable called __name__.
# When you run a file directly, Python sets __name__ = "__main__".
# When you import a file as a module, Python sets __name__ to the module’s name (the filename, without .py).

# Why Do We Use It?
# Code reusability
# You can write functions/classes in a file.
# If you import that file into another program, you don’t want the script’s test code to run automatically.
# Using if __name__ == "__main__": prevents unwanted execution.
# Testing / Entry Point
# It’s often used to keep test code or the main logic of the program separate from definitions (functions, classes).
# This makes your file usable both as:
# A standalone script
# A reusable module

# ex;
# file: myModule.py
print('THis will always run')  #this prints always even though we wanted to use function
def greet(name):
    print(f'Hello, {name}')

# /file: main.py
import myModule
myModule.greet('ALice')

# same example with __name__ :
# file: mymodule.py
def greet(name):
    print(f'Hello {name}')

if __name__ == '__main__':
    print('running as a standalone script')
    greet('bob')

# file: mian.py
import myModule
myModule.greet('ALice')

# In Python, every module has a special variable name.
# If the module is being run directly, nameis set to"main".
# We use if name == "main": to ensure certain code runs only when the file is
# executed directly, not when imported. This is useful for separating reusable code (functions, classes) from test scripts or entry points.
