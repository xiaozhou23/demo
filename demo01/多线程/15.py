import time
import threading

lock1 = threading.Lock()
lock2 = threading.Lock()

def fun1():
    lock1.acquire()
    print("fun1申请到锁1", time.ctime())
    time.sleep(2)
    lock2.acquire()
    print("fun1申请到锁2", time.ctime())
    lock2.release()
    print("fun1释放了锁2", time.ctime())
    lock1.release()
    print("fun1释放了锁1", time.ctime())

def fun2():
    lock2.acquire()
    print("fun2申请到锁2", time.ctime())
    time.sleep(4)
    lock1.acquire()
    print("fun2申请到锁1", time.ctime())
    lock1.release()
    print("fun2申请了锁1", time.ctime())
    lock2.release()
    print("fun2释放了锁2", time.ctime())


if __name__ == '__main__':
    t1 = threading.Thread(target=fun1, args=())
    t2 = threading.Thread(target=fun2, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("End....")