n = int(input())

arr = list(map(int, input().split()))

min_dist = 99999999999999
for i in range(n):
    distance = 0

    for j in range(n):
        distance += arr[j] * abs(i - j)

    if distance < min_dist:
        min_dist = distance

print(min_dist)