arr = []
player = []
for i in range(3):
    row = list(map(int, list(input())))
    arr.append(row)

    for j in row:
        if j not in player:
            player.append(j)

cnt = 0
for i in range(len(player)):
    for j in range(i+1, len(player)):
        team = set([player[i], player[j]])
        # print(f"<{team}>")

        flag = False
        for r in range(3):
            # print(set([arr[r][0], arr[r][1], arr[r][2]]))
            if set([arr[r][0], arr[r][1], arr[r][2]]) == team:
                flag = True

        for c in range(3):
            # print(set([arr[0][c], arr[1][c], arr[2][c]]))
            if set([arr[0][c], arr[1][c], arr[2][c]]) == team:
                flag = True

        # print(set([arr[0][0], arr[1][1], arr[2][2]]))
        if set([arr[0][0], arr[1][1], arr[2][2]]) == team:
            flag = True

        # print(set([arr[0][2], arr[1][1], arr[2][0]]))
        if set([arr[0][2], arr[1][1], arr[2][0]]) == team:
            flag = True

        if flag:
            cnt += 1

print(cnt)