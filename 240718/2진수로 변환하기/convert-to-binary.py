n = int(input())
ans = []

while 1 :
    ans.append(n % 2)
    n = n // 2

    if n <= 0:
        break

for a in ans[::-1]:
    print(a, end ='')