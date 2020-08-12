# homework1
'''
容器序列：list、tuple、dict、collections.deque
扁平序列：str
可变序列：list、dict、collections.deque
不可变序列：str、tuple
'''


# homework2
def f_map(func, iter_list):
    for i in iter_list:
        yield func(i)


# homework3
import time
from functools import wraps


def timer(func):
    @wraps(func)
    def run_time(*args, **kwargs):
        begin = int(time.time())
        func(*args, **kwargs)
        print(int(time.time())-begin)
    return run_time


@timer
def cal_10(*args, **kwargs):
    time.sleep(2)


if __name__ == '__main__':
    # cal_10(1)
    m = f_map(lambda x: x * 2, [1, 2, 3])
