LENGTH = 1000 * 100
arr = ['g' for i in range(-LENGTH, LENGTH + 1)]
loc = LENGTH
n = int(input())

for i in range(n):
    x, d = input().split()
    x = int(x)

    if d == 'R':    # 오른쪽으로 이동, 검은색
        for j in range(loc, loc+x):
            arr[j] = 'b'
        loc = loc + x - 1

    elif d == 'L':  # 왼쪽으로 이동, 흰색
        for j in range(loc-x+1, loc+1):
            arr[j] = 'w'
        loc = loc - x + 1

black = 0
white = 0
for a in arr:
    if a == "b":
        black += 1
    elif a == "w":
        white += 1

print(white, black)