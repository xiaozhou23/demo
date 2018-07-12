import time
import threading

def func():
    print("Start function")
    time.sleep(3)
    print("End function")

print("Main Thread Start")

t1 = threading.Thread(target=func, args=())
t1.setDaemon(True)
t1.setName("MyThread")
t1.start()
thrName = t1.getName()
print(thrName)
print(threading.currentThread())

time.sleep(1)

print("Main Thread End")