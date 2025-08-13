# int (integer
x = 10
y = -5
z = 0
print(type(x))

# float(floating point number
pi = 3.14159
speed = 2.5e2
print(type(pi))
print(pi)

# str(string
name='Python'
greeting = 'Hello'
sentence = """This is 
a multiline string."""
print(type(name))
print(name)
print(sentence)

# bool(boolean)
is_active = True
is_admin = False
print(5 > 3)

# list (mutable sequence)
fruits = ['apple', 'banana', 'cherry']
print(fruits[1])
fruits.append('orange')
fruits[1]='blueberry'
print(fruits)

# tuple (immutable sequence)
coordinates = (10.0, 20.0)
colors = ('red', 'green', 'blue')
print(coordinates[0])
print(colors[1])
print(colors[0:2])
# print(colors[2] = 'blue') # This line will raise an error because tuples are immutable

# dict(dictionary)
person = {'name': 'Alice', 'age': 30}
person['city'] = 'California'
print(person)
print(type(person))

# set - unordered collection of unique elements
numbers = {1,2,3,3}
numbers.add(4)
print(numbers)

# mutable vs immutable
# Mutable types can be changed after creation
# Immutable types cannot be changed after creation
lst = [1,2]
lst.append(3)
print(lst)

# Immutable types cannot be changed, but a new object can be created
s = 'hi'
s = s + ' there'
print(s)

# type casting
# int to float
print(float(x))

# float to int
print(int(pi))

# int to str
print(str(123))

# operators
# Arithmetic operators - + - * / % // **
a = 10
b = 3
print(a +b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b) # Floor division means it returns the largest integer less than or equal to the division result
print(a ** b) # Exponentiation means raising a number to the power of another number

# Comparison operators - == != < > <= >=
x = 5
y = 10
print(x == y)
print(x != y)
print(x < y)
print(x > y)
print(x <= y)
print(x >= y)

# Logical operators - and or not
p = True
q = False
print(p and q)
print(p or q)
print(not q)

# membership - in not in
fruits=['apple', 'banana', 'cherry']
print('apple' in fruits)
print('mango' in fruits)
print('banana' not in fruits)

# identity - is is not
# is checks identity, not value equality
a=[1,2]
b=[1,2]
c=a
print(a is b)   #false - different objects, same content
print(c is a)
print(a is not b)

# Bitwise operators - & | ^ ~ << >>
m=5
n=3
print(m & n)
print(m | n)
print(m ^ n)
print(~m)
print(m << 1)  #left shift
print(m >> 1)   #right shift


