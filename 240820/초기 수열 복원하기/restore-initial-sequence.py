import sys

n = int(input())
arr = list(map(int, input().split()))
picked = []

def pick(x):
    if x >= n:
        ans = []
        for i in range(n-1):
            ans.append(picked[i] + picked[i+1])

        if ans == arr:
            for i in range(n):
                print(picked[i], end=' ')
            sys.exit()

        return

    for i in range(1, n+1):
        if i not in picked:
            picked.append(i)
            pick(x+1)
            picked.pop()

pick(0)
print(ans)