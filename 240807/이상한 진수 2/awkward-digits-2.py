num = input()
max_n = 0

for i in range(1, len(num)):
    if num[i] == '1':
        num_change = num[:i] + '0' + num[i+1:]
    elif num[i] == '0':
        num_change = num[:i] + '1' + num[i+1:]

    n = 0
    for j in range(len(num_change)):
        n += int(num_change[len(num)-1-j]) * (2 ** j)
    
    # print(num_change, n)
    max_n = max(max_n, n)

print(max_n)