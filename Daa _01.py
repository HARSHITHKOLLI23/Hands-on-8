
import random
def partition(a, l, h):
    pivot = array[higher]
    i = l - 1
    for j in range(l, h):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[h] = array[h], array[i + 1]
    return i + 1

def quickselect(a, l, h, i):
    if l == h:
        return array[l]
    pivot_index = partition(a, l, h)
    k = pivot_index - l + 1
    if i == k:
        return array[pivot_index]
    elif i < k:
        return quickselect(a, l, pivot_index - 1, i)
    else:
        return quickselect(a, pivot_index + 1, h, i - k)

def ith_order_statistic(a, i):
    if i < 1 or i > len(a):
        return None
    return quickselect(a, 0, len(a) - 1, i)

a = [4,8,12,18,22,29,31,35,23,54,68]
i = 7
print(f"The {i}th order statistic of {a} is: {ith_order_statistic(a, i)}")
