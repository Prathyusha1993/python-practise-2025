# try:
#     # code that might cause an error
# except SomeException:
#     # code taht runs if an error occurs
# else:
#     # code that runs if no error occurs
# finally:
#     #code that always runs(clean up)
# these blocks are used to handle exception errors gracefully, so the program doesn't crash unexpectedly.

try:
    x = int(input('Enter a number: '))
    result = 10/x
except ValueError:
    print('Please enter a valid integer')
except ZeroDivisionError:
    print('Cannot divide by zero.')
else:
    print(f'result is {result}')
finally:
    print('Execution finished.')

# else runs only if no exception occurs
# finally runs no matter what
