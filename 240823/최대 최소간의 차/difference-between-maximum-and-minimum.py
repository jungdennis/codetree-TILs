import sys

n, k = map(int, input().split())
arr = list(map(int, input().split()))

min_cost = sys.maxsize
for i in range(min(arr), max(arr) - k + 1):
    bound = [i, i+k]

    cost = 0
    for n in arr:
        if n < bound[0]:
            cost += abs(n - bound[0])
        elif n > bound[1]:
            cost += abs(n - bound[1])

    min_cost = min(cost, min_cost)

print(min_cost)