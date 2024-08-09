n = int(input())
max_jump = list(map(int, input().split()))
arr = [0]
location = 0
possible = []

import sys
cnt = sys.maxsize

def jump(x):
    global location
    if location == n-1:
        global cnt
        cnt = min(cnt, x)
        possible.append(x)
        
        return

    if x >= n-2:
        return

    for dx in range(max_jump[location]+1):
        location += dx
        arr.append(location)
        jump(x+1)
        location -= dx
        arr.pop()

# if cnt == sys.maxsize:
#     cnt = -1
jump(0)
if len(possible) == 0:
    print(-1)
else:
    print(min(possible))