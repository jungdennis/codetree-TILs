n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

max_coin = 0
for r1 in range(n):
    for c1 in range(n-2):

        coin = (arr[r1][c1] + arr[r1][c1+1] + arr[r1][c1+2])

        for r2 in range(n):
            for c2 in range(n-2):
                if r1 == r2 and min(c1, c2) + 2 >= max(c1, c2):
                    continue

                coin += (arr[r2][c2] + arr[r2][c2+1] + arr[r2][c2+2])

                max_coin = max(coin, max_coin)

print(max_coin)