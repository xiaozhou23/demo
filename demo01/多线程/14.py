import time
import threading

import queue

class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize() < 10:
                for i in range(10):
                    count += 1
                    msg = self.name + " product " + str(count)
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)

class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 5:
                for i in range(5):
                    msg = self.name + " consumer " + queue.get() + " at " + time.ctime()
                    print(msg)
                    print(queue.qsize())
            time.sleep(3)

if __name__ == '__main__':
    queue = queue.Queue()
    for i in range(20):
        queue.put(" init product "+str(i))

    for i in range(2):
        p = Producer()
        p.start()

    for i in range(3):
        c = Consumer()
        c.start()