arr = [0 for i in range(-1000, 1001)]
loc = 1000
n = int(input())

for i in range(n):
    x, d = input().split()
    x = int(x)

    if d == "R":
        for j in range(x):
            arr[loc] += 1
            loc += 1
    elif d == "L":
        for j in range(x):
            arr[loc] += 1
            loc -= 1

cnt = 0
for a in arr:
    if a >= 2:
        cnt += 1
print(cnt)