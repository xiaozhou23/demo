from threading import Thread
import time

class MyThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(3)
        print(self.name)
if __name__ == '__main__':
    t = MyThread("sayhi")
    t.start()
    #t.join()
    print("Done...")