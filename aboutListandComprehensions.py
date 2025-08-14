nums = [1,2,3,4,5]
for item in nums:
    print(item * 2)

# using list comprehensions:
double = [item * 2 for item in nums]
print(double)

square = [n*n for n in nums]
print(square)

evens = [n for n in nums if n % 2 == 0]
print(evens)

pairs = [(i, j) for i in range(2) for j in range(2)]
print(pairs)

# key methods sin list:
# append: adds one object as a single element
lst = [0,4,8,10]
lst.append(12)
lst.append([13,14])  #adds a single element
print(lst)

# extend: adds multiple elements
extend_list = [2,3,4]
extend_list.extend([5,6])
print(extend_list)

# pop method:
lst.pop()
print(lst)
lst.pop(1)
print(lst)

# slicing
a = [0,1,2,3,4,5]
print(a[1:4])
print(a[:3])
print(a[::2])
print(a[::-1])

b = a[:]  #shallow copy
print(b)
a[1:3] = [9,9]

