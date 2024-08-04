n, m, k = map(int, input().split())

penalty = [-1] + [0 for i in range(n)]

fine = -1
for i in range(m):
    num = int(input())

    penalty[num] += 1

    if penalty[num] >= k:
        fine = num
        break

print(fine)