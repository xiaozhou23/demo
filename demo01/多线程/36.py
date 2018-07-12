import time
import threading

def counter():
    global n
    for i in range(50000000):
        n = n + 1
    return True
n = 0
def main():
    #n = 0
    l = []
    start_time = time.time()
    for i in range(2):
        t = threading.Thread(target=counter)
        t.start()
        l.append((t))
        #t.join()
    for i in l:
        i.join()

    print(l)
    print(n)
    end_time = time.time()

    print(end_time - start_time)

if __name__ == '__main__':
    main()