import sys

A, B, C = map(int, input().split())

max_result = -sys.maxsize
for i in range(1001):
    for j in range(1001):
        result = A * i + B * j
        if result <= C:
            max_result = max(result, max_result)

print(max_result)