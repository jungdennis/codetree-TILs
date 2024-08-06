n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

max_coin = 0
for r in range(n):
    for c in range(n-2):
        coin = arr[r][c] + arr[r][c+1] + arr[r][c+2]

        if coin > max_coin:
            max_coin = coin

print(max_coin)