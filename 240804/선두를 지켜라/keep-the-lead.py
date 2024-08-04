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

first = []
def find_first(t):
    if move_A[t] > move_B[t]:
        return 'A'
    elif move_A[t] < move_B[t]:
        return 'B'
    else:
        return first[-1]

for i in range(1, len(move_A)):
    first.append(find_first(i))

cnt = 0
for i in range(len(first)-1):
    if first[i] != first[i+1]:
        cnt += 1

print(cnt)