n = int(input())

arr = list(map(int, input().split()))

for i in range(1, n):
    key = arr[i]
    for j in range(i-1, -1, -1):
        if arr[j] > key:
            arr[j+1] = arr[j]
            arr[j] = key
        else:
            break

arr = list(map(str, arr))
print(" ".join(arr))