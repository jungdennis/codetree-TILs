from collections import deque
import copy

K, M = map(int, input().split())

arr = []
for i in range(5):
    arr.append(list(map(int, input().split())))

wall = deque(list(map(int, input().split())))

scores = []

def print_arr(arr):
    for i in range(5):
        print(arr[i])

def in_range(r, c):
    return r >= 0 and r < 5 and c >= 0 and c < 5

def rotate(arr_, r, c, n):
    for i in range(n):
        temp = [arr_[r-1][c-1], arr_[r-1][c]]
        arr_[r-1][c] = arr_[r][c-1]
        arr_[r-1][c-1] = arr_[r+1][c-1]
        arr_[r][c-1] = arr_[r+1][c]
        arr_[r+1][c-1] = arr_[r+1][c+1]
        arr_[r+1][c] = arr_[r][c+1]
        arr_[r+1][c+1] = arr_[r-1][c+1]
        arr_[r][c+1] = temp[1]
        arr_[r-1][c+1] = temp[0]

        # print(i+1)
        # for j in range(5):
        #     print(arr_[j])

    return arr_

def boom(arr_):
    visited = [[0 for i in range(5)] for j in range(5)]
    boomed = []
    q = deque()

    kind = 1
    score = 0
    for i in range(5):
        for j in range(5):
            s = []
            if visited[i][j] == 0:
                q.append((i, j))
                visited[i][j] = kind
                s.append((i, j))

                while q:
                    r, c = q.popleft()
                    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        nr, nc = r + dr, c + dc
                        if in_range(nr, nc) and visited[nr][nc] == 0 and arr_[r][c] == arr_[nr][nc]:
                            q.append((nr, nc))
                            visited[nr][nc] = kind
                            s.append((nr, nc))

                if len(s) >= 3:
                    for r, c in s:
                        boomed.append((r, c))
                    score += len(s)
                kind += 1

    return score, visited, boomed

for _ in range(K):
    score = 0
    arr_case = []
    for r in range(1, 4):
        for c in range(1, 4):
            for n in range(1, 4):
                arr_rotate = rotate(copy.deepcopy(arr), r, c, n)
                s, visited, boomed = boom(arr_rotate)
                # print(r, c, n)
                # for i in range(5):
                #     print(arr_rotate[i])
                arr_case.append((r, c, n, s, arr_rotate, boomed))
    
    arr_case.sort(key=lambda x:(-x[3], x[2], x[1], x[0]))
    best_r, best_c, best_n, best_score, best_arr, boomed = arr_case[0]
    
    # print(best_r, best_c, best_n, best_score)
    # for i in range(5):
    #     print(best_arr[i])
    # print()
    
    if best_score == 0:
        break
    else:
        while True:
            score += best_score
            # print(boomed)
            boomed.sort(key=lambda x: (x[1], -x[0]))
            for r, c in boomed:
                num = wall.popleft()
                best_arr[r][c] = num

            # print_arr(best_arr)

            best_score, visited, boomed = boom(best_arr)

            if best_score == 0:
                break

        arr = best_arr

    if score > 0:
        scores.append(score)

print(" ".join(list(map(str, scores))))

# def test():
#     r = 1
#     c = 2
#     n = 2
#     arr_rotate = rotate(arr, r, c, n)
#     print(r, c, n)
#     for i in range(5):
#         print(arr_rotate[i])
#     s, visited, boomed = boom(arr_rotate)
#     print(s)
#     print_arr(visited)
#     print()
#     for i in range(5):
#         print(boomed[i])

# test()