# dictionaries are key value mapping, insertion ordered

person = {'name': 'Alice', 'age': 30}
person['city'] = 'California'
person.get('role')
person.get('role', 'User')
print(person.get('age'))#default if missing
del person['age']
print(person)
person['gender'] = 'Male'
person['contact'] = '987654321'
print(person)


# iterating
for k in person: print(k, person[k])
for k, v in person.items(): print(k,v)
for v in person.values(): print(v)

# merging:
a = {'x': 1}
b = {'y':2, 'x':9}
print(a | b)   #b wins on conflicts

# dictionary comprehension:
squares = {n:n*n for n in range(5)}
print(squares)

double = {n*2 for n in range(6)}
print(double)

names_list = ['alice', 'bob', 'carol','david']
name_map = {name: name.title() for name in names_list}
print(name_map)

# invert a dict only if values are unique and hashable
d = {'a':1, 'b':2}
inv = {v: k for k, v in d.items()}
print(inv)