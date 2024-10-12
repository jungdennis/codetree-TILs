from collections import deque

L, Q = map(int, input().split())

belt = deque(deque() for i in range(L))
table = [[0, 0] for i in range(L)]

now_time = 0

def eating():
    global belt, table

    for i in range(L):
        name, n = table[i]
        if name != 0 and name in belt[i]:
            while name in belt[i]:
                sushi = belt[i].popleft()
                if sushi != name:
                    belt[i].append(sushi)
                else:
                    table[i][-1] -= 1
                    if table[i][-1] == 0:
                        break
    
    for i in range(L):
        if table[i][0] != 0 and table[i][-1] == 0:
            table[i] = [0, 0]

for _ in range(Q):
    order = input().split()

    dt = int(order[1]) - now_time
    for i in range(dt):
        belt.appendleft(belt.pop())

    if order[0] == '100':
        _, t, x, name = order
        x = int(x)
        
        belt[x].append(name)

        eating()
    elif order[0] == '200':
        _, t, x, name, n = order
        x = int(x)
        n = int(n)

        table[x] = [name, n]

        eating()
    elif order[0] == '300':
        eating()

        n_people = 0
        n_sushi = 0
        for i in range(L):
            if table[i][0] != 0:
                n_people += 1

            n_sushi += len(belt[i])

        print(n_people, n_sushi)

    now_time = int(order[1])
    # if order[0] != '300':
    #     print(now_time, dt, belt, table)
    # else:
    #     print(now_time, dt, belt, table, (n_people, n_sushi))