n = int(input())
arr = []

def sign(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1

for i in range(n):
    arr.append(int(input()))

max_cnt = 0
cnt = 0
temp = 0
for i in range(n):
    s_ = sign(arr[i])

    if temp == s_:
        cnt += 1
    else:
        cnt = 1
        temp = s_

    max_cnt = max(cnt, max_cnt)

print(max_cnt)