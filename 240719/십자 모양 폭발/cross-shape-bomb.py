import sys

n = int(sys.stdin.readline().rstrip())
arr = []

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

r, c = map(int, sys.stdin.readline().rstrip().split())
r -= 1
c -= 1

power = arr[r][c]

# 폭파
for i in range(power):
    for sign in [-1, 1]:
        dr = sign * i
        if (r+dr >= 0) and (r+dr < n):
            arr[r+dr][c] = 0

        dc = sign * i
        if (c+dc >= 0) and (c+dc < n):
            arr[r][c+dc] = 0

# 중력 작용
for j in range(n):
    temp = []
    cnt = 0

    for i in range(n-1, -1, -1):
        if arr[i][j] != 0:
            temp.append(arr[i][j])
            cnt += 1

    temp = temp + [0 for i in range(n - cnt)]

    for i in range(n-1, -1, -1):
        arr[i][j] = temp[n-1-i]

for i in range(n):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print()