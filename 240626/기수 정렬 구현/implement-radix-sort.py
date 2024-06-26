digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

n = int(input())

arr = input().split()
max_digit = len(str(max(map(int, arr))))

for i in range(n):
    arr[i] = arr[i].zfill(max_digit)

for i in range(max_digit-1, -1, -1):
    arr_digit = [[] for i in range(10)]

    for j in range(n):
        num = arr[j]
        idx = digit.index(num[i])
        arr_digit[idx].append(arr[j])

    arr = []
    for k in range(10):
        arr += arr_digit[k]

arr = list(map(str, map(int, arr)))
print(" ".join(arr))