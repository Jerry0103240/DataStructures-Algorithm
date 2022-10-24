import time
import numpy as np


class Timer():
    def __init__(self, algo):
        self.algo = algo

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, *args, **kwargs):
        print(f'{self.algo} time spend = {time.time() - self.start} s')


class TestCaseGenerator():
    def generate(self):
        arr = np.random.randint(0, 1000, size=10000).tolist()
        sort_arr = np.sort(arr).tolist()
        return arr, sort_arr
