A, B, x, y = map(int, input().split())

# 순간이동 없이 : A -> B
ans1 = abs(B - A)

# x -> y 순간이동 : A -> x, y -> B
ans2 = abs(A - x) + abs(B - y)

# y -> x 순간이동 : A -> y, x -> B
ans3 = abs(A - y) + abs(B - x)

print(min(ans1, ans2, ans3))