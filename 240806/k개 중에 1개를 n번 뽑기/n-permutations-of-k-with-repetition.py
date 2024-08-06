import sys
k, n = map(int, sys.stdin.readline().rstrip().split())

pick = []

def choose(x):
    if x >= n:
        for p in pick:
            print(p, end = ' ')
        print()
        return

    for i in range(1, k+1):
        pick.append(i)
        choose(x+1)
        pick.pop()

choose(0)