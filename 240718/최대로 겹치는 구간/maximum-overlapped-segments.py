n = int(input())
arr = [-1] + [0 for i in range(100)]

for i in range(n):
    x1, x2 = map(int, input().split())

    for i in range(x1, x2):
        arr[i] += 1

print(max(arr))