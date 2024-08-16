import sys

n = int(input())

case = []
for i in range(n):
    a, b, c = map(int, input().split())
    case.append((a, b, c))

max_score = -sys.maxsize

for i in range(1, 4):
    stone = [0] * 4
    stone[i] = 1
    score = 0

    for a, b, c in case:
        stone[a], stone[b] = stone[b], stone[a]
        
        if stone[c] == 1:
            score += 1

    max_score = max(score, max_score)

print(max_score)