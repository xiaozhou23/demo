from threading import Thread

n = 100

def func():
    global n
    tem = n
    n = tem -1
    print(n)

if __name__ == '__main__':
    for i in range(3):
        t = Thread(target=func)
        t.start()
    print(n)