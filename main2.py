import requests
import time

if __name__ == '__main__':
    for i in range(3):
        t1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        requests.get(f'https://pscly.cn:31002/ime?msg={t1}_我是main2')
        time.sleep(100)
    with open('log.txt', 'a') as f:
        a = time.strftime("%Y-%m-%d %H:%M:%S__main2", time.localtime())
