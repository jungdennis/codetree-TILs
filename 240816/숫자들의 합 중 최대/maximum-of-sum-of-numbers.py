import sys

X, Y = map(int, input().split())

max_sum = -sys.maxsize
for i in range(X, Y+1):
    sum_ = sum(list(map(int, list(str(i)))))
    max_sum = max(sum_, max_sum)

print(max_sum)