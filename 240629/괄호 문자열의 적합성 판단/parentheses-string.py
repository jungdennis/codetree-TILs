order = input()
s = []

for c in order:
    if c == '(':
        s.append(c)
    else:
        if len(s) == 0:
            s.append(c)
        else:
            if s[-1] == '(':
                s.pop()
            else:
                s.append(c)

if len(s) != 0:
    print('No')
else:
    print('Yes')