n = int(input())

line = []
for i in range(n):
    a, b = map(int, input().split())
    line.append((a, b))

cnt = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            overlap = [0] * 101

            for l in range(n):
                if l == i or l == j or l == k:
                    continue

                start, end = line[l]
                for m in range(start, end+1):
                    overlap[m] += 1

            flag = 1
            for o in overlap:
                if o >= 2:
                    flag = 0
                    break

            cnt += flag

print(cnt)