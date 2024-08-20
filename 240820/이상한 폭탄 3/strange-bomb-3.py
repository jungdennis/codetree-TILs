n, k = map(int, input().split())

arr = []
bomb_num = []
for i in range(n):
    bomb = int(input())
    arr.append(bomb)
    if bomb not in bomb_num:
        bomb_num.append(bomb)

max_cnt = 0
max_num = 0

for b in bomb_num:
    boom = [0] * (n + 1)
    bomb = []
    for i in range(len(arr)):
        if arr[i] == b:
            bomb.append(i)

    for i in range(len(bomb)-1):
        if bomb[i+1] - bomb[i] <= k:
            boom[i] = 1
            boom[i+1] = 1
    
    cnt = sum(boom)
    
    if cnt != 0 and cnt >= max_cnt:
        max_cnt = cnt
        max_num = max(b, max_num)

print(max_num)