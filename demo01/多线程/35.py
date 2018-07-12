import threading
import multiprocessing
import os

def func():
    pid = os.getpid()
    print(pid)

if __name__ == '__main__':
    for i in range(4):
        t = threading.Thread(target=func)
        t.start()

    for i in range(4):
        p = multiprocessing.Process(target=func)
        p.start()
