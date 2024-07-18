LENGTH = 1000 * 100
arr = [[0, 0, 0] for i in range(-LENGTH, LENGTH+1)]
loc = LENGTH

n = int(input())
# 1: 검, 2: 흰

for i in range(n):
    x, d = input().split()
    x = int(x)

    if d == 'R':    # 오른쪽 - 검정
        for j in range(loc, loc+x):
            arr[j][0] += 1
            arr[j][2] = 'black'
        loc = loc + x
    elif d == 'L':  # 왼쪽 - 흰색
        for j in range(loc-x, loc):
            arr[j][1] += 1
            arr[j][2] = 'white'
        loc = loc - x

black = 0
white = 0
gray = 0
for a in arr:
    if (a[0] >= 2) and (a[1] >= 2):
        gray += 1
    else:
        if a[-1] == 'black':
            black += 1
        elif a[-1] == 'white':
            white += 1

print(white, black, gray)