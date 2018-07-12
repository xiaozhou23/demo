import threading
from  time import sleep

def sayHi(name):
    sleep(2)
    print("{0} say hi".format(name))

if __name__ == '__main__':
    t = threading.Thread(target=sayHi, args=("lily",))
    #t.setDaemon(True)
    #t.daemon = True
    t.start()
    print("Main thread done")

    print(threading.Thread.is_alive(t))
