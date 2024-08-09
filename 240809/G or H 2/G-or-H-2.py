n = int(input())
arr = [0] * 101

for i in range(n):
    idx, c = input().split()
    idx = int(idx)

    arr[idx] = c

import sys
max_distance = 0

for i in range(101):
    for j in range(i, 101):
        if arr[i] != 0 and arr[j] != 0:
            cnt_G = 0
            cnt_H = 0

            for c in arr[i:j+1]:
                if c == 'G':
                    cnt_G += 1
                elif c == 'H':
                    cnt_H += 1

            if cnt_G == cnt_H:
                distance = abs(i-j)

                max_distance = max(max_distance, distance)

print(max_distance)