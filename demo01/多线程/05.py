import time
import threading

def loop1(name):
    print("Start loop1 at:", time.ctime())
    print("Name is", name)
    time.sleep(4)
    print("End loop1 at:", time.ctime())

def loop2(name,age):
    print("Start loop2 at:", time.ctime())
    print("Name is",name,"Age is",age)
    time.sleep(2)
    print("End loop2 at:", time.ctime())

def main():
    print("Starting at:", time.ctime())
    t1 = threading.Thread(target=loop1, args=("Lily",))
    t2 = threading.Thread(target=loop2, args=("Sam",18))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("All done at:", time.ctime())

if __name__ == '__main__':
    main()
    #while True:
    #    time.sleep(10)