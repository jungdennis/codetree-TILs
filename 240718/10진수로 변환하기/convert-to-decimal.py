binary = input()
ans = 0

for c in binary:
    c = int(c)
    ans = ans * 2 + c

print(ans)