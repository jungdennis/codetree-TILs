n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

temp = arr[0]
cnt = 1
max_cnt = 1
for i in range(1, n):
    if temp == arr[i]:
        cnt += 1
    else:
        cnt = 1
        temp = arr[i]

    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)