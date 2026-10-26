import time
from functools import wraps


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            elapsed = time.perf_counter() - start
            print(f"{func.__name__} выполнена за {elapsed:.6f} секунд")

    return wrapper


@measure_time
def no_args():
    return sum(range(100000))


@measure_time
def with_args(a, b):
    return a + b


@measure_time
def with_kwargs(*args, **kwargs):
    time.sleep(0.01)
    return args, kwargs


print(no_args())
print(with_args(2, 3))
print(with_kwargs(1, 2, key="value"))