import time
import threading

semaphore = threading.Semaphore(3)

def func():
    if semaphore.acquire():
        for i in range(1):
            print(threading.currentThread().getName() + "acquire semaphore", time.ctime())
        time.sleep(3)
        semaphore.release()
        print(threading.currentThread().getName() + "release semaphore", time.ctime())


for i in range(3):
    t1 = threading.Thread(target=func, args=())
    t1.start()
