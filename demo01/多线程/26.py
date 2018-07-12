import multiprocessing
import time

def consumer(output_q):
    print("Into consumer:", time.ctime())
    while True:
        item = output_q.get()
        if item == None:
            break
        print("Pull " + str(item) + " out of q")
    print("Out of consumer", time.ctime())

def producer(sequence, input_q):
    print("Into producer", time.ctime())
    for item in sequence:
        input_q.put(item)
        print("Put " + str(item) + " into q")
    print("Out producer", time.ctime())

if __name__ == '__main__':
    q = multiprocessing.Queue()

    con_p1 = multiprocessing.Process(target=consumer, args=(q,))
    con_p1.daemon = True
    con_p1.start()

    con_p2 = multiprocessing.Process(target=consumer, args=(q,))
    con_p2.daemon = True
    con_p2.start()

    con_p3 = multiprocessing.Process(target=consumer, args=(q,))
    con_p3.daemon = True
    con_p3.start()

    sequence = [1,2,3,4]
    producer(sequence, q)
    q.put(None)
    q.put(None)
    q.put(None)

    con_p1.join()
    con_p2.join()
    con_p3.join()