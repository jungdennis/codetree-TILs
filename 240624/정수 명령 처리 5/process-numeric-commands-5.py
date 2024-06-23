n = int(input())
ans = []

for i in range(n):
    order = input()

    if 'push_back' in order:
        A = int(order.split()[1])
        ans.append(A)
    elif 'pop_back' in order:
        ans.pop()
    elif 'size' in order:
        print(len(ans))
    elif 'get' in order:
        k = int(order.split()[1])
        print(ans[k-1])