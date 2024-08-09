n = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

def check_dist(x, y, z):
    if min(abs(x-a1), n-abs(x-a1)) <= 2 and min(abs(y-b1), n-abs(y-b1)) <= 2 and min(abs(z-c1), n-abs(z-c1)) <= 2:
        return True
    elif min(abs(x-a2), n-abs(x-a2)) <= 2 and min(abs(y-b2), n-abs(y-b2)) <= 2 and min(abs(z-c2), n-abs(z-c2)) <= 2:
        return True
    else:
        return False

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if check_dist(i, j, k):
                cnt += 1

print(cnt)