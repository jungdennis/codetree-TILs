N, M, C = map(int, input().split())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

location = []
cost = []

for i in range(N):
    for j in range(N-M+1):
        weight = 0
        c = 0
        thing = []
        for k in range(M):
            thing.append(arr[i][j+k])

        thing.sort(reverse=True)
        for w in thing:
            if weight + w > C:
                pass
            else:
                weight += w
                c += w ** 2

        location.append((i, j))
        cost.append(c)

# for i in range(len(cost)):
#     print(location[i], cost[i])

max_cost = 0
steal = []
def overlap(info0, info1):
    r0, c0 = info0
    r1, c1 = info1

    if r0 != r1:
        return False
    else:
        if min(c0, c1) + M <= max(c0, c1):
            return False
        else:
            return True

def two_thief(x):
    if x >= 2:
        global max_cost

        r0, c0, cost0 = steal[0]
        r1, c1, cost1 = steal[1]

        if not overlap((r0, c0), (r1, c1)):
            if max_cost < cost0 + cost1:
                # print((r0, c0), (r1, c1), cost0, cost1)
                max_cost = max(max_cost, cost0+cost1)

        return

    for i in range(len(location)):
        r, c = location[i]
        steal.append((r, c, cost[i]))
        two_thief(x+1)
        steal.pop()


two_thief(0)
print(max_cost)