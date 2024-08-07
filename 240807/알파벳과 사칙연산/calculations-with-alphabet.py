equ = input()

alpha = []
char = []
symbol = []
for c in equ:
    if c in ['+', '-', '*']:
        symbol.append(c)
    else:
        char.append(c)
        if c not in alpha:
            alpha.append(c)

alpha.sort()
# print(alpha)
# print(char)
# print(symbol)

num = []
max_result = 0
def calc(x):
    if x >= len(alpha):
        global max_result

        for c in equ:
            result = num[alpha.index(char[0])]

            for i in range(len(symbol)):
                n = num[alpha.index(char[i+1])]
                if symbol[i] == '+':
                    result += n
                elif symbol[i] == '-':
                    result -= n
                elif symbol[i] == '*':
                    result *= n

            max_result = max(max_result, result)

        return

    for i in range(1, 5):
        num.append(i)
        calc(x+1)
        num.pop()

calc(0)
print(max_result)