power = list(map(int, input().split()))
power_sum = sum(power)

import sys
min_diff = sys.maxsize
for i in range(6):
    for j in range(6):
        for k in range(6):
            for l in range(6):
                if i != j and i != k and i != l and j != k and j != l and k != l:
                    sum_1 = power[i] + power[j]
                    sum_2 = power[k] + power[l]
                    sum_3 = power_sum - sum_1 - sum_2
                    # print((i, j), (k, l), sum_1, sum_2, sum_3)

                    diff = max(sum_1, sum_2, sum_3) - min(sum_1, sum_2, sum_3)
                    min_diff = min(diff, min_diff)

print(min_diff)