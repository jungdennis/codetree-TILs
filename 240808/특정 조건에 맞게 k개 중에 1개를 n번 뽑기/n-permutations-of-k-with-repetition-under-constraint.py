k, n = map(int, input().split())

num = []

def pick_num(x):
    if x >= n:
        for n_ in num:
            print(n_, end = ' ')
        print()

        return

    for i in range(1, k+1):
        if (len(num) >= 2) and (num[-1] == num[-2]) and (num[-1] == i):
            pass
        else:
            num.append(i)
            pick_num(x+1)
            num.pop()

pick_num(0)