import threading
import time

def func():
    print("Run at:", time.ctime())
    time.sleep(3)
    print("Done", time.ctime())

if __name__ == '__main__':
    print("Main start at", time.ctime())
    t = threading.Timer(6, func)
    t.start()

    i = 0
    while True:
        print("{0}***********".format(i), time.ctime())
        time.sleep(3)
        i += 1