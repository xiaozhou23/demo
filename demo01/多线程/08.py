import time
import threading

def loop1():
    print("Current thread is {0}".format(threading.currentThread()))
    print("Start loop1 at:", time.ctime())
    time.sleep(2)
    print("End loop1 at:", time.ctime())

def loop2():
    print("Start loop2 at:", time.ctime())
    time.sleep(4)
    print("End loop2 at:", time.ctime())

def loop3():
    print("Start loop3 at:", time.ctime())
    time.sleep(6)
    print("End loop3 at:", time.ctime())

def main():
    print("Starting MainThread", time.ctime())
    t1 = threading.Thread(target=loop1, args=())
    t2 = threading.Thread(target=loop2, args=())
    t3 = threading.Thread(target=loop3, args=())

    t1.setName("Thr_1")
    t2.setName("Thr_2")
    t3.setName("Thr_3")

    t1.start()
    t2.start()
    t3.start()

    time.sleep(3)

    for thr in threading.enumerate():
        #print(thr)
        print("Active thread name is {0}".format(thr.getName()))

    print("Current thread is {0}".format(threading.currentThread()))

    print(threading.active_count())
    print("The active thread number is",threading.activeCount())

    t1.join()
    t2.join()
    t3.join()

    print("Ending MainThread at:", time.ctime())

if __name__ == '__main__':
    main()