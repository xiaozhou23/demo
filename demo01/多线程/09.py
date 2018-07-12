import time
import threading

class MyThread(threading.Thread):
    #def __init__(self, args):
    #   super(MyThread, self).__init__()
    #    self.args = args

    def run(self):
        time.sleep(2)
        print("Thread start at",time.ctime())
        #print("Args is {0}".format(self.args))

for i in range(5):
    t = MyThread()
    print(t.getName())
    t.start()
    t.join()

print("End.......")