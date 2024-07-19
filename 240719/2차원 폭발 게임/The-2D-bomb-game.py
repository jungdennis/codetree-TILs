import sys:
n, m, k = map(int, sys.stdin.readline().rstrip().split())

def drop(arr, padding=False):
    temp = []
    for i in range(len(arr)):
        if arr[i] != 0:
            temp.append(arr[i])

    if padding:
        return temp + [0 for i in range(n - len(temp))]
    else:
        return temp

def boom(arr):
    while 1:
        boom_ = False
        boom_idx = [0]
        cnt = 1
        temp = arr[0]

        for i in range(1, len(arr)):
            if temp == arr[i]:
                cnt += 1
                boom_idx.append(i)
            else:
                if cnt >= m:
                    for j in boom_idx:
                        arr[j] = 0
                    boom_ = True
                cnt = 1
                boom_idx = [i]
                temp = arr[i]
        
        if boom_:
            arr = drop(arr, False)
        else:
            break

        if len(arr) == 0:
            break

    return drop(arr, True)

def rotate(arr):
    for r in range(n):
        foc c in range(n):
            # 돌리는 코드

    for j in range(n):
        temp = []
        for i in range(n-1, -1, -1):
            temp.append(arr[i][j])

        temp = drop(temp, True)

        for i in range(n-1, -1, -1):
            arr[i][j] = temp[n-1-i]

    return arr

arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

for _ in range(k):
    for j in range(n):
        temp = []
        for i in range(n-1, -1, -1):
            temp.append(arr[i][j])

        temp = boom(temp)

        for i in range(n-1, -1, -1):
            arr[i][j] = temp[n-1-i]

        arr = rotate(arr)

for j in range(n):
    temp = []
    for i in range(n-1, -1, -1):
        temp.append(arr[i][j])

    temp = boom(temp)

    for i in range(n-1, -1, -1):
        arr[i][j] = temp[n-1-i]

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()