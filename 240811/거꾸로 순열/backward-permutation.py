n = int(input())

arr = []
visited = [0] * (n+1)
def pick(last_num):
    if len(arr) >= n:
        for a in arr:
            print(a, end = ' ')
        print()

        return 

    for i in range(n, 0, -1):
        if visited[i] == 1:
            continue

        arr.append(i)
        visited[i] = 1

        pick(i)

        arr.pop()
        visited[i] = 0

pick(0)