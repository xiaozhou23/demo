import time

def consumer():
    print("C start")
    r = ""
    while True:
        n = yield r
        if not n:
            return
        print("[CONSUMER] ←← Consuming %s..." % n)
        time.sleep(2)
        r = "200 OK"

def producer(c):
    print("P start")
    next(c)
    n = 0
    while n < 5:
        n = n + 1
        print("[PRODUCER] →→ Producing %s..." % n)
        cr = c.send(n)
        print('[PRODUCER] Consumer return: %s' % cr)
    c.close()

if __name__ == '__main__':
    c = consumer()
    producer(c)