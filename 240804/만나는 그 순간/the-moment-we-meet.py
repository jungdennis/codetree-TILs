n, m = map(int, input().split())

move_A = [0]
move_B = [0]

for i in range(n):
    d, t = input().split()
    t = int(t)

    if d == 'L':
        sign = -1
    elif d == 'R':
        sign = +1

    for j in range(t):
        move_A.append(move_A[-1] + sign)

for j in range(m):
    d, t = input().split()
    t = int(t)

    if d == 'L':
        sign = -1
    elif d == 'R':
        sign = +1
    
    for j in range(t):
        move_B.append(move_B[-1] + sign)

ans = -1
for i in range(1, min(len(move_A), len(move_B))):
    if move_A[i] == move_B[i]:
        ans = i
        break

print(ans)