N = int(input())
arr = list(map(int, input().split()))
arr.sort()

m = 0
for i in range(N):
    m_ = arr[i] + arr[2*N-1-i]
    if m_ >= m:
        m = m_

print(m)