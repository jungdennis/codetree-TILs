N, M, C = map(int, input().split())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

location = []
cost = []

for i in range(N):
    for j in range(N-M+1):
        for m in range(1, M+1):
            weight = 0
            c = 0
            for k in range(m):
                weight += arr[i][j+k]
                c += arr[i][j+k] ** 2

            if weight <= C:
                location.append((i, j, m))
                cost.append(c)
# print(location)
# print(cost)
max_cost = 0
steal = []
def overlap(info0, info1):
    r0, c0, len0 = info0
    r1, c1, len1 = info1

    if r0 != r1:
        return False
    else:
        if c0 <= c1:
            min_c = c0
            min_len = len0
            max_c = c1
        else:
            min_c = c1
            min_len = len1
            max_c = c0

        if min_c + min_len <= max_c:
            return False
        else:
            return True

def two_thief(x):
    if x >= 2:
        global max_cost

        r0, c0, len0, cost0 = steal[0]
        r1, c1, len1, cost1 = steal[1]

        if not overlap((r0, c0, len0), (r1, c1, len1)):
            # print((r0, c0, len0), (r1, c1, len1), cost0, cost1)
            max_cost = max(max_cost, cost0+cost1)

        return

    for i in range(len(location)):
        r, c, l = location[i]
        steal.append((r, c, l, cost[i]))
        two_thief(x+1)
        steal.pop()


two_thief(0)
print(max_cost)