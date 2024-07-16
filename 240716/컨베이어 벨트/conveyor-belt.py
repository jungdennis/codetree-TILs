import sys

n, t = map(int, sys.stdin.readline().rstrip().split())
arr = []
for i in range(2):
    arr += list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(t):
    temp = arr[-1]
    arr = [temp] + arr[:-1]

arr_up = arr[:n]
arr_down = arr[n:]

for n in arr_up:
    print(n, end=" ")
print()
for n in arr_down:
    print(n, end=" ")