# homework1
'''
容器序列：list、tuple、collections.deque
扁平序列：str
可变序列：list、collections.deque
不可变序列：str、tuple
'''


# homework2
def f_map(func, *iter_list):
    for i in zip(*iter_list):
        yield func(*i)


# homework3
import time
from functools import wraps


def timer(func):
    @wraps(func)
    def run_time(*args, **kwargs):
        begin = int(time.time())
        result = func(*args, **kwargs)
        print(int(time.time())-begin)
        return result
    return run_time


@timer
def cal_10(*args, **kwargs):
    time.sleep(2)


if __name__ == '__main__':
    # cal_10(1)
    m = f_map(lambda x: x * 2, [1, 2, 3])
    print(list(m))
