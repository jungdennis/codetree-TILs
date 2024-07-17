n = int(input())
arr = list(map(int, input().split()))
arr_ = []

for i in range(n):
    arr_.append((arr[i], i+1))

arr_.sort(key=lambda x : (x[0], x[1]))

ans = [0 for i in range(n)]

for i in range(len(arr_)):
    ans[arr_[i][1]-1] = i+1

for n in ans:
    print(n, end=' ')