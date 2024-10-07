import sys

N, M, P, C, D = map(int, sys.stdin.readline().rstrip().split())

arr = [[0 for i in range(N)] for j in range(N)]

r_r, r_c = map(int, sys.stdin.readline().rstrip().split())
r_r -= 1
r_c -= 1
arr[r_r][r_c] = 'R'

santa = []
for i in range(P):
    s_p, s_r, s_c = map(int, sys.stdin.readline().rstrip().split())
    santa.append([s_p, s_r-1, s_c-1, 0, 0])
    arr[s_r-1][s_c-1] = s_p
santa.sort(key=lambda x:x[0])

for i in range(N):
    print(arr[i])

def in_range(r, c):
    return r >= 0 and r < N and c >= 0 and c < N

def move_r(r, c, t_r, t_c):
    delta_r = t_r - r
    delta_c = t_c - c

    if delta_r > 0:
        dr = 1
    elif delta_r < 0:
        dr = -1
    else:
        dr = 0
    
    if delta_c > 0:
        dc = 1
    elif delta_c < 0:
        dc = -1
    else:
        dc = 0

    return dr, dc

def move_s(r, c, r_r, r_c):
    dist_before = (r - r_r) ** 2 + (c - r_c) ** 2
    dist = []
    for dr, dc, order in [(-1, 0, 1), (0, 1, 2), (1, 0, 3), (0, -1, 4)]:
        nr, nc = r + dr, c + dc
        
        if in_range(nr, nc) and (arr[nr][nc] == 0 or arr[nr][nc] == 'R'):
            dist_after = (nr - r_r) ** 2 + (nc - r_c) ** 2

            if dist_before > dist_after:
                dist.append((dist_after, order, dr, dc))

    if dist:
        dist.sort(key=lambda x:(x[0], x[1]))
        _, __, dr, dc = dist[0]
        return dr, dc
    else:
        return 0, 0

for stage in range(1, M+1):
    print(f"<Stage {stage}>")
    # 루돌프 이동
    print('루돌프 턴')
    print(r_r, r_c)
    distance = []

    for p, r, c, stun, score in santa:
        if in_range(r, c):
            dist = (r - r_r) ** 2 + (c - r_c) ** 2
            distance.append((p, dist, r, c))
    
    distance.sort(key=lambda x:(x[1], -x[1], -x[2]))
    print(distance)

    t_p, t_d, t_r, t_c = distance[0]

    dr, dc = move_r(r_r, r_c, t_r, t_c)
    r_nr = r_r + dr
    r_nc = r_c + dc

    # 충돌여부 체크
    if arr[r_nr][r_nc] != 0 and arr[r_nr][r_nc] != 'R':
        santa[t_p-1][-1] += C
        santa[t_p-1][-2] = stage

        t_nr = t_r + dr * C
        t_nc = t_c + dc * C

        # 상호작용 stack 작성
        relation = [(t_p, t_nr, t_nc)]
        r, c = t_r, t_c
        while arr[r][c] != 0:
            p = arr[r][c]
            nr, nc = r + dr, c + dc
            relation.append((p, r, c))
            r, c = nr, nc

            if not in_range(r, c):
                break

        # 상호작용 결과 반영
        for p, r, c in relation:
            santa[p-1][1] = r
            santa[p-1][2] = c
            
            if in_range(r, c):
                arr[r][c] = p

    arr[r_r][r_c] = 0
    arr[r_nr][r_nc] = 'R'

    r_r, r_c = r_nr, r_nc

    for i in range(N):
        print(arr[i])

    # 산타 이동
    for s_p, s_r, s_c, s_stun, s_score in santa:
        if not in_range(s_r, s_c):
            print(f"{s_p}번 산타 out")
            for i in range(N):
                print(arr[i])
            continue

        if s_stun != 0 and stage - s_stun < 2:
            print(f"{s_p}번 산타 stun")
            for i in range(N):
                print(arr[i])
            continue

        if in_range(s_r, s_c):
            dr, dc = move_s(s_r, s_c, r_r, r_c)
            s_nr = s_r + dr
            s_nc = s_c + dc

            relation = []

            print(f"{s_p}번 산타 턴 {s_nr, s_nc}")

            if arr[s_nr][s_nc] == 'R':
                santa[s_p-1][-1] += D
                santa[s_p-1][-2] = stage

                s_nr = s_nr - dr * D
                s_nc = s_nc - dc * D

                if in_range(s_nr, s_nc) and arr[r][c] != 0:
                    r, c = s_nr, s_nc
                    while True:
                        if not in_range(r, c) or arr[r][c] == 0:
                            break
                        
                        p = arr[r][c]
                        nr, nc = r - dr, c - dc
                        relation.append((p, r, c)) 

                        r, c = nr, nc
                        if len(relation) == 10:
                            print(relation)
                            break

            if not relation:
                relation.append((s_p, s_nr, s_nc))
            print(relation)
            # 상호작용 결과 반영된 산타이동
            while relation:
                p, r, c = relation.pop()
                santa[p-1][1] = r
                santa[p-1][2] = c
                
                if in_range(r, c):
                    arr[r][c] = p

                if in_range(s_nr, s_nc):
                    arr[s_nr][s_nc] = s_p

            arr[s_r][s_c] = 0

        
        for i in range(N):
            print(arr[i])
            
    # 생존자 점수 부여
    score = []
    stun = []
    for s_p, s_r, s_c, s_stun, s_score in santa:
        if in_range(s_r, s_c):
            s_score += 1

        score.append(s_score)
        stun.append(s_stun)
    
    print(f"score : {score}")
    print(f'stun : {stun}')
    print(santa)