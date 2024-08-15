import sys

N, M, D, S = map(int, input().split())

eat_record = []
for i in range(D):
    p, m, t = map(int, input().split())
    eat_record.append((p, m, t))
# eat_record.sort(key=lambda x:x[2])

ill_record = []
for i in range(S):
    p, t = map(int, input().split())
    ill_record.append((p, t))
# ill_record.sort(key=lambda x:x[1])

bad_cheese = [0] * (M + 1)
for m in range(1, M+1):
    flag = 0

    for p, t in ill_record:
        for p_, m_, t_ in eat_record:
            if p == p_ and m == m_ and t_ < t:
                flag += 1
    
    if flag == len(ill_record):
        bad_cheese[m] = 1

max_cnt = -sys.maxsize
for m in range(1, M+1):
    ill_person = [0] * (N + 1)
    for p, m, t in eat_record:
        if bad_cheese[m] == 1:
            ill_person[p] = 1
    cnt = sum(ill_person)
    max_cnt = max(cnt, max_cnt)

print(sum(ill_person))