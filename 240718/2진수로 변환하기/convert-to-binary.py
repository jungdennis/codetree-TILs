n = int(input())
ans = []

while n > 0 :
    ans.append(n % 2)
    n = n // 2

for a in ans[::-1]:
    print(a, end ='')