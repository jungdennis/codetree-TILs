arr = list(input())

cnt = 0
for i in range(len(arr)-1):
    if arr[i] == '(' and arr[i+1] == '(':
        for j in range(i+1, len(arr)-1):
            if arr[j] == ')' and arr[j+1] == ')':
                cnt += 1

print(cnt)