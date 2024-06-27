def heapify(idx, n):
    maximum = arr[idx]
    max_idx = idx
    idx_left = 2 * idx
    idx_right = 2 * idx + 1

    if idx_left <= n and arr[idx_left] > maximum:
        maximum = arr[idx_left]
        max_idx = idx_left
    if idx_right <= n and arr[idx_right] > maximum:
        maximum = arr[idx_right]
        max_idx = idx_right

    if maximum != arr[idx]:
        arr[idx], arr[max_idx] = arr[max_idx], arr[idx]
        heapify(max_idx, n)

def heap_sort(n):
    for i in range(n//2, 0, -1):
        heapify(i, n)
    for i in range(n, 0, -1):
        arr[i], arr[1] = arr[1], arr[i]
        heapify(1, i-1)

n = int(input())
arr = [-1] + list(map(int, input().split()))

heap_sort(n)

arr = arr[1:]

for i in arr:
    print(i, end=' ')