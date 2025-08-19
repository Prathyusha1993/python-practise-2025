# module is a python file which caontians classes, functions, variables where we can reuse in another python file.
# import module:
import math
print(math.sqrt(16))

# from module import name:
from math import sqrt
print(sqrt(25))

# import with alias
import math as m
print(m.pi)

# import multiple names:
from math import sqrt, pi, ceil
print(sqrt(49), ceil(43.2), pi)

# import all names: (not recommended)
from math import *
print(floor(4.7))