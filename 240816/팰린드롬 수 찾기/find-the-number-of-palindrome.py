X, Y = map(int, input().split())

cnt = 0
for n in range(X, Y+1):
    n_str = str(n)

    for i in range(len(n_str) // 2):
        flag = True

        if n_str[i] != n_str[len(n_str)-1-i]:
            flag = False
            break

    if flag:
        cnt += 1

print(cnt)