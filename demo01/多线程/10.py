import threading
import time

#loop = [4,2]

class ThreadFunc:
    def __init__(self, name):
        self.name = name

    def loop(self, nloop, nsec):
        print("Start", nloop, "at", time.ctime())
        time.sleep(nsec)
        print("Done loop", nloop, "at", time.ctime())

def main():
    print("Starting at", time.ctime())
    t = ThreadFunc("loop")
    t1 = threading.Thread(target=t.loop, args=("loop1", 4))
    t2 = threading.Thread(target=ThreadFunc("loop").loop, args=("loop2", 2))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("All done at", time.ctime())

if __name__ == '__main__':
    main()
