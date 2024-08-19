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
    if arr[0] > th or arr[-1] > th:
        flag = False
    else:
        for j in range(len(route)-1):
            if abs(route[j+1] - route[j]) > k:
                flag = False
                break

    if flag:
        ans = min(ans, th)

print(ans)