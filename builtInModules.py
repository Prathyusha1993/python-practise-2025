# os - Opertaing system
import math
import os
import random

print(os.getcwd())   # Get current working directory
os.mkdir('test_folder')     #create a new directory
print(os.listdir('.'))   # List files in current directory
os.rename('test_folder', 'renamed_folder')   # Rename directory
os.rmdir('renamed_folder')   # Remove directory


# sys - System-specific parameters and functions
import sys
print(sys.version)
# print(sys.path)   # List of directories Python searches for modules

# datetime - Date and time manipulation
from datetime import datetime
now = datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))

# math -Mathematical functions
import math
print(math.factorial(5))
print(math.pi)
print(math.sqrt(16))
print(math.exp(5))

# random - Generate random numbers
import random
print(random.randint(1, 10))  # Random integer between 1 and 10
print(random.choice(['apple', 'banana', 'cherry']))  # Random choice from a list
