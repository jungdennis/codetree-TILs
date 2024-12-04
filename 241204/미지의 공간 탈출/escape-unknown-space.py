# 동, 서, 남, 북
dr = []
dc = []

N, M, F = map(int, input().split())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

wall = [[] for i in range(5)]
for i in range(5):
    for j in range(M):
        wall[i].append(list(map(int, input().split())))

abnormal = []
for i in range(F):
    abnormal.append(list(map(int, input().split())))

# 시간의 벽 2D 화
wall_2d = [[0 for i in range(3 * M)] for j in range(3 * M)]

for i in range(M):
    for j in range(M):
        wall_2d[i][j] = 1
    
    for j in range(2*M, 3*M):
        wall_2d[i][j] = 1

for i in range(2*M, 3*M):
    for j in range(M):
        wall_2d[i][j] = 1
    
    for j in range(2*M, 3*M):
        wall_2d[i][j] = 1
  
for i in range(M):
    for j in range(M):
        wall_2d[i][j+M] = wall[3][i][j]
        wall_2d[i+M][j] = wall[1][i][j]
        wall_2d[i+M][j+M] = wall[4][i][j]
        wall_2d[i+M][j+2*M] = wall[0][i][j]
        wall_2d[i+2*M][j+M] = wall[2][i][j]

for i in range(len(wall_2d)):
    print(wall_2d[i])

# wall_2D 탈출구 찾기
r, c = -1, -1
for i in range(N):
    for j in range(N):
        if arr[i][j] == 3:
            r, c = i, j
            break

    if r != -1 and c != -1:
        break

print(r, c)
for i in range(r-1, r)
