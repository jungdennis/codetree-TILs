k, n = map(int, input().split())
battle = []
for i in range(k):
    battle.append(list(map(int, input().split())))

cnt = 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            continue
        
        flag = True

        for result in battle:
            a_rank = result.index(a)
            b_rank = result.index(b)

            if a_rank > b_rank:
                flag = False
                break

        if flag:
            cnt += 1

print(cnt)