n, m = map(int, input().split())
num = list(map(int, input().split()))
arr = []

import sys
max_ans = -sys.maxsize
def pick(n_pick, last_idx):
    if n_pick >= m:
        global max_ans
        
        ans = arr[0]

        for i in range(1, m):
            ans = ans ^ arr[i]

        max_ans = max(ans, max_ans)

    for i in range(n):
        if i <= last_idx:
            continue

        arr.append(num[i])
        pick(n_pick + 1, i)
        arr.pop()

pick(0, -1)
print(max_ans)