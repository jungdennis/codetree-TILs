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
    check = [0] * (max_num+1)

    for x1, x2 in s:
        for i in range(x1, x2+1):
            check[i] += 1

            if check[i] > 1:
                return False
    
    return True

def pick_line(x):
    if x >= n:
        global max_cnt
        set_pick = set(pick)
        
        if detect(set_pick):
            max_cnt = max(max_cnt, len(set_pick))

        return 

    for i in range(n):
        if line[i] not in pick:
            pick.append(line[i])
            pick_line(x+1)
            pick.pop()

pick_line(0)
print(max_cnt)