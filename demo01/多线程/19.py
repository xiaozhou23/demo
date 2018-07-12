import time
import threading

class MyThread(threading.Thread):
    def run(self):
        global num
        #time.sleep(1)

        if mutex.acquire():
            num += 1
            msg = self.name + " set num is " + str(num)
            print(msg)
            mutex.acquire()
            mutex.release()
            mutex.release()

num = 0
mutex = threading.RLock()

for i in range(5):
    t = MyThread()
    t.start()
