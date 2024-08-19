n = int(input())

arr = []
for i in range(n):
    start, end = map(int, input().split())
    arr.append((start, end))

ans = 1
while True:
    flag = True
    x = ans

    for a, b in arr:
        x *= 2
        if x < a or x > b:
            flag = False
            break

    if flag:
        break
    else:
        ans += 1

print(ans)