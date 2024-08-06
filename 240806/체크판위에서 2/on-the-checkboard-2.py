R, C = map(int, input().split())

arr = []
for i in range(R):
    arr.append(input().split())

cnt = 0
for r in range(R):
    for c in range(C):
        color = [arr[0][0]]

        if arr[r][c] != color[-1] and r > 0 and c > 0:
            color.append(arr[r][c])

            for r_ in range(r+1, R):
                for c_ in range(c+1, C):
                    if arr[r_][c_] != color[-1] and arr[r_][c_] != arr[R-1][C-1] and r_ < R-1 and c_ < C-1:
                        cnt += 1
                        # print((r, c), (r_, c_))

print(cnt)