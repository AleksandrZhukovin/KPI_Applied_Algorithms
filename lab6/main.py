import sys


__all__ = ('top_down_merge_sort', 'bottom_up_merge_sort', 'bottom_up_merge_sort_optimized', 'bottom_up_merge_sort_10')


def top_down_merge_sort(nums):
    total_memory_used = sys.getsizeof(nums)
    compare_count = 0
    copy_count = 0

    def merge(left, right):
        nonlocal compare_count, copy_count
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            compare_count += 1
            if left[i] < right[j]:
                result.append(left[i])
                copy_count += 1
                i += 1
            else:
                result.append(right[j])
                copy_count += 1
                j += 1
        result.extend(left[i:])
        copy_count += len(left[i:])
        result.extend(right[j:])
        copy_count += len(right[j:])
        return result

    def sort(nums):
        nonlocal total_memory_used, compare_count, copy_count
        if len(nums) <= 1:
            total_memory_used += sys.getsizeof(nums)
            return nums

        mid = len(nums) // 2

        left_half = sort(nums[:mid])
        right_half = sort(nums[mid:])

        result = merge(left_half, right_half)

        total_memory_used += sys.getsizeof(left_half) + sys.getsizeof(right_half) + sys.getsizeof(result)

        return result

    sorted_nums = sort(nums)
    print("Пам'ять:", total_memory_used, "байт")
    print("Порівнянь:", compare_count)
    print("Копіювань:", copy_count)

    return sorted_nums



def bottom_up_merge_sort(nums):
    total_memory_used = sys.getsizeof(nums)
    compare_count = 0
    copy_count = 0

    width = 1
    n = len(nums)

    def merge(left, right):
        nonlocal compare_count, copy_count
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            compare_count += 1
            if left[i] < right[j]:
                result.append(left[i])
                copy_count += 1
                i += 1
            else:
                result.append(right[j])
                copy_count += 1
                j += 1
        result.extend(left[i:])
        copy_count += len(left[i:])
        result.extend(right[j:])
        copy_count += len(right[j:])
        return result

    while width < n:
        for i in range(0, n, 2 * width):
            left = nums[i:i + width]
            right = nums[i + width:i + 2 * width]
            merged = merge(left, right)
            total_memory_used += sys.getsizeof(left) + sys.getsizeof(right) + sys.getsizeof(merged)
            nums[i:i + len(merged)] = merged
        width *= 2

    print("Пам'ять:", total_memory_used, "байт")
    print("Порівнянь:", compare_count)
    print("Копіювань:", copy_count)

    return nums


def bottom_up_merge_sort_optimized(nums):
    total_memory_used = sys.getsizeof(nums)
    compare_count = 0
    copy_count = 0

    def insertion_sort(sub_arr):
        nonlocal compare_count, copy_count
        for i in range(1, len(sub_arr)):
            key = sub_arr[i]
            j = i - 1
            while j >= 0 and sub_arr[j] > key:
                compare_count += 1
                sub_arr[j + 1] = sub_arr[j]
                copy_count += 1
                j -= 1
            sub_arr[j + 1] = key
            copy_count += 1

    def merge(arr, temp, low, mid, high):
        nonlocal compare_count, copy_count
        for k in range(low, high + 1):
            temp[k] = arr[k]
            copy_count += 1
        i, j = low, mid + 1
        for k in range(low, high + 1):
            if i > mid:
                arr[k] = temp[j]
                copy_count += 1
                j += 1
            elif j > high:
                arr[k] = temp[i]
                copy_count += 1
                i += 1
            else:
                compare_count += 1
                if temp[j] < temp[i]:
                    arr[k] = temp[j]
                    copy_count += 1
                    j += 1
                else:
                    arr[k] = temp[i]
                    copy_count += 1
                    i += 1

    n = len(nums)
    temp = nums[:]
    total_memory_used += sys.getsizeof(temp)
    width = 1
    while width < n:
        for i in range(0, n, 2 * width):
            low = i
            mid = min(i + width - 1, n - 1)
            high = min(i + 2 * width - 1, n - 1)

            if (high - low + 1) <= 100:
                insertion_sort(nums[low:high + 1])
            else:
                if mid < len(nums) - 1 and nums[mid] <= nums[mid + 1]:
                    compare_count += 1
                    continue
                merge(nums, temp, low, mid, high)
        width *= 2

    print("Пам'ять:", total_memory_used, "байт")
    print("Порівнянь:", compare_count)
    print("Копіювань:", copy_count)

    return nums


def bottom_up_merge_sort_10(nums):
    total_memory_used = sys.getsizeof(nums)
    compare_count = 0
    copy_count = 0

    def merge(arr, temp, low, mid1, mid2, mid3, mid4, mid5, mid6, mid7, mid8, mid9, high):
        nonlocal compare_count, copy_count
        for k in range(low, high + 1):
            temp[k] = arr[k]
            copy_count += 1

        pointers = [low, mid1 + 1, mid2 + 1, mid3 + 1, mid4 + 1, mid5 + 1, mid6 + 1, mid7 + 1, mid8 + 1, mid9 + 1]

        for k in range(low, high + 1):
            min_value = float('inf')
            min_index = -1
            for i in range(10):
                if pointers[i] <= mid1 and pointers[i] <= high and temp[pointers[i]] < min_value:
                    min_value = temp[pointers[i]]
                    min_index = i
                    compare_count += 1
            arr[k] = min_value
            copy_count += 1
            pointers[min_index] += 1

    n = len(nums)
    temp = nums[:]
    total_memory_used += sys.getsizeof(temp)

    width = 1
    while width < n:
        for i in range(0, n, 10 * width):
            low = i
            mid1 = min(i + width - 1, n - 1)
            mid2 = min(i + 2 * width - 1, n - 1)
            mid3 = min(i + 3 * width - 1, n - 1)
            mid4 = min(i + 4 * width - 1, n - 1)
            mid5 = min(i + 5 * width - 1, n - 1)
            mid6 = min(i + 6 * width - 1, n - 1)
            mid7 = min(i + 7 * width - 1, n - 1)
            mid8 = min(i + 8 * width - 1, n - 1)
            mid9 = min(i + 9 * width - 1, n - 1)
            high = min(i + 10 * width - 1, n - 1)
            merge(nums, temp, low, mid1, mid2, mid3, mid4, mid5, mid6, mid7, mid8, mid9, high)
        width *= 10

    print("Пам'ять:", total_memory_used, "байт")
    print("Порівнянь:", compare_count)
    print("Копіювань:", copy_count)

    return nums
