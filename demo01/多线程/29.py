import multiprocessing
import threading
import os
import time

def work():
    print("Hello",time.ctime(),threading.currentThread(),os.getpid())

if __name__ == '__main__':
    t1 = threading.Thread(target=work)
    t2 = threading.Thread(target=work)
    t1.start()
    t2.start()
    #time.sleep(2)
    print("thread pid", os.getpid() , time.ctime())

    p1 = multiprocessing.Process(target=work)
    p2 = multiprocessing.Process(target=work)
    p1.start()
    p2.start()
    print("process pid", os.getpid(), time.ctime())