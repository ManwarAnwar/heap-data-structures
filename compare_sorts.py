import random, time
from heapsort import heapsort

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    lesser = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quicksort(lesser) + [pivot] + quicksort(greater)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    result.extend(left or right)
    return result

def run_comparison():
    sizes = [1000, 5000, 10000]
    for size in sizes:
        arr = [random.randint(0, 10000) for _ in range(size)]
        print(f"\nArray size: {size}")

        for sort_name, sort_func in [("Heapsort", heapsort), ("Quicksort", quicksort), ("Merge Sort", merge_sort)]:
            arr_copy = arr.copy()
            start = time.time()
            sort_func(arr_copy)
            print(f"{sort_name}: {time.time() - start:.5f} sec")

if __name__ == "__main__":
    run_comparison()
