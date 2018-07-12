import threading

sum = 0
loopSum = 1000000

def myAdd():
    global sum , loopSum
    for i in range(0, loopSum):
        sum += 1

def myMinu():
    global sum, loopSum
    for i in range(0, loopSum):
        sum -= 1

def main():
    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myMinu, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("All is done, Sum is {0}".format(sum))

if __name__ == '__main__':
    main()