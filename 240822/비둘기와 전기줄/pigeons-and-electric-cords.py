n = int(input())

bird ={}

for i in range(n):
    b, r = map(int, input().split())

    if b not in bird:
        bird[b] = []

    bird[b].append(r)

cnt = 0
for b in bird:
    record = bird[b]

    for i in range(len(record) - 1):
        if record[i] != record[i+1]:
            cnt += 1

print(cnt)