import sys
n = int(sys.stdin.readline().rstrip())

arr = [0 for i in range(n)]
for i in range(n):
    arr[i] = int(sys.stdin.readline().rstrip())

for i in range(2):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    for j in range(start-1, end):
        arr[j] = 0

    temp = []
    cnt = 0
    for a in arr:
        if a != 0:
            temp.append(a)

    arr = temp

print(len(arr))
for a in arr:
    print(a)