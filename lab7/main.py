import random
import time
import sys


__all__ = (
    'sort_lomuto_last',
    'sort_lomuto_random',
    'sort_lomuto_median_three',
    'sort_lomuto_median_random',
    'sort_hoare_last',
    'sort_hoare_random',
    'sort_hoare_median_three',
    'sort_hoare_median_random',
    'sort_three_quicksort',
    'sort_with_dual_pivot',
)

sys.setrecursionlimit(5000)

comparisons = 0
swaps = 0
memory = 0


def reset():
    global memory, swaps, comparisons
    memory = 0
    swaps = 0
    comparisons = 0


def track_memory():
    global memory
    memory += sys.getsizeof(comparisons) + sys.getsizeof(swaps) + sys.getsizeof(memory)


def sort_lomuto_last(arr):
    reset()
    start = time.time()
    lomuto_last(arr, 0, len(arr) - 1)
    finish = time.time()
    print(f"Час виконання: {finish - start}")
    print(f"Кількість порівнянь: {comparisons}")
    print(f"Кількість замін: {swaps}")
    print(f"Використання пам'яті: {memory}")


def sort_lomuto_random(arr):
    reset()
    start = time.time()
    lomuto_random(arr, 0, len(arr) - 1)
    finish = time.time()
    print(f"Час виконання: {finish - start}")
    print(f"Кількість порівнянь: {comparisons}")
    print(f"Кількість замін: {swaps}")
    print(f"Використання пам'яті: {memory}")


def sort_lomuto_median_three(arr):
    reset()
    start = time.time()
    lomuto_median_three(arr, 0, len(arr) - 1)
    finish = time.time()
    print(f"Час виконання: {finish - start}")
    print(f"Кількість порівнянь: {comparisons}")
    print(f"Кількість замін: {swaps}")
    print(f"Використання пам'яті: {memory}")


def sort_lomuto_median_random(arr):
    reset()
    start = time.time()
    lomuto_median_random(arr, 0, len(arr) - 1)
    finish = time.time()
    print(f"Час виконання: {finish - start}")
    print(f"Кількість порівнянь: {comparisons}")
    print(f"Кількість замін: {swaps}")
    print(f"Використання пам'яті: {memory}")


def sort_hoare_last(arr):
    reset()
    start = time.time()
    hoare_last(arr, 0, len(arr) - 1)
    finish = time.time()
    print(f"Час виконання: {finish - start}")
    print(f"Кількість порівнянь: {comparisons}")
    print(f"Кількість замін: {swaps}")
    print(f"Використання пам'яті: {memory}")


def sort_hoare_random(arr):
    reset()
    start = time.time()
    hoare_random(arr, 0, len(arr) - 1)
    finish = time.time()
    print(f"Час виконання: {finish - start}")
    print(f"Кількість порівнянь: {comparisons}")
    print(f"Кількість замін: {swaps}")
    print(f"Використання пам'яті: {memory}")


def sort_hoare_median_three(arr):
    reset()
    start = time.time()
    hoare_median_three(arr, 0, len(arr) - 1)
    finish = time.time()
    print(f"Час виконання: {finish - start}")
    print(f"Кількість порівнянь: {comparisons}")
    print(f"Кількість замін: {swaps}")
    print(f"Використання пам'яті: {memory}")


def sort_hoare_median_random(arr):
    reset()
    start = time.time()
    hoare_median_random(arr, 0, len(arr) - 1)
    finish = time.time()
    print(f"Час виконання: {finish - start}")
    print(f"Кількість порівнянь: {comparisons}")
    print(f"Кількість замін: {swaps}")
    print(f"Використання пам'яті: {memory}")


def sort_dual_pivot(arr):
    reset()
    start = time.time()
    quicksort_dual_pivot(arr, 0, len(arr) - 1)
    finish = time.time()
    print(f"Час виконання: {finish - start}")
    print(f"Кількість порівнянь: {comparisons}")
    print(f"Кількість замін: {swaps}")
    print(f"Використання пам'яті: {memory}")


