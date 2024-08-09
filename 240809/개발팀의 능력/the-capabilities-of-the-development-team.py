power = list(map(int, input().split()))
max_power = sum(power)

import sys
min_diff = sys.maxsize
for i in range(5):
    sum_1 = power[i]

    for j in range(5):
        for k in range(j+1, 5):
            if i != j and i != k:
                l, m = list(set([0, 1, 2, 3, 4]) - set([i, j, k]))

                sum_2 = power[j] + power[k]
                sum_3 = power[l] + power[m]

                if sum_1 != sum_2 and sum_2 != sum_3 and sum_3 != sum_1:
                    diff = max(sum_1, sum_2, sum_3) - min(sum_1, sum_2, sum_3)
                    # print(power[i], (power[j], power[k]), (power[l], power[m]), diff)
                    min_diff = min(diff, min_diff)

if min_diff == sys.maxsize:
    min_diff = -1
print(min_diff)