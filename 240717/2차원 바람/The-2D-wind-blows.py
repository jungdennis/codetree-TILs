import sys

n, m, q = map(int, sys.stdin.readline().rstrip().split())

arr = []

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 2 2 4 6
def wind(r1, c1, r2, c2):
    # 경계면 시계방향 회전
    # (r1, c1) -> (r2, c1)
    temp = arr[r1][c1]
    for i in range(r1, r2):
        arr[i][c1] = arr[i+1][c1]
    # (r2, c1) -> (r2, c2)
    for i in range(c1, c2):
        arr[r2][i] = arr[r2][i+1]
    # (r2, c2) -> (r1, c2)
    for i in range(r2, r1, -1):
        arr[i][c2] = arr[i-1][c2]
    # (r1, c2) -> (r1, c1)
    for i in range(c2, c1+1, -1):
        arr[r1][i] = arr[r1][i-1]
    arr[r1][c1+1] = temp
    
    # 모든 원소 평균값으로 대체
    memory = [[0 for i in range(m)] for j in range(n)]
    delta = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]

    for r in range(r1, r2+1):
        for c in range(c1, c2+1):
            num_list = []

            for dr, dc in delta:
                r_new = r + dr
                c_new = c + dc

                if (r_new >= 0) and (r_new < n) and (c_new >= 0) and (c_new < m):
                    num_list.append(arr[r_new][c_new])
            
            memory[r][c] = int(sum(num_list) / len(num_list))

    for r in range(r1, r2+1):
        for c in range(c1, c2+1):
            arr[r][c] = memory[r][c]


for t in range(q):
    r1, c1, r2, c2 = map(int, sys.stdin.readline().rstrip().split())
    wind(r1-1, c1-1, r2-1, c2-1)

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()