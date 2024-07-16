n = int(input())
arr_num = list(map(int, input().split()))
arr = []
for i in range(n):
    arr.append(arr_num[i])

    if i % 2 == 0:
        print(arr[i//2], end=' ')