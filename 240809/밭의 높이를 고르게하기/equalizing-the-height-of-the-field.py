import sys

n, h, t = map(int, input().split())
height = list(map(int, input().split()))

min_cost = sys.maxsize
for i in range(n):
    for j in range(i+t-1, n):
        cost = 0

        for h_ in height[i:j+1]:
            cost += abs(h_ - h)
        
        min_cost = min(cost, min_cost)

print(min_cost)