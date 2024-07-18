N, B = map(int, input().split())
ans = []
while 1:
    ans.append(N % B)
    N = N // B

    if N <= 0:
        break

for i in ans[::-1]:
    print(i, end='')