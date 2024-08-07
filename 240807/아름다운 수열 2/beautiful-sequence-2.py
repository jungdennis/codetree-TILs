n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B.sort()

cnt = 0
for i in range(n-m+1):
    A_part = A[i:i+m]
    A_part.sort()

    if A_part == B:
        cnt += 1

print(cnt)