import time

def loop1():
    print("Start loop1 at:", time.ctime())
    time.sleep(4)
    print("End loop1 at:", time.ctime())

def loop2():
    print("Start loop2 at:", time.ctime())
    time.sleep(2)
    print("End loop2 at:", time.ctime())

def main():
    print("Starting at:", time.ctime())
    loop1()
    loop2()
    print("All end at", time.ctime())

if __name__ == '__main__':
    main()