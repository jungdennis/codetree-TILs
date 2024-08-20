import sys

n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

min_cost = sys.maxsize
for x in range(84):
    cost = 0 
    for h in arr:
        if h < x:
            cost += abs(h - x) ** 2
        elif h > x + 17:
            cost += abs(h - x - 17) ** 2

    min_cost = min(cost, min_cost)

print(min_cost)