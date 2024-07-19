import sys

n, m  = map(int, sys.stdin.readline().rstrip().split())

arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))


for k in range(m):
    c = int(sys.stdin.readline().rstrip())
    c -= 1

    for r in range(n):
        power = arr[r][c]
        
        if power == 0:
            pass
        else:
            for i in range(power):
                for sign in [-1, 1]:
                    dr = i * sign
                    if (r+dr >= 0) and (r+dr < n):
                        arr[r+dr][c] = 0
                    
                    dc = i * sign
                    if (c+dc >= 0) and (c+dc < n):
                        arr[r][c+dc] = 0

            for j in range(n):
                temp = []
                
                for i in range(n-1, -1, -1):
                    if arr[i][j] != 0:
                        temp.append(arr[i][j])

                temp = temp + [0 for i in range(n - len(temp))]

                for i in range(n-1, -1, -1):
                    arr[i][j] = temp[n-1-i]

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()