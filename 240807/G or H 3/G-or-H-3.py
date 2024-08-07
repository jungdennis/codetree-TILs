n, k = map(int, input().split())

arr = [0] * 10001
for i in range(n):
    n, s = input().split()
    arr[int(n)] = s

import sys
max_score = -sys.maxsize
for i in range(1, 10001-(k+1)+1):
    score = 0
    for j in range(k+1):
        if arr[i+j] == 'G':
            score += 1
        elif arr[i+j] == 'H':
            score += 2

    max_score = max(max_score, score)

print(max_score)