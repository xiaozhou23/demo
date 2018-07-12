import time
import threading

def loop1(name):
    print("Start loop1 at:", time.ctime())
    print("Name is", name)
    time.sleep(8)
    print("End loop1 at:", time.ctime())

def loop2(name,age):
    print("Start loop2 at:", time.ctime())
    print("Name is",name,"Age is",age)
    time.sleep(2)
    print("End loop2 at:", time.ctime())

if __name__ == '__main__':
    print("Starting at:", time.ctime())
    t1 = threading.Thread(target=loop1, args=("Lily",))
    t1.daemon = True
    t2 = threading.Thread(target=loop2, args=("Sam",18))
    t2.setDaemon(True)
    t1.start()
    t2.start()
    print("All end at:", time.ctime())
