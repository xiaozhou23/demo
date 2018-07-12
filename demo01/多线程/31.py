import multiprocessing
import threading
import os
import time

def work():
    time.sleep(3)
    print("Hello",time.ctime(),threading.currentThread(),threading.currentThread().getName(),os.getpid())

if __name__ == '__main__':
    t1 = threading.Thread(target=work)
    t2 = threading.Thread(target=work)
    t1.start()
    t2.start()
    print(t1.is_alive())
    t1.join()
    print("thread pid", os.getpid() , time.ctime())
    print(threading.currentThread().getName())
    print(threading.currentThread())
    print(threading.enumerate())
    print(threading.activeCount())
    t2.join()
    print(t2.is_alive())
