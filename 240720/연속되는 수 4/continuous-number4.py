n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

temp = 9999
cnt = 0
max_cnt = 0

for i in range(n):
    if arr[i] > temp:
        cnt += 1
    else:
        cnt = 1
        
    temp = arr[i]

    max_cnt = max(cnt, max_cnt)

print(max_cnt)