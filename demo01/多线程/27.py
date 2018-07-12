from threading import Thread
from time import sleep, ctime

def sayHi(name):
    sleep(2)
    print("{0} say hi".format(name))

if __name__ == '__main__':
    t = Thread(target=sayHi, args=("Lily",))
    t.start()
    t.setDaemon(True)
    #t.join()
    print("Done...")