# python uses a private heap space for memory managment. developer don't directly maange memory unlike  c/c++.
# pyhton handles it using reference counting and garbage collection.

# reference counting is a technique where each object keeps track of how many references point to it.
# when the reference count drops to zero, the object is deallocated.
# ex of reference counting:

import sys
a = [1,2,3]
b = a
print(sys.getrefcount(a))    # reference count is > 2 (a, b, and the argument to getrefcount)

del b
print(sys.getrefcount(a))


# garbage collection hhandles objects invloved in reference cycles
# Reference counting fails if two objects reference each other.
# uses generational garbage collection which divides objects into generations based on their lifespan.
    #Gen 0: Young objects (allocated recently)
    #Gen 1: Objects that survived one collection
    #GEn 2: older objects (survived multiple collections)

# ex of garbage collection:
import gc

class Node:
    def __init__(self):
        self.ref = None

a = Node()
b = Node()
a.ref = b
b.ref = a

del a
del b
print('garbage collection:', gc.collect())  # this will collect the circular reference

# Both a and b reference each other → their reference count never becomes 0.
# Without garbage collection, this would cause a memory leak.


# Garbage Collector (GC)
# Python has a garbage collector to handle these circular references.
# It uses an algorithm called “Generational Garbage Collection”:
# Objects are grouped into generations (young → old).
# New objects go into young generation.
# If objects survive multiple GC cycles, they get promoted to older generations.
# The idea is: most objects die young, so Python cleans younger ones more frequently.
#
# ✅ Example: Forcing Garbage Collection
import gc

print("Garbage collection enabled:", gc.isenabled())

gc.collect()   # manually run garbage collection
print("Garbage collection complete.")

# Why do we need Garbage Collection?
# Without GC: memory leaks happen (unused objects stay in memory).
# With GC: Python automatically detects and clears circular references.