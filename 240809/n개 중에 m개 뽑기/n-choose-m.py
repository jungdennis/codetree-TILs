n, m = map(int, input().split())
arr = []

def pick(n_pick, last_num):
    if n_pick >= m:
        for num in arr:
            print(num, end = ' ')
        print()

        return

    for i in range(1, n+1):
        if i <= last_num:
            continue

        arr.append(i)
        pick(n_pick+1, i)
        arr.pop()

pick(0, 0)