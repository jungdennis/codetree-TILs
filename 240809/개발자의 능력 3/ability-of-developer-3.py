power = list(map(int, input().split()))
power_sum = sum(power)

import sys
min_diff = sys.maxsize

for i in range(6):
    for j in range(i+1, 6):
        for k in range(j+1, 6):
            p = power[i] + power[j] + power[k]
            p_ = power_sum - p

            diff = abs(p - p_)
            min_diff = min(diff, min_diff)

print(min_diff)