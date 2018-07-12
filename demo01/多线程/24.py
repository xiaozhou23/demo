import multiprocessing
import time

def consumer(output_q):
    print("Into consumer:", time.ctime())
    while True:
        item = output_q.get()
        if item == None:
            break
        print("Pull " + str(item) + " out of q")
        output_q.task_done()
    print("Out of consumer", time.ctime())

def producer(sequence, input_q):
    print("Into producer", time.ctime())
    for item in sequence:
        input_q.put(item)
        print("Put " + str(item) + " into q")
    print("Out producer", time.ctime())

if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()

    con_p = multiprocessing.Process(target=consumer, args=(q,))
    con_p.daemon = True
    con_p.start()
    sequence = [1,2,3,4]
    producer(sequence, q)
    q.put(None)
    q.join()