def sort_three_quicksort(arr):
    reset()
    start = time.time()
    quicksort_three(arr, 0, len(arr) - 1)
    finish = time.time()
    print(f"Час виконання: {finish - start}")
    print(f"Кількість порівнянь: {comparisons}")
    print(f"Кількість замін: {swaps}")
    print(f"Використання пам'яті: {memory}")


def sort_with_dual_pivot(arr):
    reset()
    start = time.time()
    quicksort_dual_pivot(arr, 0, len(arr) - 1)
    finish = time.time()
    print(f"Час виконання: {finish - start}")
    print(f"Кількість порівнянь: {comparisons}")
    print(f"Кількість замін: {swaps}")
    print(f"Використання пам'яті: {memory}")


def lomuto_last(arr, low, high):
    global memory, comparisons, swaps
    if low < high:
        comparisons += 1
        pivot = lomuto_partition_last(arr, low, high)
        lomuto_last(arr, low, pivot - 1)
        lomuto_last(arr, pivot + 1, high)
        track_memory()


def lomuto_partition_last(arr, low, high):
    global memory, comparisons, swaps
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        comparisons += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    swaps += 1
    memory += sys.getsizeof(pivot) + sys.getsizeof(i)
    return i + 1


def lomuto_random(arr, low, high):
    global memory, comparisons, swaps
    if low < high:
        comparisons += 1
        pivot = lomuto_partition_random(arr, low, high)
        lomuto_random(arr, low, pivot - 1)
        lomuto_random(arr, pivot + 1, high)
        track_memory()


def lomuto_partition_random(arr, low, high):
    global memory, comparisons, swaps
    random_index = random.randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]
    swaps += 1
    return lomuto_partition_last(arr, low, high)


def lomuto_median_three(arr, low, high):
    global memory, comparisons, swaps
    if low < high:
        comparisons += 1
        pivot = lomuto_partition_median_three(arr, low, high)
        lomuto_median_three(arr, low, pivot - 1)
        lomuto_median_three(arr, pivot + 1, high)
        track_memory()


def lomuto_partition_median_three(arr, low, high):
    global memory, comparisons, swaps
    mid = (low + high) // 2
    pivot_index = sorted([(arr[low], low), (arr[mid], mid), (arr[high], high)])[1][1]
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    swaps += 1
    memory += sys.getsizeof(mid) + sys.getsizeof(pivot_index)
    return lomuto_partition_last(arr, low, high)


def lomuto_median_random(arr, low, high):
    global memory, comparisons, swaps
    if low < high:
        comparisons += 1
        pivot = lomuto_partition_median_random(arr, low, high)
        lomuto_median_random(arr, low, pivot - 1)
        lomuto_median_random(arr, pivot + 1, high)
        track_memory()


def lomuto_partition_median_random(arr, low, high):
    indices = list(range(low, high + 1)) if high - low + 1 < 3 else random.sample(range(low, high + 1), 3)

    pivot_index = sorted(indices, key=lambda x: arr[x])[len(indices) // 2]
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]

    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def hoare_last(arr, low, high):
    if low < high:
        pivot = hoare_partition_last(arr, low, high)

        if pivot == low:
            return

        hoare_last(arr, low, pivot - 1)
        hoare_last(arr, pivot + 1, high)


def hoare_partition_last(arr, low, high):
    pivot = arr[high]
    i = low - 1
    j = high

    while True:
        while True:
            i += 1
            if arr[i] >= pivot:
                break

        while True:
            j -= 1
            if arr[j] <= pivot or j == low:
                break

        if i >= j:
            arr[i], arr[high] = arr[high], arr[i]
            return i

        arr[i], arr[j] = arr[j], arr[i]



def hoare_random(arr, low, high):
    global memory, comparisons, swaps
    if low < high:
        comparisons += 1
        pivot = hoare_partition_random(arr, low, high)
        hoare_random(arr, low, pivot)
        hoare_random(arr, pivot + 1, high)
        track_memory()


def hoare_partition_random(arr, low, high):
    global memory, comparisons, swaps
    random_index = random.randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]
    swaps += 1
    return hoare_partition_last(arr, low, high)


