n = int(input())

arr = []
visited = [0] * (n+1)
def pick(last_pick):
    if len(arr) >= n:
        for j in arr:
            print(j, end=' ')
        print()

        return

    for i in range(1, n+1):
        if visited[i] == 1:
            continue

        arr.append(i)
        visited[i] = 1

        pick(i)
        
        arr.pop()
        visited[i] = 0

pick(0)