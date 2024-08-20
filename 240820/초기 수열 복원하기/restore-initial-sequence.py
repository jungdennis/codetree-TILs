n = int(input())
arr = list(map(int, input().split()))

for i in range(1, arr[0]+1):
    picked = []
    picked.append(i)

    for s in arr:
        picked.append(s - picked[-1])

    if sorted(picked) == list(range(1, n+1)):
        for x in picked:
            print(x, end=' ')

        break