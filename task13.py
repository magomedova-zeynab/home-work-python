import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.perf_counter() - self.start
        print(f"Время выполнения: {self.elapsed:.6f} с")
        return False 



    
import time
from contextlib import contextmanager


@contextmanager
def timer():
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f"Время выполнения: {elapsed:.6f} с")