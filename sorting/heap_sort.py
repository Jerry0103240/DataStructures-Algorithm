import sys
sys.path.append('D:/DataStructures/sorting/')
from gen_test_cases import TestCaseGenerator, Timer


class HeapSort():
    def __init__(self, arr) -> None:
        self.count = len(arr)
        self.arr = [None] + arr
        self.build_max_heap()

    def max_heapify(self, k):
        self.sink(k)

    def sink(self, k):
        while 2 * k <= self.count:
            j = 2 * k
            if j + 1 <= self.count and self.arr[j] < self.arr[j + 1]:
                j += 1
            if self.arr[j] < self.arr[k]:
                break
            self.swap(k, j)
            k = j

    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def dec_count(self):
        self.count -= 1

    def build_max_heap(self):
        for k in range(self.count // 2, 0, -1):
            self.max_heapify(k)

    def sort(self):
        for _ in range(1, len(self.arr)):
            self.swap(1, self.count)
            self.dec_count()
            self.max_heapify(1)
        # print(self.arr[1:])


if __name__ == '__main__':
    arr, sort_arr = TestCaseGenerator().generate()
    with Timer('heap_sort') as timer:
        heap_sort = HeapSort(arr)
        heap_sort.sort()

    assert heap_sort.arr[1:] == sort_arr
