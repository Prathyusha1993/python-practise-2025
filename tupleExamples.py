# tuple: ordered, immutable and aloows duplicates. Hasbale if all elements are hashable -> can be dict keys/set elements

pt = (10.5, 20.2)
record = ('Alice', 30)

def stats(a,b):
    return a+b, a*b

sum, prod = stats(3,4)
print(sum, prod)

a,b = (1,2)
print(a,b)
first, *mid, last = (1,2,3,4,5,6)
print(first, mid, last)