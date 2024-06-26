n = int(input())
arr = list(map(int, input().split()))


for i in range(n):
    min_idx = i

    for j in range(i, n):
        if arr[j] < arr[min_idx]:
            min_idx = j
    
    temp = arr[i]
    arr[i] = arr[min_idx]
    arr[min_idx] = temp

arr = list(map(str, arr))

print(" ".join(arr))