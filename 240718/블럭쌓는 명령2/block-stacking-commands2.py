N, k = map(int, input().split())

block = [-1] + [0 for i in range(N)]

for i in range(k):
    a, b = map(int, input().split())

    for j in range(a, b+1):
        block[j] += 1

print(max(block))