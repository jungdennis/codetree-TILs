n = int(input())
max_jump = list(map(int, input().split()))

debug = [1]
location = 1
cnt = n+1

def jump(x):
    global location, cnt

    if location == n:
        cnt = min(cnt, x)
        return

    if x >= n:
        return

    for i in range(1, max_jump[x]+1):
        location += i
        jump(x+1)
        location -= i

jump(0)
print(cnt)