import sys

n, t = map(int, sys.stdin.readline().rstrip().split())

belt = []
for i in range(3):
    belt += list(map(int, sys.stdin.readline().rstrip().split()))

temp = 0
for i in range(t):
    temp = belt[-1]
    belt = [temp] + belt[:-1]

for i in range(3):
    for j in range(n):
        print(belt[n*i+j], end=' ')
    print()