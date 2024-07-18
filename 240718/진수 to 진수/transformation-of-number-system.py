a, b = map(int, input().split())
n_a = input()

# a진수 -> 10진수
n_a = list(map(int, list(n_a)))
n_10 = 0

for i in n_a:
    n_10 = n_10 * a + i

# 10진수 -> b진수
n_b = []

while 1:
    n_b.append(n_10 % b)
    n_10 = n_10 // b

    if n_10 <= 0:
        break

for i in n_b[::-1]:
    print(i, end='')