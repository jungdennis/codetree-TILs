import sys
n, k = map(int, input().split())

bomb = []
max_size = -sys.maxsize

for i in range(n):
    b = int(input())
    bomb.append(b)
    max_num = max(b, max_size)

max_num = -1
for i in range(len(bomb)):
    for j in range(i+1, len(bomb)):
        if bomb[i] == bomb[j] and abs(i - j) <= k:
            max_num = max(bomb[i], max_num)
print(max_num)