n = int(input())
dot = []
for i in range(n):
    x, y = map(int, input().split())
    dot.append((x, y, i+1))

dot.sort(key=lambda x : (abs(x[0]) + abs(x[1]), x[2]))

for d in dot:
    print(d[2])