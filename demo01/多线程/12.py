import threading
import time

sum = 0
loopSum = 1000000

lock = threading.Lock()

def myAdd():
    global sum , loopSum
    lock.acquire()
    print("Add is start", time.ctime())
    for i in range(0, loopSum):
        sum += 1
    time.sleep(2)
    lock.release()
    print("Add is end", time.ctime())

def myMinu():
    global sum, loopSum
    lock.acquire()
    print("Minu is start", time.ctime())
    for i in range(0, loopSum):
        sum -= 1
    time.sleep(2)
    lock.release()
    print("Minu is end", time.ctime())

def main():
    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myMinu, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("All is done, Sum is {0}".format(sum))

if __name__ == '__main__':
    main()