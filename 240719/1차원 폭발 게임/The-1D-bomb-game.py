import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

while 1:
    if len(arr) == 0:
        break

    boom = False
    boom_idx = [0]
    memory = arr[0]
    cnt = 1
    for i in range(1, len(arr)):
        if arr[i] == memory:
            boom_idx.append(i)
            cnt += 1
            memory = arr[i]
        else:
            if cnt >= m:
                boom = True
                for j in boom_idx:
                    arr[j] = 0
            
            cnt = 1
            memory = arr[i]
            boom_idx = [i]
    
    if cnt >= m:
        boom = True
        for j in boom_idx:
            arr[j] = 0

    if boom:
        temp = []
        for a in arr:
            if a != 0:
                temp.append(a)
        arr = temp
    else:
        break

print(len(arr))
for a in arr:
    print(a)