# MultiProcessing uses seperate processes each with its own python intepreter and memory space.
# ideal for CPU-bound task like image processing, mathematical computations because it bypasses python's GIL (Global Interpreter Lock) allowing true parallel execution.

# when to use:
    # large computations (matrix multiplication, simulations, ML model training)
    # video/image processing (filtering, transformations)
    # data transformations on huge datasets


from multiprocessing import Process
import os

def worker(task):
    print(f'task {task} is executed by process {os.getpid()}')

if __name__ == '__main__':
    processes = []

    for i in range(5):
        p = Process(target=worker, args=(i, ))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print('All processes have finished execution.')