import multiprocessing
import threading
import os
import time

def work():
    global n
    n = 0

if __name__ == '__main__':
    n = 100
    t = threading.Thread(target=work)
    t.start()
    t.join()
    print(n)

    n = 200
    p = multiprocessing.Process(target=work)
    p.start()
    p.join()
    print(n)