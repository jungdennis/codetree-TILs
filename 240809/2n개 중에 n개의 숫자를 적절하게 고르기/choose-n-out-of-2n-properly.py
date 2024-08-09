n = int(input())
num = list(map(int, input().split()))
sum_num = sum(num)
arr = []

import sys
min_diff = sys.maxsize
def pick(n_pick, last_idx):
    if n_pick >= n:
        global min_diff
        sum_1 = sum(arr)
        sum_2 = sum_num - sum_1

        diff = abs(sum_1 - sum_2)

        min_diff = min(diff, min_diff)

        return

    for i in range(2*n):
        if i <= last_idx:
            continue

        arr.append(num[i])
        pick(n_pick + 1, i)
        arr.pop()

pick(0, -1)
print(min_diff)