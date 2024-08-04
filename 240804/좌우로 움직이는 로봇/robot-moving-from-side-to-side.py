n, m = map(int, input().split())

move_A = [0]
move_B = [0]

for i in range(n):
    t, d = input().split()

    if d == 'L':
        sign = -1
    elif d == 'R':
        sign = +1

    t = int(t)
    for j in range(t):
        move_A.append(move_A[-1] + sign)

for i in range(m):
    t, d = input().split()

    if d == 'L':
        sign = -1
    elif d == 'R':
        sign = +1

    t = int(t)
    for j in range(t):
        move_B.append(move_B[-1] + sign)

n_A = len(move_A)
n_B = len(move_B)

if n_A < n_B:
    move_A += [move_A[-1]] * (n_B - n_A)
elif n_A > n_B:
    move_B += [move_B[-1]] * (n_A - n_B)

cnt = 0
for i in range(1, len(move_B)):
    if (move_A[i-1] != move_B[i-1]) and(move_A[i] == move_B[i]):
        cnt += 1

print(cnt)