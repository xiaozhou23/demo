import time
import _thread as thread

def loop1(name):
    print("Start loop1 at:", time.ctime())
    print("Name is", name)
    time.sleep(4)
    print("End loop1 at:", time.ctime())

def loop2(name,age):
    print("Start loop2 at:", time.ctime())
    print("Name is",name,"Age is",age)
    time.sleep(2)
    print("End loop2 at:", time.ctime())

def main():
    print("Starting at:", time.ctime())
    thread.start_new_thread(loop1, ("Lily",))
    thread.start_new_thread(loop2, ("Sam",18))
    print("All done at:", time.ctime())

if __name__ == '__main__':
    main()
    while True:
        print("-" * 20)
        time.sleep(1)