def hoare_median_three(arr, low, high):
    global memory, comparisons, swaps
    if low < high:
        comparisons += 1
        pivot = hoare_partition_median_three(arr, low, high)
        hoare_median_three(arr, low, pivot)
        hoare_median_three(arr, pivot + 1, high)
        track_memory()


def hoare_partition_median_three(arr, low, high):
    global memory, comparisons, swaps
    mid = (low + high) // 2
    pivot_index = sorted([(arr[low], low), (arr[mid], mid), (arr[high], high)])[1][1]
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    swaps += 1
    memory += sys.getsizeof(mid) + sys.getsizeof(pivot_index)
    return hoare_partition_last(arr, low, high)


def hoare_median_random(arr, low, high):
    if low < high:
        pivot = hoare_partition_median_random(arr, low, high)

        if pivot == low or pivot == high:
            return

        hoare_median_random(arr, low, pivot)
        hoare_median_random(arr, pivot + 1, high)


def hoare_partition_median_random(arr, low, high):
    if high - low + 1 < 3:
        pivot_index = random.randint(low, high)
    else:
        indices = random.sample(range(low, high + 1), 3)
        pivot_index = sorted(indices, key=lambda x: arr[x])[len(indices) // 2]

    pivot = arr[pivot_index]
    i = low - 1
    j = high + 1

    while True:
        while True:
            i += 1
            if arr[i] >= pivot:
                break

        while True:
            j -= 1
            if arr[j] <= pivot:
                break

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]


def quicksort_three(arr, low, high):
    global comparisons, swaps
    if low < high:
        track_memory()
        lt, gt = partition_quicksort_three(arr, low, high)
        quicksort_three(arr, low, lt - 1)
        quicksort_three(arr, gt + 1, high)


def partition_quicksort_three(arr, low, high):
    global comparisons, swaps, memory
    if high - low + 1 < 3:
        pivot = arr[random.randint(low, high)]
    else:
        indices = random.sample(range(low, high + 1), 3)
        pivot = sorted([arr[i] for i in indices])[1]
        comparisons += 3

    lt = low
    gt = high
    i = low
    while i <= gt:
        comparisons += 1
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
            swaps += 1
        elif arr[i] > pivot:
            arr[gt], arr[i] = arr[i], arr[gt]
            gt -= 1
            swaps += 1
        else:
            i += 1

    memory += sys.getsizeof(pivot) + sys.getsizeof(lt) + sys.getsizeof(gt) + sys.getsizeof(i)
    return lt, gt


def quicksort_dual_pivot(arr, low, high):
    global comparisons, swaps
    if low < high:
        track_memory()
        lp, rp = partition_dual_pivot(arr, low, high)
        quicksort_dual_pivot(arr, low, lp - 1)
        quicksort_dual_pivot(arr, lp + 1, rp - 1)
        quicksort_dual_pivot(arr, rp + 1, high)


def partition_dual_pivot(arr, low, high):
    global comparisons, swaps, memory

    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
        swaps += 1

    pivot1 = arr[low]
    pivot2 = arr[high]
    comparisons += 1

    i = low + 1
    lt = low + 1
    gt = high - 1

    while i <= gt:
        comparisons += 1
        if arr[i] < pivot1:
            arr[i], arr[lt] = arr[lt], arr[i]
            swaps += 1
            lt += 1
        elif arr[i] > pivot2:
            arr[i], arr[gt] = arr[gt], arr[i]
            swaps += 1
            gt -= 1
            i -= 1
        i += 1

    arr[low], arr[lt - 1] = arr[lt - 1], arr[low]
    swaps += 1
    arr[high], arr[gt + 1] = arr[gt + 1], arr[high]
    swaps += 1

    memory += sys.getsizeof(pivot1) + sys.getsizeof(pivot2) + sys.getsizeof(i)
    return lt - 1, gt + 1


# a = [10, 34, 21, 2, 5, 12, 45, 66, 32, 12, 34, 67]
# sort_hoare_random(a)
