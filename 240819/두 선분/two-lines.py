x1, x2, x3, x4 = map(int, input().split())

if max(x1, x3) <= min(x2, x4):
    print('intersecting')
else:
    print('nonintersecting')