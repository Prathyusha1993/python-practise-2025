# sets: unordered, unique elements, mutable. baked by hash tables.
# sets are unordered no indexing/slicing
s = {1,2,3,4,3,4}
print(s)  #removes duplicates
s.add(5)
print(s)
s.discard(1)
print(s)

# set algebra:
A= {1,2,3}
B = {3,4}
print(A | B)   #union
print(A & B)   #intersection
print(A - B)   #difference
print(A ^ B)    #symmetric difference

# set comprehension:
words = {'a', 'b','v', 'd', 'a', 'c', 'd'}
unique = {w for w in words}
print(unique)
