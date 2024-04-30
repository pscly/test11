import time
from pathlib import Path

if __name__ == '__main__':
    dist = Path('./dist')
    dist.mkdir(exist_ok=True, parents=True)
    with open(dist / 'log.txt', 'a') as f:
        a = time.strftime("%Y-%m-%d %H:%M:%S__main3", time.localtime())
