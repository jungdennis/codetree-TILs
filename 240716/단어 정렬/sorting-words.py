n = int(input())
arr = []

for i in range(n):
    arr.append(input())

arr.sort()

for i in range(n):
    print(arr[i])