arr = [0 for i in range(-1000, 1001)]
loc = 1000
n = int(input())

for i in range(n):
    x, d = input().split()
    x = int(x)

    if d == "R":
        for j in range(loc, loc + x):
            arr[j] += 1
        loc = loc + x
    elif d == "L":
        for j in range(loc - x, x):
            arr[j] += 1
        loc = loc - x

    # l = []
    # for i in range(len(arr)):
    #     if arr[i] >= 1:
    #         l.append((i - 1000, arr[i]))
    # print(l)

cnt = 0
# l = []
for i in range(len(arr)):
    if arr[i] >= 1:
        # cnt += 1
        l.append((i - 1000, arr[i]))
# print(l)
print(cnt)