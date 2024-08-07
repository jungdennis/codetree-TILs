n = int(input())

line = []
max_num = 0
for i in range(n):
    x1, x2 = list(map(int, input().split()))
    line.append((x1, x2))
    max_num = max(max_num, x2)

pick = []
max_cnt = 0

def detect(s):
    x1, x2 = s[-1]

    for start, end in s[:-1]:
        if x1 <= end:
            return False
    
    return True

def pick_line(x):
    global max_cnt
    
    if len(pick) != 0:
        if detect(pick):
            max_cnt = max(max_cnt, len(pick))
        else:
            return 

    if x >= n:
        return 

    for i in range(n):
        # 선분을 넣었을 경우
        pick.append(line[i])
        pick_line(x+1)
        
        # 선분을 뺐을 경우
        pick.pop()
        pick_line(x+1)

pick_line(0)
print(max_cnt)