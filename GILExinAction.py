import threading
import time

def cpu_task():
    count = 0
    for _ in range(10**7):
        count += 1

start = time.time()
t1 = threading.Thread(target=cpu_task)
t2 = threading.Thread(target=cpu_task)

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()
print('TIme taken with thread:', end - start)


# same example using multiprocessing bypasses GIL and allows true parallel execution
import multiprocessing
import time

def cpu_task1():
    count = 0
    for _ in range(10**7):
        count += 1


if __name__ == '__main__':
    start = time.time()
    p1 = multiprocessing.Process(target=cpu_task1)
    p2 = multiprocessing.Process(target=cpu_task1)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    end = time.time()
    print('Time taken with multiprocessing:', end - start)