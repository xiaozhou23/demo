from multiprocessing import Pool
import threading
import time

def foo(args):
    time.sleep(1)
    print(args, time.ctime())
    print(threading.currentThread().getName())

if __name__ == '__main__':
    p = Pool(5)
    for i in range(30):
        p.apply_async(func=foo, args=(i,))

    p.close()
    p.join()