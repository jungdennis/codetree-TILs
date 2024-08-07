import sys

equ = input()

max_result = - sys.maxsize
alpha = ['a', 'b', 'c', 'd', 'e', 'f']
num = []
char = []
symbol = []
for c in equ:
    if c in ['+', '-', '*']:
        symbol.append(c)
    else:
        char.append(c)

def calc(x):
    if x >= 6:
        global max_result
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