def select_pivot(low, high):
    length = high - low + 1

    if length <= 3:
        return high, arr[high]
    else:
        mid = (low + high) // 2

        low_ = arr[low]
        mid_ = arr[mid]
        high_ = arr[high]

        med_sort = [low_, mid_, high_]
        med_sort.sort()

        median = med_sort[1]
        
        if low_ == median:
            idx = low
        elif mid_ == median:
            idx = mid
        elif high_ == median:
            idx = high

        return idx, median

def swap(i, j):
    if i != j:
        arr[i], arr[j] = arr[j], arr[i]

def partition(low, high):
    idx, pivot = select_pivot(low, high)
    swap(idx, high)

    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            swap(i, j)
            i += 1

    swap(i, high)

    return i

def quick_sort(low, high):
    if low < high:
        pos = partition(low, high)

        quick_sort(low, pos-1)
        quick_sort(pos+1, high)

n = int(input())
arr = list(map(int, input().split()))

quick_sort(0, n-1)

for i in arr:
    print(i, end=' ')