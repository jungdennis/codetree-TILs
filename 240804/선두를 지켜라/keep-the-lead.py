n, m = map(int, input().split())

move_A = [0]
move_B = [0]

for i in range(n):
    v, t = map(int, input().split())

    for j in range(t):
        move_A.append(move_A[-1] + v)

for i in range(m):
    v, t = map(int, input().split())

    for j in range(t):
        move_B.append(move_B[-1] + v)

first = 0
cnt = 0
for i in range(1, len(move_A)):
    if move_A[i] > move_B[i]:
        if first == 'B':
            cnt += 1

        first = 'A'
    elif move_A[i] < move_B[i]:
        if first == 'A':
            cnt += 1

        first = 'B'

print(cnt)