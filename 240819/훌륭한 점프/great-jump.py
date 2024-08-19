import sys

n, k = map(int, input().split())
arr = list(map(int, input().split()))

ans = sys.maxsize

for i in range(n):
    th = arr[i]
    route = [0]

    for j in range(1, n-1):
        if arr[j] <= th:
            route.append(j)

    route.append(n-1)

    flag = True
    for i in range(len(route)-1):
        if abs(route[i+1] - route[i]) > k:
            flag = False
            break

    if flag:
        ans = min(ans, th)

print(ans)