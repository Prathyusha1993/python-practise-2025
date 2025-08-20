# Shallow Copy: creates a new object but elements inside still point to the original refreneces
# works fine for immutable objects like strings, tuples, and numbers, but nested mutable objects like lists or dictionaries can lead to unexpected behavior.

# ex:
import copy

list1 = [[1,2], [3,4]]
shallow_copy = copy.copy(list1)

shallow_copy[0][0] = 99
print('Original', list1)
print('shallow copy', shallow_copy)     # both got modified becuase the inner lists were not copied deeply.

# deep copy: creates anew object and recursively copies all nestedobjects
# completely independent

# ex:
import copy

list2 = [[1,2], [3,4]]
deep_copy = copy.deepcopy(list2)

deep_copy[0][0] = 99
print('original', list2)
print('deep copy', deep_copy)