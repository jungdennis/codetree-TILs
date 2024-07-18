arr = [0 for i in range(-1000, 1001)]
loc = 1000
n = int(input())

for i in range(n):
    x, d = input().split()
    x = int(x)

    if d == "R":
        for j in range(loc, loc + x):
            arr[j] = arr[j] + 1
        loc = loc + x
    elif d == "L":
        for j in range(loc - x, loc):
            arr[j] = arr[j] + 1
        loc = loc - x

cnt = 0
for i in range(len(arr)):
    if arr[i] >= 2:
        cnt += 1
print(cnt)