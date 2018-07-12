import time
import threading

def loop1():
    print("Start loop1 at:", time.ctime())
    time.sleep(8)
    print("End loop1 at:", time.ctime())

def loop2():
    print("Start loop2 at:", time.ctime())
    time.sleep(2)
    print("End loop2 at:", time.ctime())

def main():
    print("Starting at:", time.ctime())
    t1 = threading.Thread(target=loop1, args=())
    t2 = threading.Thread(target=loop2, args=())
    t1.start()
    t2.start()
    print("All done at:", time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(10)