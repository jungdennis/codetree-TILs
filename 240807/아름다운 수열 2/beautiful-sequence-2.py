n, m = map(int, input().split())
A = list(map(int, input().split()))
B = set(map(int, input().split()))

cnt = 0
for i in range(n-m+1):
    A_part = set(A[i:i+m])

    if A_part == B:
        cnt += 1

print(cnt)