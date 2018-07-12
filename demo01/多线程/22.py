import multiprocessing
import os
import time

def info(title):
    print(title)
    print("module name is",__name__)
    print("parent process id is", os.getppid())
    print("process id is", os.getpid())

def f(name):
    info("Function f")
    print("hello", name)

if __name__ == '__main__':
    info("main line")
    p = multiprocessing.Process(target=f, args=("LILY",))
    p.start()
    p.join()