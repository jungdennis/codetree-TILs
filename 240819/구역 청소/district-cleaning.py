a, b = map(int, input().split())
c, d = map(int, input().split())

if b < c or d < a:
    print(abs(a-b) + abs(c-d))
else:
    print(abs(max(b, d) - min(a, c)))