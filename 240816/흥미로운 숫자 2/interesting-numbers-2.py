X, Y = map(int, input().split())

n_cnt = 0
for n in range(X, Y+1):
    num = []
    cnt = []

    n_str = str(n)

    for c in n_str:
        if c not in num:
            num.append(c)
            cnt.append(1)
        else:
            idx = num.index(c)
            cnt[idx] += 1

    if len(num) == 2 and (cnt == [1, len(n_str)-1] or cnt == [len(n_str)-1, 1]):
        n_cnt += 1

print(n_cnt)