import sys

n = int(input())

case = []
for i in range(n):
    a, b, c = map(int, input().split())
    case.append((a, b, c))

stone = [0] * 4
max_score = -sys.maxsize
max_idx = 0
for i in range(1, 4):
    stone[i] = 1
    score = 0
    for a, b, c in case:
        stone[a], stone[b] = stone[b], stone[a]
        
        if stone[c] == 1:
            score += 1

    if score > max_score:
        max_score = score
        max_idx = i

print(max_idx)