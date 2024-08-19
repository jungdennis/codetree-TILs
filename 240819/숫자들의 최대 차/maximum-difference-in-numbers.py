n, k = map(int, input().split())

arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()

ans = []
for i in range(n):
    for j in range(i+1, n):
        if arr[j] - arr[i] <= k:
            ans.append(abs(j-i+1))

print(max(ans))