# A thread is the smallest unit of execution in a program.
# Multithreading means running multiple thread within a single process.
# good for I/O bound tasks like network requests, file reading/writing, db queries, since threads can run while others wait for i/o

# when to u se:
    #downloading multiple web pages simultaneously
    #handling multiple client requests in a web server
    #reading/writing multiple files concurrently

# ex:
import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(f'Number: {i}')
        time.sleep(1)


def print_letters():
    for letter in 'ABCDEF':
        print(f'letter: {letter}')
        time.sleep(1)

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# start threads
t1.start()
t2.start()

# wait for threads to finish
t1.join()
t2.join()
print('Both threads have finished execution.')