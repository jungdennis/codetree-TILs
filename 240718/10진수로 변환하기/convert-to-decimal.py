binary = list(map(int, list(input())))
ans = 0

for c in binary:
    ans = ans * 2 + c

print(ans)