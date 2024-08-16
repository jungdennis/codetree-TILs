import sys

n = int(input())

height = []
for i in range(n):
    height.append(int(input()))

max_cnt = -sys.maxsize
for th in range(1, 1002):
    cnt = 0
    flag = False

    for h in height:
        if h > th:
            if not flag:
                cnt += 1
            flag = True
        else:
            flag = False

    max_cnt = max(cnt, max_cnt)    

print(max_cnt)