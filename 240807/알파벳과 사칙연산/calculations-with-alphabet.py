equ = input()

arr = []
for c in equ:
    if c in ['+', '-', '*']:
        arr.append(c)

num = []
max_result = 0
def calc(x):
    if x >= len(arr)+1:
        global max_result

        result = num[0]

        for i in range(len(arr)):
            if arr[i] == '+':
                result += num[i+1]
            elif arr[i] == '-':
                result -= num[i+1]
            elif arr[i] == '*':
                result *= num[i+1]

        max_result = max(max_result, result)

        return

    for i in range(1, 5):
        num.append(i)
        calc(x+1)
        num.pop()

calc(0)
print(max_result)