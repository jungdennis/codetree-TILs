n = int(input())

line = []
for i in range(n):
    start, end = map(int, input().split())
    line.append((start, end))

flag = True
for i in range(n):
    for j in range(i+1, n):
        a1, a2 = line[i]
        b1, b2 = line[j]

        if a2 < b1 or b2 < a1:
            flag = False

if flag:
    print('Yes')
else:
    print('No')