import time

if __name__ == '__main__':
    with open('log.txt', 'a') as f:
        a = time.strftime("%Y-%m-%d %H:%M:%S__main3", time.localtime())
